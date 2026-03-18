# BlockerAnalyzer

A research project for analyzing fuzzing "blockers" — branches that coverage-guided fuzzers fail to reach — and diagnosing why.

## Project Structure

```
BlockerAnalyzer/
├── coverage/           # Fuzzer coverage reports (llvm-cov annotated source format)
│   ├── harfbuzz/
│   │   ├── cmplog.cov  # Coverage from AFL++ cmplog fuzzer
│   │   └── n4.cov      # Coverage from AFL++ n4 fuzzer
│   ├── htslib/
│   └── libpcap/
├── fuzz/               # AFL++ fuzzing campaign output (per-target)
│   └── <target>_out/default/  # queue/, crashes/, fuzzer_stats, etc.
├── targets/            # Source code of fuzz targets
│   ├── harfbuzz/       # Real-world target: HarfBuzz text shaping library
│   ├── htslib/         # Real-world target: HTSlib genomics library
│   ├── libpcap/        # Real-world target: libpcap packet capture library
│   ├── blocker_1/      # Synthetic: indirect input dependency
│   ├── blocker_2/      # Synthetic: missing function call
│   ├── blocker_3/      # Synthetic: compile-time gate
│   └── blocker_4/      # Synthetic: magic value conjunction
├── blockers/           # Output from fuzzing-branch-analyzer (<target>_blockers.md)
├── slices/             # Output from program-slice-builder (<target>_slices.md)
├── reports/            # Output from fuzzing-root-cause-analyzer (<target>_report.md)
├── analysis/           # Output from fuzzing-coverage-analyst (<target>_analysis.md)
├── tools/              # Reusable analysis scripts
│   └── extract_blockers.py  # Pre-processes llvm-cov files → structured JSON of blocking branches
├── output/             # Legacy one-off reports (superseded by blockers/reports/analysis/)
└── .claude/
    ├── agents/         # Specialized Claude agents for analysis
    └── settings.json   # Project permissions (Bash allowed for all agents)
```

## Synthetic Blocker Benchmarks

These are minimal libFuzzer harnesses designed to represent specific blocker patterns:

- **blocker_1**: Indirect input dependency — the blocking branch `if (secret_unlocked)` at line 65 guards on a variable, not directly on input bytes. `secret_unlocked` is set via two input-dependent paths: directly when `data[0] == 0xFF`, or indirectly via `process_secret()` when `compute_checksum(fp->data) == PROTO_SECURE (0x04)`. The fuzzer sees a branch on a derived/intermediate variable rather than on the raw input, making the dependency indirect and harder to infer.
- **blocker_2**: Missing function call — `process_secret()` (which sets `secret_unlocked = 1`) is defined but never called from any reachable code path. The `if (secret_unlocked)` branch is permanently dead because the function that would flip the flag is simply absent from the call graph.
- **blocker_3**: Compile-time gate — `g_session.unlocked` is controlled by the `UNLOCK_SECRET` preprocessor macro, not runtime input. The blocking branch cannot be reached without recompilation.
- **blocker_4**: Magic value conjunction — `__builtin_trap()` requires matching three separate magic byte sequences simultaneously: header `0xDEAD`, type `0xCAFEBABE`, and footer `0xC0DE`.

## Coverage Report Format

Reports are llvm-cov annotated source files. Branch data appears inline:

```
  |  Branch (900:11): [True: 37, False: 4]
  |  Branch (900:31): [True: 2, False: 2]
  |  Branch (900:48): [True: 0, False: 2]
```

`True: 0` or `False: 0` indicates an unvisited branch side.

## Agents

Four specialized agents are available in `.claude/agents/`:

| Agent | Output folder | File naming | Purpose |
|-------|--------------|-------------|---------|
| **fuzzing-branch-analyzer** | `blockers/` | `<target>_blockers.md` | Parses coverage reports, identifies asymmetric branch pairs, cross-references across fuzzers to confirm input-dependency |
| **program-slice-builder** | `slices/` | `<target>_slices.md` | Applies NEG pre-screening and traces execution paths (program slices) from the fuzzer entry point to each blocking branch; default batch size 10 |
| **fuzzing-root-cause-analyzer** | `reports/` | `<target>_report.md` | Reads pre-built slices, clusters by slice similarity, classifies root causes, and writes findings with mitigations |
| **fuzzing-coverage-analyst** | `analysis/` | `<target>_analysis.md` | Analyzes fuzzing campaigns (seed queues, mutation patterns) to diagnose why a fuzzer failed to penetrate input-dependent blockers |

## Permissions

`.claude/settings.json` grants `Bash(*)` project-wide, so all agents can run shell commands (including `extract_blockers.py`) without prompting. Do not remove this — the `fuzzing-branch-analyzer` agent requires Bash to invoke the pre-processing tool on large coverage files.

