# Input-Dependent Blocking Branches — libpcap (All, Ranked by Flip Strength)

**Coverage sources:** `coverage/libpcap/cmplog.cov` (AFL++ cmplog), `coverage/libpcap/n4.cov` (AFL++ n4)  
**Analysis date:** 2026-03-17  
**Ranking:** descending by *flip strength* = hitcount of the blocked side in the confirming fuzzer

## Summary

| Metric | Value |
|--------|-------|
| Branch pairs (cmplog) | 3,336 |
| Branch pairs (n4) | 2,696 |
| Asymmetric in cmplog | 634 |
| Asymmetric in n4 | 671 |
| **Confirmed input-dependent** | **170** |
| Unconfirmed candidates | 1,135 |

## Ranked Summary Table

| Rank | Function | Line:Col | Blocked | Flip Strength | cmplog T:F | n4 T:F | Confirmed By |
|------|----------|----------|---------|---------------|------------|--------|--------------|
| 1 | `/benchmarks/libpcap/bpf_filter.c` | 203:3 | True | 28,400 | 0:274000 | 28400:3950000 | n4 |
| 2 | `/benchmarks/libpcap/optimize.c` | 1086:7 | True | 1,440 | 0:2790 | 1440:1930 | n4 |
| 3 | `/benchmarks/libpcap/bpf_filter.c` | 311:3 | True | 1,300 | 1300:272000 | 0:3980000 | cmplog |
| 4 | `/benchmarks/libpcap/sf-pcap.c` | 558:2 | False | 794 | 30000:794 | 295000:0 | cmplog |
| 5 | `/benchmarks/libpcap/sf-pcap.c` | 572:2 | True | 794 | 794:30000 | 0:295000 | cmplog |
| 6 | `/benchmarks/libpcap/gencode.c` | 3973:7 | False | 730 | 1680:730 | 484:0 | cmplog |
| 7 | `/benchmarks/libpcap/optimize.c` | 525:2 | True | 694 | 694:915000 | 0:16900000 | cmplog |
| 8 | `/benchmarks/libpcap/optimize.c` | 564:2 | True | 694 | 694:825000 | 0:16399999 | cmplog |
| 9 | `/benchmarks/libpcap/gencode.c` | 6065:2 | False | 663 | 453:663 | 32:0 | cmplog |
| 10 | `/benchmarks/libpcap/gencode.c` | 6131:2 | False | 660 | 452:660 | 30:0 | cmplog |
| 11 | `/benchmarks/libpcap/gencode.c` | 1204:2 | True | 447 | 447:479 | 0:35 | cmplog |
| 12 | `/benchmarks/libpcap/gencode.c` | 6060:2 | True | 445 | 445:671 | 0:32 | cmplog |
| 13 | `/benchmarks/libpcap/gencode.c` | 6126:2 | True | 445 | 445:667 | 0:30 | cmplog |
| 14 | `/benchmarks/libpcap/optimize.c` | 1381:2 | True | 347 | 347:613000 | 0:19900000 | cmplog |
| 15 | `/benchmarks/libpcap/gencode.c` | 6010:2 | False | 216 | 901:216 | 32:0 | cmplog |
| 16 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3898:1 | True | 215 | 215:91500 | 0:815000 | cmplog |
| 17 | `/benchmarks/libpcap/gencode.c` | 6000:2 | True | 215 | 215:902 | 0:32 | cmplog |
| 18 | `/benchmarks/libpcap/gencode.c` | 6059:2 | True | 215 | 215:901 | 0:32 | cmplog |
| 19 | `/benchmarks/libpcap/gencode.c` | 6093:2 | True | 212 | 212:900 | 0:30 | cmplog |
| 20 | `/benchmarks/libpcap/gencode.c` | 6103:2 | False | 212 | 900:212 | 30:0 | cmplog |
| 21 | `/benchmarks/libpcap/gencode.c` | 6125:2 | True | 212 | 212:900 | 0:30 | cmplog |
| 22 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2706:3 | True | 197 | 197:101000 | 0:1280000 | cmplog |
| 23 | `/benchmarks/libpcap/gencode.c` | 7405:30 | True | 183 | 183:1 | 0:2 | cmplog |
| 24 | `/benchmarks/libpcap/gencode.c` | 3968:2 | True | 148 | 148:13000 | 0:14200 | cmplog |
| 25 | `/benchmarks/libpcap/gencode.c` | 4320:2 | True | 126 | 126:13000 | 0:14200 | cmplog |
| 26 | `/benchmarks/libpcap/gencode.c` | 4330:2 | True | 99 | 99:13100 | 0:14200 | cmplog |
| 27 | `/benchmarks/libpcap/gencode.c` | 4317:2 | True | 84 | 84:13100 | 0:14200 | cmplog |
| 28 | `/benchmarks/libpcap/gencode.c` | 4332:2 | True | 84 | 84:13100 | 0:14200 | cmplog |
| 29 | `/benchmarks/libpcap/gencode.c` | 7275:2 | True | 84 | 84:3700 | 0:1840 | cmplog |
| 30 | `/benchmarks/libpcap/gencode.c` | 7292:20 | True | 84 | 84:2790 | 0:1820 | cmplog |
| 31 | `/benchmarks/libpcap/gencode.c` | 4323:2 | True | 81 | 81:13100 | 0:14200 | cmplog |
| 32 | `/benchmarks/libpcap/gencode.c` | 5851:2 | True | 78 | 78:846 | 0:1460 | cmplog |
| 33 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2340:3 | True | 67 | 67:101000 | 0:1280000 | cmplog |
| 34 | `/benchmarks/libpcap/gencode.c` | 3970:2 | True | 64 | 64:13100 | 0:14200 | cmplog |
| 35 | `/benchmarks/libpcap/gencode.c` | 3969:2 | True | 60 | 60:13100 | 0:14200 | cmplog |
| 36 | `/benchmarks/libpcap/gencode.c` | 1182:2 | True | 48 | 48:11700 | 0:15600 | cmplog |
| 37 | `/benchmarks/libpcap/gencode.c` | 4326:2 | True | 42 | 42:13100 | 0:14200 | cmplog |
| 38 | `/benchmarks/libpcap/gencode.c` | 7280:21 | True | 40 | 40:699 | 0:1680 | cmplog |
| 39 | `/benchmarks/libpcap/gencode.c` | 4325:2 | True | 38 | 38:13100 | 0:14200 | cmplog |
| 40 | `/benchmarks/libpcap/gencode.c` | 7308:2 | True | 37 | 37:3750 | 0:1840 | cmplog |
| 41 | `/benchmarks/libpcap/gencode.c` | 4718:2 | True | 30 | 30:22500 | 0:51100 | cmplog |
| 42 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2436:3 | True | 28 | 28:101000 | 0:1280000 | cmplog |
| 43 | `/benchmarks/libpcap/gencode.c` | 7435:26 | False | 27 | 1:27 | 1:0 | cmplog |
| 44 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3688:1 | True | 26 | 26:91700 | 0:815000 | cmplog |
| 45 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2544:3 | True | 25 | 25:101000 | 0:1280000 | cmplog |
| 46 | `/benchmarks/libpcap/gencode.c` | 1180:2 | True | 24 | 24:11700 | 0:15600 | cmplog |
| 47 | `/benchmarks/libpcap/gencode.c` | 5906:2 | True | 23 | 23:901 | 0:1460 | cmplog |
| 48 | `/benchmarks/libpcap/gencode.c` | 4324:2 | True | 20 | 20:13200 | 0:14200 | cmplog |
| 49 | `/benchmarks/libpcap/gencode.c` | 6628:2 | True | 20 | 20:2140 | 0:1170 | cmplog |
| 50 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3683:1 | True | 19 | 0:91800 | 19:815000 | n4 |
| 51 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2538:3 | True | 19 | 0:101000 | 19:1280000 | n4 |
| 52 | `/benchmarks/libpcap/gencode.c` | 5899:2 | True | 17 | 0:924 | 17:1440 | n4 |
| 53 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2700:3 | True | 17 | 17:101000 | 0:1280000 | cmplog |
| 54 | `/benchmarks/libpcap/gencode.c` | 7048:7 | False | 16 | 18:16 | 1:0 | cmplog |
| 55 | `/benchmarks/libpcap/nametoaddr.c` | 322:6 | False | 13 | 20:13 | 1:0 | cmplog |
| 56 | `/benchmarks/libpcap/nametoaddr.c` | 407:6 | True | 13 | 13:20 | 0:1 | cmplog |
| 57 | `/benchmarks/libpcap/gencode.c` | 5825:2 | True | 13 | 13:911 | 0:1460 | cmplog |
| 58 | `/benchmarks/libpcap/sf-pcap.c` | 241:6 | False | 12 | 891:12 | 870:0 | cmplog |
| 59 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2244:3 | True | 12 | 12:101000 | 0:1280000 | cmplog |
| 60 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2918:3 | True | 12 | 12:101000 | 0:1280000 | cmplog |
| 61 | `/benchmarks/libpcap/sf-pcap.c` | 338:7 | True | 11 | 11:2990 | 0:8710 | cmplog |
| 62 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3828:1 | True | 11 | 11:91700 | 0:815000 | cmplog |
| 63 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2792:3 | True | 11 | 11:101000 | 0:1280000 | cmplog |
| 64 | `/benchmarks/libpcap/gencode.c` | 2829:2 | True | 11 | 11:2400 | 0:484 | cmplog |
| 65 | `/benchmarks/libpcap/gencode.c` | 3039:2 | True | 11 | 11:712 | 0:1040 | cmplog |
| 66 | `/benchmarks/libpcap/gencode.c` | 5837:2 | True | 11 | 11:913 | 0:1460 | cmplog |
| 67 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2598:3 | True | 10 | 10:101000 | 0:1280000 | cmplog |
| 68 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2286:3 | True | 9 | 9:101000 | 0:1280000 | cmplog |
| 69 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 3253:3 | True | 9 | 9:101000 | 0:1280000 | cmplog |
| 70 | `/benchmarks/libpcap/gencode.c` | 2202:2 | True | 9 | 9:2990 | 0:8710 | cmplog |
| 71 | `/benchmarks/libpcap/gencode.c` | 2292:2 | True | 9 | 9:2990 | 0:8710 | cmplog |
| 72 | `/benchmarks/libpcap/optimize.c` | 2221:8 | True | 8 | 8:1560 | 0:1580 | cmplog |
| 73 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3663:1 | True | 8 | 8:91700 | 0:815000 | cmplog |
| 74 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4013:1 | True | 8 | 8:91700 | 0:815000 | cmplog |
| 75 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2520:3 | True | 8 | 8:101000 | 0:1280000 | cmplog |
| 76 | `/benchmarks/libpcap/gencode.c` | 2294:2 | True | 8 | 8:2990 | 0:8710 | cmplog |
| 77 | `/benchmarks/libpcap/bpf_filter.c` | 180:8 | True | 7 | 7:44 | 0:3 | cmplog |
| 78 | `/benchmarks/libpcap/sf-pcapng.c` | 795:6 | False | 7 | 881:7 | 867:0 | cmplog |
| 79 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2262:3 | True | 7 | 7:101000 | 0:1280000 | cmplog |
| 80 | `/benchmarks/libpcap/gencode.c` | 2203:2 | True | 7 | 7:2990 | 0:8710 | cmplog |
| 81 | `/benchmarks/libpcap/gencode.c` | 5871:2 | True | 7 | 7:917 | 0:1460 | cmplog |
| 82 | `/benchmarks/libpcap/sf-pcap.c` | 289:3 | True | 6 | 6:1 | 0:1 | cmplog |
| 83 | `/benchmarks/libpcap/sf-pcap.c` | 391:2 | False | 6 | 2990:6 | 8710:0 | cmplog |
| 84 | `/benchmarks/libpcap/sf-pcap.c` | 400:2 | True | 6 | 6:2990 | 0:8710 | cmplog |
| 85 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3648:1 | True | 6 | 6:91700 | 0:815000 | cmplog |
| 86 | `/benchmarks/libpcap/gencode.c` | 2204:2 | True | 6 | 6:2990 | 0:8710 | cmplog |
| 87 | `/benchmarks/libpcap/optimize.c` | 799:7 | False | 5 | 3:0 | 5:5 | n4 |
| 88 | `/benchmarks/libpcap/nametoaddr.c` | 364:6 | False | 5 | 28:5 | 1:0 | cmplog |
| 89 | `/benchmarks/libpcap/gencode.c` | 1206:2 | True | 5 | 5:921 | 0:35 | cmplog |
| 90 | `/benchmarks/libpcap/gencode.c` | 2437:7 | False | 5 | 214:5 | 363:0 | cmplog |
| 91 | `/benchmarks/libpcap/gencode.c` | 5849:2 | True | 5 | 5:919 | 0:1460 | cmplog |
| 92 | `/benchmarks/libpcap/gencode.c` | 7606:2 | True | 5 | 5:858 | 0:12000 | cmplog |
| 93 | `/benchmarks/libpcap/optimize.c` | 1266:9 | True | 4 | 0:118 | 4:627 | n4 |
| 94 | `/benchmarks/libpcap/sf-pcap.c` | 240:6 | False | 4 | 903:4 | 870:0 | cmplog |
| 95 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4018:1 | True | 4 | 4:91700 | 0:815000 | cmplog |
| 96 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 5633:43 | True | 4 | 4:1760 | 0:2640 | cmplog |
| 97 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2508:3 | True | 4 | 4:101000 | 0:1280000 | cmplog |
| 98 | `/benchmarks/libpcap/gencode.c` | 5610:2 | True | 4 | 4:206 | 0:3 | cmplog |
| 99 | `/benchmarks/libpcap/gencode.c` | 5611:2 | True | 4 | 4:206 | 0:3 | cmplog |
| 100 | `/benchmarks/libpcap/gencode.c` | 5621:2 | True | 4 | 4:206 | 0:3 | cmplog |
| 101 | `/benchmarks/libpcap/gencode.c` | 6271:2 | False | 4 | 50:4 | 4:0 | cmplog |
| 102 | `/benchmarks/libpcap/gencode.c` | 6299:6 | False | 4 | 10:4 | 1:0 | cmplog |
| 103 | `/benchmarks/libpcap/optimize.c` | 817:7 | False | 3 | 8:3 | 1:0 | cmplog |
| 104 | `/benchmarks/libpcap/sf-pcap.c` | 409:6 | True | 3 | 3:3000 | 0:8710 | cmplog |
| 105 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4414:1 | True | 3 | 3:91700 | 0:815000 | cmplog |
| 106 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 3259:3 | True | 3 | 3:101000 | 0:1280000 | cmplog |
| 107 | `/benchmarks/libpcap/gencode.c` | 2393:2 | True | 3 | 3:3000 | 0:8710 | cmplog |
| 108 | `/benchmarks/libpcap/gencode.c` | 5609:2 | True | 3 | 3:207 | 0:3 | cmplog |
| 109 | `/benchmarks/libpcap/gencode.c` | 6061:2 | True | 3 | 3:1110 | 0:32 | cmplog |
| 110 | `/benchmarks/libpcap/gencode.c` | 6127:2 | True | 3 | 3:1100 | 0:30 | cmplog |
| 111 | `/benchmarks/libpcap/gencode.c` | 6269:10 | True | 3 | 3:51 | 0:4 | cmplog |
| 112 | `/benchmarks/libpcap/gencode.c` | 6622:10 | True | 3 | 3:2150 | 0:1170 | cmplog |
| 113 | `/benchmarks/libpcap/gencode.c` | 7607:2 | True | 3 | 3:860 | 0:12000 | cmplog |
| 114 | `/benchmarks/libpcap/sf-pcap.c` | 754:8 | True | 2 | 0:16 | 2:252 | n4 |
| 115 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4038:1 | True | 2 | 0:91800 | 2:815000 | n4 |
| 116 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2610:3 | True | 2 | 0:101000 | 2:1280000 | n4 |
| 117 | `/benchmarks/libpcap/nametoaddr.c` | 423:6 | True | 2 | 2:18 | 0:1 | cmplog |
| 118 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3628:1 | True | 2 | 2:91800 | 0:815000 | cmplog |
| 119 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4008:1 | True | 2 | 2:91800 | 0:815000 | cmplog |
| 120 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 5743:9 | True | 2 | 2:17300 | 0:119000 | cmplog |
| 121 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2424:3 | True | 2 | 2:101000 | 0:1280000 | cmplog |
| 122 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2460:3 | True | 2 | 2:101000 | 0:1280000 | cmplog |
| 123 | `/benchmarks/libpcap/gencode.c` | 2412:2 | True | 2 | 2:3000 | 0:8710 | cmplog |
| 124 | `/benchmarks/libpcap/gencode.c` | 2869:7 | True | 2 | 2:2380 | 0:471 | cmplog |
| 125 | `/benchmarks/libpcap/gencode.c` | 4668:7 | True | 2 | 2:2950 | 0:2230 | cmplog |
| 126 | `/benchmarks/libpcap/gencode.c` | 5612:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 127 | `/benchmarks/libpcap/gencode.c` | 5615:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 128 | `/benchmarks/libpcap/gencode.c` | 5616:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 129 | `/benchmarks/libpcap/gencode.c` | 5617:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 130 | `/benchmarks/libpcap/gencode.c` | 5618:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 131 | `/benchmarks/libpcap/gencode.c` | 5620:2 | True | 2 | 2:208 | 0:3 | cmplog |
| 132 | `/benchmarks/libpcap/gencode.c` | 5862:2 | True | 2 | 2:922 | 0:1460 | cmplog |
| 133 | `/benchmarks/libpcap/gencode.c` | 7024:2 | True | 2 | 2:102 | 0:2070 | cmplog |
| 134 | `/benchmarks/libpcap/gencode.c` | 7362:6 | True | 2 | 2:21 | 0:57 | cmplog |
| 135 | `/benchmarks/libpcap/optimize.c` | 1263:9 | True | 1 | 0:118 | 1:631 | n4 |
| 136 | `/benchmarks/libpcap/bpf_filter.c` | 179:8 | True | 1 | 0:75 | 1:26 | n4 |
| 137 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3998:1 | True | 1 | 0:91800 | 1:815000 | n4 |
| 138 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4159:1 | True | 1 | 0:91800 | 1:815000 | n4 |
| 139 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 1993:3 | True | 1 | 0:101000 | 1:1280000 | n4 |
| 140 | `/benchmarks/libpcap/sf-pcap.c` | 244:7 | False | 1 | 889:1 | 867:0 | cmplog |
| 141 | `/benchmarks/libpcap/sf-pcap.c` | 245:7 | False | 1 | 888:1 | 867:0 | cmplog |
| 142 | `/benchmarks/libpcap/nametoaddr.c` | 647:7 | True | 1 | 1:7610 | 0:427 | cmplog |
| 143 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3578:1 | True | 1 | 1:91800 | 0:815000 | cmplog |
| 144 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3653:1 | True | 1 | 1:91800 | 0:815000 | cmplog |
| 145 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 3923:1 | True | 1 | 1:91800 | 0:815000 | cmplog |
| 146 | `/benchmarks/libpcap/build_llvm_cov/scanner.c` | 4043:1 | True | 1 | 1:91800 | 0:815000 | cmplog |
| 147 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 1975:11 | True | 1 | 1:11 | 0:4 | cmplog |
| 148 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 1981:18 | True | 1 | 1:10 | 0:4 | cmplog |
| 149 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2030:18 | True | 1 | 1:2150 | 0:158 | cmplog |
| 150 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2048:11 | True | 1 | 1:9 | 0:4 | cmplog |
| 151 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2078:18 | True | 1 | 1:17 | 0:54 | cmplog |
| 152 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2232:3 | True | 1 | 1:101000 | 0:1280000 | cmplog |
| 153 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2430:3 | True | 1 | 1:101000 | 0:1280000 | cmplog |
| 154 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2514:3 | True | 1 | 1:101000 | 0:1280000 | cmplog |
| 155 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 2929:3 | True | 1 | 1:101000 | 0:1280000 | cmplog |
| 156 | `/benchmarks/libpcap/build_llvm_cov/grammar.c` | 3176:3 | True | 1 | 1:101000 | 0:1280000 | cmplog |
| 157 | `/benchmarks/libpcap/gencode.c` | 2398:2 | True | 1 | 1:3000 | 0:8710 | cmplog |
| 158 | `/benchmarks/libpcap/gencode.c` | 3885:6 | True | 1 | 1:1690 | 0:484 | cmplog |
| 159 | `/benchmarks/libpcap/gencode.c` | 5614:2 | True | 1 | 1:209 | 0:3 | cmplog |
| 160 | `/benchmarks/libpcap/gencode.c` | 5619:2 | True | 1 | 1:209 | 0:3 | cmplog |
| 161 | `/benchmarks/libpcap/gencode.c` | 5823:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 162 | `/benchmarks/libpcap/gencode.c` | 5826:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 163 | `/benchmarks/libpcap/gencode.c` | 5828:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 164 | `/benchmarks/libpcap/gencode.c` | 5835:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 165 | `/benchmarks/libpcap/gencode.c` | 5854:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 166 | `/benchmarks/libpcap/gencode.c` | 5870:2 | True | 1 | 1:923 | 0:1460 | cmplog |
| 167 | `/benchmarks/libpcap/gencode.c` | 6017:2 | True | 1 | 1:1110 | 0:32 | cmplog |
| 168 | `/benchmarks/libpcap/gencode.c` | 6277:2 | True | 1 | 1:53 | 0:4 | cmplog |
| 169 | `/benchmarks/libpcap/gencode.c` | 7361:24 | True | 1 | 1:23 | 0:57 | cmplog |
| 170 | `/benchmarks/libpcap/gencode.c` | 7377:2 | True | 1 | 1:9 | 0:43 | cmplog |

