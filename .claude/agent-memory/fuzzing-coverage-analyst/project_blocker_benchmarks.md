---
name: BlockerAnalyzer synthetic benchmark targets
description: Summary of the four synthetic blocker benchmark targets in this project, their blocker types, and key structural properties
type: project
---

Four synthetic libFuzzer harnesses in `targets/blocker_N/blocker_N.c`, each representing a distinct blocker category:

- **blocker_1**: Two-phase conjunction blocker. `if (phase_one_done && phase_two_done)` at line 65. `phase_one_done` set via `compute_checksum == PROTO_SECURE (0x04)` in FUNC(). `phase_two_done` set via 4-byte magic `{0xDE,0xAD,0xBE,0xEF}` at lines 47–53 but that setter has `return 0` before line 65 — structural conjunction impossibility. Coverage reports in `coverage/blocker_1/afl.cov` (llvm-cov annotated source format).

- **blocker_2**: Dead code — `process_secret()` sets `secret_unlocked = 1` but has no callers. Branch is permanently unreachable regardless of input.

- **blocker_3**: Compile-time gate — `UNLOCK_SECRET` preprocessor macro controls the blocking branch. No runtime input can satisfy it.

- **blocker_4**: Magic value conjunction — `__builtin_trap()` requires three simultaneous magic byte sequences: header `0xDEAD`, type `0xCAFEBABE`, footer `0xC0DE`.

**Why:** These are research benchmarks to study and diagnose fuzzer failure modes. Each represents a distinct root cause category that has been analyzed by the fuzzing-root-cause-analyzer agent, with reports in `output/blocker_N_report.md`.

**How to apply:** When asked to analyze any blocker_N, cross-reference source in `targets/`, coverage in `coverage/`, and fuzzer output in `fuzz/blocker_N_out/`. Note that blocker_1's source differs from some prompt descriptions — always treat the actual source file and coverage report as authoritative.
