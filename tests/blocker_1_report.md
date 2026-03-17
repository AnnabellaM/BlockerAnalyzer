# Blocking Branch Root Cause Report: blocker_1

**Target:** `/home/miao/work/BlockerAnalyzer/targets/blocker_1/blocker_1.c`
**Analysis Date:** 2026-03-17

---

## BLOCKING BRANCH ANALYSIS

```
Location:         blocker_1.c:65  (LLVMFuzzerTestOneInput)
Branch Condition: if (secret_unlocked)  [true side]
Coverage Status:  0 hits
```

### Execution Path to Branch

```
LLVMFuzzerTestOneInput()  [entry, line 46]
  size >= 2                                          [line 48 guard]
  data[0] != 0xFF                                    [line 51 guard — must NOT take early return]
  FUNC(&fp)                                          [line 63]
    compute_checksum(fp->data, fp->data_len)         [line 36]
    computed == PROTO_SECURE (0x04)                  [line 41]
      process_secret(&fp)                            [line 42]
        secret_unlocked = 1                          [line 22]
  if (secret_unlocked)   <-- BLOCKING BRANCH        [line 65]
    target_reached = 1                               [line 66]
```

### Root Cause Category

**Indirect Input Dependency — Structural Short-Circuit + Checksum Magic Value**

### Root Cause Explanation

There are two input-dependent paths that can set `secret_unlocked = 1`, but both are blocked from reaching line 65:

**Barrier 1 — Structural Short-Circuit (Critical)**

- **Path A:** `data[0] == 0xFF` (line 51) → `secret_unlocked = 1` → `return 0` (line 53). This path is discovered trivially by the fuzzer (1-in-256 chance), but the `return 0` exits the function *before* line 65 is reached. `secret_unlocked` is set but the blocking branch is never evaluated. Path A is a structural decoy — the most discoverable setter is mutually exclusive with the target branch.

- **Path B:** `data[0] != 0xFF`, payload bytes sum to `0x04` mod 256 → `FUNC` triggers `process_secret` → `secret_unlocked = 1` → falls through to line 65. This is the only viable path to the blocking branch.

**Barrier 2 — Checksum Magic Value Constraint (High)**

Path B requires `compute_checksum(fp->data, fp->data_len) == 0x04` (i.e., `PROTO_SECURE`). The checksum is the low 8 bits of the sum of all payload bytes:

- Random single-byte payloads hit the target with probability 1/256.
- For multi-byte payloads, any mutation that flips or inserts a byte changes the sum, breaking a previously valid constraint — there is no gradient to guide recovery.
- The three sibling branches (`PROTO_BASIC=0x01`, `PROTO_EXTENDED=0x02`, `PROTO_LEGACY=0x03`) absorb coverage signal, leaving no incentive for the fuzzer to specifically pursue `0x04`.

**Combined Effect:** The fuzzer quickly finds `data[0] == 0xFF` (covering the set of `secret_unlocked = 1`) but exits early every time. Reaching line 65 requires Path B, which demands a checksum constraint the fuzzer rarely satisfies without guidance. This is the essence of **indirect input dependency**: the blocking condition checks a derived variable (`secret_unlocked`), not the raw input bytes, making the connection between input and branch opaque to the fuzzer.

**Fuzzer Barrier Severity: Critical**

---

## Suggested Solution to Unblock

### Option 1 — Remove the early return (highest priority, structural fix)

The `return 0` at line 53 is the primary blocker. Removing it allows Path A to set `secret_unlocked` and fall through to line 65. The fuzzer discovers `data[0] == 0xFF` within seconds.

```c
if (data[0] == 0xFF) {
    secret_unlocked = 1;
    // remove: return 0;
}
```

### Option 2 — Add a handcrafted seed corpus entry

Place a 2-byte seed `{0x00, 0x04}` in the corpus before campaign start:
- `data[0] = 0x00` (not 0xFF, so no early return)
- `data[1] = 0x04` (payload sum = 0x04 = `PROTO_SECURE`)

This immediately satisfies all path conditions for Path B on the very first execution.

### Option 3 — Add a fuzzer dictionary

Add `"\x04"` as a magic token in a `.dict` file passed with `-dict=`. This helps the mutation engine insert the correct payload byte via token insertion rather than random mutation.

### Option 4 — Reset global state at entry (hygiene)

Add `secret_unlocked = 0; target_reached = 0;` at the top of `LLVMFuzzerTestOneInput` to prevent non-deterministic cross-invocation state contamination, which can produce misleading coverage data.

**Priority order:** Option 1 (structural) > Option 2 (seed) > Option 3 (dictionary) > Option 4 (hygiene). Options 1 + 2 together fully unblock the branch.

---

## Summary Table

| Attribute | Detail |
|-----------|--------|
| Blocking location | `blocker_1.c:65`, true branch of `if (secret_unlocked)` |
| Root cause category | Indirect Input Dependency — Structural Short-Circuit + Checksum Barrier |
| Blocking variable | `static int secret_unlocked` (line 17) |
| Viable path to branch | Path B: `data[0] != 0xFF` + `compute_checksum == 0x04` |
| Key barrier | Early `return 0` at line 53 cuts off the easiest setter (Path A) |
| Severity | Critical |
| Primary fix | Remove `return 0` at line 53; add seed `{0x00, 0x04}` |
