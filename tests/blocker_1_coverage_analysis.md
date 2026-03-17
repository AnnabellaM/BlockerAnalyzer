## Fuzzing Campaign Analysis Report: blocker_1

**Target:** `targets/blocker_1/blocker_1.c`
**Fuzzer:** AFL++ v4.36a
**Campaign runtime:** 58 seconds
**Analysis date:** 2026-03-17

---

### Executive Summary

AFL++ ran for 58 seconds, executing 1,488,444 inputs, and achieved 70% bitmap coverage (14 of 20 edges). The blocking branch at `blocker_1.c:65` — the true side of `if (secret_unlocked)` — was never triggered to advance `target_reached = 1`. The fuzzer correctly discovered that `compute_checksum == PROTO_SECURE` can be satisfied (2 hits on the `computed == PROTO_SECURE` branch), meaning `secret_unlocked` was set via `process_secret()` twice. However, the concurrent decoy path (`data[0] == 0xFF`) sets `secret_unlocked = 1` and exits via `return 0` before reaching line 65, making that path structurally useless. The fuzzer's havoc-only strategy, absence of CmpLog, and absence of a handcrafted seed corpus all compounded this structural problem.

---

### Coverage Overview

| Metric | Value |
|--------|-------|
| Bitmap coverage | 70.00% (14 / 20 edges) |
| Corpus count | 15 (1 original + 14 found) |
| Total executions | 1,488,444 |
| Runtime | 58 seconds |
| Crashes | 0 |
| Cycles without new finds | 366 / 374 (97.9%) |
| Max depth | 6 |
| CmpLog used | No (`cmplog_time: 0`) |
| Auto-dict entries | 0 |

The blocking branch is the true side of `if (secret_unlocked)` at line 65 — evaluated twice (when `process_secret()` was called via Path B), but `target_reached = 1` was never reached. The 30% uncovered edges all lie behind this blocked condition.

---

### Input-Dependent Blockers Identified

#### Blocker 1: Structural Short-Circuit — `secret_unlocked` at line 65

- **Location:** `blocker_1.c:65`, true side of `if (secret_unlocked)`
- **Type:** Structural decoy path + indirect input dependency
- **Root cause:** Two paths set `secret_unlocked = 1`:
  - **Path A (decoy):** `data[0] == 0xFF` → `secret_unlocked = 1` → `return 0` at line 53. Exits *before* line 65. The fuzzer discovers this trivially but it is structurally useless.
  - **Path B (viable):** `data[0] != 0xFF` + `compute_checksum(fp->data) == PROTO_SECURE (0x04)` → `process_secret()` → `secret_unlocked = 1` → falls through to line 65.
- **Campaign evidence:** The id:000011–000014 depth chain (evolving from the first PROTO_SECURE hits at id:000009–000010) confirms the fuzzer found Path B twice but then stagnated — the branch was evaluated but the condition only holds when Path B is taken, which requires the checksum constraint.
- **Fuzzer verdict:** The fuzzer discovered the decoy (Path A) rapidly and likely stored seeds triggering it. AFL++ then spent most of its budget mutating those Path A seeds, which always hit `return 0` and never advance to line 65. This is the classic indirect-input-dependency trap: the variable `secret_unlocked` is controlled by input, but the *path* to both setting it and reaching the guarded branch is non-obvious to a coverage-only fuzzer.

#### Blocker 2: Checksum Magic Value — `computed == PROTO_SECURE` (and siblings)

- **Location:** `blocker_1.c:37–41`, true sides of all four `computed == PROTO_*` branches
- **Type:** Checksum magic value — sum-of-bytes mod 256 must equal a specific constant
- **Campaign evidence:** PROTO_SECURE true branch: 2 hits out of 47 FUNC() invocations (4.3%); PROTO_BASIC/EXTENDED/LEGACY: 0 hits each. The fuzzer stumbled into PROTO_SECURE twice by chance but never converged on the sibling values.
- **Root cause:** Without CmpLog, the `computed vs. 0x04` comparison is opaque. Havoc mutations change payload bytes randomly, shifting the sum without targeting residue 0x04. For multi-byte payloads, each mutation destroys a previously valid checksum with no recovery signal.

---

### Seed Queue Mutation Pattern Analysis

**AFL++ naming convention decoded:**
`id:NNNNNN` = corpus index | `src:NNNNNN` = parent | `time:N` = ms since start | `execs:N` = total execs when saved | `op:OPNAME` = mutation operator | `rep:N` = mutation rounds | `+cov` = new edge discovered

**Phase 1 — Rapid diversification from original seed (id:000001–000010, execs 22–1648, 0–62ms)**

All 10 seeds derive from id:000000. The fuzzer finds 4 new edges (`+cov` on ids 000001, 000002, 000009, 000010) and retains 6 non-`+cov` seeds for structural reasons. The two late `+cov` seeds (ids 000009–000010, execs 1,583–1,648) represent the first contact with a qualitatively different code path — almost certainly the first accidental PROTO_SECURE checksum hits, setting `secret_unlocked` via Path B and advancing to line 65 for the first time.

**Phase 2 — Linear depth chain from id:000010 (id:000011–000014, execs 13142–30618, 509–1202ms)**

A strict depth-4–6 chain: 000010 → 000011 → 000012 → 000013 → 000014. Rep counts escalate sharply (5 → 22 → 13 → 21), AFL++'s automatic response to finding-difficulty: the engine increases `havoc_expansion` (confirmed: `havoc_expansion: 5`) when new edges are scarce.

