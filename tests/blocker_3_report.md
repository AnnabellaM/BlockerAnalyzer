# Blocking Branch Root Cause Report: blocker_3

**Target:** `/home/miao/work/BlockerAnalyzer/targets/blocker_3/blocker_3.c`
**Analysis Date:** 2026-03-17

---

## BLOCKING BRANCH ANALYSIS

```
Location:       blocker_3.c:26 (process_packet)
Branch:         if (gate)  — true side (leads to __builtin_trap())
Coverage:       0 hits (never reached by any fuzzer input)
```

### Execution Path to Branch

```
LLVMFuzzerTestOneInput()   [line 34]
  size >= 1 check passes
  process_packet(data, size)   [line 39]
    gate = check_gate(&g_session)   [line 24]
      returns g_session.unlocked   [line 19]
    if (gate) { __builtin_trap(); }   [line 26]  <-- BLOCKING BRANCH
```

### Path Conditions Required

1. `size >= 1` — trivially satisfied by any non-empty input; not the barrier.
2. `gate != 0` — requires `check_gate(&g_session)` to return non-zero.
3. `g_session.unlocked != 0` — requires that field to be non-zero at call time.
4. `g_session.unlocked` was initialized to `0` at compile time (line 14, the `#else` branch of `#ifdef UNLOCK_SECRET`) and **no code anywhere in the program ever writes to it at runtime**.

---

### Root Cause Category

**Compile-Time Gate / Dead Code Under Default Build Configuration**

### Root Cause Explanation

`g_session` is a `static` global defined at file scope. Its `unlocked` field is set once by the linker/loader:

- With `-DUNLOCK_SECRET`: initializer is `{ 1 }` (line 12) — branch is always taken.
- Without it (default): initializer is `{ 0 }` (line 14) — branch is **permanently unreachable for the entire process lifetime**.

Three structural facts make this a hard compile-time gate:

1. **No runtime mutation path exists.** There are zero assignments to `g_session.unlocked` (or `g_session`) anywhere in any function body. The value is fixed in the binary's `.data` segment.

2. **`check_gate` is a pure, trivial read.** Lines 17-20 do nothing but `return s->unlocked`. No input-derived data flows into it. Its return value is a compile-time constant `0` for the entire fuzzing session.

3. **`gate` is therefore a compile-time constant `0`.** Under `-O1` or higher the compiler will likely eliminate the true branch from the object code entirely — making it absent from the binary, not merely hard to reach.

4. **The fuzzer's input (`data`, `len`) has zero influence on `gate`.** Lines 30-31 explicitly discard both with `(void)` casts. No mutation strategy can change what `gate` evaluates to.

This is the strongest possible fuzzing barrier: **logically impossible to satisfy** in the default-compiled binary. No corpus, dictionary, coverage-guided mutation, or longer runtime helps.

**Fuzzer Barrier Severity: Critical**

---

## Suggested Solution to Unblock

### Option 1 — Recompile with the unlock flag (quickest, for targeted testing)

```sh
clang -fsanitize=fuzzer,address -DUNLOCK_SECRET -o blocker_3_unlocked blocker_3.c
```

This selects line 12 (`{ 1 }`), making `gate` always `1`. Use this build to confirm the instrumented path is reachable and sanitizers fire on `__builtin_trap()`.

### Option 2 — Make the gate runtime-controllable via fuzz input (recommended for autonomous discovery)

Refactor `LLVMFuzzerTestOneInput` so byte 0 drives the session state:

```c
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < 1)
        return 0;

    g_session.unlocked = data[0];           // gate is now fuzzer-controlled
    process_packet(data + 1, size - 1);

    return 0;
}
```

Any input with a non-zero first byte reaches the true branch. A coverage-guided fuzzer finds this within the first few hundred executions.

### Option 3 — Add a libFuzzer dictionary entry

```
# fuzzer.dict
"\x01"
```

```sh
./blocker_3_fuzzer -dict=fuzzer.dict corpus/
```

Seeds the mutation engine with the required byte value (only effective if Option 2 is also applied, since the gate is otherwise not input-driven).

### Option 4 — Dual build targets with merged coverage

```makefile
blocker_3_locked:   # build without -DUNLOCK_SECRET
blocker_3_unlocked: # build with    -DUNLOCK_SECRET
```

Run both, merge profiles with `llvm-profdata merge`, generate a single `llvm-cov` report. Both sides appear covered in aggregate.

### Option 5 — Remove the dead compile-time branch (code quality fix)

If the `UNLOCK_SECRET` path is vestigial debug code, delete lines 11-15, replace with a single unconditional initializer, and remove the `if (gate)` block. This eliminates the unreachable branch from all future coverage reports without requiring special build flags.

---

## Summary Table

| Property | Value |
|---|---|
| Blocking branch | `blocker_3.c:26`, true side of `if (gate)` |
| Root cause category | Compile-Time Gate / Dead Code |
| Fuzzer barrier severity | Critical |
| Input-controllable? | No — fuzzer input bytes have zero influence on `gate` |
| Fix requires recompilation? | Yes (Options 1, 4) or source refactoring (Options 2, 3, 5) |
| Recommended action | Option 2 for fuzz coverage; Option 5 if the path is vestigial |