## Tools

### `tools/extract_blockers.py`

Pre-processes one or more llvm-cov annotated source files into a structured JSON of blocking branches. Used by `fuzzing-branch-analyzer` automatically when coverage files exceed 5,000 lines (to avoid context window exhaustion).

```bash
# Write ranked Markdown report directly (preferred):
python3 tools/extract_blockers.py \
  --target <name> \
  --output blockers/<name>_blockers.md \
  coverage/<target>/cmplog.cov coverage/<target>/n4.cov

# Output raw JSON to stdout for custom processing:
python3 tools/extract_blockers.py \
  --target <name> \
  coverage/<target>/cmplog.cov coverage/<target>/n4.cov > out.json
```

With `--output`, produces a fully formatted, ranked Markdown report directly — no further processing needed. Without `--output`, outputs raw JSON to stdout.

Each confirmed blocker carries a `source_line` field: the raw source text at the branch's line, extracted from the coverage file. This appears as `**Statement**: \`...\`` in the Markdown listings and gives `fuzzing-root-cause-analyzer` quick context before reading full source files.

### Program Slices

`program-slice-builder` constructs a **program slice** for each confirmed blocker: an ordered sequence of control and data flow nodes from the fuzzer entry point to the blocking branch. Each node carries the exact statement text, file:line, types, and function signatures — enough for an LLM to reconstruct a compilable C skeleton.

Node types: `ENTRY` (fuzzer entry), `CALL` (function call on path), `CTRL` (control flow condition, annotated with required direction), `DATA` (variable binding that feeds the blocking condition), `BRANCH` (the blocking branch, always last).

Slices are written to `slices/<target>_slices.md` and consumed by `fuzzing-root-cause-analyzer`. The file is appended to across batches, so multiple runs accumulate into a single target file.

### Branch Clustering

Clustering is performed by `fuzzing-root-cause-analyzer` from pre-built slices, using **program slice similarity**.

Two blockers are clustered when their slices share structural ancestry:

| Relationship | Criterion | Cluster role |
|--------------|-----------|-------------|
| **Downstream** | Slice A ⊇ Slice B (A has all of B's nodes plus more) | B is the cluster root; A is a downstream member |
| **Peer** | Slices share the same root node but neither contains the other | Both are peers; the shared root variable/condition is the cluster focus |

The cluster representative is always the blocker with the simplest (most upstream) slice. Resolving the root blocker's barrier also unblocks all downstream members. Peer members share the same fix strategy.

Cluster IDs (C01, C02, …) are assigned by the root cause analyzer in Step 2 and carried through the report.

### Negative Rules (Pre-screening)

`program-slice-builder` screens each blocker against four negative rules before building its slice. A blocker that matches is **skipped** and recorded in the Skipped Blockers section of the slices file, then carried through to the Skipped Blockers section of the root cause report.

| Rule | Criterion |
|------|-----------|
| **NEG-1** | Blocked block body contains only a `return` statement |
| **NEG-2** | Blocked block body contains only an error handler (`opt_error`, `fprintf`+`exit`, `abort`, `assert`, etc.) |
| **NEG-3** | Blocked block body contains only cleanup (`free`, `close`, `destroy`, etc.) |
| **NEG-4** | Branch or context is annotated `deprecated`, `legacy`, or `obsolete` |

Rules are defined inline in `program-slice-builder.md` — `rules.md` is superseded.

### Blocker Ranking

Confirmed input-dependent blockers are ranked by **flip strength** (descending):

> **Flip strength** = hitcount of the blocked side in the confirming fuzzer

Because the blocked side has 0 hits in the primary fuzzer, flip strength equals the absolute hitcount difference for that side between fuzzers. A high value means the confirming fuzzer hits the branch frequently while the primary misses it entirely — a strong signal of input-dependent reachability and a high-value target for fuzzer improvement.

## Typical Workflow

1. Run fuzzers (e.g., AFL++ cmplog and n4 variants) on a target, collect llvm-cov reports into `coverage/<target>/`.
2. Use `fuzzing-branch-analyzer` to identify input-dependent blocking branches → output in `blockers/`.
3. Use `program-slice-builder` on the blockers file to apply NEG screening and trace execution paths → output in `slices/`. Default batch size is 10; specify rank ranges for large targets.
4. Use `fuzzing-root-cause-analyzer` on the slices file to cluster, classify root causes, and write findings → output in `reports/`.
5. Use `fuzzing-coverage-analyst` on input-dependent blockers with fuzzing campaign data to diagnose fuzzer logic weaknesses → output in `analysis/`.