Each seed in the chain yields `+cov`, but the chain terminates at id:000014 with no further descendants. After exec 30,618, the campaign runs for another ~1,457,826 executions — **97.9% of the total budget** — without a single new find.

**The stagnation fingerprint:** The id:000011–000014 chain likely represents the fuzzer evolving Path B inputs (checksum = 0x04, data[0] != 0xFF) and discovering incremental hit-count bucket changes inside FUNC(). But AFL++ cannot bridge the gap to `target_reached = 1` because every Path A mutation (`data[0] = 0xFF`) exits at line 53, and every Path B mutation requires hitting checksum 0x04 by chance with no gradient to guide it.

**Absence of non-havoc operators:** No seed contains `op:flip1`, `op:arith`, `op:interest`, or `op:splice`. This indicates deterministic stages ran but produced nothing worth keeping, and the fuzzer moved permanently to havoc mode — random byte flipping without any structural bias toward the specific comparison targets.

---

### How the Indirect Input Dependency Defeated the Fuzzer

**The decoy path trap.** The `data[0] == 0xFF` path (line 51) is more discoverable than the viable path because it requires matching a single byte at a fixed position — havoc can do this trivially. The fuzzer exhausted coverage of the `data[0]` branch (both sides hit) and stored multiple Path A seeds. But every Path A seed terminates at `return 0`, so every mutation of a Path A seed also terminates before line 65. The fuzzer was learning to satisfy the wrong precondition.

**Checksum opacity without CmpLog.** The viable path requires `compute_checksum(fp->data) == 0x04`. This is opaque because the comparison happens on a derived value, not a raw input byte. CmpLog's comparison-logging instrumentation would expose the `computed` vs. `0x04` operands to RedQueen. Without it (`cmplog_time: 0`), the fuzzer cannot observe what the checksum value is and cannot target it.

**No fitness gradient.** Being "one off" from checksum 0x04 provides zero coverage signal. The branch outcome (True/False) is binary, and the fuzzer has no signal distinguishing `computed = 0x03` from `computed = 0xFF`. Both produce identical coverage bitmaps from FUNC()'s perspective, so the mutation engine has no incentive to move toward 0x04 specifically.

**No global state reset.** The harness uses `static int secret_unlocked` without resetting between calls. In AFL++'s persistent mode (`target_mode: persistent`), this accumulates across iterations, potentially producing non-deterministic coverage. The 2 hits on the `if (secret_unlocked)` branch may reflect cross-iteration contamination rather than a clean Path B execution.

---

### Cross-Cutting Fuzzer Design Weaknesses

1. **Exclusive reliance on havoc.** Every corpus seed was produced by `op:havoc`. Havoc is effective for structural exploration but has no directional bias toward specific comparison targets or checksum residues.

2. **No CmpLog.** `cmplog_time: 0` confirms CmpLog was never active. CmpLog is the primary mechanism for exposing comparison operands and enabling targeted mutation on derived values like checksums.

3. **No dictionary.** `auto_dict_entries: 0`. The protocol constants (`0x01`–`0x04`) and the Path A magic byte (`0xFF`) were never available as mutation tokens.

4. **Single-seed corpus start.** Starting from one seed forced the fuzzer to discover all input diversity randomly. A handcrafted corpus with a known-good Path B input (e.g., `{0x00, 0x04}`: not 0xFF, single payload byte summing to 0x04) would have provided Path B coverage from execution 0.

5. **No structural awareness of the path exclusivity.** AFL++ treats the `if (secret_unlocked)` branch as a single coverage target and cannot model that Path A and Path B have mutually exclusive preconditions with respect to reaching line 65.

---

### Prioritized Recommendations

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Remove `return 0` at line 53 (structural fix) | Trivial | Prerequisite — allows Path A to fall through to line 65 |
| 2 | Add seed `{0x00, 0x04}` to corpus | Trivial | Immediate Path B coverage from exec 0 |
| 3 | Enable CmpLog (`-c ./blocker_1_fuzz_cmplog`) | Low | Targets checksum constraint directly via RedQueen |
| 4 | Add dictionary: `\x01\x02\x03\x04\xff` | Low | Accelerates protocol constant discovery |
| 5 | Reset global state at harness entry | Low | Correctness: prevents cross-iteration contamination |
| 6 | Run second instance with `AFL_LLVM_CTX=1` | Medium | Context-sensitive coverage for conjunction blockers |

**Recommendation 1** is a prerequisite: without it, Path A still exits early and the structural impossibility remains. **Recommendations 1 + 2 + 3** together fully unblock the branch and eliminate both root causes.

---

### Summary Table

| Attribute | Value |
|-----------|-------|
| Blocking branch | `blocker_1.c:65`, true side of `if (secret_unlocked)` → `target_reached = 1` |
| Primary root cause | Structural decoy: Path A sets `secret_unlocked` but exits before line 65 |
| Secondary root cause | Checksum opacity: `compute_checksum == 0x04` unguided without CmpLog |
| Fuzzer configuration | Havoc-only, no CmpLog, no dictionary, single seed |
| Coverage achieved | 70% (14/20 edges); target branch: effectively 0 useful hits |
| Stagnation onset | Exec 30,618 of 1,488,444 (97.9% of budget wasted) |
| Cycles without finds | 366 / 374 (97.9%) |
| Critical structural fix | Remove `return 0` at line 53 |
| Highest-leverage fuzzer fix | Enable CmpLog + add seed `{0x00, 0x04}` |
