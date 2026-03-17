---
name: htslib blocker patterns
description: Key blocking branch patterns and fuzzer complementarity observed in htslib coverage analysis
type: project
---

Analysis date: 2026-03-17. Fuzzers: cmplog (6,247 branch pairs) and n4 (3,297 branch pairs).

**Result**: 217 confirmed input-dependent blocking branches out of 3,688 asymmetric candidates total.

**Dominant direction**: The vast majority of confirmed blockers (210+) have cmplog hitting the missing side — meaning n4 is the primary fuzzer that fails to reach those branches and cmplog confirms their reachability. A small number (~7) are reversed (n4 confirms for cmplog).

**Top blocking locations by flip strength**:
- `cram_free_container` @ 3747:13 — flip strength 138,000 (highest; n4 misses the False branch)
- `header.c:ks_resize` @ 162:6 — flip strength 27,800
- `hts.c:get_severity_tag` @ 5123:5 and 5125:5 — switch-case cluster (C003), flip strength 22,600 each
- `pool_destroy` @ 87:17 — flip strength 12,400
- `sam_hdr_fill_hrecs` @ 1142:21 — flip strength 7,260

**Recurring functions with multiple blocking branches**:
- `cram_free_container`: at least 8 confirmed blockers across lines 3720–3781
- `cram_free_slice`: at least 10 confirmed blockers across lines 4430–4498
- `hts_detect_format2`: at least 12 confirmed blockers across lines 576–746
- `sam_hdr_destroy`: 5 confirmed blockers at lines 122, 127, 134, 136
- `hts_hopen`: 5+ confirmed blockers at lines 1563, 1564, 1572, 1573, 1583, 1584, 1587
- `cram_encode_container`: 5+ confirmed blockers
- `cram_encode.c:process_one_read`: 8+ confirmed blockers

**Fuzzer complementarity**: cmplog consistently reaches CRAM codec and header-handling paths that n4 misses. n4-confirmed blockers are rare — appearing in `kh_resize` hash-table functions (cram_encode.c, cram_stats.c) and bgzf write/compression paths.

**Why:** First full htslib run; patterns here should accelerate future root-cause and coverage-analyst analysis.

**How to apply:** When root-cause analyzing htslib blockers, prioritize `cram_free_container`, `hts_detect_format2`, and `cram_free_slice` clusters. The CRAM codec and SAM header parsing subsystems are the primary blind spots for n4.
