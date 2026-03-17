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

Three specialized agents are available in `.claude/agents/`:

| Agent | Output folder | File naming | Purpose |
|-------|--------------|-------------|---------|
| **fuzzing-branch-analyzer** | `blockers/` | `<target>_blockers.md` | Parses coverage reports, identifies asymmetric branch pairs, cross-references across fuzzers to confirm input-dependency |
| **fuzzing-root-cause-analyzer** | `reports/` | `<target>_report.md` | Traces execution paths to blocking branches and classifies root causes (magic value, checksum, dead code, compile-time gate, etc.) |
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

### Branch Clustering

`extract_blockers.py` automatically clusters confirmed blockers using source line text extracted from the coverage file. Each branch receives a `cluster_id` and `cluster_type` in the output:

| Type | Detection rule | Meaning |
|------|---------------|---------|
| `logical` | Source line contains `&&` or `\|\|` | Sub-conditions of one logical expression (multiple branches per line) |
| `switch` | Source line starts with `case`/`default:`; backward brace-depth scan confirms enclosing `switch` | Arms of the same switch statement |
| `chain` | Source line contains `else if (`; backward brace-depth scan finds opening `if` | Arms of the same if/else-if chain |
| `ternary` | Source line contains `?` but no `if`/`case`/`else` keyword | Conditional expression (`x ? a : b`) |
| `single` | No recognizable pattern | Standalone condition |

Each branch in the output also carries a `source_line` field with the raw source text at that line. This appears as `**Statement**: \`...\`` in the detail listings.

The backward scan tracks brace depth to find the correct enclosing construct, handling one level of nesting. Deeper nesting may occasionally produce mis-grouped clusters; `fuzzing-root-cause-analyzer` confirms and refines all clusters in Step 1.5 using source code.

The Cluster column in the Markdown summary table shows e.g. `C003 (switch×2)`. Detail listings include cross-references: `also at rank 4`.

### Blocker Ranking

Confirmed input-dependent blockers are ranked by **flip strength** (descending):

> **Flip strength** = hitcount of the blocked side in the confirming fuzzer

Because the blocked side has 0 hits in the primary fuzzer, flip strength equals the absolute hitcount difference for that side between fuzzers. A high value means the confirming fuzzer hits the branch frequently while the primary misses it entirely — a strong signal of input-dependent reachability and a high-value target for fuzzer improvement.

## Typical Workflow

1. Run fuzzers (e.g., AFL++ cmplog and n4 variants) on a target, collect llvm-cov reports into `coverage/<target>/`.
2. Use `fuzzing-branch-analyzer` to identify input-dependent blocking branches → output in `blockers/`.
3. Use `fuzzing-root-cause-analyzer` on confirmed blocking branches to produce structured root-cause reports → output in `reports/`.
4. Use `fuzzing-coverage-analyst` on input-dependent blockers with fuzzing campaign data to diagnose fuzzer logic weaknesses → output in `analysis/`.
