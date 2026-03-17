---
name: Recurring fuzzer design weakness patterns
description: Observed fuzzer design weaknesses and their seed queue / coverage fingerprints, built from campaign analyses in this project
type: reference
---

## Pattern 1: Conjunction Impossibility (structural)

**Signature:** One operand of a `&&` branch is satisfied (non-zero true hits) but the other is always false. Branch evaluated N times, true hits = 0. The setter for the unsatisfied operand is in a code path that short-circuits (early `return`) before reaching the branch.

**Coverage fingerprint:** `Branch (L:C1): [True: N>0, False: M]` followed by `Branch (L:C2): [True: 0, False: N]` in llvm-cov output (short-circuit evaluation exposes this as two separate branch entries on the same line).

**Seed queue fingerprint:** Depth chain with escalating rep counts, corpus growth stalls after small N, 95%+ cycles without finds.

**Fix:** Remove or restructure the early `return` so both setters can be reached in the same execution. Then: add CmpLog, handcrafted seeds, dictionary.

---

## Pattern 2: Checksum Opacity (without CmpLog)

**Signature:** A derived value (sum, hash, XOR fold) is compared against a small set of constants. The fuzzer hits the comparison branch but rarely or never hits specific constant values. Sibling branches for nearby constant values are also missed.

**Coverage fingerprint:** All `computed == CONST_N` branches show [True: 0] or very low true counts despite many executions of the enclosing function.

**Seed queue fingerprint:** All seeds sourced via havoc; no dictionary tokens in seed names; auto_dict_entries: 0; cmplog_time: 0.

**Fix:** Enable CmpLog (`-c` flag); add dictionary with all magic constants; add handcrafted seeds with known-good derived values.

---

## Pattern 3: Decoy Setter (structural short-circuit)

**Signature:** A variable can be set via two paths. Path A is easy to discover but exits early (e.g., `data[0] == 0xFF → set_flag(); return 0;`). Path B is the only viable path to the target branch. Fuzzer discovers Path A quickly, gains coverage signal for `set_flag()`, but never reaches the branch that depends on the flag.

**Coverage fingerprint:** The function that sets the flag shows execution hits. The target branch shows [True: 0]. The early-exit path shows hit counts.

**Fix:** Remove early exit from Path A, or add a handcrafted seed that follows Path B directly.