## Detail Listings

### 1. `/benchmarks/libpcap/bpf_filter.c` @ 203:3
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 274,000, n4: 3,950,000)
- **Flip strength**: 28,400 (blocked side hit 28,400× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:274,000
- **n4 coverage**:     T:28,400  F:3,950,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_203_3_T` — cmplog:0  n4:28,400
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_203_3_F` — cmplog:274,000  n4:3,950,000

### 2. `/benchmarks/libpcap/optimize.c` @ 1086:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,790, n4: 1,930)
- **Flip strength**: 1,440 (blocked side hit 1,440× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,790
- **n4 coverage**:     T:1,440  F:1,930
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_1086_7_T` — cmplog:0  n4:1,440
  - `libpcap_/benchmarks/libpcap/optimize.c_1086_7_F` — cmplog:2,790  n4:1,930

### 3. `/benchmarks/libpcap/bpf_filter.c` @ 311:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 272,000, n4: 3,980,000)
- **Flip strength**: 1,300 (blocked side hit 1,300× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,300  F:272,000
- **n4 coverage**:     T:0  F:3,980,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_311_3_T` — cmplog:1,300  n4:0
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_311_3_F` — cmplog:272,000  n4:3,980,000

### 4. `/benchmarks/libpcap/sf-pcap.c` @ 558:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 30,000, n4: 295,000)
- **Flip strength**: 794 (blocked side hit 794× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:30,000  F:794
- **n4 coverage**:     T:295,000  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_558_2_T` — cmplog:30,000  n4:295,000
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_558_2_F` — cmplog:794  n4:0

### 5. `/benchmarks/libpcap/sf-pcap.c` @ 572:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 30,000, n4: 295,000)
- **Flip strength**: 794 (blocked side hit 794× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:794  F:30,000
- **n4 coverage**:     T:0  F:295,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_572_2_T` — cmplog:794  n4:0
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_572_2_F` — cmplog:30,000  n4:295,000

### 6. `/benchmarks/libpcap/gencode.c` @ 3973:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,680, n4: 484)
- **Flip strength**: 730 (blocked side hit 730× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,680  F:730
- **n4 coverage**:     T:484  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3973_7_T` — cmplog:1,680  n4:484
  - `libpcap_/benchmarks/libpcap/gencode.c_3973_7_F` — cmplog:730  n4:0

### 7. `/benchmarks/libpcap/optimize.c` @ 525:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 915,000, n4: 16,900,000)
- **Flip strength**: 694 (blocked side hit 694× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:694  F:915,000
- **n4 coverage**:     T:0  F:16,900,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_525_2_T` — cmplog:694  n4:0
  - `libpcap_/benchmarks/libpcap/optimize.c_525_2_F` — cmplog:915,000  n4:16,900,000

### 8. `/benchmarks/libpcap/optimize.c` @ 564:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 825,000, n4: 16,399,999)
- **Flip strength**: 694 (blocked side hit 694× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:694  F:825,000
- **n4 coverage**:     T:0  F:16,399,999
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_564_2_T` — cmplog:694  n4:0
  - `libpcap_/benchmarks/libpcap/optimize.c_564_2_F` — cmplog:825,000  n4:16,399,999

### 9. `/benchmarks/libpcap/gencode.c` @ 6065:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 453, n4: 32)
- **Flip strength**: 663 (blocked side hit 663× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:453  F:663
- **n4 coverage**:     T:32  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6065_2_T` — cmplog:453  n4:32
  - `libpcap_/benchmarks/libpcap/gencode.c_6065_2_F` — cmplog:663  n4:0

### 10. `/benchmarks/libpcap/gencode.c` @ 6131:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 452, n4: 30)
- **Flip strength**: 660 (blocked side hit 660× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:452  F:660
- **n4 coverage**:     T:30  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6131_2_T` — cmplog:452  n4:30
  - `libpcap_/benchmarks/libpcap/gencode.c_6131_2_F` — cmplog:660  n4:0

### 11. `/benchmarks/libpcap/gencode.c` @ 1204:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 479, n4: 35)
- **Flip strength**: 447 (blocked side hit 447× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:447  F:479
- **n4 coverage**:     T:0  F:35
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_1204_2_T` — cmplog:447  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_1204_2_F` — cmplog:479  n4:35

### 12. `/benchmarks/libpcap/gencode.c` @ 6060:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 671, n4: 32)
- **Flip strength**: 445 (blocked side hit 445× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:445  F:671
- **n4 coverage**:     T:0  F:32
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6060_2_T` — cmplog:445  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6060_2_F` — cmplog:671  n4:32

### 13. `/benchmarks/libpcap/gencode.c` @ 6126:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 667, n4: 30)
- **Flip strength**: 445 (blocked side hit 445× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:445  F:667
- **n4 coverage**:     T:0  F:30
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6126_2_T` — cmplog:445  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6126_2_F` — cmplog:667  n4:30

### 14. `/benchmarks/libpcap/optimize.c` @ 1381:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 613,000, n4: 19,900,000)
- **Flip strength**: 347 (blocked side hit 347× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:347  F:613,000
- **n4 coverage**:     T:0  F:19,900,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_1381_2_T` — cmplog:347  n4:0
  - `libpcap_/benchmarks/libpcap/optimize.c_1381_2_F` — cmplog:613,000  n4:19,900,000

### 15. `/benchmarks/libpcap/gencode.c` @ 6010:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 901, n4: 32)
- **Flip strength**: 216 (blocked side hit 216× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:901  F:216
- **n4 coverage**:     T:32  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6010_2_T` — cmplog:901  n4:32
  - `libpcap_/benchmarks/libpcap/gencode.c_6010_2_F` — cmplog:216  n4:0

### 16. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3898:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,500, n4: 815,000)
- **Flip strength**: 215 (blocked side hit 215× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:215  F:91,500
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3898_1_T` — cmplog:215  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3898_1_F` — cmplog:91,500  n4:815,000

### 17. `/benchmarks/libpcap/gencode.c` @ 6000:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 902, n4: 32)
- **Flip strength**: 215 (blocked side hit 215× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:215  F:902
- **n4 coverage**:     T:0  F:32
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6000_2_T` — cmplog:215  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6000_2_F` — cmplog:902  n4:32

### 18. `/benchmarks/libpcap/gencode.c` @ 6059:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 901, n4: 32)
- **Flip strength**: 215 (blocked side hit 215× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:215  F:901
- **n4 coverage**:     T:0  F:32
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6059_2_T` — cmplog:215  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6059_2_F` — cmplog:901  n4:32

### 19. `/benchmarks/libpcap/gencode.c` @ 6093:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 900, n4: 30)
- **Flip strength**: 212 (blocked side hit 212× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:212  F:900
- **n4 coverage**:     T:0  F:30
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6093_2_T` — cmplog:212  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6093_2_F` — cmplog:900  n4:30

### 20. `/benchmarks/libpcap/gencode.c` @ 6103:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 900, n4: 30)
- **Flip strength**: 212 (blocked side hit 212× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:900  F:212
- **n4 coverage**:     T:30  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6103_2_T` — cmplog:900  n4:30
  - `libpcap_/benchmarks/libpcap/gencode.c_6103_2_F` — cmplog:212  n4:0

### 21. `/benchmarks/libpcap/gencode.c` @ 6125:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 900, n4: 30)
- **Flip strength**: 212 (blocked side hit 212× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:212  F:900
- **n4 coverage**:     T:0  F:30
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6125_2_T` — cmplog:212  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6125_2_F` — cmplog:900  n4:30

### 22. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2706:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 197 (blocked side hit 197× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:197  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2706_3_T` — cmplog:197  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2706_3_F` — cmplog:101,000  n4:1,280,000

### 23. `/benchmarks/libpcap/gencode.c` @ 7405:30
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1, n4: 2)
- **Flip strength**: 183 (blocked side hit 183× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:183  F:1
- **n4 coverage**:     T:0  F:2
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7405_30_T` — cmplog:183  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7405_30_F` — cmplog:1  n4:2

### 24. `/benchmarks/libpcap/gencode.c` @ 3968:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,000, n4: 14,200)
- **Flip strength**: 148 (blocked side hit 148× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:148  F:13,000
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3968_2_T` — cmplog:148  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_3968_2_F` — cmplog:13,000  n4:14,200

### 25. `/benchmarks/libpcap/gencode.c` @ 4320:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,000, n4: 14,200)
- **Flip strength**: 126 (blocked side hit 126× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:126  F:13,000
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4320_2_T` — cmplog:126  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4320_2_F` — cmplog:13,000  n4:14,200

### 26. `/benchmarks/libpcap/gencode.c` @ 4330:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 99 (blocked side hit 99× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:99  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4330_2_T` — cmplog:99  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4330_2_F` — cmplog:13,100  n4:14,200

### 27. `/benchmarks/libpcap/gencode.c` @ 4317:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 84 (blocked side hit 84× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4317_2_T` — cmplog:84  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4317_2_F` — cmplog:13,100  n4:14,200

### 28. `/benchmarks/libpcap/gencode.c` @ 4332:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 84 (blocked side hit 84× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4332_2_T` — cmplog:84  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4332_2_F` — cmplog:13,100  n4:14,200

### 29. `/benchmarks/libpcap/gencode.c` @ 7275:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,700, n4: 1,840)
- **Flip strength**: 84 (blocked side hit 84× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:3,700
- **n4 coverage**:     T:0  F:1,840
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7275_2_T` — cmplog:84  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7275_2_F` — cmplog:3,700  n4:1,840

### 30. `/benchmarks/libpcap/gencode.c` @ 7292:20
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,790, n4: 1,820)
- **Flip strength**: 84 (blocked side hit 84× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:2,790
- **n4 coverage**:     T:0  F:1,820
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7292_20_T` — cmplog:84  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7292_20_F` — cmplog:2,790  n4:1,820

### 31. `/benchmarks/libpcap/gencode.c` @ 4323:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 81 (blocked side hit 81× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:81  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4323_2_T` — cmplog:81  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4323_2_F` — cmplog:13,100  n4:14,200

### 32. `/benchmarks/libpcap/gencode.c` @ 5851:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 846, n4: 1,460)
- **Flip strength**: 78 (blocked side hit 78× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:78  F:846
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5851_2_T` — cmplog:78  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5851_2_F` — cmplog:846  n4:1,460

### 33. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2340:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 67 (blocked side hit 67× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:67  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2340_3_T` — cmplog:67  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2340_3_F` — cmplog:101,000  n4:1,280,000

### 34. `/benchmarks/libpcap/gencode.c` @ 3970:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 64 (blocked side hit 64× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:64  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3970_2_T` — cmplog:64  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_3970_2_F` — cmplog:13,100  n4:14,200

### 35. `/benchmarks/libpcap/gencode.c` @ 3969:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 60 (blocked side hit 60× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:60  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3969_2_T` — cmplog:60  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_3969_2_F` — cmplog:13,100  n4:14,200

### 36. `/benchmarks/libpcap/gencode.c` @ 1182:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11,700, n4: 15,600)
- **Flip strength**: 48 (blocked side hit 48× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:48  F:11,700
- **n4 coverage**:     T:0  F:15,600
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_1182_2_T` — cmplog:48  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_1182_2_F` — cmplog:11,700  n4:15,600

### 37. `/benchmarks/libpcap/gencode.c` @ 4326:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 42 (blocked side hit 42× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:42  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4326_2_T` — cmplog:42  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4326_2_F` — cmplog:13,100  n4:14,200

### 38. `/benchmarks/libpcap/gencode.c` @ 7280:21
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 699, n4: 1,680)
- **Flip strength**: 40 (blocked side hit 40× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:40  F:699
- **n4 coverage**:     T:0  F:1,680
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7280_21_T` — cmplog:40  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7280_21_F` — cmplog:699  n4:1,680

### 39. `/benchmarks/libpcap/gencode.c` @ 4325:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,100, n4: 14,200)
- **Flip strength**: 38 (blocked side hit 38× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:38  F:13,100
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4325_2_T` — cmplog:38  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4325_2_F` — cmplog:13,100  n4:14,200

### 40. `/benchmarks/libpcap/gencode.c` @ 7308:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,750, n4: 1,840)
- **Flip strength**: 37 (blocked side hit 37× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:37  F:3,750
- **n4 coverage**:     T:0  F:1,840
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7308_2_T` — cmplog:37  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7308_2_F` — cmplog:3,750  n4:1,840

### 41. `/benchmarks/libpcap/gencode.c` @ 4718:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 22,500, n4: 51,100)
- **Flip strength**: 30 (blocked side hit 30× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:30  F:22,500
- **n4 coverage**:     T:0  F:51,100
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4718_2_T` — cmplog:30  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4718_2_F` — cmplog:22,500  n4:51,100

### 42. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2436:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 28 (blocked side hit 28× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:28  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2436_3_T` — cmplog:28  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2436_3_F` — cmplog:101,000  n4:1,280,000

### 43. `/benchmarks/libpcap/gencode.c` @ 7435:26
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1, n4: 1)
- **Flip strength**: 27 (blocked side hit 27× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:27
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7435_26_T` — cmplog:1  n4:1
  - `libpcap_/benchmarks/libpcap/gencode.c_7435_26_F` — cmplog:27  n4:0

### 44. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3688:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 26 (blocked side hit 26× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:26  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3688_1_T` — cmplog:26  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3688_1_F` — cmplog:91,700  n4:815,000

### 45. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2544:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 25 (blocked side hit 25× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:25  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2544_3_T` — cmplog:25  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2544_3_F` — cmplog:101,000  n4:1,280,000

### 46. `/benchmarks/libpcap/gencode.c` @ 1180:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11,700, n4: 15,600)
- **Flip strength**: 24 (blocked side hit 24× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:24  F:11,700
- **n4 coverage**:     T:0  F:15,600
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_1180_2_T` — cmplog:24  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_1180_2_F` — cmplog:11,700  n4:15,600

### 47. `/benchmarks/libpcap/gencode.c` @ 5906:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 901, n4: 1,460)
- **Flip strength**: 23 (blocked side hit 23× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:23  F:901
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5906_2_T` — cmplog:23  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5906_2_F` — cmplog:901  n4:1,460

### 48. `/benchmarks/libpcap/gencode.c` @ 4324:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,200, n4: 14,200)
- **Flip strength**: 20 (blocked side hit 20× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:13,200
- **n4 coverage**:     T:0  F:14,200
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4324_2_T` — cmplog:20  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4324_2_F` — cmplog:13,200  n4:14,200

### 49. `/benchmarks/libpcap/gencode.c` @ 6628:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,140, n4: 1,170)
- **Flip strength**: 20 (blocked side hit 20× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:2,140
- **n4 coverage**:     T:0  F:1,170
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6628_2_T` — cmplog:20  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6628_2_F` — cmplog:2,140  n4:1,170

### 50. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3683:1
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91,800
- **n4 coverage**:     T:19  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3683_1_T` — cmplog:0  n4:19
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3683_1_F` — cmplog:91,800  n4:815,000

### 51. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2538:3
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:101,000
- **n4 coverage**:     T:19  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2538_3_T` — cmplog:0  n4:19
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2538_3_F` — cmplog:101,000  n4:1,280,000

### 52. `/benchmarks/libpcap/gencode.c` @ 5899:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 924, n4: 1,440)
- **Flip strength**: 17 (blocked side hit 17× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:924
- **n4 coverage**:     T:17  F:1,440
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5899_2_T` — cmplog:0  n4:17
  - `libpcap_/benchmarks/libpcap/gencode.c_5899_2_F` — cmplog:924  n4:1,440

### 53. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2700:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 17 (blocked side hit 17× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:17  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2700_3_T` — cmplog:17  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2700_3_F` — cmplog:101,000  n4:1,280,000

### 54. `/benchmarks/libpcap/gencode.c` @ 7048:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 18, n4: 1)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:16
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7048_7_T` — cmplog:18  n4:1
  - `libpcap_/benchmarks/libpcap/gencode.c_7048_7_F` — cmplog:16  n4:0

### 55. `/benchmarks/libpcap/nametoaddr.c` @ 322:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 20, n4: 1)
- **Flip strength**: 13 (blocked side hit 13× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:13
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_322_6_T` — cmplog:20  n4:1
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_322_6_F` — cmplog:13  n4:0

### 56. `/benchmarks/libpcap/nametoaddr.c` @ 407:6
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 20, n4: 1)
- **Flip strength**: 13 (blocked side hit 13× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:13  F:20
- **n4 coverage**:     T:0  F:1
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_407_6_T` — cmplog:13  n4:0
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_407_6_F` — cmplog:20  n4:1

### 57. `/benchmarks/libpcap/gencode.c` @ 5825:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 911, n4: 1,460)
- **Flip strength**: 13 (blocked side hit 13× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:13  F:911
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5825_2_T` — cmplog:13  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5825_2_F` — cmplog:911  n4:1,460

### 58. `/benchmarks/libpcap/sf-pcap.c` @ 241:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 891, n4: 870)
- **Flip strength**: 12 (blocked side hit 12× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:891  F:12
- **n4 coverage**:     T:870  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_241_6_T` — cmplog:891  n4:870
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_241_6_F` — cmplog:12  n4:0

### 59. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2244:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 12 (blocked side hit 12× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2244_3_T` — cmplog:12  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2244_3_F` — cmplog:101,000  n4:1,280,000

### 60. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2918:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 12 (blocked side hit 12× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2918_3_T` — cmplog:12  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2918_3_F` — cmplog:101,000  n4:1,280,000

### 61. `/benchmarks/libpcap/sf-pcap.c` @ 338:7
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_338_7_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_338_7_F` — cmplog:2,990  n4:8,710

### 62. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3828:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3828_1_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3828_1_F` — cmplog:91,700  n4:815,000

### 63. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2792:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2792_3_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2792_3_F` — cmplog:101,000  n4:1,280,000

### 64. `/benchmarks/libpcap/gencode.c` @ 2829:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,400, n4: 484)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:2,400
- **n4 coverage**:     T:0  F:484
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2829_2_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2829_2_F` — cmplog:2,400  n4:484

### 65. `/benchmarks/libpcap/gencode.c` @ 3039:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 712, n4: 1,040)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:712
- **n4 coverage**:     T:0  F:1,040
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3039_2_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_3039_2_F` — cmplog:712  n4:1,040

### 66. `/benchmarks/libpcap/gencode.c` @ 5837:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 913, n4: 1,460)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:913
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5837_2_T` — cmplog:11  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5837_2_F` — cmplog:913  n4:1,460

### 67. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2598:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 10 (blocked side hit 10× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2598_3_T` — cmplog:10  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2598_3_F` — cmplog:101,000  n4:1,280,000

### 68. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2286:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2286_3_T` — cmplog:9  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2286_3_F` — cmplog:101,000  n4:1,280,000

### 69. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 3253:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3253_3_T` — cmplog:9  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3253_3_F` — cmplog:101,000  n4:1,280,000

### 70. `/benchmarks/libpcap/gencode.c` @ 2202:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2202_2_T` — cmplog:9  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2202_2_F` — cmplog:2,990  n4:8,710

### 71. `/benchmarks/libpcap/gencode.c` @ 2292:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2292_2_T` — cmplog:9  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2292_2_F` — cmplog:2,990  n4:8,710

### 72. `/benchmarks/libpcap/optimize.c` @ 2221:8
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,560, n4: 1,580)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:1,560
- **n4 coverage**:     T:0  F:1,580
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_2221_8_T` — cmplog:8  n4:0
  - `libpcap_/benchmarks/libpcap/optimize.c_2221_8_F` — cmplog:1,560  n4:1,580

### 73. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3663:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3663_1_T` — cmplog:8  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3663_1_F` — cmplog:91,700  n4:815,000

### 74. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4013:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4013_1_T` — cmplog:8  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4013_1_F` — cmplog:91,700  n4:815,000

### 75. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2520:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2520_3_T` — cmplog:8  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2520_3_F` — cmplog:101,000  n4:1,280,000

### 76. `/benchmarks/libpcap/gencode.c` @ 2294:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2294_2_T` — cmplog:8  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2294_2_F` — cmplog:2,990  n4:8,710

### 77. `/benchmarks/libpcap/bpf_filter.c` @ 180:8
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 44, n4: 3)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:44
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_180_8_T` — cmplog:7  n4:0
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_180_8_F` — cmplog:44  n4:3

### 78. `/benchmarks/libpcap/sf-pcapng.c` @ 795:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 881, n4: 867)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:881  F:7
- **n4 coverage**:     T:867  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcapng.c_795_6_T` — cmplog:881  n4:867
  - `libpcap_/benchmarks/libpcap/sf-pcapng.c_795_6_F` — cmplog:7  n4:0

### 79. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2262:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2262_3_T` — cmplog:7  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2262_3_F` — cmplog:101,000  n4:1,280,000

### 80. `/benchmarks/libpcap/gencode.c` @ 2203:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2203_2_T` — cmplog:7  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2203_2_F` — cmplog:2,990  n4:8,710

### 81. `/benchmarks/libpcap/gencode.c` @ 5871:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 917, n4: 1,460)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:917
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5871_2_T` — cmplog:7  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5871_2_F` — cmplog:917  n4:1,460

### 82. `/benchmarks/libpcap/sf-pcap.c` @ 289:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1, n4: 1)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:1
- **n4 coverage**:     T:0  F:1
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_289_3_T` — cmplog:6  n4:0
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_289_3_F` — cmplog:1  n4:1

### 83. `/benchmarks/libpcap/sf-pcap.c` @ 391:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,990  F:6
- **n4 coverage**:     T:8,710  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_391_2_T` — cmplog:2,990  n4:8,710
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_391_2_F` — cmplog:6  n4:0

### 84. `/benchmarks/libpcap/sf-pcap.c` @ 400:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_400_2_T` — cmplog:6  n4:0
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_400_2_F` — cmplog:2,990  n4:8,710

### 85. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3648:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3648_1_T` — cmplog:6  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3648_1_F` — cmplog:91,700  n4:815,000

### 86. `/benchmarks/libpcap/gencode.c` @ 2204:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,990, n4: 8,710)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:2,990
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2204_2_T` — cmplog:6  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2204_2_F` — cmplog:2,990  n4:8,710

### 87. `/benchmarks/libpcap/optimize.c` @ 799:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 5)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**:     T:5  F:5
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_799_7_T` — cmplog:3  n4:5
  - `libpcap_/benchmarks/libpcap/optimize.c_799_7_F` — cmplog:0  n4:5

### 88. `/benchmarks/libpcap/nametoaddr.c` @ 364:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 28, n4: 1)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:28  F:5
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_364_6_T` — cmplog:28  n4:1
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_364_6_F` — cmplog:5  n4:0

### 89. `/benchmarks/libpcap/gencode.c` @ 1206:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 921, n4: 35)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:921
- **n4 coverage**:     T:0  F:35
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_1206_2_T` — cmplog:5  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_1206_2_F` — cmplog:921  n4:35

### 90. `/benchmarks/libpcap/gencode.c` @ 2437:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 214, n4: 363)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:214  F:5
- **n4 coverage**:     T:363  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2437_7_T` — cmplog:214  n4:363
  - `libpcap_/benchmarks/libpcap/gencode.c_2437_7_F` — cmplog:5  n4:0

### 91. `/benchmarks/libpcap/gencode.c` @ 5849:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 919, n4: 1,460)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:919
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5849_2_T` — cmplog:5  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5849_2_F` — cmplog:919  n4:1,460

### 92. `/benchmarks/libpcap/gencode.c` @ 7606:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 858, n4: 12,000)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:858
- **n4 coverage**:     T:0  F:12,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7606_2_T` — cmplog:5  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7606_2_F` — cmplog:858  n4:12,000

### 93. `/benchmarks/libpcap/optimize.c` @ 1266:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 118, n4: 627)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:118
- **n4 coverage**:     T:4  F:627
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_1266_9_T` — cmplog:0  n4:4
  - `libpcap_/benchmarks/libpcap/optimize.c_1266_9_F` — cmplog:118  n4:627

### 94. `/benchmarks/libpcap/sf-pcap.c` @ 240:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 903, n4: 870)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:903  F:4
- **n4 coverage**:     T:870  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_240_6_T` — cmplog:903  n4:870
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_240_6_F` — cmplog:4  n4:0

### 95. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4018:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4018_1_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4018_1_F` — cmplog:91,700  n4:815,000

### 96. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 5633:43
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,760, n4: 2,640)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:1,760
- **n4 coverage**:     T:0  F:2,640
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_5633_43_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_5633_43_F` — cmplog:1,760  n4:2,640

### 97. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2508:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2508_3_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2508_3_F` — cmplog:101,000  n4:1,280,000

### 98. `/benchmarks/libpcap/gencode.c` @ 5610:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 206, n4: 3)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:206
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5610_2_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5610_2_F` — cmplog:206  n4:3

### 99. `/benchmarks/libpcap/gencode.c` @ 5611:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 206, n4: 3)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:206
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5611_2_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5611_2_F` — cmplog:206  n4:3

### 100. `/benchmarks/libpcap/gencode.c` @ 5621:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 206, n4: 3)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:206
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5621_2_T` — cmplog:4  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5621_2_F` — cmplog:206  n4:3

### 101. `/benchmarks/libpcap/gencode.c` @ 6271:2
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 50, n4: 4)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:50  F:4
- **n4 coverage**:     T:4  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6271_2_T` — cmplog:50  n4:4
  - `libpcap_/benchmarks/libpcap/gencode.c_6271_2_F` — cmplog:4  n4:0

### 102. `/benchmarks/libpcap/gencode.c` @ 6299:6
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 10, n4: 1)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:4
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6299_6_T` — cmplog:10  n4:1
  - `libpcap_/benchmarks/libpcap/gencode.c_6299_6_F` — cmplog:4  n4:0

### 103. `/benchmarks/libpcap/optimize.c` @ 817:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 8, n4: 1)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:3
- **n4 coverage**:     T:1  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_817_7_T` — cmplog:8  n4:1
  - `libpcap_/benchmarks/libpcap/optimize.c_817_7_F` — cmplog:3  n4:0

### 104. `/benchmarks/libpcap/sf-pcap.c` @ 409:6
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,000, n4: 8,710)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:3,000
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_409_6_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_409_6_F` — cmplog:3,000  n4:8,710

### 105. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4414:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,700, n4: 815,000)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:91,700
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4414_1_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4414_1_F` — cmplog:91,700  n4:815,000

### 106. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 3259:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3259_3_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3259_3_F` — cmplog:101,000  n4:1,280,000

### 107. `/benchmarks/libpcap/gencode.c` @ 2393:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,000, n4: 8,710)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:3,000
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2393_2_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2393_2_F` — cmplog:3,000  n4:8,710

### 108. `/benchmarks/libpcap/gencode.c` @ 5609:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 207, n4: 3)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:207
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5609_2_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5609_2_F` — cmplog:207  n4:3

### 109. `/benchmarks/libpcap/gencode.c` @ 6061:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,110, n4: 32)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:1,110
- **n4 coverage**:     T:0  F:32
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6061_2_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6061_2_F` — cmplog:1,110  n4:32

### 110. `/benchmarks/libpcap/gencode.c` @ 6127:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,100, n4: 30)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:1,100
- **n4 coverage**:     T:0  F:30
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6127_2_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6127_2_F` — cmplog:1,100  n4:30

### 111. `/benchmarks/libpcap/gencode.c` @ 6269:10
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 51, n4: 4)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:51
- **n4 coverage**:     T:0  F:4
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6269_10_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6269_10_F` — cmplog:51  n4:4

### 112. `/benchmarks/libpcap/gencode.c` @ 6622:10
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,150, n4: 1,170)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:2,150
- **n4 coverage**:     T:0  F:1,170
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6622_10_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6622_10_F` — cmplog:2,150  n4:1,170

### 113. `/benchmarks/libpcap/gencode.c` @ 7607:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 860, n4: 12,000)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:860
- **n4 coverage**:     T:0  F:12,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7607_2_T` — cmplog:3  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7607_2_F` — cmplog:860  n4:12,000

### 114. `/benchmarks/libpcap/sf-pcap.c` @ 754:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16, n4: 252)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16
- **n4 coverage**:     T:2  F:252
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_754_8_T` — cmplog:0  n4:2
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_754_8_F` — cmplog:16  n4:252

### 115. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4038:1
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91,800
- **n4 coverage**:     T:2  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4038_1_T` — cmplog:0  n4:2
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4038_1_F` — cmplog:91,800  n4:815,000

### 116. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2610:3
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:101,000
- **n4 coverage**:     T:2  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2610_3_T` — cmplog:0  n4:2
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2610_3_F` — cmplog:101,000  n4:1,280,000

### 117. `/benchmarks/libpcap/nametoaddr.c` @ 423:6
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 18, n4: 1)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:18
- **n4 coverage**:     T:0  F:1
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_423_6_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_423_6_F` — cmplog:18  n4:1

### 118. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3628:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3628_1_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3628_1_F` — cmplog:91,800  n4:815,000

### 119. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4008:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4008_1_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4008_1_F` — cmplog:91,800  n4:815,000

### 120. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 5743:9
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 17,300, n4: 119,000)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:17,300
- **n4 coverage**:     T:0  F:119,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_5743_9_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_5743_9_F` — cmplog:17,300  n4:119,000

### 121. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2424:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2424_3_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2424_3_F` — cmplog:101,000  n4:1,280,000

### 122. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2460:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2460_3_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2460_3_F` — cmplog:101,000  n4:1,280,000

### 123. `/benchmarks/libpcap/gencode.c` @ 2412:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,000, n4: 8,710)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:3,000
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2412_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2412_2_F` — cmplog:3,000  n4:8,710

### 124. `/benchmarks/libpcap/gencode.c` @ 2869:7
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,380, n4: 471)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:2,380
- **n4 coverage**:     T:0  F:471
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2869_7_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2869_7_F` — cmplog:2,380  n4:471

### 125. `/benchmarks/libpcap/gencode.c` @ 4668:7
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,950, n4: 2,230)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:2,950
- **n4 coverage**:     T:0  F:2,230
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_4668_7_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_4668_7_F` — cmplog:2,950  n4:2,230

### 126. `/benchmarks/libpcap/gencode.c` @ 5612:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5612_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5612_2_F` — cmplog:208  n4:3

### 127. `/benchmarks/libpcap/gencode.c` @ 5615:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5615_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5615_2_F` — cmplog:208  n4:3

### 128. `/benchmarks/libpcap/gencode.c` @ 5616:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5616_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5616_2_F` — cmplog:208  n4:3

### 129. `/benchmarks/libpcap/gencode.c` @ 5617:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5617_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5617_2_F` — cmplog:208  n4:3

### 130. `/benchmarks/libpcap/gencode.c` @ 5618:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5618_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5618_2_F` — cmplog:208  n4:3

### 131. `/benchmarks/libpcap/gencode.c` @ 5620:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 208, n4: 3)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:208
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5620_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5620_2_F` — cmplog:208  n4:3

### 132. `/benchmarks/libpcap/gencode.c` @ 5862:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 922, n4: 1,460)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:922
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5862_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5862_2_F` — cmplog:922  n4:1,460

### 133. `/benchmarks/libpcap/gencode.c` @ 7024:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 102, n4: 2,070)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:102
- **n4 coverage**:     T:0  F:2,070
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7024_2_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7024_2_F` — cmplog:102  n4:2,070

### 134. `/benchmarks/libpcap/gencode.c` @ 7362:6
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 21, n4: 57)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:21
- **n4 coverage**:     T:0  F:57
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7362_6_T` — cmplog:2  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7362_6_F` — cmplog:21  n4:57

### 135. `/benchmarks/libpcap/optimize.c` @ 1263:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 118, n4: 631)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:118
- **n4 coverage**:     T:1  F:631
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/optimize.c_1263_9_T` — cmplog:0  n4:1
  - `libpcap_/benchmarks/libpcap/optimize.c_1263_9_F` — cmplog:118  n4:631

### 136. `/benchmarks/libpcap/bpf_filter.c` @ 179:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 75, n4: 26)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:75
- **n4 coverage**:     T:1  F:26
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_179_8_T` — cmplog:0  n4:1
  - `libpcap_/benchmarks/libpcap/bpf_filter.c_179_8_F` — cmplog:75  n4:26

### 137. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3998:1
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91,800
- **n4 coverage**:     T:1  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3998_1_T` — cmplog:0  n4:1
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3998_1_F` — cmplog:91,800  n4:815,000

### 138. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4159:1
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91,800
- **n4 coverage**:     T:1  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4159_1_T` — cmplog:0  n4:1
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4159_1_F` — cmplog:91,800  n4:815,000

### 139. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 1993:3
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:101,000
- **n4 coverage**:     T:1  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1993_3_T` — cmplog:0  n4:1
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1993_3_F` — cmplog:101,000  n4:1,280,000

### 140. `/benchmarks/libpcap/sf-pcap.c` @ 244:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 889, n4: 867)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:889  F:1
- **n4 coverage**:     T:867  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_244_7_T` — cmplog:889  n4:867
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_244_7_F` — cmplog:1  n4:0

### 141. `/benchmarks/libpcap/sf-pcap.c` @ 245:7
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 888, n4: 867)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:888  F:1
- **n4 coverage**:     T:867  F:0
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_245_7_T` — cmplog:888  n4:867
  - `libpcap_/benchmarks/libpcap/sf-pcap.c_245_7_F` — cmplog:1  n4:0

### 142. `/benchmarks/libpcap/nametoaddr.c` @ 647:7
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,610, n4: 427)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:7,610
- **n4 coverage**:     T:0  F:427
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_647_7_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/nametoaddr.c_647_7_F` — cmplog:7,610  n4:427

### 143. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3578:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3578_1_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3578_1_F` — cmplog:91,800  n4:815,000

### 144. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3653:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3653_1_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3653_1_F` — cmplog:91,800  n4:815,000

### 145. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 3923:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3923_1_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_3923_1_F` — cmplog:91,800  n4:815,000

### 146. `/benchmarks/libpcap/build_llvm_cov/scanner.c` @ 4043:1
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 91,800, n4: 815,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:91,800
- **n4 coverage**:     T:0  F:815,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4043_1_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/scanner.c_4043_1_F` — cmplog:91,800  n4:815,000

### 147. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 1975:11
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11, n4: 4)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:11
- **n4 coverage**:     T:0  F:4
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1975_11_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1975_11_F` — cmplog:11  n4:4

### 148. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 1981:18
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10, n4: 4)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:10
- **n4 coverage**:     T:0  F:4
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1981_18_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_1981_18_F` — cmplog:10  n4:4

### 149. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2030:18
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,150, n4: 158)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:2,150
- **n4 coverage**:     T:0  F:158
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2030_18_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2030_18_F` — cmplog:2,150  n4:158

### 150. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2048:11
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 9, n4: 4)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:9
- **n4 coverage**:     T:0  F:4
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2048_11_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2048_11_F` — cmplog:9  n4:4

### 151. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2078:18
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 17, n4: 54)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:17
- **n4 coverage**:     T:0  F:54
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2078_18_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2078_18_F` — cmplog:17  n4:54

### 152. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2232:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2232_3_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2232_3_F` — cmplog:101,000  n4:1,280,000

### 153. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2430:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2430_3_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2430_3_F` — cmplog:101,000  n4:1,280,000

### 154. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2514:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2514_3_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2514_3_F` — cmplog:101,000  n4:1,280,000

### 155. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 2929:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2929_3_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_2929_3_F` — cmplog:101,000  n4:1,280,000

### 156. `/benchmarks/libpcap/build_llvm_cov/grammar.c` @ 3176:3
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 101,000, n4: 1,280,000)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:101,000
- **n4 coverage**:     T:0  F:1,280,000
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3176_3_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/build_llvm_cov/grammar.c_3176_3_F` — cmplog:101,000  n4:1,280,000

### 157. `/benchmarks/libpcap/gencode.c` @ 2398:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,000, n4: 8,710)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:3,000
- **n4 coverage**:     T:0  F:8,710
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_2398_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_2398_2_F` — cmplog:3,000  n4:8,710

### 158. `/benchmarks/libpcap/gencode.c` @ 3885:6
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,690, n4: 484)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:1,690
- **n4 coverage**:     T:0  F:484
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_3885_6_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_3885_6_F` — cmplog:1,690  n4:484

### 159. `/benchmarks/libpcap/gencode.c` @ 5614:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 209, n4: 3)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:209
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5614_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5614_2_F` — cmplog:209  n4:3

### 160. `/benchmarks/libpcap/gencode.c` @ 5619:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 209, n4: 3)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:209
- **n4 coverage**:     T:0  F:3
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5619_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5619_2_F` — cmplog:209  n4:3

### 161. `/benchmarks/libpcap/gencode.c` @ 5823:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5823_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5823_2_F` — cmplog:923  n4:1,460

### 162. `/benchmarks/libpcap/gencode.c` @ 5826:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5826_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5826_2_F` — cmplog:923  n4:1,460

### 163. `/benchmarks/libpcap/gencode.c` @ 5828:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5828_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5828_2_F` — cmplog:923  n4:1,460

### 164. `/benchmarks/libpcap/gencode.c` @ 5835:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5835_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5835_2_F` — cmplog:923  n4:1,460

### 165. `/benchmarks/libpcap/gencode.c` @ 5854:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5854_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5854_2_F` — cmplog:923  n4:1,460

### 166. `/benchmarks/libpcap/gencode.c` @ 5870:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 923, n4: 1,460)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:923
- **n4 coverage**:     T:0  F:1,460
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_5870_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_5870_2_F` — cmplog:923  n4:1,460

### 167. `/benchmarks/libpcap/gencode.c` @ 6017:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,110, n4: 32)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:1,110
- **n4 coverage**:     T:0  F:32
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6017_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6017_2_F` — cmplog:1,110  n4:32

### 168. `/benchmarks/libpcap/gencode.c` @ 6277:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 53, n4: 4)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:53
- **n4 coverage**:     T:0  F:4
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_6277_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_6277_2_F` — cmplog:53  n4:4

### 169. `/benchmarks/libpcap/gencode.c` @ 7361:24
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 23, n4: 57)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:23
- **n4 coverage**:     T:0  F:57
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7361_24_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7361_24_F` — cmplog:23  n4:57

### 170. `/benchmarks/libpcap/gencode.c` @ 7377:2
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 9, n4: 43)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:9
- **n4 coverage**:     T:0  F:43
- **Canonical identifiers**:
  - `libpcap_/benchmarks/libpcap/gencode.c_7377_2_T` — cmplog:1  n4:0
  - `libpcap_/benchmarks/libpcap/gencode.c_7377_2_F` — cmplog:9  n4:43
