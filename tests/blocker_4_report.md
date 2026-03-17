# Blocking Branch Root Cause Report: blocker_4

**Target:** `/home/miao/work/BlockerAnalyzer/targets/blocker_4/blocker_4.c`
**Analysis Date:** 2026-03-17

---

## BLOCKING BRANCH ANALYSIS

```
Location:         blocker_4.c:32  (process_packet)
Branch Condition: if (a && b && c)
Coverage Status:  True branch — 0 hits; False branch — 3 hits
```

### Execution Path to Branch

```
LLVMFuzzerTestOneInput (line 37)
  → [size >= 8 (MIN_SIZE)]
  → process_packet(data, size) (line 42)
    → check_header(data)         → a  (line 28)
    → check_type(data)           → b  (line 29)
    → check_footer(data, size)   → c  (line 30)
    → if (a && b && c)           ← BLOCKING BRANCH (line 32)
         → __builtin_trap()      ← never reached
```

### Path Conditions Required

1. `size >= 8`
2. `data[0]==0xDE` AND `data[1]==0xAD`  (MAGIC_HEADER, line 7)
3. `data[2]==0xCA` AND `data[3]==0xFE` AND `data[4]==0xBA` AND `data[5]==0xBE`  (MAGIC_TYPE, line 8)
4. `data[size-2]==0xC0` AND `data[size-1]==0xDE`  (MAGIC_FOOTER, line 9)
5. All of conditions 2–4 must be true in the **same input simultaneously**

---

### Root Cause Category

**Magic Value Conjunction — No Coverage Gradient**

### Root Cause Explanation

The branch at line 32 is protected by three independent multi-byte magic comparisons that must all be satisfied simultaneously:

| Check | Bytes | Magic Value | Probability (random) |
|---|---|---|---|
| `check_header` (line 11) | `data[0..1]` | `{0xDE, 0xAD}` | ~1/65,536 |
| `check_type` (line 16) | `data[2..5]` | `{0xCA, 0xFE, 0xBA, 0xBE}` | ~1/4.3B |
| `check_footer` (line 21) | `data[size-2..size-1]` | `{0xC0, 0xDE}` | ~1/65,536 |

Combined probability for a random input: **~1/2^56** — cryptographically infeasible by random mutation.

The critical structural problem is the **absence of a coverage gradient**. AFL++ CmpLog can detect and invert individual byte comparisons, but satisfying `check_header` alone does NOT change the branch outcome at line 32 — it remains False as long as `check_type` or `check_footer` also fail. Because the branch outcome (the coverage edge) is identical for "0 checks pass" and "1 or 2 checks pass", the fuzzer receives no reward for partial progress and cannot converge. The three `memcmp()` calls return their results before the branch is reached; there are no intermediate branches guarding each check individually.

Coverage data confirms this: `a` (`check_header`) was true once (col 9: `True=1`), but at that same execution `b` (`check_type`) was False (col 14: `True=0, False=1`), terminating short-circuit evaluation before `c` was ever evaluated (col 19: `True=0, False=0`).

There are no checksums, cryptographic operations, state machines, or external dependencies in the path. The sole barrier is simultaneous satisfaction of three hard-coded byte sequences at specific offsets.

**Fuzzer Barrier Severity: Critical**

Mathematically infeasible by random mutation (~1/2^56). No intermediate coverage gradient exists to guide the fuzzer toward partial solutions. Even AFL++ CmpLog, which excels at inverting individual comparisons, cannot overcome the lack of feedback for conjunctive multi-check satisfaction.

---

## Suggested Solution to Unblock

### Option 1 — Structured seed corpus (highest leverage)

Provide one seed file with the exact layout satisfying all three checks:

```
bytes 0-1: {0xDE, 0xAD}
bytes 2-5: {0xCA, 0xFE, 0xBA, 0xBE}
bytes 6-7: {0xC0, 0xDE}
```

Total: 8 bytes — the minimum valid input. This collapses the problem entirely and lets the fuzzer explore from a valid base, mutating the interior bytes freely.

```sh
printf '\xde\xad\xca\xfe\xba\xbe\xc0\xde' > corpus/seed_valid
```

### Option 2 — Fuzzer dictionary tokens

Add all three magic sequences to the AFL++/libFuzzer dictionary:

```
# blocker_4.dict
token_1="\xde\xad"
token_2="\xca\xfe\xba\xbe"
token_3="\xc0\xde"
```

Combined with mutation, this increases the chance of placing them at correct offsets, but positional placement is still random without a seed. Best used together with Option 1.

### Option 3 — Custom AFL++ mutator

Implement a mutator that always writes the three magic sequences at their correct positional offsets before returning a test case. This guarantees every generated input reaches the `__builtin_trap()` branch and fuzzes only the bytes between the magic fields.

### Option 4 — Split checks into separate guarded branches

Refactor `process_packet` to check each magic value independently, creating intermediate coverage edges:

```c
static void process_packet(const uint8_t *data, size_t size)
{
    if (!check_header(data)) return;
    if (!check_type(data))   return;
    if (!check_footer(data, size)) return;
    __builtin_trap();
}
```

Now each satisfied check advances coverage, giving the fuzzer a gradient to follow. No seed changes needed — AFL++ CmpLog will converge through each gate individually.

**Priority order:** Option 4 (structural refactor, best long-term) > Option 1 (seed, fastest result) > Option 2 (dictionary, supports Option 1) > Option 3 (custom mutator, most engineering effort).

---

## Summary Table

| Attribute | Detail |
|-----------|--------|
| Blocking location | `blocker_4.c:32`, true branch of `if (a && b && c)` |
| Root cause category | Magic Value Conjunction — No Coverage Gradient |
| Sub-checks | `check_header` (2B), `check_type` (4B), `check_footer` (2B) |
| Combined random probability | ~1/2^56 |
| Coverage gradient? | None — partial satisfaction gives no new edges |
| Severity | Critical |
| Primary fix | Structured seed `\xDE\xAD\xCA\xFE\xBA\xBE\xC0\xDE` (8 bytes) |
| Structural fix | Split conjunction into sequential early-return guards |
