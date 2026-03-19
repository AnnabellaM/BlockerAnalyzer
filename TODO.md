# BlockerAnalyzer — TODO

## [ ] Build `tools/ir_slice_builder.py` — IR-based dynamic slice extractor

Extract the dynamic execution trace (hit basic blocks + counts) from IR + profile data, then hand the structured result to the `program-slice-builder` agent to construct the semantic slice.

### Architecture: hybrid tool + agent

The tool handles the mechanical, graph-algorithm work that LLMs are bad at. The agent handles semantic classification and annotation that requires source-level reasoning.

| Responsibility | Owner |
|---|---|
| Hot path extraction (follow hot edges ENTRY → blocking BB) | Tool |
| Divergence point detection (first BB where one fuzzer drops to 0) | Tool |
| Source location mapping (IR debug info → file:line) | Tool |
| Per-block hitcount annotation | Tool |
| Node classification (ENTRY/CALL/CTRL/DATA/BRANCH) | Agent |
| Type context, variable names, function signatures | Agent |
| Path conditions and key variables | Agent |
| Slice Markdown output | Agent |

### Tool output (JSON)

```json
{
  "blocker": "cram_free_container|3747:13",
  "blocked_side": "False",
  "flip_strength": 138000,
  "fuzzers": ["cmplog", "n4"],
  "divergence_point": {
    "function": "cram_dopen",
    "source": "cram/cram_io.c:1823",
    "counts": {"cmplog": 3421, "n4": 0}
  },
  "hit_blocks": [
    {"function": "LLVMFuzzerTestOneInput", "source": "hts_open_fuzzer.c:171", "counts": {"cmplog": 5120, "n4": 2010}},
    {"function": "view_sam",              "source": "hts_open_fuzzer.c:199",  "counts": {"cmplog": 3860, "n4": 1940}},
    {"function": "cram_dopen",            "source": "cram/cram_io.c:1823",    "counts": {"cmplog": 3421, "n4": 0}},
    ...
  ]
}
```

### Tool scope (tractable — no SSA tracing needed)

1. Map blocker's `file:line:col` → IR basic block via `DILocation` debug metadata
2. CFG traversal: follow hot edges (non-zero count in confirming fuzzer) forward from ENTRY to blocking BB — eliminates the wrong-path problem
3. Divergence point: BFS backward from blocking BB — first BB where `count(confirming_fuzzer) > 0` and `count(primary_fuzzer) == 0`
4. Map each hit block to source location via debug info
5. Emit structured JSON

SSA def-use tracing is intentionally excluded — the agent handles that from the structured hit-block list plus targeted source reads.

### Implementation approach

Option A: `llvm-dis` (text IR) + `llvm-profdata show --all-functions --counts` (text profdata), parsed in Python. Lowest effort, sufficient for validation before committing to llvmlite or a C++ opt plugin.

### CLI

```bash
python3 tools/ir_slice_builder.py \
  --target htslib \
  --ir build/htslib.bc \
  --profiles coverage/htslib/cmplog.profdata coverage/htslib/n4.profdata \
  --blockers blockers/htslib_blockers.md \
  --ranks 1-10 \
  --output-json slices/htslib_dynamic.json
```

The agent then reads `htslib_dynamic.json` alongside source files and writes `slices/htslib_slices.md` in the existing format.

### Open questions (resolve before implementing)

1. Do we have (or can produce) `.bc` and `.profdata` files for existing targets (harfbuzz, htslib, libpcap)?
2. Optimization level: O1 assumed — confirm fuzzing setup uses O1.
3. Profile format: `-fprofile-instr-generate` (clang source-based) vs `-fprofile-generate` (GCC-compatible)?
4. IR scope: whole-program IR via LTO (`-flto -emit-llvm`) needed for cross-TU slices — is LTO feasible for existing targets?

### Integration

- Tool runs before `program-slice-builder` agent when IR + profdata are available
- Agent reads the JSON dynamic slice instead of tracing source manually — wrong-path problem eliminated, counts pre-populated
- `program-slice-builder` agent (source-only tracing) remains as fallback when IR is unavailable
- `fuzzing-root-cause-analyzer` Step 3b spot checks become redundant when IR dynamic slice is used
- Update `CLAUDE.md` and `program-slice-builder.md` to document the two-path workflow once implemented



1. Test on another pair of blockers
2. Should we add the logic in root cause analyzer to infer the reason why Fuzzer A is better on blocker A, apart from just tell us how to unblock the branch. 
3. Should we output root cause of each blocker into a separate file.
4. Should have another agent to read each root cause report and if any new feature is detected, we can reconstruct a new program to test it, if it passes, we add a new feature for the benchmark creation.