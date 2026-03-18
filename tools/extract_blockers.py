#!/usr/bin/env python3
"""
extract_blockers.py — pre-process llvm-cov annotated source files to identify
input-dependent blocking branches across multiple fuzzer coverage reports.

Usage:
    python3 extract_blockers.py --target <name> [--limit <N>] [--output <path>] <cov_file1> [<cov_file2> ...]

Arguments:
    --target   Target name used in canonical branch identifiers (e.g. "htslib")
    --limit    Stop after this many confirmed input-dependent branches (default: unlimited)
    --output   Write a formatted Markdown report to this path instead of JSON to stdout.
               If omitted, outputs raw JSON to stdout.
    cov_files  One or more llvm-cov annotated source files

Output without --output (stdout, JSON):
    {
      "target": "<name>",
      "stats": { ... },
      "confirmed": [
        {
          "key":           "<func>|<line>:<col>",
          "func":          "<function name (raw/mangled)>",
          "demangled_func":"<demangled name, present only when func is a C++ mangled symbol>",
          "line":          "<line>",
          "col":           "<col>",
          "blocked_side":  "T_blocked" | "F_blocked",
          "primary_fuzzer":"<filename>",
          "confirm_fuzzer":"<filename>",
          "source_line":   "<raw source text at the branch line>",
          "hits": { "<filename>": {"T": N, "F": N}, ... }
        }, ...
      ],
      "unconfirmed": [ ... ]
    }

Output with --output (Markdown report):
    Ranked by flip strength (descending).

Each branch record includes a 'source_line' field with the raw source text at
that line, shown in the Markdown detail listings for quick context.
Clustering is performed by the fuzzing-root-cause-analyzer agent using program
slice analysis during root cause tracing.
"""

import re
import sys
import json
import argparse
import datetime
import subprocess
from collections import defaultdict


def parse_count(s):
    """Parse an llvm-cov hit count string to int. Handles k/K/m/M suffixes and commas."""
    s = s.strip().replace(',', '')
    if not s or s == '-':
        return 0
    if s[-1] in ('k', 'K'):
        return int(float(s[:-1]) * 1_000)
    if s[-1] in ('m', 'M'):
        return int(float(s[:-1]) * 1_000_000)
    return int(s)


def parse_cov_file(path):
    """
    Parse an llvm-cov annotated source file.

    Returns:
      branches: dict  key -> {"T": int, "F": int, "func": str, "line": str, "col": str,
                               "_section_lines": <dict of line_no->text for this source file>}

    Key format: "<function_name>|<line>:<col>"

    Source lines are captured from the llvm-cov format:
        <line_no> | <hit_count> | <source_text>
    Branch annotations are:
        Branch (<line>:<col>): [True: N, False: M]
    Function headers are bare lines ending in ':' with no '|' or 'Branch'.
    They come in two forms:
        file.c:funcname:   — function in a named non-primary source file
        funcname:          — function in the current (or initial) source file

    A new source file section is detected when a 'file.c:funcname:' header appears
    with a different file part than the previous. The section line buffer is reset so
    that line numbers from different source files never collide in lookups.

    Each branch stores a reference to its section's line buffer (_section_lines).
    This dict is shared (not copied) across all branches in the same section and is
    fully populated by end-of-section, so source line lookups always see correct text.
    """
    branches = {}
    current_func = None
    current_source_file = None      # file part extracted from 'file.c:funcname:' headers
    current_section_lines = {}      # line_no -> source text; reset per source file

    branch_re = re.compile(
        r'Branch \((\d+):(\d+)\): \[True: ([\d.,kKmM]+), False: ([\d.,kKmM]+)\]'
    )
    source_re = re.compile(r'^\s*(\d+)\s*\|[^|]*\|(.*)')
    # Matches 'file.c:funcname' or 'file.cpp:funcname' etc.
    file_func_re = re.compile(r'^(.+\.[ch](?:pp|xx)?):(.+)$', re.I)

    with open(path, errors='replace') as f:
        for line in f:
            stripped = line.strip()

            # Function/file header: ends with ':', no pipe, no 'Branch'
            if (stripped.endswith(':')
                    and '|' not in stripped
                    and 'Branch' not in stripped
                    and stripped != ':'):
                header = stripped[:-1]
                fm = file_func_re.match(header)
                if fm:
                    # 'file.c:funcname' form — may signal a new source file section
                    new_file = fm.group(1)
                    current_func = header
                    if new_file != current_source_file:
                        current_source_file = new_file
                        current_section_lines = {}   # new dict = new section
                else:
                    # plain 'funcname' (e.g. mangled C++ symbol with no file prefix).
                    # Start a fresh section so this function's source lines don't
                    # bleed into unrelated functions that share the same line numbers
                    # (common in C++ template instantiations from different headers).
                    current_func = header
                    current_section_lines = {}

            # Source line: add to current section buffer (last write wins within section)
            sm = source_re.match(line)
            if sm:
                current_section_lines[int(sm.group(1))] = sm.group(2)

            # Branch annotation
            m = branch_re.search(line)
            if m and current_func:
                line_no, col, true_s, false_s = m.groups()
                key = f"{current_func}|{line_no}:{col}"
                branches[key] = {
                    'T': parse_count(true_s),
                    'F': parse_count(false_s),
                    'func': current_func,
                    'line': line_no,
                    'col': col,
                    '_section_lines': current_section_lines,  # shared ref, not a copy
                }

    return branches


