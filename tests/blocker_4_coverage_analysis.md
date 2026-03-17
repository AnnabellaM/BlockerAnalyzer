## Fuzzing Campaign Analysis Report: blocker_4

**Target:** `blocker_4.c` — Magic Value Conjunction (`process_packet`)
**Fuzzer:** AFL++ v4.36a
**Analysis Date:** 2026-03-17

---

### Executive Summary

The AFL++ campaign against `blocker_4` executed 1,528,961 inputs over 58 seconds yet produced only 3 new seeds and zero crashes. Coverage stalled at ~96k executions — 6% of total runtime — and the fuzzer spent the remaining 94% cycling uselessly over an already-exhausted corpus. The root cause is a **magic value conjunction with no coverage gradient**: reaching the `__builtin_trap()` at line 32 requires three independent `memcmp` checks to pass simultaneously, with no intermediate edges rewarding partial satisfaction. The absence of CmpLog instrumentation removed the one AFL++ mechanism that could have given the fuzzer per-byte comparison feedback to approach the 8-byte magic sequence incrementally.

---

### Coverage Overview

| Metric | Value |
|--------|-------|
| Total executions | 1,528,961 |
| Bitmap coverage | 55.56% (10/18 edges) |
| Corpus entries | 4 (1 seed + 3 found) |
| Crashes | 0 |
| Cycles without new finds | 1,097 / 1,293 (84.8%) |
| Max depth | 3 |
| Auto-detected dictionary entries | 0 |
| CmpLog enabled | No |

The blocking branch is the true side of `if (a && b && c)` at line 32 — 0 hits. The false side has 3 hits. All 8 uncovered edges are gated behind the unsatisfied conjunction.

---

### Seed Queue Analysis

AFL++ names entries: `id:NNNNNN,src:NNNNNN,time:T,execs:E,op:OPNAME,rep:N[,+cov]`

**Decoded lineage:**

- `id:000000` — original human-provided seed; root of the tree
- `id:000001` — `src:000000, op:havoc, rep:4, +cov, execs:12, time:1ms` — found at exec 12, essentially immediately; a structural variant that bumped a bitmap bucket
- `id:000002` — `src:000000, op:havoc, rep:26, +cov, execs:93768, time:3671ms` — found after 93k failed attempts; 26 havoc rounds required, indicating the fuzzer was thrashing before accidentally hitting a new hit-count bucket (not a new branch)
- `id:000003` — `src:000001, op:havoc, rep:6, +cov, execs:96391, time:3774ms` — found 2,623 execs after id:000002; coverage discovery ended here

**All three new seeds were found within 6.3% of total runtime.** After exec 96,391, 1,432,570 more executions produced zero new seeds. The mutation tree is entirely flat (max depth 3). The 1,097 cycles without finds (84.8% of all cycles) confirm the fuzzer recognized its own stagnation but had no path forward.

---

### Why the Conjunction's Gradient Absence Made It Unfuzzable

The core AFL++ feedback loop requires a chain of rewarding edges. For `blocker_4.c:32`:

| `a` | `b` | `c` | Branch outcome | New AFL++ edge? |
|-----|-----|-----|----------------|-----------------|
| 0 | 0 | 0 | False | No (baseline) |
| 1 | 0 | 0 | False | **No** |
| 0 | 1 | 0 | False | **No** |
| 0 | 0 | 1 | False | **No** |
| 1 | 1 | 0 | False | **No** |
| 1 | 0 | 1 | False | **No** |
| 0 | 1 | 1 | False | **No** |
| 1 | 1 | 1 | **True** | **Yes** |

Every partial-satisfaction state maps to the identical False edge. The fuzzer cannot tell that a seed with `a=1` is "closer" to the target than the original seed. No amount of additional mutation time can close a gap the feedback signal cannot measure. The footer check `data[size-2..size-1]` adds a further complication: any length-changing havoc mutation simultaneously invalidates any partial footer match by shifting the expected position.

The random probability of satisfying all three simultaneously is **~1/2^56**. At 1,528,961 executions the expected number of successes is ~2×10^-11 — effectively zero. Reaching 50% probability would require ~5×10^16 executions, approximately 100 years at this throughput.

---

### How the Absence of CmpLog Compounded the Problem

AFL++ CmpLog instruments `memcmp` and equality comparisons to log expected vs. actual byte values, then applies RedQueen to splice the expected values directly into the input. For a single `memcmp(data, MAGIC, N)`, CmpLog would generate a seed with the magic bytes at the observed offset without relying on random mutation.

However, even CmpLog cannot fully solve the conjunction blocker in its current form. C's `&&` short-circuits: if `a=0`, `check_type` is never called and CmpLog never observes the `b` comparison. CmpLog can only observe each sub-check after all preceding checks pass. More importantly, even when CmpLog generates a seed satisfying `check_header` (`a=1`), AFL++ has no reason to keep it — it produces the same False branch edge as every other seed. CmpLog generates solutions that the feedback loop discards.

CmpLog's effectiveness is gated on the same gradient that havoc requires. Its real value would emerge only after the conjunction is refactored into sequential early-return guards (where each check produces its own independent coverage edge).

---

### Cross-Cutting Fuzzer Design Weaknesses

1. **Havoc-only strategy with no deterministic passes:** All three discovered seeds used `op:havoc`. No dictionary-guided or deterministic mutation stages contributed any new coverage. This is consistent with AFL++'s behavior when seeds do not benefit from deterministic passes, but it means the fuzzer had no structured approach to byte-level magic values.

2. **Zero auto-detected dictionary tokens:** `Auto dict entries: 0` means AFL++ did not extract the magic byte sequences from the binary. The three magic constants (`MAGIC_HEADER`, `MAGIC_TYPE`, `MAGIC_FOOTER`) were never available as mutation tokens.

3. **Position-dependent footer constraint:** `check_footer` checks `data[size-2..size-1]`. Havoc mutations that alter input length invalidate any accidentally-correct footer placement. Structure-unaware mutation cannot reliably satisfy a position-dependent footer while also mutating the interior.

4. **Max depth stalled at 3:** Productive campaigns grow corpora dozens to hundreds of levels deep. Depth 3 is the hallmark of a hard early-stage barrier: the fuzzer found a handful of bitmap variants and immediately hit a wall it cannot cross.

---

### Prioritized Recommendations

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Structured seed `\xDE\xAD\xCA\xFE\xBA\xBE\xC0\xDE` | Trivial (1 command) | Immediate — blocker cleared on first execution |
| 2 | Refactor to sequential early-return guards | Low (3-line change) | Permanent structural fix; creates coverage gradient |
| 3 | Enable CmpLog after refactor | Low (recompile + flag) | Accelerates convergence through each guard independently |
| 4 | Fuzzer dictionary for all three magic tokens | Low (3-line dict file) | Moderate supplement to seed and refactor |
| 5 | Custom structure-aware mutator | High | Maximum post-gate exploration throughput |

**Recommendation 1 alone** clears the blocker immediately. **Recommendations 1 + 2** together are the complete solution. **Recommendation 3** should always accompany 2 for real-world targets.
