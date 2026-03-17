---
name: blocker_1 AFL++ campaign findings
description: Key findings from the AFL++ v4.36a fuzzing campaign on blocker_1, including seed queue stagnation pattern and identified root causes
type: project
---

Campaign: AFL++ v4.36a, 58 seconds, 1,488,444 execs, 70% bitmap coverage (14/20 edges), 0 crashes.

**Blocking branch:** `blocker_1.c:65`, true side of `if (phase_one_done && phase_two_done)` — never reached. `Branch (65:27): [True: 0, False: 2]`.

**Root cause 1 (primary, structural):** `phase_two_done` is set at lines 52–53 which includes `return 0` — exits before reaching line 65. `phase_one_done` is set via FUNC() which is only called when the line 47–53 block is NOT taken. The two setters have mutually exclusive preconditions on `data[0]`; the conjunction is structurally impossible in a single execution.

**Root cause 2 (secondary, checksum opacity):** `phase_one_done` requires `compute_checksum(fp->data, fp->data_len) == 0x04`. CmpLog was not enabled (`cmplog_time: 0`). No dictionary. Fuzzer cannot observe the implicit comparison operands. Coverage shows only 2 hits on the PROTO_SECURE branch (line 37) out of 47 FUNC() invocations.

**Seed queue stagnation signature:** 15 corpus entries total. Seeds 000001–000010 all sourced from id:000000 (original seed) within first 1,648 execs (62ms). Seeds 000011–000014 form a strict depth chain (10 → 11 → 12 → 13 → 14) with escalating rep counts (5, 22, 13, 21). After id:000014 at exec 30,618, no new finds for 1,457,826 execs (97.9% of budget). Cycles_wo_finds: 366/374.

**All mutation operators:** Havoc only. No deterministic stages preserved. No splice. No CmpLog/redqueen.

**Why:** Research analysis campaign. Findings documented in `output/blocker_1_coverage_analysis.md`.

**How to apply:** Use this stagnation signature (rapid early diversification + single depth chain + escalating rep counts + 97%+ cycles without finds) as a fingerprint for conjunction/checksum blockers in future campaigns.