def find_asymmetric(branches):
    """
    Return branches where exactly one side is hit.
    Value: ('T_blocked', entry) if True=0,False>0  (True side is blocked)
           ('F_blocked', entry) if True>0,False=0  (False side is blocked)
    """
    result = {}
    for key, b in branches.items():
        if b['T'] > 0 and b['F'] == 0:
            result[key] = ('F_blocked', b)
        elif b['F'] > 0 and b['T'] == 0:
            result[key] = ('T_blocked', b)
    return result


def cross_reference(all_branches, limit=None):
    """
    Cross-reference asymmetric branches across all fuzzers.

    all_branches: dict of {fuzzer_label: parsed_branches_dict}
    Returns (confirmed, unconfirmed) lists, each entry is a dict.
    """
    fuzzer_labels = list(all_branches.keys())
    asymmetric_per = {label: find_asymmetric(all_branches[label]) for label in fuzzer_labels}

    confirmed = []
    unconfirmed = []
    seen_confirmed = set()

    for primary_label in fuzzer_labels:
        for key, (blocked_side, b) in asymmetric_per[primary_label].items():
            if key in seen_confirmed:
                continue

            need_side = 'T' if blocked_side == 'T_blocked' else 'F'

            confirm_label = None
            for other_label in fuzzer_labels:
                if other_label == primary_label:
                    continue
                other_b = all_branches[other_label].get(key)
                if other_b and other_b[need_side] > 0:
                    confirm_label = other_label
                    break

            hits = {}
            for label in fuzzer_labels:
                entry = all_branches[label].get(key)
                if entry:
                    hits[label] = {'T': entry['T'], 'F': entry['F']}

            record = {
                'key': key,
                'func': b['func'],
                'line': b['line'],
                'col': b['col'],
                'blocked_side': blocked_side,
                'primary_fuzzer': primary_label,
                'hits': hits,
                '_section_lines': b.get('_section_lines', {}),
            }

            if confirm_label:
                record['confirm_fuzzer'] = confirm_label
                confirmed.append(record)
                seen_confirmed.add(key)
                if limit and len(confirmed) >= limit:
                    return confirmed, unconfirmed
            else:
                if key not in seen_confirmed:
                    unconfirmed.append(record)

    return confirmed, unconfirmed


