---
name: libpcap blocker patterns
description: Key blocking branch patterns, top locations, and fuzzer complementarity for libpcap (2026-03-18, 170 confirmed blockers)
type: project
---

Analysis of libpcap fuzzing coverage (cmplog.cov: 53,624 lines, n4.cov: 43,075 lines). Run 2026-03-18.

**Why:** Recorded to accelerate future libpcap sessions and inform root-cause analysis.

**How to apply:** Use as baseline when re-running analysis or comparing future fuzzer runs.

## Stats
- cmplog branch pairs: 3,336; n4 branch pairs: 2,696
- Asymmetric in cmplog: 634; asymmetric in n4: 671
- Confirmed input-dependent: 170
- Unconfirmed candidates: 1,135

## Top Blockers (by flip strength)

| Rank | File | Line:Col | Blocked | Flip Strength | Confirmed By |
|------|------|----------|---------|---------------|--------------|
| 1 | `bpf_filter.c` | 203:3 | True | 28,400 | n4 |
| 2 | `optimize.c` | 1086:7 | True | 1,440 | n4 |
| 3 | `bpf_filter.c` | 311:3 | True | 1,300 | cmplog |
| 4 | `sf-pcap.c` | 558:2 | False | 794 | cmplog |
| 5 | `sf-pcap.c` | 572:2 | True | 794 | cmplog |
| 6 | `gencode.c` | 3973:7 | False | 730 | cmplog |
| 7 | `optimize.c` | 525:2 | True | 694 | cmplog |
| 8 | `optimize.c` | 564:2 | True | 694 | cmplog |

## Key Patterns

- **bpf_filter.c** (ranks 1 and 3): `#endif` at 203:3 and 311:3 — likely compiler preprocessor branches around platform/version-specific BPF filter code. Cmplog misses 203:3 True (flip 28,400 by n4); n4 misses 311:3 True (flip 1,300 by cmplog). Strong asymmetry between fuzzers here.
- **optimize.c**: Multiple high-ranking blockers (525:2, 564:2, 1086:7, 1381:2) — BPF optimizer code is a significant source of unexplored branches.
- **sf-pcap.c**: Several blockers in pcap save-file parsing (240:6, 241:6, 244:7, 245:7, 289:3, 338:7, 391:2, 400:2, 409:6, 558:2, 572:2, 754:8) — input format handling has many asymmetric branches.
- **gencode.c**: Heavily represented (ranks 6, 9–15, 17–21, 23–32, etc.) — BPF code generation is the largest source of confirmed blockers. Lines around 6000–6131 form a cluster of related True-blocked branches (switch/chain pattern).
- **build_llvm_cov/grammar.c and scanner.c**: Many blockers in the bpf filter expression parser and lexer — grammar rules for filter expressions are incompletely exercised.

## Fuzzer Complementarity

- **cmplog** is the primary confirmer for most blockers (confirms ~155 of 170).
- **n4** is the primary confirmer for ranks 1, 2, 50–52, 87, 93, 114–116, 135–139 — indicates n4 explores some BPF opcode paths and parser branches that cmplog does not.
- The two fuzzers are highly complementary: cmplog's asymmetric set and n4's asymmetric set have significant mutual confirmation.

## File Coverage Summary (confirmed blockers per file)

- `gencode.c`: ~80+ blockers (dominant source)
- `build_llvm_cov/grammar.c`: ~30+ blockers (filter expression grammar)
- `build_llvm_cov/scanner.c`: ~20+ blockers (filter expression lexer)
- `optimize.c`: ~10 blockers
- `sf-pcap.c`: ~12 blockers
- `bpf_filter.c`: 4 blockers
- `nametoaddr.c`: 5 blockers
- `sf-pcapng.c`: 1 blocker
