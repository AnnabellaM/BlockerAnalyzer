# Blocking Branch Root Cause Report: blocker_2

**Target:** `/home/miao/work/BlockerAnalyzer/targets/blocker_2/blocker_2.c`
**Analysis Date:** 2026-03-17

---

## BLOCKING BRANCH ANALYSIS

```
Location:         blocker_2.c:37  (LLVMFuzzerTestOneInput)
Branch Condition: if (secret_unlocked)   [true side -> __builtin_trap()]
Coverage Status:  0 hits (never taken)
```

### Execution Path to Branch

```
LLVMFuzzerTestOneInput(data, size)
  └─ [size >= 2 check passes]
  └─ FilePacket fp initialised and populated from input bytes
  └─ if (secret_unlocked)   <- BLOCKING BRANCH (line 37)
       └─ __builtin_trap()  <- never reached
```

`process_secret()` — the only function that writes `secret_unlocked = 1` — is defined at line 19 but is **never called from anywhere in the program**.

### Path Conditions Required

1. `size >= 2` — satisfied trivially.
2. `secret_unlocked == 1` at line 37.

Condition 2 can only be true if `process_secret()` has executed. Because `process_secret()` has no callers, the variable stays `0` for the entire lifetime of the process.

---

### Root Cause Category

**Code Unreachability — Missing Function Call (Dead Writer)**

### Root Cause Explanation

`secret_unlocked` is a file-scoped static integer initialised to `0` (line 17). Static-storage-duration variables in C are zero-initialised before any code runs and retain their value across calls within a single fuzzing process.

The only assignment to `secret_unlocked` in the entire translation unit is inside `process_secret()` (line 21). A call-graph search rooted at `LLVMFuzzerTestOneInput` shows:

| Caller | Calls |
|--------|-------|
| `LLVMFuzzerTestOneInput` | `memset`, `memcpy` (stdlib only) |

`process_secret` appears in no caller. Its `static` linkage prevents calls from other translation units. There is no function pointer, callback, or indirect dispatch that could reach it at runtime.

Because `secret_unlocked` starts at `0` and no reachable code can write `1` to it, the true branch of `if (secret_unlocked)` is permanently dead — regardless of input length, content, or mutation strategy. This is not a fuzzer limitation; it is a structural program invariant.

**Fuzzer Barrier Severity: Critical**

Not probabilistic or input-dependent. No amount of additional fuzzing time, better seeds, or smarter mutations can produce coverage of this branch through the harness as written.

---

## Suggested Solution to Unblock

### Option 1 — Wire the call into the fuzzer harness (recommended)

Add a conditional call to `process_secret()` driven by a fuzzer-controlled input byte. Treat `data[0]` as a mode byte:

```c
// Inside LLVMFuzzerTestOneInput, after populating fp:
if (data[0] == 0x42) {
    process_secret(&fp);
}
```

**Concrete steps:**
1. Add the conditional call above inside `LLVMFuzzerTestOneInput` after `fp` is populated.
2. Add a seed file containing `\x42` followed by any payload to the seed corpus.
3. Add `\x42` as a dictionary token in the AFL++/libFuzzer dictionary file.
4. Re-run the fuzzer; coverage of line 38 (`__builtin_trap`) will be achieved rapidly.

### Option 2 — Use a flags byte in a two-phase input protocol

Define bit 0 of `data[0]` as the "unlock secret" flag:

```c
uint8_t flags = data[0];
if (flags & 0x01) {
    process_secret(&fp);
}
```

This is cleaner if the intent is to model `__builtin_trap` as a crash-on-invariant-violation guard that can be triggered through normal protocol variation.

### Option 3 — Separate harness entry point

If the production design has `process_secret` called from a separate code path, create a second fuzzing harness that pre-calls `process_secret` before exercising the guarded logic. This keeps the main harness structure unmodified.

### Supporting fuzzer configuration (all options)

- **Seed corpus:** include at least one seed satisfying the unlock condition.
- **Dictionary:** add the unlock trigger byte(s) as dictionary tokens.
- **Sanitizer:** compile with `-fsanitize=address,undefined` so `SIGILL` from `__builtin_trap()` is captured cleanly by crash detection.

---

## Summary Table

| Attribute | Detail |
|-----------|--------|
| Blocking location | `blocker_2.c:37`, true branch of `if (secret_unlocked)` |
| Root cause category | Code Unreachability — Missing Function Call (Dead Writer) |
| Blocking variable | `static int secret_unlocked` (line 17) |
| Sole writer | `process_secret()` (line 21) — never called |
| Input-dependence | None — no input can change `secret_unlocked` |
| Severity | Critical |
| Primary fix | Call `process_secret()` from a fuzzer-input-driven conditional in `LLVMFuzzerTestOneInput` |