def flip_strength(b):
    """Hitcount of the blocked side in the confirming fuzzer (= absolute cross-fuzzer diff)."""
    blocked_side = 'T' if b['blocked_side'] == 'T_blocked' else 'F'
    return b['hits'].get(b.get('confirm_fuzzer', ''), {}).get(blocked_side, 0)


def batch_demangle(names):
    """
    Demangle a list of C++ symbol names via c++filt.

    Returns a dict mapping original name -> demangled name.
    Names that are unchanged (i.e. not mangled) map to themselves.
    Falls back gracefully if c++filt is unavailable.
    """
    if not names:
        return {}
    try:
        result = subprocess.run(
            ['c++filt'],
            input='\n'.join(names),
            capture_output=True,
            text=True,
            timeout=10,
        )
        demangled = result.stdout.splitlines()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return {n: n for n in names}
    return {orig: dem for orig, dem in zip(names, demangled)}


def finalize_ranked(ranked):
    """
    Strip internal _section_lines from each branch record and attach source_line.
    Also adds demangled_func when the C++ symbol differs from the raw func name.

    source_line carries the raw source text at the branch's line number, extracted
    from the coverage file. Used by the root cause analyzer as quick context.
    """
    # Batch-demangle all func names in one c++filt call
    funcs = [b['func'] for b in ranked]
    demangle_map = batch_demangle(funcs)

    result = []
    for b in ranked:
        b = dict(b)
        section_lines = b.pop('_section_lines', {})
        b['source_line'] = section_lines.get(int(b['line']), '').strip()
        demangled = demangle_map.get(b['func'], b['func'])
        if demangled != b['func']:
            b['demangled_func'] = demangled
        result.append(b)
    return result


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_markdown(target, stats, ranked, cov_files):
    """Render a ranked Markdown report from confirmed input-dependent blockers."""
    today = datetime.date.today().isoformat()
    fuzzer_labels = [p.split('/')[-1].replace('.cov', '') for p in cov_files]
    source_str = ', '.join(f'`coverage/{target}/{l}.cov`' for l in fuzzer_labels)

    lines = []
    lines.append(f"# Input-Dependent Blocking Branches — {target} (All, Ranked by Flip Strength)\n")
    lines.append(f"**Coverage sources:** {source_str}  ")
    lines.append(f"**Analysis date:** {today}  ")
    lines.append("**Ranking:** descending by *flip strength* = hitcount of the blocked side in the confirming fuzzer\n")

    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    for label in fuzzer_labels:
        lines.append(f"| Branch pairs ({label}) | {stats['branches_per_fuzzer'].get(label, 0):,} |")
    for label in fuzzer_labels:
        lines.append(f"| Asymmetric in {label} | {stats['asymmetric_per_fuzzer'].get(label, 0):,} |")
    lines.append(f"| **Confirmed input-dependent** | **{len(ranked):,}** |")
    lines.append(f"| Unconfirmed candidates | {stats['unconfirmed_candidates']:,} |\n")

    lines.append("## Ranked Summary Table\n")
    lines.append("| Rank | Function | Line:Col | Blocked | Flip Strength | " +
                 " | ".join(f"{l} T:F" for l in fuzzer_labels) + " | Confirmed By |")
    lines.append("|------|----------|----------|---------|---------------|" +
                 "".join("------------|" for _ in fuzzer_labels) + "--------------|")

    for i, b in enumerate(ranked, 1):
        func = b.get('demangled_func', b['func'])
        if len(func) > 50:
            func = func[:47] + '...'
        loc = f"{b['line']}:{b['col']}"
        blocked = 'True' if b['blocked_side'] == 'T_blocked' else 'False'
        fs = flip_strength(b)
        hits_cols = []
        for label in fuzzer_labels:
            h = b['hits'].get(label, {})
            hits_cols.append(f"{h.get('T', '-')}:{h.get('F', '-')}")
        lines.append(f"| {i} | `{func}` | {loc} | {blocked} | {fs:,} | " +
                     " | ".join(hits_cols) + f" | {b.get('confirm_fuzzer', '-')} |")

    lines.append("")
    lines.append("## Detail Listings\n")

    for i, b in enumerate(ranked, 1):
        blocked_label = 'True' if b['blocked_side'] == 'T_blocked' else 'False'
        hit_label     = 'False' if b['blocked_side'] == 'T_blocked' else 'True'
        hit_key       = 'T' if hit_label == 'True' else 'F'
        fs = flip_strength(b)

        src = b.get('source_line', '').strip()
        display_func = b.get('demangled_func', b['func'])
        lines.append(f"### {i}. `{display_func}` @ {b['line']}:{b['col']}")
        if src:
            lines.append(f"- **Statement**: `{src}`")
        lines.append(f"- **Blocked side**: {blocked_label} (0 hits in `{b['primary_fuzzer']}`)")
        hit_parts = ', '.join(
            f"{l}: {b['hits'].get(l, {}).get(hit_key, 0):,}"
            for l in fuzzer_labels
        )
        lines.append(f"- **Hit side**: {hit_label} ({hit_parts})")
        lines.append(f"- **Flip strength**: {fs:,} (blocked side hit {fs:,}× by `{b.get('confirm_fuzzer', '-')}`)")
        lines.append(f"- **Status**: ✅ CONFIRMED INPUT-DEPENDENT")
        for label in fuzzer_labels:
            h = b['hits'].get(label, {})
            lines.append(f"- **{label} coverage**: T:{h.get('T', 0):,}  F:{h.get('F', 0):,}")
        lines.append(f"- **Canonical identifiers**:")
        lines.append(f"  - `{target}_{b['func']}_{b['line']}_{b['col']}_T` — " +
                     '  '.join(f"{l}:{b['hits'].get(l,{}).get('T',0):,}" for l in fuzzer_labels))
        lines.append(f"  - `{target}_{b['func']}_{b['line']}_{b['col']}_F` — " +
                     '  '.join(f"{l}:{b['hits'].get(l,{}).get('F',0):,}" for l in fuzzer_labels))
        lines.append("")

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Extract input-dependent blocking branches from llvm-cov files.')
    parser.add_argument('--target', required=True, help='Target name (e.g. htslib)')
    parser.add_argument('--limit', type=int, default=None, help='Stop after N confirmed branches')
    parser.add_argument('--output', default=None, help='Write Markdown report to this file path instead of JSON to stdout')
    parser.add_argument('cov_files', nargs='+', help='llvm-cov annotated source files')
    args = parser.parse_args()

    all_branches = {}
    for path in args.cov_files:
        label = path.split('/')[-1].replace('.cov', '')
        sys.stderr.write(f"Parsing {path} ...\n")
        branches = parse_cov_file(path)
        all_branches[label] = branches
        sys.stderr.write(f"  {len(all_branches[label])} branches found\n")

    confirmed, unconfirmed = cross_reference(all_branches, limit=args.limit)

    stats = {
        'branches_per_fuzzer': {label: len(b) for label, b in all_branches.items()},
        'asymmetric_per_fuzzer': {
            label: len(find_asymmetric(b)) for label, b in all_branches.items()
        },
        'confirmed_input_dependent': len(confirmed),
        'unconfirmed_candidates': len(unconfirmed),
    }

    ranked = sorted(confirmed, key=flip_strength, reverse=True)
    ranked = finalize_ranked(ranked)

    if args.output:
        report = render_markdown(args.target, stats, ranked, args.cov_files)
        with open(args.output, 'w') as f:
            f.write(report)
        sys.stderr.write(f"Report written to {args.output} ({len(ranked)} entries)\n")
    else:
        # Strip _section_lines from unconfirmed before JSON output
        clean_unconfirmed = [{k: v for k, v in u.items() if k != '_section_lines'}
                             for u in unconfirmed]
        output = {
            'target': args.target,
            'stats': stats,
            'confirmed': ranked,
            'unconfirmed': clean_unconfirmed,
        }
        print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
