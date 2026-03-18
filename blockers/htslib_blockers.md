# Input-Dependent Blocking Branches — htslib (All, Ranked by Flip Strength)

**Coverage sources:** `coverage/htslib/cmplog.cov`, `coverage/htslib/n4.cov`  
**Analysis date:** 2026-03-18  
**Ranking:** descending by *flip strength* = hitcount of the blocked side in the confirming fuzzer

## Summary

| Metric | Value |
|--------|-------|
| Branch pairs (cmplog) | 6,247 |
| Branch pairs (n4) | 3,297 |
| Asymmetric in cmplog | 2,408 |
| Asymmetric in n4 | 1,497 |
| **Confirmed input-dependent** | **217** |
| Unconfirmed candidates | 3,688 |

## Ranked Summary Table

| Rank | Function | Line:Col | Blocked | Flip Strength | cmplog T:F | n4 T:F | Confirmed By |
|------|----------|----------|---------|---------------|------------|------------|--------------|
| 1 | `cram_free_container` | 3747:13 | False | 138,000 | 118000:138000 | 101000:0 | cmplog |
| 2 | `header.c:ks_resize` | 162:6 | False | 27,800 | 15900:27800 | 5490:0 | cmplog |
| 3 | `hts.c:get_severity_tag` | 5123:5 | False | 22,600 | 7640:22600 | 279:0 | cmplog |
| 4 | `hts.c:get_severity_tag` | 5125:5 | True | 22,600 | 22600:7640 | 0:279 | cmplog |
| 5 | `pool_destroy` | 87:17 | True | 12,400 | 12400:30400 | 0:14600 | cmplog |
| 6 | `sam_hdr_fill_hrecs` | 1142:21 | True | 7,260 | 7260:3420 | 0:1830 | cmplog |
| 7 | `hts_hopen` | 1583:5 | True | 6,840 | 6840:20500 | 0:13000 | cmplog |
| 8 | `sam_read1` | 4394:9 | True | 5,940 | 5940:20200 | 0:200000 | cmplog |
| 9 | `sam_hdr_read` | 2207:5 | True | 5,130 | 5130:5760 | 0:5490 | cmplog |
| 10 | `sam_hdr_destroy` | 122:9 | True | 5,050 | 5050:15300 | 0:7330 | cmplog |
| 11 | `cram_free_container` | 3730:9 | False | 4,930 | 4230:4930 | 3600:0 | cmplog |
| 12 | `cram_free_container` | 3751:9 | False | 4,930 | 4230:4930 | 3600:0 | cmplog |
| 13 | `cram_free_container` | 3723:9 | False | 4,850 | 4310:4850 | 3600:0 | cmplog |
| 14 | `sam_hdr_destroy` | 134:9 | False | 4,220 | 11100:4220 | 7330:0 | cmplog |
| 15 | `header.c:add_stub_ref_sq_lines` | 1109:19 | True | 4,030 | 4030:11100 | 0:7330 | cmplog |
| 16 | `sam_hdr_destroy` | 127:9 | True | 3,590 | 3590:11700 | 0:7330 | cmplog |
| 17 | `sam_hdr_fill_hrecs` | 1134:9 | True | 3,540 | 3540:11600 | 0:7330 | cmplog |
| 18 | `sam_hdr_count_lines` | 1789:13 | True | 3,020 | 3020:7650 | 0:5490 | cmplog |
| 19 | `hts_detect_format2` | 696:15 | True | 3,000 | 3000:418 | 0:409 | cmplog |
| 20 | `cram_free_container` | 3720:9 | False | 2,650 | 6510:2650 | 3600:0 | cmplog |
| 21 | `sam_hrecs_free` | 2461:9 | True | 2,490 | 2490:12700 | 0:7330 | cmplog |
| 22 | `sam_hrecs_rebuild_text` | 2018:22 | False | 2,360 | 6010:2360 | 5490:0 | cmplog |
| 23 | `refs_free` | 2438:39 | True | 2,200 | 2200:4540 | 0:1830 | cmplog |
| 24 | `hts_detect_format2` | 694:45 | True | 2,110 | 2110:4970 | 0:409 | cmplog |
| 25 | `cram_dopen` | 5314:9 | True | 2,070 | 2070:3630 | 0:1830 | cmplog |
| 26 | `hts_detect_format2` | 633:21 | True | 2,070 | 2070:13900 | 0:7350 | cmplog |
| 27 | `refs_free` | 2452:9 | False | 2,009 | 2530:2009 | 1830:0 | cmplog |
| 28 | `sam_hdr_update_target_arrays` | 943:28 | True | 1,950 | 1950:3640 | 0:1830 | cmplog |
| 29 | `bam_hdr_write` | 395:17 | True | 1,880 | 1880:3550 | 0:1830 | cmplog |
| 30 | `bam_hdr_write` | 388:13 | True | 1,780 | 1780:1770 | 0:1830 | cmplog |
| 31 | `kstring.c:ks_resize` | 162:6 | False | 1,650 | 41600:1650 | 229000:0 | cmplog |
| 32 | `cram_free_block` | 1562:9 | True | 1,530 | 1530:48700 | 0:44200 | cmplog |
| 33 | `hts_detect_format2` | 695:45 | True | 1,460 | 1460:3420 | 0:409 | cmplog |
| 34 | `sam.c:sam_format1_append` | 4497:12 | True | 1,310 | 1310:5700 | 0:65099 | cmplog |
| 35 | `hts_hopen` | 1572:13 | True | 1,150 | 1150:4540 | 0:1830 | cmplog |
| 36 | `bam_aux_get` | 4925:32 | True | 1,110 | 1110:5460 | 0:65099 | cmplog |
| 37 | `cram_free_container` | 3754:42 | True | 1,070 | 1070:4230 | 0:3600 | cmplog |
| 38 | `cram_io.c:refs_from_header` | 2777:13 | True | 1,020 | 1020:3400 | 0:1830 | cmplog |
| 39 | `sam_hdr_write` | 2242:13 | True | 1,020 | 1020:2530 | 0:1830 | cmplog |
| 40 | `hts_open_fuzzer.c:view_sam` | 99:9 | True | 1,020 | 1020:9650 | 0:5490 | cmplog |
| 41 | `sam_hdr_destroy` | 136:9 | True | 1,010 | 1010:14300 | 0:7330 | cmplog |
| 42 | `refs2id` | 2747:17 | True | 1,000 | 1000:2530 | 0:1830 | cmplog |
| 43 | `sam_hdr_dup` | 180:9 | True | 1,000 | 1000:3230 | 0:1830 | cmplog |
| 44 | `sam_hdr_dup` | 200:9 | False | 1,000 | 3230:1000 | 1830:0 | cmplog |
| 45 | `bam_hdr_write` | 352:9 | False | 1,000 | 2550:1000 | 1830:0 | cmplog |
| 46 | `sam_hdr_write` | 2254:13 | True | 1,000 | 1000:2550 | 0:1830 | cmplog |
| 47 | `sam_hdr_write` | 2262:13 | False | 1,000 | 2550:1000 | 1830:0 | cmplog |
| 48 | `cram_encode_compression_header` | 471:42 | True | 984 | 984:1680 | 0:1770 | cmplog |
| 49 | `cram_close` | 5643:43 | True | 960 | 960:4540 | 0:1830 | cmplog |
| 50 | `cram_encode.c:kh_resize_m_s2i` | 187:27 | False | 930 | 1750:0 | 3030:930 | n4 |
| 51 | `cram_encode.c:kh_resize_m_s2i` | 177:24 | False | 930 | 1750:0 | 3030:930 | n4 |
| 52 | `cram_dopen` | 5353:25 | False | 916 | 3630:916 | 1830:0 | cmplog |
| 53 | `cram_close` | 5570:9 | False | 916 | 3630:916 | 1830:0 | cmplog |
| 54 | `cram_close` | 5578:9 | True | 916 | 916:3630 | 0:1830 | cmplog |
| 55 | `cram_close` | 5600:21 | False | 916 | 3610:916 | 1830:0 | cmplog |
| 56 | `hts_hopen` | 1573:13 | True | 916 | 916:3630 | 0:1830 | cmplog |
| 57 | `hts_close` | 1645:13 | True | 916 | 916:3630 | 0:1830 | cmplog |
| 58 | `cram_dopen` | 5379:19 | False | 860 | 3680:860 | 1830:0 | cmplog |
| 59 | `cram_encode.c:cram_encode_aux` | 2800:12 | True | 854 | 854:5360 | 0:65099 | cmplog |
| 60 | `hts_detect_format2` | 641:13 | True | 793 | 793:28 | 0:2 | cmplog |
| 61 | `hts_hopen` | 1563:5 | True | 793 | 793:26600 | 0:13000 | cmplog |
| 62 | `sam.c:kputsn_` | 276:19 | False | 771 | 21500:771 | 250000:0 | cmplog |
| 63 | `cram_write_SAM_hdr` | 5025:13 | True | 761 | 761:1770 | 0:1830 | cmplog |
| 64 | `sam_hdr_update_target_arrays` | 924:9 | True | 735 | 735:2900 | 0:1830 | cmplog |
| 65 | `cram_io.c:itf8_size` | 756:49 | False | 706 | 782:706 | 949:0 | cmplog |
| 66 | `sam_hdr_write` | 2287:13 | True | 703 | 703:2850 | 0:1830 | cmplog |
| 67 | `cram_io.c:refs_from_header` | 2781:9 | False | 692 | 5290:692 | 3660:0 | cmplog |
| 68 | `sam_hdr_read` | 2204:5 | True | 687 | 687:10200 | 0:5490 | cmplog |
| 69 | `sam_read1` | 4390:9 | True | 687 | 687:25500 | 0:200000 | cmplog |
| 70 | `bgzf.c:bgzf_read_init` | 402:35 | False | 628 | 202:628 | 7:0 | cmplog |
| 71 | `sam_hdr_read` | 2201:5 | True | 594 | 594:10300 | 0:5490 | cmplog |
| 72 | `cram_free_slice` | 4450:21 | True | 510 | 510:1730 | 0:1770 | cmplog |
| 73 | `cram_encode.c:cram_encode_slice` | 1166:21 | True | 485 | 485:1680 | 0:1770 | cmplog |
| 74 | `cram_encode.c:cram_compress_slice` | 956:49 | True | 485 | 485:1680 | 0:1770 | cmplog |
| 75 | `bam_aux_first` | 4903:9 | False | 461 | 5020:461 | 65099:0 | cmplog |
| 76 | `kvsprintf` | 166:6 | True | 435 | 435:10900 | 0:4030 | cmplog |
| 77 | `sam_hdr_fill_hrecs` | 1156:9 | True | 405 | 405:10700 | 0:7330 | cmplog |
| 78 | `sam_read1` | 4386:9 | True | 365 | 365:25800 | 0:200000 | cmplog |
| 79 | `hts_detect_format2` | 686:27 | True | 357 | 357:12400 | 0:7050 | cmplog |
| 80 | `hts_hopen` | 1584:5 | True | 357 | 357:27000 | 0:13000 | cmplog |
| 81 | `hts_close` | 1664:5 | True | 357 | 357:25800 | 0:12900 | cmplog |
| 82 | `cram_write_SAM_hdr` | 4924:21 | True | 350 | 350:2190 | 0:1830 | cmplog |
| 83 | `refs2id` | 2737:9 | True | 346 | 346:2190 | 0:1830 | cmplog |
| 84 | `sam_hrecs_free` | 2473:9 | True | 345 | 345:14800 | 0:7330 | cmplog |
| 85 | `cram_get_ref` | 3410:9 | False | 341 | 1650:341 | 1770:0 | cmplog |
| 86 | `cram_io.c:cram_compress_block3` | 2286:13 | True | 315 | 315:2250 | 0:1830 | cmplog |
| 87 | `cram_io.c:cram_init_tables` | 5193:9 | True | 311 | 311:5390 | 0:1830 | cmplog |
| 88 | `cram_free_compression_header` | 4401:9 | False | 306 | 4230:306 | 3600:0 | cmplog |
| 89 | `cram_free_compression_header` | 4403:9 | False | 306 | 4230:306 | 3600:0 | cmplog |
| 90 | `sam_hrecs_free` | 2476:9 | True | 285 | 285:14900 | 0:7330 | cmplog |
| 91 | `cram_byte_array_len_encode_store` | 3489:9 | False | 282 | 1680:282 | 1770:0 | cmplog |
| 92 | `cram_free_compression_header` | 4399:9 | False | 282 | 4260:282 | 3600:0 | cmplog |
| 93 | `cram_huffman_encode_store` | 3113:9 | False | 233 | 19200:233 | 17700:0 | cmplog |
| 94 | `hts_open_fuzzer.c:view_sam` | 87:9 | True | 219 | 219:10600 | 0:5490 | cmplog |
| 95 | `cram_byte_array_stop_encode_store` | 3733:9 | False | 203 | 5050:203 | 5320:0 | cmplog |
| 96 | `hts_close` | 1638:5 | True | 199 | 199:25900 | 0:12900 | cmplog |
| 97 | `cram_encode_container` | 2081:13 | True | 195 | 195:1490 | 0:1770 | cmplog |
| 98 | `cram_free_slice` | 4498:9 | True | 195 | 195:1530 | 0:1770 | cmplog |
| 99 | `sam.c:kputll` | 393:9 | False | 189 | 16900:189 | 195000:0 | cmplog |
| 100 | `cram_encode.c:cram_compress_slice` | 974:47 | False | 187 | 77500:187 | 81600:0 | cmplog |
| 101 | `hts_detect_format2` | 694:15 | True | 184 | 184:7080 | 0:409 | cmplog |
| 102 | `tokenise_name3.c:free_context` | 215:9 | False | 184 | 2840:184 | 2330:0 | cmplog |
| 103 | `hts_open_fuzzer.c:view_sam` | 107:13 | True | 174 | 174:16500 | 0:195000 | cmplog |
| 104 | `sam.c:hts_reg2bin` | 1510:13 | False | 163 | 18000:163 | 195000:0 | cmplog |
| 105 | `hts_detect_format2` | 576:17 | True | 156 | 156:30 | 0:5 | cmplog |
| 106 | `bgzf.c:bgzf_read_init` | 403:60 | True | 155 | 155:30 | 0:5 | cmplog |
| 107 | `cram_encode.c:cram_encode_slice_read` | 598:9 | False | 137 | 5200:137 | 65099:0 | cmplog |
| 108 | `LLVMFuzzerTestOneInput` | 205:9 | True | 126 | 126:3730 | 0:1940 | cmplog |
| 109 | `kvsprintf` | 155:6 | False | 112 | 11200:112 | 4030:0 | cmplog |
| 110 | `bgzf_close` | 2116:11 | True | 108 | 108:4510 | 0:1840 | cmplog |
| 111 | `bam_write1` | 869:31 | True | 107 | 107:5480 | 0:65099 | cmplog |
| 112 | `sam_hrecs_free` | 2467:9 | True | 90 | 90:15100 | 0:7330 | cmplog |
| 113 | `bam_cigar2qlen` | 651:21 | True | 85 | 85:5900 | 0:55400 | cmplog |
| 114 | `cram_encode.c:process_one_read` | 3403:9 | False | 82 | 5290:82 | 65099:0 | cmplog |
| 115 | `cram_encode.c:process_one_read` | 71:20 | True | 77 | 77:5290 | 0:65099 | cmplog |
| 116 | `hts_detect_format2` | 695:15 | True | 76 | 76:4890 | 0:409 | cmplog |
| 117 | `cram_close` | 5620:9 | False | 73 | 4470:73 | 1830:0 | cmplog |
| 118 | `sam.c:kputw` | 370:9 | True | 65 | 65:22600 | 0:130000 | cmplog |
| 119 | `cram_close` | 5628:9 | True | 63 | 63:4480 | 0:1830 | cmplog |
| 120 | `cram_encode.c:process_one_read` | 3415:13 | True | 58 | 58:5260 | 0:65099 | cmplog |
| 121 | `cram_encode_container` | 2183:9 | False | 55 | 1630:55 | 1770:0 | cmplog |
| 122 | `cram_dopen` | 5379:58 | False | 52 | 3630:52 | 1830:0 | cmplog |
| 123 | `bam_write1` | 867:9 | True | 51 | 51:5600 | 0:65099 | cmplog |
| 124 | `cram_encode_compression_header` | 167:17 | True | 50 | 50:1630 | 0:1770 | cmplog |
| 125 | `cram_encode_compression_header` | 201:13 | True | 50 | 50:6740 | 0:7100 | cmplog |
| 126 | `cram_encode_container` | 1871:13 | False | 50 | 1650:50 | 1770:0 | cmplog |
| 127 | `cram_encode_container` | 1939:9 | False | 50 | 1650:50 | 1770:0 | cmplog |
| 128 | `cram_encode_container` | 2528:9 | False | 50 | 1630:50 | 1770:0 | cmplog |
| 129 | `cram_stats.c:kh_resize_m_i2i` | 187:27 | False | 49 | 5600:0 | 5930:49 | n4 |
| 130 | `cram_stats.c:kh_resize_m_i2i` | 177:24 | False | 49 | 5600:0 | 5930:49 | n4 |
| 131 | `cram_encode.c:process_one_read` | 3414:9 | False | 49 | 5320:49 | 65099:0 | cmplog |
| 132 | `cram_free_slice` | 4430:9 | False | 49 | 1680:49 | 1770:0 | cmplog |
| 133 | `cram_free_slice` | 4433:9 | False | 49 | 1680:49 | 1770:0 | cmplog |
| 134 | `cram_encode.c:cram_allocate_block` | 1013:5 | True | 47 | 47:31300 | 0:33300 | cmplog |
| 135 | `cram_io.c:cram_init_varint` | 5135:9 | True | 42 | 42:5660 | 0:1830 | cmplog |
| 136 | `cram_free_compression_header` | 4374:44 | True | 39 | 39:145000 | 0:115000 | cmplog |
| 137 | `sam_hdr_rebuild` | 1259:9 | False | 36 | 3260:36 | 1830:0 | cmplog |
| 138 | `cram_free_slice` | 4457:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 139 | `cram_free_slice` | 4460:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 140 | `cram_free_slice` | 4469:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 141 | `cram_free_slice` | 4478:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 142 | `cram_free_slice` | 4481:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 143 | `cram_free_slice` | 4490:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 144 | `cram_free_slice` | 4493:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 145 | `cram_free_slice` | 4495:9 | False | 33 | 1700:33 | 1770:0 | cmplog |
| 146 | `hts_getline` | 2027:5 | False | 33 | 108000:33 | 745000:0 | cmplog |
| 147 | `cram_encode.c:cram_compress_slice` | 879:28 | True | 32 | 0:47100 | 32:49600 | n4 |
| 148 | `cram_io.c:cram_compress_block3` | 2023:17 | True | 32 | 0:6580 | 32:8870 | n4 |
| 149 | `bgzf_close` | 2103:13 | False | 30 | 17:30 | 7:0 | cmplog |
| 150 | `cram_block_method2str` | 2352:5 | True | 29 | 0:9150 | 29:10700 | n4 |
| 151 | `cram_free_compression_header` | 4397:9 | True | 24 | 24:4520 | 0:3600 | cmplog |
| 152 | `hts_hopen` | 1564:5 | True | 21 | 21:27400 | 0:13000 | cmplog |
| 153 | `hts_close` | 1640:5 | True | 21 | 21:26100 | 0:12900 | cmplog |
| 154 | `sam.c:hts_reg2bin` | 1509:29 | False | 21 | 18100:21 | 195000:0 | cmplog |
| 155 | `hts_getline` | 2035:5 | True | 18 | 18:108000 | 0:745000 | cmplog |
| 156 | `tokenise_name3.c:search_trie` | 627:32 | False | 17 | 107000:17 | 158000:0 | cmplog |
| 157 | `cram_flush_container` | 4150:9 | True | 16 | 16:1680 | 0:1770 | cmplog |
| 158 | `cram_free_slice_header` | 4418:9 | False | 16 | 1680:16 | 1770:0 | cmplog |
| 159 | `cram_free_slice` | 4463:9 | True | 16 | 16:1710 | 0:1770 | cmplog |
| 160 | `cram_free_slice` | 4466:9 | True | 16 | 16:1710 | 0:1770 | cmplog |
| 161 | `cram_free_slice` | 4472:9 | True | 16 | 16:1710 | 0:1770 | cmplog |
| 162 | `cram_free_slice` | 4475:9 | True | 16 | 16:1710 | 0:1770 | cmplog |
| 163 | `cram_close` | 5574:13 | True | 16 | 16:1680 | 0:1770 | cmplog |
| 164 | `cram_close` | 5600:9 | False | 16 | 4530:16 | 1830:0 | cmplog |
| 165 | `rANS_static4x16pr.c:normalise_freq_shift` | 153:9 | True | 16 | 16:61100 | 0:140000 | cmplog |
| 166 | `sam.c:sam_format1_append` | 4454:9 | True | 16 | 16:5680 | 0:65099 | cmplog |
| 167 | `bgzf.c:hwrite` | 296:9 | True | 15 | 0:9540 | 15:6200 | n4 |
| 168 | `bgzf.c:hwrite` | 302:9 | False | 15 | 9540:0 | 6200:15 | n4 |
| 169 | `bgzf.c:hwrite` | 305:12 | False | 15 | 9540:0 | 6200:15 | n4 |
| 170 | `hts_detect_format2` | 660:18 | True | 15 | 15:6 | 0:2 | cmplog |
| 171 | `hts_getline` | 2036:5 | True | 15 | 15:108000 | 0:745000 | cmplog |
| 172 | `sam.c:fastq_parse1` | 4103:18 | True | 15 | 15:4630 | 0:5680 | cmplog |
| 173 | `sam.c:kputll` | 388:9 | True | 13 | 13:17000 | 0:195000 | cmplog |
| 174 | `cram_free_compression_header` | 4366:9 | True | 12 | 12:4530 | 0:3600 | cmplog |
| 175 | `cram_huffman_encode_init` | 3301:13 | False | 11 | 19400:11 | 17700:0 | cmplog |
| 176 | `sam.c:sam_format1_append` | 4462:9 | False | 11 | 5690:11 | 65099:0 | cmplog |
| 177 | `bam_write1` | 869:9 | True | 10 | 10:5590 | 0:65099 | cmplog |
| 178 | `cram_encode.c:process_one_read` | 3780:19 | True | 9 | 9:5350 | 0:65099 | cmplog |
| 179 | `string_alloc` | 127:13 | False | 9 | 25700:9 | 90200:0 | cmplog |
| 180 | `cram_encoder_init` | 3928:13 | False | 8 | 34200:8 | 35100:0 | cmplog |
| 181 | `cram_encoder_init` | 3930:13 | True | 8 | 8:34200 | 0:35100 | cmplog |
| 182 | `cram_encode_container` | 2039:17 | True | 8 | 8:5360 | 0:65099 | cmplog |
| 183 | `cram_encode_container` | 2212:9 | True | 8 | 8:1680 | 0:1770 | cmplog |
| 184 | `cram_encode.c:process_one_read` | 3719:9 | True | 8 | 8:5360 | 0:65099 | cmplog |
| 185 | `cram_free_container` | 3781:9 | True | 8 | 8:9160 | 0:3600 | cmplog |
| 186 | `cram_encode.c:cram_compress_slice` | 945:9 | True | 7 | 7:1670 | 0:1770 | cmplog |
| 187 | `rANS_static32x16pr_avx2.c:normalise_freq_shift` | 153:9 | True | 7 | 7:7490 | 0:14600 | cmplog |
| 188 | `tokenise_name3.c:encode_name` | 930:31 | False | 6 | 204:0 | 398:6 | n4 |
| 189 | `hts_detect_format2` | 654:18 | True | 6 | 6:21 | 0:2 | cmplog |
| 190 | `sam_realloc_bam_data` | 442:9 | True | 5 | 5:15600 | 0:75700 | cmplog |
| 191 | `tokenise_name3.c:create_context` | 173:9 | True | 4 | 4:3020 | 0:2330 | cmplog |
| 192 | `bam_write1` | 868:9 | True | 4 | 4:5600 | 0:65099 | cmplog |
| 193 | `bgzf_hopen` | 538:13 | True | 3 | 3:866 | 0:9 | cmplog |
| 194 | `bgzf.c:bgzf_read_init` | 404:46 | True | 3 | 3:182 | 0:5 | cmplog |
| 195 | `string_alloc` | 135:9 | True | 3 | 3:7660 | 0:2420 | cmplog |
| 196 | `hts_detect_format2` | 578:22 | True | 3 | 3:27 | 0:5 | cmplog |
| 197 | `hts_detect_format2` | 586:27 | True | 2 | 2:15700 | 0:7210 | cmplog |
| 198 | `hts_detect_format2` | 598:26 | True | 2 | 2:15900 | 0:7350 | cmplog |
| 199 | `hts_detect_format2` | 746:18 | True | 2 | 2:86 | 0:69 | cmplog |
| 200 | `hts_hopen` | 1587:17 | True | 2 | 2:53 | 0:9 | cmplog |
| 201 | `hts.c:decompress_peek_gz` | 334:13 | True | 2 | 2:251 | 0:14 | cmplog |
| 202 | `sam_write1` | 4732:17 | True | 2 | 2:5700 | 0:65099 | cmplog |
| 203 | `cram_encode.c:process_one_read` | 3380:9 | False | 1 | 5370:1 | 65099:0 | cmplog |
| 204 | `cram_encode.c:process_one_read` | 3826:17 | True | 1 | 1:29 | 0:20500 | cmplog |
| 205 | `cram_encode.c:process_one_read` | 3950:17 | True | 1 | 1:5360 | 0:65099 | cmplog |
| 206 | `hopen` | 1310:16 | True | 1 | 1:16200 | 0:7510 | cmplog |
| 207 | `hts_detect_format2` | 607:26 | True | 1 | 1:16000 | 0:7440 | cmplog |
| 208 | `hts_detect_format2` | 614:9 | True | 1 | 1:16200 | 0:7510 | cmplog |
| 209 | `hts_detect_format2` | 648:18 | True | 1 | 1:27 | 0:2 | cmplog |
| 210 | `hts_detect_format2` | 667:18 | True | 1 | 1:5 | 0:2 | cmplog |
| 211 | `hts_detect_format2` | 673:18 | True | 1 | 1:4 | 0:2 | cmplog |
| 212 | `hts_detect_format2` | 707:26 | True | 1 | 1:5910 | 0:7270 | cmplog |
| 213 | `hts_detect_format2` | 719:25 | True | 1 | 1:5880 | 0:7240 | cmplog |
| 214 | `hts_hopen` | 1479:13 | True | 1 | 1:16200 | 0:7510 | cmplog |
| 215 | `hts_hopen` | 1486:16 | True | 1 | 1:16200 | 0:7510 | cmplog |
| 216 | `hts_hopen` | 1566:13 | True | 1 | 1:4570 | 0:1830 | cmplog |
| 217 | `tokenise_name3.c:create_context` | 177:9 | True | 1 | 1:3020 | 0:2330 | cmplog |

## Detail Listings

### 1. `cram_free_container` @ 3747:13
- **Statement**: `if (c->stats[id]) cram_stats_free(c->stats[id]);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 118,000, n4: 101,000)
- **Flip strength**: 138,000 (blocked side hit 138,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:118,000  F:138,000
- **n4 coverage**: T:101,000  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_container_3747_13_T` — cmplog:118,000  n4:101,000
  - `htslib_cram_free_container_3747_13_F` — cmplog:138,000  n4:0

### 2. `header.c:ks_resize` @ 162:6
- **Statement**: `if (s->m < size) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 15,900, n4: 5,490)
- **Flip strength**: 27,800 (blocked side hit 27,800× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15,900  F:27,800
- **n4 coverage**: T:5,490  F:0
- **Canonical identifiers**:
  - `htslib_header.c:ks_resize_162_6_T` — cmplog:15,900  n4:5,490
  - `htslib_header.c:ks_resize_162_6_F` — cmplog:27,800  n4:0

### 3. `hts.c:get_severity_tag` @ 5123:5
- **Statement**: `case HTS_LOG_ERROR:`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 7,640, n4: 279)
- **Flip strength**: 22,600 (blocked side hit 22,600× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7,640  F:22,600
- **n4 coverage**: T:279  F:0
- **Canonical identifiers**:
  - `htslib_hts.c:get_severity_tag_5123_5_T` — cmplog:7,640  n4:279
  - `htslib_hts.c:get_severity_tag_5123_5_F` — cmplog:22,600  n4:0

### 4. `hts.c:get_severity_tag` @ 5125:5
- **Statement**: `case HTS_LOG_WARNING:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,640, n4: 279)
- **Flip strength**: 22,600 (blocked side hit 22,600× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:22,600  F:7,640
- **n4 coverage**: T:0  F:279
- **Canonical identifiers**:
  - `htslib_hts.c:get_severity_tag_5125_5_T` — cmplog:22,600  n4:0
  - `htslib_hts.c:get_severity_tag_5125_5_F` — cmplog:7,640  n4:279

### 5. `pool_destroy` @ 87:17
- **Statement**: `for (i = 0; i < p->npools; i++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 30,400, n4: 14,600)
- **Flip strength**: 12,400 (blocked side hit 12,400× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12,400  F:30,400
- **n4 coverage**: T:0  F:14,600
- **Canonical identifiers**:
  - `htslib_pool_destroy_87_17_T` — cmplog:12,400  n4:0
  - `htslib_pool_destroy_87_17_F` — cmplog:30,400  n4:14,600

### 6. `sam_hdr_fill_hrecs` @ 1142:21
- **Statement**: `if (bh->text && bh->l_text > 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,420, n4: 1,830)
- **Flip strength**: 7,260 (blocked side hit 7,260× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7,260  F:3,420
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_fill_hrecs_1142_21_T` — cmplog:7,260  n4:0
  - `htslib_sam_hdr_fill_hrecs_1142_21_F` — cmplog:3,420  n4:1,830

### 7. `hts_hopen` @ 1583:5
- **Statement**: `case sam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 20,500, n4: 13,000)
- **Flip strength**: 6,840 (blocked side hit 6,840× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,840  F:20,500
- **n4 coverage**: T:0  F:13,000
- **Canonical identifiers**:
  - `htslib_hts_hopen_1583_5_T` — cmplog:6,840  n4:0
  - `htslib_hts_hopen_1583_5_F` — cmplog:20,500  n4:13,000

### 8. `sam_read1` @ 4394:9
- **Statement**: `case sam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 20,200, n4: 200,000)
- **Flip strength**: 5,940 (blocked side hit 5,940× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,940  F:20,200
- **n4 coverage**: T:0  F:200,000
- **Canonical identifiers**:
  - `htslib_sam_read1_4394_9_T` — cmplog:5,940  n4:0
  - `htslib_sam_read1_4394_9_F` — cmplog:20,200  n4:200,000

### 9. `sam_hdr_read` @ 2207:5
- **Statement**: `case sam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,760, n4: 5,490)
- **Flip strength**: 5,130 (blocked side hit 5,130× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,130  F:5,760
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_sam_hdr_read_2207_5_T` — cmplog:5,130  n4:0
  - `htslib_sam_hdr_read_2207_5_F` — cmplog:5,760  n4:5,490

### 10. `sam_hdr_destroy` @ 122:9
- **Statement**: `if (bh->ref_count > 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 15,300, n4: 7,330)
- **Flip strength**: 5,050 (blocked side hit 5,050× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,050  F:15,300
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hdr_destroy_122_9_T` — cmplog:5,050  n4:0
  - `htslib_sam_hdr_destroy_122_9_F` — cmplog:15,300  n4:7,330

### 11. `cram_free_container` @ 3730:9
- **Statement**: `if (c->slices) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,230, n4: 3,600)
- **Flip strength**: 4,930 (blocked side hit 4,930× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,230  F:4,930
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_container_3730_9_T` — cmplog:4,230  n4:3,600
  - `htslib_cram_free_container_3730_9_F` — cmplog:4,930  n4:0

### 12. `cram_free_container` @ 3751:9
- **Statement**: `if (c->tags_used) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,230, n4: 3,600)
- **Flip strength**: 4,930 (blocked side hit 4,930× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,230  F:4,930
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_container_3751_9_T` — cmplog:4,230  n4:3,600
  - `htslib_cram_free_container_3751_9_F` — cmplog:4,930  n4:0

### 13. `cram_free_container` @ 3723:9
- **Statement**: `if (c->comp_hdr)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,310, n4: 3,600)
- **Flip strength**: 4,850 (blocked side hit 4,850× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,310  F:4,850
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_container_3723_9_T` — cmplog:4,310  n4:3,600
  - `htslib_cram_free_container_3723_9_F` — cmplog:4,850  n4:0

### 14. `sam_hdr_destroy` @ 134:9
- **Statement**: `if (bh->hrecs)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 11,100, n4: 7,330)
- **Flip strength**: 4,220 (blocked side hit 4,220× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11,100  F:4,220
- **n4 coverage**: T:7,330  F:0
- **Canonical identifiers**:
  - `htslib_sam_hdr_destroy_134_9_T` — cmplog:11,100  n4:7,330
  - `htslib_sam_hdr_destroy_134_9_F` — cmplog:4,220  n4:0

### 15. `header.c:add_stub_ref_sq_lines` @ 1109:19
- **Statement**: `for (tid = 0; tid < hrecs->nref; tid++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11,100, n4: 7,330)
- **Flip strength**: 4,030 (blocked side hit 4,030× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,030  F:11,100
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_header.c:add_stub_ref_sq_lines_1109_19_T` — cmplog:4,030  n4:0
  - `htslib_header.c:add_stub_ref_sq_lines_1109_19_F` — cmplog:11,100  n4:7,330

### 16. `sam_hdr_destroy` @ 127:9
- **Statement**: `if (bh->target_name) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11,700, n4: 7,330)
- **Flip strength**: 3,590 (blocked side hit 3,590× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,590  F:11,700
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hdr_destroy_127_9_T` — cmplog:3,590  n4:0
  - `htslib_sam_hdr_destroy_127_9_F` — cmplog:11,700  n4:7,330

### 17. `sam_hdr_fill_hrecs` @ 1134:9
- **Statement**: `if (bh->target_name && bh->target_len && bh->n_targets > 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 11,600, n4: 7,330)
- **Flip strength**: 3,540 (blocked side hit 3,540× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,540  F:11,600
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hdr_fill_hrecs_1134_9_T` — cmplog:3,540  n4:0
  - `htslib_sam_hdr_fill_hrecs_1134_9_F` — cmplog:11,600  n4:7,330

### 18. `sam_hdr_count_lines` @ 1789:13
- **Statement**: `if (sam_hdr_fill_hrecs(bh) != 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,650, n4: 5,490)
- **Flip strength**: 3,020 (blocked side hit 3,020× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,020  F:7,650
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_sam_hdr_count_lines_1789_13_T` — cmplog:3,020  n4:0
  - `htslib_sam_hdr_count_lines_1789_13_F` — cmplog:7,650  n4:5,490

### 19. `hts_detect_format2` @ 696:15
- **Statement**: `memcmp(s, "@CO\t", 4) == 0)) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 418, n4: 409)
- **Flip strength**: 3,000 (blocked side hit 3,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,000  F:418
- **n4 coverage**: T:0  F:409
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_696_15_T` — cmplog:3,000  n4:0
  - `htslib_hts_detect_format2_696_15_F` — cmplog:418  n4:409

### 20. `cram_free_container` @ 3720:9
- **Statement**: `if (c->landmark)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 6,510, n4: 3,600)
- **Flip strength**: 2,650 (blocked side hit 2,650× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,510  F:2,650
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_container_3720_9_T` — cmplog:6,510  n4:3,600
  - `htslib_cram_free_container_3720_9_F` — cmplog:2,650  n4:0

### 21. `sam_hrecs_free` @ 2461:9
- **Statement**: `if (hrecs->ref)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 12,700, n4: 7,330)
- **Flip strength**: 2,490 (blocked side hit 2,490× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,490  F:12,700
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hrecs_free_2461_9_T` — cmplog:2,490  n4:0
  - `htslib_sam_hrecs_free_2461_9_F` — cmplog:12,700  n4:7,330

### 22. `sam_hrecs_rebuild_text` @ 2018:22
- **Statement**: `if (!hrecs->h || !hrecs->h->size) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 6,010, n4: 5,490)
- **Flip strength**: 2,360 (blocked side hit 2,360× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,010  F:2,360
- **n4 coverage**: T:5,490  F:0
- **Canonical identifiers**:
  - `htslib_sam_hrecs_rebuild_text_2018_22_T` — cmplog:6,010  n4:5,490
  - `htslib_sam_hrecs_rebuild_text_2018_22_F` — cmplog:2,360  n4:0

### 23. `refs_free` @ 2438:39
- **Statement**: `for (k = kh_begin(r->h_meta); k != kh_end(r->h_meta); k++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,540, n4: 1,830)
- **Flip strength**: 2,200 (blocked side hit 2,200× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,200  F:4,540
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_refs_free_2438_39_T` — cmplog:2,200  n4:0
  - `htslib_refs_free_2438_39_F` — cmplog:4,540  n4:1,830

### 24. `hts_detect_format2` @ 694:45
- **Statement**: `(memcmp(s, "@HD\t", 4) == 0 || memcmp(s, "@SQ\t", 4) == 0 ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,970, n4: 409)
- **Flip strength**: 2,110 (blocked side hit 2,110× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,110  F:4,970
- **n4 coverage**: T:0  F:409
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_694_45_T` — cmplog:2,110  n4:0
  - `htslib_hts_detect_format2_694_45_F` — cmplog:4,970  n4:409

### 25. `cram_dopen` @ 5314:9
- **Statement**: `if (fd->mode == 'r') {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 2,070 (blocked side hit 2,070× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,070  F:3,630
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_dopen_5314_9_T` — cmplog:2,070  n4:0
  - `htslib_cram_dopen_5314_9_F` — cmplog:3,630  n4:1,830

### 26. `hts_detect_format2` @ 633:21
- **Statement**: `if (len >= 6 && memcmp(s,"CRAM",4) == 0 && s[4]>=1 && s[4]<=7 && s[5]<=7) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 13,900, n4: 7,350)
- **Flip strength**: 2,070 (blocked side hit 2,070× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,070  F:13,900
- **n4 coverage**: T:0  F:7,350
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_633_21_T` — cmplog:2,070  n4:0
  - `htslib_hts_detect_format2_633_21_F` — cmplog:13,900  n4:7,350

### 27. `refs_free` @ 2452:9
- **Statement**: `if (r->ref_id)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 2,530, n4: 1,830)
- **Flip strength**: 2,009 (blocked side hit 2,009× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,530  F:2,009
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_refs_free_2452_9_T` — cmplog:2,530  n4:1,830
  - `htslib_refs_free_2452_9_F` — cmplog:2,009  n4:0

### 28. `sam_hdr_update_target_arrays` @ 943:28
- **Statement**: `for (i = refs_changed; i < hrecs->nref; i++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,640, n4: 1,830)
- **Flip strength**: 1,950 (blocked side hit 1,950× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,950  F:3,640
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_update_target_arrays_943_28_T` — cmplog:1,950  n4:0
  - `htslib_sam_hdr_update_target_arrays_943_28_F` — cmplog:3,640  n4:1,830

### 29. `bam_hdr_write` @ 395:17
- **Statement**: `for (i = 0; i != h->n_targets; ++i) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,550, n4: 1,830)
- **Flip strength**: 1,880 (blocked side hit 1,880× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,880  F:3,550
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_bam_hdr_write_395_17_T` — cmplog:1,880  n4:0
  - `htslib_bam_hdr_write_395_17_F` — cmplog:3,550  n4:1,830

### 30. `bam_hdr_write` @ 388:13
- **Statement**: `if (l_text) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,770, n4: 1,830)
- **Flip strength**: 1,780 (blocked side hit 1,780× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,780  F:1,770
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_bam_hdr_write_388_13_T` — cmplog:1,780  n4:0
  - `htslib_bam_hdr_write_388_13_F` — cmplog:1,770  n4:1,830

### 31. `kstring.c:ks_resize` @ 162:6
- **Statement**: `if (s->m < size) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 41,600, n4: 229,000)
- **Flip strength**: 1,650 (blocked side hit 1,650× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:41,600  F:1,650
- **n4 coverage**: T:229,000  F:0
- **Canonical identifiers**:
  - `htslib_kstring.c:ks_resize_162_6_T` — cmplog:41,600  n4:229,000
  - `htslib_kstring.c:ks_resize_162_6_F` — cmplog:1,650  n4:0

### 32. `cram_free_block` @ 1562:9
- **Statement**: `if (!b)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 48,700, n4: 44,200)
- **Flip strength**: 1,530 (blocked side hit 1,530× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,530  F:48,700
- **n4 coverage**: T:0  F:44,200
- **Canonical identifiers**:
  - `htslib_cram_free_block_1562_9_T` — cmplog:1,530  n4:0
  - `htslib_cram_free_block_1562_9_F` — cmplog:48,700  n4:44,200

### 33. `hts_detect_format2` @ 695:45
- **Statement**: `memcmp(s, "@RG\t", 4) == 0 || memcmp(s, "@PG\t", 4) == 0 ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,420, n4: 409)
- **Flip strength**: 1,460 (blocked side hit 1,460× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,460  F:3,420
- **n4 coverage**: T:0  F:409
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_695_45_T` — cmplog:1,460  n4:0
  - `htslib_hts_detect_format2_695_45_F` — cmplog:3,420  n4:409

### 34. `sam.c:sam_format1_append` @ 4497:12
- **Statement**: `while (end - s >= 4) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,700, n4: 65,099)
- **Flip strength**: 1,310 (blocked side hit 1,310× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,310  F:5,700
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_sam.c:sam_format1_append_4497_12_T` — cmplog:1,310  n4:0
  - `htslib_sam.c:sam_format1_append_4497_12_F` — cmplog:5,700  n4:65,099

### 35. `hts_hopen` @ 1572:13
- **Statement**: `if (fp->fp.cram == NULL) goto error;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,540, n4: 1,830)
- **Flip strength**: 1,150 (blocked side hit 1,150× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,150  F:4,540
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_hts_hopen_1572_13_T` — cmplog:1,150  n4:0
  - `htslib_hts_hopen_1572_13_F` — cmplog:4,540  n4:1,830

### 36. `bam_aux_get` @ 4925:32
- **Statement**: `for (s = bam_aux_first(b); s; s = bam_aux_next(b, s))`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,460, n4: 65,099)
- **Flip strength**: 1,110 (blocked side hit 1,110× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,110  F:5,460
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_bam_aux_get_4925_32_T` — cmplog:1,110  n4:0
  - `htslib_bam_aux_get_4925_32_F` — cmplog:5,460  n4:65,099

### 37. `cram_free_container` @ 3754:42
- **Statement**: `for (k = kh_begin(c->tags_used); k != kh_end(c->tags_used); k++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,230, n4: 3,600)
- **Flip strength**: 1,070 (blocked side hit 1,070× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,070  F:4,230
- **n4 coverage**: T:0  F:3,600
- **Canonical identifiers**:
  - `htslib_cram_free_container_3754_42_T` — cmplog:1,070  n4:0
  - `htslib_cram_free_container_3754_42_F` — cmplog:4,230  n4:3,600

### 38. `cram_io.c:refs_from_header` @ 2777:13
- **Statement**: `if (-1 == sam_hdr_fill_hrecs(h))`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,400, n4: 1,830)
- **Flip strength**: 1,020 (blocked side hit 1,020× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,020  F:3,400
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_io.c:refs_from_header_2777_13_T` — cmplog:1,020  n4:0
  - `htslib_cram_io.c:refs_from_header_2777_13_F` — cmplog:3,400  n4:1,830

### 39. `sam_hdr_write` @ 2242:13
- **Statement**: `if (cram_set_header2(fd, h) < 0) return -1;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,530, n4: 1,830)
- **Flip strength**: 1,020 (blocked side hit 1,020× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,020  F:2,530
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_write_2242_13_T` — cmplog:1,020  n4:0
  - `htslib_sam_hdr_write_2242_13_F` — cmplog:2,530  n4:1,830

### 40. `hts_open_fuzzer.c:view_sam` @ 99:9
- **Statement**: `if (sam_hdr_write(out, hdr) != 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 9,650, n4: 5,490)
- **Flip strength**: 1,020 (blocked side hit 1,020× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,020  F:9,650
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_hts_open_fuzzer.c:view_sam_99_9_T` — cmplog:1,020  n4:0
  - `htslib_hts_open_fuzzer.c:view_sam_99_9_F` — cmplog:9,650  n4:5,490

### 41. `sam_hdr_destroy` @ 136:9
- **Statement**: `if (bh->sdict)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 14,300, n4: 7,330)
- **Flip strength**: 1,010 (blocked side hit 1,010× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,010  F:14,300
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hdr_destroy_136_9_T` — cmplog:1,010  n4:0
  - `htslib_sam_hdr_destroy_136_9_F` — cmplog:14,300  n4:7,330

### 42. `refs2id` @ 2747:17
- **Statement**: `for (i = 0; i < h->nref; i++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,530, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,000  F:2,530
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_refs2id_2747_17_T` — cmplog:1,000  n4:0
  - `htslib_refs2id_2747_17_F` — cmplog:2,530  n4:1,830

### 43. `sam_hdr_dup` @ 180:9
- **Statement**: `if (!h0->hrecs) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,230, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,000  F:3,230
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_dup_180_9_T` — cmplog:1,000  n4:0
  - `htslib_sam_hdr_dup_180_9_F` — cmplog:3,230  n4:1,830

### 44. `sam_hdr_dup` @ 200:9
- **Statement**: `if (h0->hrecs) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,230, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,230  F:1,000
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_sam_hdr_dup_200_9_T` — cmplog:3,230  n4:1,830
  - `htslib_sam_hdr_dup_200_9_F` — cmplog:1,000  n4:0

### 45. `bam_hdr_write` @ 352:9
- **Statement**: `if (h->hrecs) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 2,550, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,550  F:1,000
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_bam_hdr_write_352_9_T` — cmplog:2,550  n4:1,830
  - `htslib_bam_hdr_write_352_9_F` — cmplog:1,000  n4:0

### 46. `sam_hdr_write` @ 2254:13
- **Statement**: `if (!h->hrecs && !h->text)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,550, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,000  F:2,550
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_write_2254_13_T` — cmplog:1,000  n4:0
  - `htslib_sam_hdr_write_2254_13_F` — cmplog:2,550  n4:1,830

### 47. `sam_hdr_write` @ 2262:13
- **Statement**: `if (h->hrecs) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 2,550, n4: 1,830)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,550  F:1,000
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_sam_hdr_write_2262_13_T` — cmplog:2,550  n4:1,830
  - `htslib_sam_hdr_write_2262_13_F` — cmplog:1,000  n4:0

### 48. `cram_encode_compression_header` @ 471:42
- **Statement**: `for (k = kh_begin(c->tags_used); k != kh_end(c->tags_used); k++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 984 (blocked side hit 984× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:984  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode_compression_header_471_42_T` — cmplog:984  n4:0
  - `htslib_cram_encode_compression_header_471_42_F` — cmplog:1,680  n4:1,770

### 49. `cram_close` @ 5643:43
- **Statement**: `for (k = kh_begin(fd->tags_used); k != kh_end(fd->tags_used); k++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,540, n4: 1,830)
- **Flip strength**: 960 (blocked side hit 960× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:960  F:4,540
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_close_5643_43_T` — cmplog:960  n4:0
  - `htslib_cram_close_5643_43_F` — cmplog:4,540  n4:1,830

### 50. `cram_encode.c:kh_resize_m_s2i` @ 187:27
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,750, n4: 3,030)
- **Flip strength**: 930 (blocked side hit 930× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,750  F:0
- **n4 coverage**: T:3,030  F:930
- **Canonical identifiers**:
  - `htslib_cram_encode.c:kh_resize_m_s2i_187_27_T` — cmplog:1,750  n4:3,030
  - `htslib_cram_encode.c:kh_resize_m_s2i_187_27_F` — cmplog:0  n4:930

### 51. `cram_encode.c:kh_resize_m_s2i` @ 177:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,750, n4: 3,030)
- **Flip strength**: 930 (blocked side hit 930× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,750  F:0
- **n4 coverage**: T:3,030  F:930
- **Canonical identifiers**:
  - `htslib_cram_encode.c:kh_resize_m_s2i_177_24_T` — cmplog:1,750  n4:3,030
  - `htslib_cram_encode.c:kh_resize_m_s2i_177_24_F` — cmplog:0  n4:930

### 52. `cram_dopen` @ 5353:25
- **Statement**: `fd->prefix = strdup((cp = strrchr(filename, '/')) ? cp+1 : filename);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,630  F:916
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_dopen_5353_25_T` — cmplog:3,630  n4:1,830
  - `htslib_cram_dopen_5353_25_F` — cmplog:916  n4:0

### 53. `cram_close` @ 5570:9
- **Statement**: `if (fd->mode == 'w' && fd->ctr) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,630  F:916
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_close_5570_9_T` — cmplog:3,630  n4:1,830
  - `htslib_cram_close_5570_9_F` — cmplog:916  n4:0

### 54. `cram_close` @ 5578:9
- **Statement**: `if (fd->mode != 'w')`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:916  F:3,630
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_close_5578_9_T` — cmplog:916  n4:0
  - `htslib_cram_close_5578_9_F` — cmplog:3,630  n4:1,830

### 55. `cram_close` @ 5600:21
- **Statement**: `if (ret == 0 && fd->mode == 'w') {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,610, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,610  F:916
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_close_5600_21_T` — cmplog:3,610  n4:1,830
  - `htslib_cram_close_5600_21_F` — cmplog:916  n4:0

### 56. `hts_hopen` @ 1573:13
- **Statement**: `if (!fp->is_write)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:916  F:3,630
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_hts_hopen_1573_13_T` — cmplog:916  n4:0
  - `htslib_hts_hopen_1573_13_F` — cmplog:3,630  n4:1,830

### 57. `hts_close` @ 1645:13
- **Statement**: `if (!fp->is_write) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 916 (blocked side hit 916× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:916  F:3,630
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_hts_close_1645_13_T` — cmplog:916  n4:0
  - `htslib_hts_close_1645_13_F` — cmplog:3,630  n4:1,830

### 58. `cram_dopen` @ 5379:19
- **Statement**: `fd->use_tok = (CRAM_MAJOR_VERS(fd->version) >= 3) && (CRAM_MINOR_VERS(fd->version) >= 1);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,680, n4: 1,830)
- **Flip strength**: 860 (blocked side hit 860× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,680  F:860
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_dopen_5379_19_T` — cmplog:3,680  n4:1,830
  - `htslib_cram_dopen_5379_19_F` — cmplog:860  n4:0

### 59. `cram_encode.c:cram_encode_aux` @ 2800:12
- **Statement**: `while (aux_end - aux >= 1 && aux[0] != 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,360, n4: 65,099)
- **Flip strength**: 854 (blocked side hit 854× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:854  F:5,360
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_encode_aux_2800_12_T` — cmplog:854  n4:0
  - `htslib_cram_encode.c:cram_encode_aux_2800_12_F` — cmplog:5,360  n4:65,099

### 60. `hts_detect_format2` @ 641:13
- **Statement**: `if (memcmp(s, "BAM\1", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 28, n4: 2)
- **Flip strength**: 793 (blocked side hit 793× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:793  F:28
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_641_13_T` — cmplog:793  n4:0
  - `htslib_hts_detect_format2_641_13_F` — cmplog:28  n4:2

### 61. `hts_hopen` @ 1563:5
- **Statement**: `case bam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 26,600, n4: 13,000)
- **Flip strength**: 793 (blocked side hit 793× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:793  F:26,600
- **n4 coverage**: T:0  F:13,000
- **Canonical identifiers**:
  - `htslib_hts_hopen_1563_5_T` — cmplog:793  n4:0
  - `htslib_hts_hopen_1563_5_F` — cmplog:26,600  n4:13,000

### 62. `sam.c:kputsn_` @ 276:19
- **Statement**: `if (ks_resize(s, new_sz ? new_sz : 1) < 0) return EOF;`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 21,500, n4: 250,000)
- **Flip strength**: 771 (blocked side hit 771× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:21,500  F:771
- **n4 coverage**: T:250,000  F:0
- **Canonical identifiers**:
  - `htslib_sam.c:kputsn__276_19_T` — cmplog:21,500  n4:250,000
  - `htslib_sam.c:kputsn__276_19_F` — cmplog:771  n4:0

### 63. `cram_write_SAM_hdr` @ 5025:13
- **Statement**: `if (header_len)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,770, n4: 1,830)
- **Flip strength**: 761 (blocked side hit 761× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:761  F:1,770
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_write_SAM_hdr_5025_13_T` — cmplog:761  n4:0
  - `htslib_cram_write_SAM_hdr_5025_13_F` — cmplog:1,770  n4:1,830

### 64. `sam_hdr_update_target_arrays` @ 924:9
- **Statement**: `if (bh->n_targets < hrecs->nref) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,900, n4: 1,830)
- **Flip strength**: 735 (blocked side hit 735× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:735  F:2,900
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_update_target_arrays_924_9_T` — cmplog:735  n4:0
  - `htslib_sam_hdr_update_target_arrays_924_9_F` — cmplog:2,900  n4:1,830

### 65. `cram_io.c:itf8_size` @ 756:49
- **Statement**: `return ((!((v)&~0x7f))?1:(!((v)&~0x3fff))?2:(!((v)&~0x1fffff))?3:(!((v)&~0xfffffff))?4:5);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 782, n4: 949)
- **Flip strength**: 706 (blocked side hit 706× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:782  F:706
- **n4 coverage**: T:949  F:0
- **Canonical identifiers**:
  - `htslib_cram_io.c:itf8_size_756_49_T` — cmplog:782  n4:949
  - `htslib_cram_io.c:itf8_size_756_49_F` — cmplog:706  n4:0

### 66. `sam_hdr_write` @ 2287:13
- **Statement**: `if (no_sq) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,850, n4: 1,830)
- **Flip strength**: 703 (blocked side hit 703× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:703  F:2,850
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_sam_hdr_write_2287_13_T` — cmplog:703  n4:0
  - `htslib_sam_hdr_write_2287_13_F` — cmplog:2,850  n4:1,830

### 67. `cram_io.c:refs_from_header` @ 2781:9
- **Statement**: `if (h->hrecs->nref == 0)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,290, n4: 3,660)
- **Flip strength**: 692 (blocked side hit 692× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,290  F:692
- **n4 coverage**: T:3,660  F:0
- **Canonical identifiers**:
  - `htslib_cram_io.c:refs_from_header_2781_9_T` — cmplog:5,290  n4:3,660
  - `htslib_cram_io.c:refs_from_header_2781_9_F` — cmplog:692  n4:0

### 68. `sam_hdr_read` @ 2204:5
- **Statement**: `case cram:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10,200, n4: 5,490)
- **Flip strength**: 687 (blocked side hit 687× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:687  F:10,200
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_sam_hdr_read_2204_5_T` — cmplog:687  n4:0
  - `htslib_sam_hdr_read_2204_5_F` — cmplog:10,200  n4:5,490

### 69. `sam_read1` @ 4390:9
- **Statement**: `case cram:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 25,500, n4: 200,000)
- **Flip strength**: 687 (blocked side hit 687× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:687  F:25,500
- **n4 coverage**: T:0  F:200,000
- **Canonical identifiers**:
  - `htslib_sam_read1_4390_9_T` — cmplog:687  n4:0
  - `htslib_sam_read1_4390_9_F` — cmplog:25,500  n4:200,000

### 70. `bgzf.c:bgzf_read_init` @ 402:35
- **Statement**: `return NULL;`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 202, n4: 7)
- **Flip strength**: 628 (blocked side hit 628× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:202  F:628
- **n4 coverage**: T:7  F:0
- **Canonical identifiers**:
  - `htslib_bgzf.c:bgzf_read_init_402_35_T` — cmplog:202  n4:7
  - `htslib_bgzf.c:bgzf_read_init_402_35_F` — cmplog:628  n4:0

### 71. `sam_hdr_read` @ 2201:5
- **Statement**: `case bam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10,300, n4: 5,490)
- **Flip strength**: 594 (blocked side hit 594× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:594  F:10,300
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_sam_hdr_read_2201_5_T` — cmplog:594  n4:0
  - `htslib_sam_hdr_read_2201_5_F` — cmplog:10,300  n4:5,490

### 72. `cram_free_slice` @ 4450:21
- **Statement**: `for (i = 0; i < s->naux_block; i++)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,730, n4: 1,770)
- **Flip strength**: 510 (blocked side hit 510× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:510  F:1,730
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4450_21_T` — cmplog:510  n4:0
  - `htslib_cram_free_slice_4450_21_F` — cmplog:1,730  n4:1,770

### 73. `cram_encode.c:cram_encode_slice` @ 1166:21
- **Statement**: `for (n = 0; n < s->naux_block; n++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 485 (blocked side hit 485× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:485  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_encode_slice_1166_21_T` — cmplog:485  n4:0
  - `htslib_cram_encode.c:cram_encode_slice_1166_21_F` — cmplog:1,680  n4:1,770

### 74. `cram_encode.c:cram_compress_slice` @ 956:49
- **Statement**: `for (i = DS_END /*num_blk - naux_blk*/; i < s->hdr->num_blocks; i++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 485 (blocked side hit 485× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:485  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_compress_slice_956_49_T` — cmplog:485  n4:0
  - `htslib_cram_encode.c:cram_compress_slice_956_49_F` — cmplog:1,680  n4:1,770

### 75. `bam_aux_first` @ 4903:9
- **Statement**: `if (end - s <= 2) { errno = ENOENT; return NULL; }`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,020, n4: 65,099)
- **Flip strength**: 461 (blocked side hit 461× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,020  F:461
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_bam_aux_first_4903_9_T` — cmplog:5,020  n4:65,099
  - `htslib_bam_aux_first_4903_9_F` — cmplog:461  n4:0

### 76. `kvsprintf` @ 166:6
- **Statement**: `if (l + 1 > s->m - s->l) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10,900, n4: 4,030)
- **Flip strength**: 435 (blocked side hit 435× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:435  F:10,900
- **n4 coverage**: T:0  F:4,030
- **Canonical identifiers**:
  - `htslib_kvsprintf_166_6_T` — cmplog:435  n4:0
  - `htslib_kvsprintf_166_6_F` — cmplog:10,900  n4:4,030

### 77. `sam_hdr_fill_hrecs` @ 1156:9
- **Statement**: `if (hrecs->refs_changed >= 0 && rebuild_target_arrays(bh) != 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10,700, n4: 7,330)
- **Flip strength**: 405 (blocked side hit 405× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:405  F:10,700
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hdr_fill_hrecs_1156_9_T` — cmplog:405  n4:0
  - `htslib_sam_hdr_fill_hrecs_1156_9_F` — cmplog:10,700  n4:7,330

### 78. `sam_read1` @ 4386:9
- **Statement**: `case bam:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 25,800, n4: 200,000)
- **Flip strength**: 365 (blocked side hit 365× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:365  F:25,800
- **n4 coverage**: T:0  F:200,000
- **Canonical identifiers**:
  - `htslib_sam_read1_4386_9_T` — cmplog:365  n4:0
  - `htslib_sam_read1_4386_9_F` — cmplog:25,800  n4:200,000

### 79. `hts_detect_format2` @ 686:27
- **Statement**: `else if (len >= 16 && memcmp(s, "##fileformat=VCF", 16) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 12,400, n4: 7,050)
- **Flip strength**: 357 (blocked side hit 357× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:357  F:12,400
- **n4 coverage**: T:0  F:7,050
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_686_27_T` — cmplog:357  n4:0
  - `htslib_hts_detect_format2_686_27_F` — cmplog:12,400  n4:7,050

### 80. `hts_hopen` @ 1584:5
- **Statement**: `case vcf:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 27,000, n4: 13,000)
- **Flip strength**: 357 (blocked side hit 357× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:357  F:27,000
- **n4 coverage**: T:0  F:13,000
- **Canonical identifiers**:
  - `htslib_hts_hopen_1584_5_T` — cmplog:357  n4:0
  - `htslib_hts_hopen_1584_5_F` — cmplog:27,000  n4:13,000

### 81. `hts_close` @ 1664:5
- **Statement**: `case vcf:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 25,800, n4: 12,900)
- **Flip strength**: 357 (blocked side hit 357× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:357  F:25,800
- **n4 coverage**: T:0  F:12,900
- **Canonical identifiers**:
  - `htslib_hts_close_1664_5_T` — cmplog:357  n4:0
  - `htslib_hts_close_1664_5_F` — cmplog:25,800  n4:12,900

### 82. `cram_write_SAM_hdr` @ 4924:21
- **Statement**: `for (i = 0; i < hdr->hrecs->nref; i++) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,190, n4: 1,830)
- **Flip strength**: 350 (blocked side hit 350× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:350  F:2,190
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_write_SAM_hdr_4924_21_T` — cmplog:350  n4:0
  - `htslib_cram_write_SAM_hdr_4924_21_F` — cmplog:2,190  n4:1,830

### 83. `refs2id` @ 2737:9
- **Statement**: `if (r->ref_id)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,190, n4: 1,830)
- **Flip strength**: 346 (blocked side hit 346× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:346  F:2,190
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_refs2id_2737_9_T` — cmplog:346  n4:0
  - `htslib_refs2id_2737_9_F` — cmplog:2,190  n4:1,830

### 84. `sam_hrecs_free` @ 2473:9
- **Statement**: `if (hrecs->pg)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 14,800, n4: 7,330)
- **Flip strength**: 345 (blocked side hit 345× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:345  F:14,800
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hrecs_free_2473_9_T` — cmplog:345  n4:0
  - `htslib_sam_hrecs_free_2473_9_F` — cmplog:14,800  n4:7,330

### 85. `cram_get_ref` @ 3410:9
- **Statement**: `if (id == -1 || start < 1)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,650, n4: 1,770)
- **Flip strength**: 341 (blocked side hit 341× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,650  F:341
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_get_ref_3410_9_T` — cmplog:1,650  n4:1,770
  - `htslib_cram_get_ref_3410_9_F` — cmplog:341  n4:0

### 86. `cram_io.c:cram_compress_block3` @ 2286:13
- **Statement**: `if (comp_size < b->uncomp_size) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2,250, n4: 1,830)
- **Flip strength**: 315 (blocked side hit 315× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:315  F:2,250
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_io.c:cram_compress_block3_2286_13_T` — cmplog:315  n4:0
  - `htslib_cram_io.c:cram_compress_block3_2286_13_F` — cmplog:2,250  n4:1,830

### 87. `cram_io.c:cram_init_tables` @ 5193:9
- **Statement**: `if (CRAM_MAJOR_VERS(fd->version) == 1) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,390, n4: 1,830)
- **Flip strength**: 311 (blocked side hit 311× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:311  F:5,390
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_io.c:cram_init_tables_5193_9_T` — cmplog:311  n4:0
  - `htslib_cram_io.c:cram_init_tables_5193_9_F` — cmplog:5,390  n4:1,830

### 88. `cram_free_compression_header` @ 4401:9
- **Statement**: `if (hdr->TD_hash)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,230, n4: 3,600)
- **Flip strength**: 306 (blocked side hit 306× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,230  F:306
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4401_9_T` — cmplog:4,230  n4:3,600
  - `htslib_cram_free_compression_header_4401_9_F` — cmplog:306  n4:0

### 89. `cram_free_compression_header` @ 4403:9
- **Statement**: `if (hdr->TD_keys)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,230, n4: 3,600)
- **Flip strength**: 306 (blocked side hit 306× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,230  F:306
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4403_9_T` — cmplog:4,230  n4:3,600
  - `htslib_cram_free_compression_header_4403_9_F` — cmplog:306  n4:0

### 90. `sam_hrecs_free` @ 2476:9
- **Statement**: `if (hrecs->pg_end)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 14,900, n4: 7,330)
- **Flip strength**: 285 (blocked side hit 285× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:285  F:14,900
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hrecs_free_2476_9_T` — cmplog:285  n4:0
  - `htslib_sam_hrecs_free_2476_9_F` — cmplog:14,900  n4:7,330

### 91. `cram_byte_array_len_encode_store` @ 3489:9
- **Statement**: `if (prefix) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 282 (blocked side hit 282× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,680  F:282
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_byte_array_len_encode_store_3489_9_T` — cmplog:1,680  n4:1,770
  - `htslib_cram_byte_array_len_encode_store_3489_9_F` — cmplog:282  n4:0

### 92. `cram_free_compression_header` @ 4399:9
- **Statement**: `if (hdr->TD_blk)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,260, n4: 3,600)
- **Flip strength**: 282 (blocked side hit 282× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,260  F:282
- **n4 coverage**: T:3,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4399_9_T` — cmplog:4,260  n4:3,600
  - `htslib_cram_free_compression_header_4399_9_F` — cmplog:282  n4:0

### 93. `cram_huffman_encode_store` @ 3113:9
- **Statement**: `if (prefix) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 19,200, n4: 17,700)
- **Flip strength**: 233 (blocked side hit 233× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:19,200  F:233
- **n4 coverage**: T:17,700  F:0
- **Canonical identifiers**:
  - `htslib_cram_huffman_encode_store_3113_9_T` — cmplog:19,200  n4:17,700
  - `htslib_cram_huffman_encode_store_3113_9_F` — cmplog:233  n4:0

### 94. `hts_open_fuzzer.c:view_sam` @ 87:9
- **Statement**: `if (hdr == NULL) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 10,600, n4: 5,490)
- **Flip strength**: 219 (blocked side hit 219× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:219  F:10,600
- **n4 coverage**: T:0  F:5,490
- **Canonical identifiers**:
  - `htslib_hts_open_fuzzer.c:view_sam_87_9_T` — cmplog:219  n4:0
  - `htslib_hts_open_fuzzer.c:view_sam_87_9_F` — cmplog:10,600  n4:5,490

### 95. `cram_byte_array_stop_encode_store` @ 3733:9
- **Statement**: `if (prefix) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,050, n4: 5,320)
- **Flip strength**: 203 (blocked side hit 203× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,050  F:203
- **n4 coverage**: T:5,320  F:0
- **Canonical identifiers**:
  - `htslib_cram_byte_array_stop_encode_store_3733_9_T` — cmplog:5,050  n4:5,320
  - `htslib_cram_byte_array_stop_encode_store_3733_9_F` — cmplog:203  n4:0

### 96. `hts_close` @ 1638:5
- **Statement**: `case binary_format:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 25,900, n4: 12,900)
- **Flip strength**: 199 (blocked side hit 199× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:199  F:25,900
- **n4 coverage**: T:0  F:12,900
- **Canonical identifiers**:
  - `htslib_hts_close_1638_5_T` — cmplog:199  n4:0
  - `htslib_hts_close_1638_5_F` — cmplog:25,900  n4:12,900

### 97. `cram_encode_container` @ 2081:13
- **Statement**: `if (c->tags_used->n_occupied) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,490, n4: 1,770)
- **Flip strength**: 195 (blocked side hit 195× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:195  F:1,490
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode_container_2081_13_T` — cmplog:195  n4:0
  - `htslib_cram_encode_container_2081_13_F` — cmplog:1,490  n4:1,770

### 98. `cram_free_slice` @ 4498:9
- **Statement**: `if (s->aux_block)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,530, n4: 1,770)
- **Flip strength**: 195 (blocked side hit 195× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:195  F:1,530
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4498_9_T` — cmplog:195  n4:0
  - `htslib_cram_free_slice_4498_9_F` — cmplog:1,530  n4:1,770

### 99. `sam.c:kputll` @ 393:9
- **Statement**: `if (x <= UINT32_MAX)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 16,900, n4: 195,000)
- **Flip strength**: 189 (blocked side hit 189× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16,900  F:189
- **n4 coverage**: T:195,000  F:0
- **Canonical identifiers**:
  - `htslib_sam.c:kputll_393_9_T` — cmplog:16,900  n4:195,000
  - `htslib_sam.c:kputll_393_9_F` — cmplog:189  n4:0

### 100. `cram_encode.c:cram_compress_slice` @ 974:47
- **Statement**: `for (i = 1; i < s->hdr->num_blocks && i < DS_END; i++) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 77,500, n4: 81,600)
- **Flip strength**: 187 (blocked side hit 187× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:77,500  F:187
- **n4 coverage**: T:81,600  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_compress_slice_974_47_T` — cmplog:77,500  n4:81,600
  - `htslib_cram_encode.c:cram_compress_slice_974_47_F` — cmplog:187  n4:0

### 101. `hts_detect_format2` @ 694:15
- **Statement**: `(memcmp(s, "@HD\t", 4) == 0 || memcmp(s, "@SQ\t", 4) == 0 ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,080, n4: 409)
- **Flip strength**: 184 (blocked side hit 184× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:184  F:7,080
- **n4 coverage**: T:0  F:409
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_694_15_T` — cmplog:184  n4:0
  - `htslib_hts_detect_format2_694_15_F` — cmplog:7,080  n4:409

### 102. `tokenise_name3.c:free_context` @ 215:9
- **Statement**: `if (ctx->t_head)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 2,840, n4: 2,330)
- **Flip strength**: 184 (blocked side hit 184× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,840  F:184
- **n4 coverage**: T:2,330  F:0
- **Canonical identifiers**:
  - `htslib_tokenise_name3.c:free_context_215_9_T` — cmplog:2,840  n4:2,330
  - `htslib_tokenise_name3.c:free_context_215_9_F` — cmplog:184  n4:0

### 103. `hts_open_fuzzer.c:view_sam` @ 107:13
- **Statement**: `if (sam_write1(out, hdr, b) < 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,500, n4: 195,000)
- **Flip strength**: 174 (blocked side hit 174× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:174  F:16,500
- **n4 coverage**: T:0  F:195,000
- **Canonical identifiers**:
  - `htslib_hts_open_fuzzer.c:view_sam_107_13_T` — cmplog:174  n4:0
  - `htslib_hts_open_fuzzer.c:view_sam_107_13_F` — cmplog:16,500  n4:195,000

### 104. `sam.c:hts_reg2bin` @ 1510:13
- **Statement**: `if (beg>>s == end>>s) return t + (beg>>s);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 18,000, n4: 195,000)
- **Flip strength**: 163 (blocked side hit 163× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18,000  F:163
- **n4 coverage**: T:195,000  F:0
- **Canonical identifiers**:
  - `htslib_sam.c:hts_reg2bin_1510_13_T` — cmplog:18,000  n4:195,000
  - `htslib_sam.c:hts_reg2bin_1510_13_F` — cmplog:163  n4:0

### 105. `hts_detect_format2` @ 576:17
- **Statement**: `if (memcmp(&s[12], "BC\2\0", 4) == 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 30, n4: 5)
- **Flip strength**: 156 (blocked side hit 156× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:156  F:30
- **n4 coverage**: T:0  F:5
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_576_17_T` — cmplog:156  n4:0
  - `htslib_hts_detect_format2_576_17_F` — cmplog:30  n4:5

### 106. `bgzf.c:bgzf_read_init` @ 403:60
- **Statement**: `mc++;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 30, n4: 5)
- **Flip strength**: 155 (blocked side hit 155× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:155  F:30
- **n4 coverage**: T:0  F:5
- **Canonical identifiers**:
  - `htslib_bgzf.c:bgzf_read_init_403_60_T` — cmplog:155  n4:0
  - `htslib_bgzf.c:bgzf_read_init_403_60_F` — cmplog:30  n4:5

### 107. `cram_encode.c:cram_encode_slice_read` @ 598:9
- **Statement**: `if (c->pos_sorted) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,200, n4: 65,099)
- **Flip strength**: 137 (blocked side hit 137× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,200  F:137
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_encode_slice_read_598_9_T` — cmplog:5,200  n4:65,099
  - `htslib_cram_encode.c:cram_encode_slice_read_598_9_F` — cmplog:137  n4:0

### 108. `LLVMFuzzerTestOneInput` @ 205:9
- **Statement**: `case variant_data:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,730, n4: 1,940)
- **Flip strength**: 126 (blocked side hit 126× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:126  F:3,730
- **n4 coverage**: T:0  F:1,940
- **Canonical identifiers**:
  - `htslib_LLVMFuzzerTestOneInput_205_9_T` — cmplog:126  n4:0
  - `htslib_LLVMFuzzerTestOneInput_205_9_F` — cmplog:3,730  n4:1,940

### 109. `kvsprintf` @ 155:6
- **Statement**: `if (!s->s) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 11,200, n4: 4,030)
- **Flip strength**: 112 (blocked side hit 112× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11,200  F:112
- **n4 coverage**: T:4,030  F:0
- **Canonical identifiers**:
  - `htslib_kvsprintf_155_6_T` — cmplog:11,200  n4:4,030
  - `htslib_kvsprintf_155_6_F` — cmplog:112  n4:0

### 110. `bgzf_close` @ 2116:11
- **Statement**: `ret = fp->errcode ? -1 : 0;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,510, n4: 1,840)
- **Flip strength**: 108 (blocked side hit 108× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:108  F:4,510
- **n4 coverage**: T:0  F:1,840
- **Canonical identifiers**:
  - `htslib_bgzf_close_2116_11_T` — cmplog:108  n4:0
  - `htslib_bgzf_close_2116_11_F` — cmplog:4,510  n4:1,840

### 111. `bam_write1` @ 869:31
- **Statement**: `c->isize < INT_MIN || c->isize > INT_MAX) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,480, n4: 65,099)
- **Flip strength**: 107 (blocked side hit 107× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:107  F:5,480
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_bam_write1_869_31_T` — cmplog:107  n4:0
  - `htslib_bam_write1_869_31_F` — cmplog:5,480  n4:65,099

### 112. `sam_hrecs_free` @ 2467:9
- **Statement**: `if (hrecs->rg)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 15,100, n4: 7,330)
- **Flip strength**: 90 (blocked side hit 90× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:90  F:15,100
- **n4 coverage**: T:0  F:7,330
- **Canonical identifiers**:
  - `htslib_sam_hrecs_free_2467_9_T` — cmplog:90  n4:0
  - `htslib_sam_hrecs_free_2467_9_F` — cmplog:15,100  n4:7,330

### 113. `bam_cigar2qlen` @ 651:21
- **Statement**: `for (k = l = 0; k < n_cigar; ++k)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,900, n4: 55,400)
- **Flip strength**: 85 (blocked side hit 85× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:85  F:5,900
- **n4 coverage**: T:0  F:55,400
- **Canonical identifiers**:
  - `htslib_bam_cigar2qlen_651_21_T` — cmplog:85  n4:0
  - `htslib_bam_cigar2qlen_651_21_F` — cmplog:5,900  n4:55,400

### 114. `cram_encode.c:process_one_read` @ 3403:9
- **Statement**: `if (!no_ref || CRAM_MAJOR_VERS(fd->version) >= 3)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,290, n4: 65,099)
- **Flip strength**: 82 (blocked side hit 82× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,290  F:82
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3403_9_T` — cmplog:5,290  n4:65,099
  - `htslib_cram_encode.c:process_one_read_3403_9_F` — cmplog:82  n4:0

### 115. `cram_encode.c:process_one_read` @ 71:20
- **Statement**: `int i;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,290, n4: 65,099)
- **Flip strength**: 77 (blocked side hit 77× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:77  F:5,290
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_71_20_T` — cmplog:77  n4:0
  - `htslib_cram_encode.c:process_one_read_71_20_F` — cmplog:5,290  n4:65,099

### 116. `hts_detect_format2` @ 695:15
- **Statement**: `memcmp(s, "@RG\t", 4) == 0 || memcmp(s, "@PG\t", 4) == 0 ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,890, n4: 409)
- **Flip strength**: 76 (blocked side hit 76× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:76  F:4,890
- **n4 coverage**: T:0  F:409
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_695_15_T` — cmplog:76  n4:0
  - `htslib_hts_detect_format2_695_15_F` — cmplog:4,890  n4:409

### 117. `cram_close` @ 5620:9
- **Statement**: `if (fd->header)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,470, n4: 1,830)
- **Flip strength**: 73 (blocked side hit 73× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,470  F:73
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_close_5620_9_T` — cmplog:4,470  n4:1,830
  - `htslib_cram_close_5620_9_F` — cmplog:73  n4:0

### 118. `sam.c:kputw` @ 370:9
- **Statement**: `if (c < 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 22,600, n4: 130,000)
- **Flip strength**: 65 (blocked side hit 65× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:65  F:22,600
- **n4 coverage**: T:0  F:130,000
- **Canonical identifiers**:
  - `htslib_sam.c:kputw_370_9_T` — cmplog:65  n4:0
  - `htslib_sam.c:kputw_370_9_F` — cmplog:22,600  n4:130,000

### 119. `cram_close` @ 5628:9
- **Statement**: `if (fd->ctr_mt && fd->ctr_mt != fd->ctr)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,480, n4: 1,830)
- **Flip strength**: 63 (blocked side hit 63× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:63  F:4,480
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_close_5628_9_T` — cmplog:63  n4:0
  - `htslib_cram_close_5628_9_F` — cmplog:4,480  n4:1,830

### 120. `cram_encode.c:process_one_read` @ 3415:13
- **Statement**: `*/`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,260, n4: 65,099)
- **Flip strength**: 58 (blocked side hit 58× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:58  F:5,260
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3415_13_T` — cmplog:58  n4:0
  - `htslib_cram_encode.c:process_one_read_3415_13_F` — cmplog:5,260  n4:65,099

### 121. `cram_encode_container` @ 2183:9
- **Statement**: `if (c->pos_sorted || CRAM_MAJOR_VERS(fd->version) >= 4) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,630, n4: 1,770)
- **Flip strength**: 55 (blocked side hit 55× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,630  F:55
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode_container_2183_9_T` — cmplog:1,630  n4:1,770
  - `htslib_cram_encode_container_2183_9_F` — cmplog:55  n4:0

### 122. `cram_dopen` @ 5379:58
- **Statement**: `fd->use_tok = (CRAM_MAJOR_VERS(fd->version) >= 3) && (CRAM_MINOR_VERS(fd->version) >= 1);`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,630, n4: 1,830)
- **Flip strength**: 52 (blocked side hit 52× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,630  F:52
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_dopen_5379_58_T` — cmplog:3,630  n4:1,830
  - `htslib_cram_dopen_5379_58_F` — cmplog:52  n4:0

### 123. `bam_write1` @ 867:9
- **Statement**: `if (c->pos > INT_MAX ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,600, n4: 65,099)
- **Flip strength**: 51 (blocked side hit 51× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:51  F:5,600
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_bam_write1_867_9_T` — cmplog:51  n4:0
  - `htslib_bam_write1_867_9_F` — cmplog:5,600  n4:65,099

### 124. `cram_encode_compression_header` @ 167:17
- **Statement**: `if (no_ref || embed_ref>0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,630, n4: 1,770)
- **Flip strength**: 50 (blocked side hit 50× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:50  F:1,630
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode_compression_header_167_17_T` — cmplog:50  n4:0
  - `htslib_cram_encode_compression_header_167_17_F` — cmplog:1,630  n4:1,770

### 125. `cram_encode_compression_header` @ 201:13
- **Statement**: `case CRAM_KEY('R','R'):`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 6,740, n4: 7,100)
- **Flip strength**: 50 (blocked side hit 50× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:50  F:6,740
- **n4 coverage**: T:0  F:7,100
- **Canonical identifiers**:
  - `htslib_cram_encode_compression_header_201_13_T` — cmplog:50  n4:0
  - `htslib_cram_encode_compression_header_201_13_F` — cmplog:6,740  n4:7,100

### 126. `cram_encode_container` @ 1871:13
- **Statement**: `if (embed_ref <= 1) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,650, n4: 1,770)
- **Flip strength**: 50 (blocked side hit 50× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,650  F:50
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode_container_1871_13_T` — cmplog:1,650  n4:1,770
  - `htslib_cram_encode_container_1871_13_F` — cmplog:50  n4:0

### 127. `cram_encode_container` @ 1939:9
- **Statement**: `if (!no_ref && c->refs_used) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,650, n4: 1,770)
- **Flip strength**: 50 (blocked side hit 50× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,650  F:50
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode_container_1939_9_T` — cmplog:1,650  n4:1,770
  - `htslib_cram_encode_container_1939_9_F` — cmplog:50  n4:0

### 128. `cram_encode_container` @ 2528:9
- **Statement**: `if (!no_ref && c->refs_used) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,630, n4: 1,770)
- **Flip strength**: 50 (blocked side hit 50× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,630  F:50
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode_container_2528_9_T` — cmplog:1,630  n4:1,770
  - `htslib_cram_encode_container_2528_9_F` — cmplog:50  n4:0

### 129. `cram_stats.c:kh_resize_m_i2i` @ 187:27
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5,600, n4: 5,930)
- **Flip strength**: 49 (blocked side hit 49× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,600  F:0
- **n4 coverage**: T:5,930  F:49
- **Canonical identifiers**:
  - `htslib_cram_stats.c:kh_resize_m_i2i_187_27_T` — cmplog:5,600  n4:5,930
  - `htslib_cram_stats.c:kh_resize_m_i2i_187_27_F` — cmplog:0  n4:49

### 130. `cram_stats.c:kh_resize_m_i2i` @ 177:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5,600, n4: 5,930)
- **Flip strength**: 49 (blocked side hit 49× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,600  F:0
- **n4 coverage**: T:5,930  F:49
- **Canonical identifiers**:
  - `htslib_cram_stats.c:kh_resize_m_i2i_177_24_T` — cmplog:5,600  n4:5,930
  - `htslib_cram_stats.c:kh_resize_m_i2i_177_24_F` — cmplog:0  n4:49

### 131. `cram_encode.c:process_one_read` @ 3414:9
- **Statement**: `* Or shortcut for unsorted data where we load once and never free?`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,320, n4: 65,099)
- **Flip strength**: 49 (blocked side hit 49× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,320  F:49
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3414_9_T` — cmplog:5,320  n4:65,099
  - `htslib_cram_encode.c:process_one_read_3414_9_F` — cmplog:49  n4:0

### 132. `cram_free_slice` @ 4430:9
- **Statement**: `if (s->hdr_block)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 49 (blocked side hit 49× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,680  F:49
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4430_9_T` — cmplog:1,680  n4:1,770
  - `htslib_cram_free_slice_4430_9_F` — cmplog:49  n4:0

### 133. `cram_free_slice` @ 4433:9
- **Statement**: `if (s->block) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 49 (blocked side hit 49× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,680  F:49
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4433_9_T` — cmplog:1,680  n4:1,770
  - `htslib_cram_free_slice_4433_9_F` — cmplog:49  n4:0

### 134. `cram_encode.c:cram_allocate_block` @ 1013:5
- **Statement**: `case E_BETA:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 31,300, n4: 33,300)
- **Flip strength**: 47 (blocked side hit 47× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:47  F:31,300
- **n4 coverage**: T:0  F:33,300
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_allocate_block_1013_5_T` — cmplog:47  n4:0
  - `htslib_cram_encode.c:cram_allocate_block_1013_5_F` — cmplog:31,300  n4:33,300

### 135. `cram_io.c:cram_init_varint` @ 5135:9
- **Statement**: `if (version >= 4) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,660, n4: 1,830)
- **Flip strength**: 42 (blocked side hit 42× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:42  F:5,660
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_cram_io.c:cram_init_varint_5135_9_T` — cmplog:42  n4:0
  - `htslib_cram_io.c:cram_init_varint_5135_9_F` — cmplog:5,660  n4:1,830

### 136. `cram_free_compression_header` @ 4374:44
- **Statement**: `for (m = hdr->rec_encoding_map[i]; m; m = m2) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 145,000, n4: 115,000)
- **Flip strength**: 39 (blocked side hit 39× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:39  F:145,000
- **n4 coverage**: T:0  F:115,000
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4374_44_T` — cmplog:39  n4:0
  - `htslib_cram_free_compression_header_4374_44_F` — cmplog:145,000  n4:115,000

### 137. `sam_hdr_rebuild` @ 1259:9
- **Statement**: `if (!hrecs->dirty)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3,260, n4: 1,830)
- **Flip strength**: 36 (blocked side hit 36× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3,260  F:36
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_sam_hdr_rebuild_1259_9_T` — cmplog:3,260  n4:1,830
  - `htslib_sam_hdr_rebuild_1259_9_F` — cmplog:36  n4:0

### 138. `cram_free_slice` @ 4457:9
- **Statement**: `if (s->hdr)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4457_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4457_9_F` — cmplog:33  n4:0

### 139. `cram_free_slice` @ 4460:9
- **Statement**: `if (s->seqs_blk)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4460_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4460_9_F` — cmplog:33  n4:0

### 140. `cram_free_slice` @ 4469:9
- **Statement**: `if (s->aux_blk)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4469_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4469_9_F` — cmplog:33  n4:0

### 141. `cram_free_slice` @ 4478:9
- **Statement**: `if (s->cigar)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4478_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4478_9_F` — cmplog:33  n4:0

### 142. `cram_free_slice` @ 4481:9
- **Statement**: `if (s->crecs)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4481_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4481_9_F` — cmplog:33  n4:0

### 143. `cram_free_slice` @ 4490:9
- **Statement**: `if (s->pair_keys)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4490_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4490_9_F` — cmplog:33  n4:0

### 144. `cram_free_slice` @ 4493:9
- **Statement**: `if (s->pair[0])`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4493_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4493_9_F` — cmplog:33  n4:0

### 145. `cram_free_slice` @ 4495:9
- **Statement**: `if (s->pair[1])`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,700, n4: 1,770)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,700  F:33
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4495_9_T` — cmplog:1,700  n4:1,770
  - `htslib_cram_free_slice_4495_9_F` — cmplog:33  n4:0

### 146. `hts_getline` @ 2027:5
- **Statement**: `case no_compression:`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 108,000, n4: 745,000)
- **Flip strength**: 33 (blocked side hit 33× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:108,000  F:33
- **n4 coverage**: T:745,000  F:0
- **Canonical identifiers**:
  - `htslib_hts_getline_2027_5_T` — cmplog:108,000  n4:745,000
  - `htslib_hts_getline_2027_5_F` — cmplog:33  n4:0

### 147. `cram_encode.c:cram_compress_slice` @ 879:28
- **Statement**: `if (c->stats[i] && c->stats[i]->nvals > 16)`
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 47,100, n4: 49,600)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:47,100
- **n4 coverage**: T:32  F:49,600
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_compress_slice_879_28_T` — cmplog:0  n4:32
  - `htslib_cram_encode.c:cram_compress_slice_879_28_F` — cmplog:47,100  n4:49,600

### 148. `cram_io.c:cram_compress_block3` @ 2023:17
- **Statement**: `if (unpackable && CRAM_MAJOR_VERS(fd->version) > 3) {`
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,580, n4: 8,870)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,580
- **n4 coverage**: T:32  F:8,870
- **Canonical identifiers**:
  - `htslib_cram_io.c:cram_compress_block3_2023_17_T` — cmplog:0  n4:32
  - `htslib_cram_io.c:cram_compress_block3_2023_17_F` — cmplog:6,580  n4:8,870

### 149. `bgzf_close` @ 2103:13
- **Statement**: `if (fp->gz_stream == NULL) ret = Z_OK;`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 17, n4: 7)
- **Flip strength**: 30 (blocked side hit 30× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:17  F:30
- **n4 coverage**: T:7  F:0
- **Canonical identifiers**:
  - `htslib_bgzf_close_2103_13_T` — cmplog:17  n4:7
  - `htslib_bgzf_close_2103_13_F` — cmplog:30  n4:0

### 150. `cram_block_method2str` @ 2352:5
- **Statement**: `case RANS_PR1:    return "RANS_PR1";`
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9,150, n4: 10,700)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9,150
- **n4 coverage**: T:29  F:10,700
- **Canonical identifiers**:
  - `htslib_cram_block_method2str_2352_5_T` — cmplog:0  n4:29
  - `htslib_cram_block_method2str_2352_5_F` — cmplog:9,150  n4:10,700

### 151. `cram_free_compression_header` @ 4397:9
- **Statement**: `if (hdr->TL)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,520, n4: 3,600)
- **Flip strength**: 24 (blocked side hit 24× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:24  F:4,520
- **n4 coverage**: T:0  F:3,600
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4397_9_T` — cmplog:24  n4:0
  - `htslib_cram_free_compression_header_4397_9_F` — cmplog:4,520  n4:3,600

### 152. `hts_hopen` @ 1564:5
- **Statement**: `case bcf:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 27,400, n4: 13,000)
- **Flip strength**: 21 (blocked side hit 21× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:21  F:27,400
- **n4 coverage**: T:0  F:13,000
- **Canonical identifiers**:
  - `htslib_hts_hopen_1564_5_T` — cmplog:21  n4:0
  - `htslib_hts_hopen_1564_5_F` — cmplog:27,400  n4:13,000

### 153. `hts_close` @ 1640:5
- **Statement**: `case bcf:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 26,100, n4: 12,900)
- **Flip strength**: 21 (blocked side hit 21× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:21  F:26,100
- **n4 coverage**: T:0  F:12,900
- **Canonical identifiers**:
  - `htslib_hts_close_1640_5_T` — cmplog:21  n4:0
  - `htslib_hts_close_1640_5_F` — cmplog:26,100  n4:12,900

### 154. `sam.c:hts_reg2bin` @ 1509:29
- **Statement**: `for (--end, l = n_lvls; l > 0; --l, s += 3, t -= 1<<((l<<1)+l))`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 18,100, n4: 195,000)
- **Flip strength**: 21 (blocked side hit 21× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18,100  F:21
- **n4 coverage**: T:195,000  F:0
- **Canonical identifiers**:
  - `htslib_sam.c:hts_reg2bin_1509_29_T` — cmplog:18,100  n4:195,000
  - `htslib_sam.c:hts_reg2bin_1509_29_F` — cmplog:21  n4:0

### 155. `hts_getline` @ 2035:5
- **Statement**: `case gzip:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 108,000, n4: 745,000)
- **Flip strength**: 18 (blocked side hit 18× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:108,000
- **n4 coverage**: T:0  F:745,000
- **Canonical identifiers**:
  - `htslib_hts_getline_2035_5_T` — cmplog:18  n4:0
  - `htslib_hts_getline_2035_5_F` — cmplog:108,000  n4:745,000

### 156. `tokenise_name3.c:search_trie` @ 627:32
- **Statement**: `for (i = 0; i < len && data[i] > ' '; i++)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 107,000, n4: 158,000)
- **Flip strength**: 17 (blocked side hit 17× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:107,000  F:17
- **n4 coverage**: T:158,000  F:0
- **Canonical identifiers**:
  - `htslib_tokenise_name3.c:search_trie_627_32_T` — cmplog:107,000  n4:158,000
  - `htslib_tokenise_name3.c:search_trie_627_32_F` — cmplog:17  n4:0

### 157. `cram_flush_container` @ 4150:9
- **Statement**: `if (0 != cram_encode_container(fd, c))`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_flush_container_4150_9_T` — cmplog:16  n4:0
  - `htslib_cram_flush_container_4150_9_F` — cmplog:1,680  n4:1,770

### 158. `cram_free_slice_header` @ 4418:9
- **Statement**: `if (hdr->block_content_ids)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,680  F:16
- **n4 coverage**: T:1,770  F:0
- **Canonical identifiers**:
  - `htslib_cram_free_slice_header_4418_9_T` — cmplog:1,680  n4:1,770
  - `htslib_cram_free_slice_header_4418_9_F` — cmplog:16  n4:0

### 159. `cram_free_slice` @ 4463:9
- **Statement**: `if (s->qual_blk)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,710, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,710
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4463_9_T` — cmplog:16  n4:0
  - `htslib_cram_free_slice_4463_9_F` — cmplog:1,710  n4:1,770

### 160. `cram_free_slice` @ 4466:9
- **Statement**: `if (s->name_blk)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,710, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,710
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4466_9_T` — cmplog:16  n4:0
  - `htslib_cram_free_slice_4466_9_F` — cmplog:1,710  n4:1,770

### 161. `cram_free_slice` @ 4472:9
- **Statement**: `if (s->base_blk)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,710, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,710
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4472_9_T` — cmplog:16  n4:0
  - `htslib_cram_free_slice_4472_9_F` — cmplog:1,710  n4:1,770

### 162. `cram_free_slice` @ 4475:9
- **Statement**: `if (s->soft_blk)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,710, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,710
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_free_slice_4475_9_T` — cmplog:16  n4:0
  - `htslib_cram_free_slice_4475_9_F` — cmplog:1,710  n4:1,770

### 163. `cram_close` @ 5574:13
- **Statement**: `if (-1 == cram_flush_container_mt(fd, fd->ctr))`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_close_5574_13_T` — cmplog:16  n4:0
  - `htslib_cram_close_5574_13_F` — cmplog:1,680  n4:1,770

### 164. `cram_close` @ 5600:9
- **Statement**: `if (ret == 0 && fd->mode == 'w') {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,530, n4: 1,830)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,530  F:16
- **n4 coverage**: T:1,830  F:0
- **Canonical identifiers**:
  - `htslib_cram_close_5600_9_T` — cmplog:4,530  n4:1,830
  - `htslib_cram_close_5600_9_F` — cmplog:16  n4:0

### 165. `rANS_static4x16pr.c:normalise_freq_shift` @ 153:9
- **Statement**: `if (size == 0 || size == max_tot)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 61,100, n4: 140,000)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:61,100
- **n4 coverage**: T:0  F:140,000
- **Canonical identifiers**:
  - `htslib_rANS_static4x16pr.c:normalise_freq_shift_153_9_T` — cmplog:16  n4:0
  - `htslib_rANS_static4x16pr.c:normalise_freq_shift_153_9_F` — cmplog:61,100  n4:140,000

### 166. `sam.c:sam_format1_append` @ 4454:9
- **Statement**: `if (c->n_cigar) { // cigar`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,680, n4: 65,099)
- **Flip strength**: 16 (blocked side hit 16× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:5,680
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_sam.c:sam_format1_append_4454_9_T` — cmplog:16  n4:0
  - `htslib_sam.c:sam_format1_append_4454_9_F` — cmplog:5,680  n4:65,099

### 167. `bgzf.c:hwrite` @ 296:9
- **Statement**: `if (nbytes >= n && fp->begin == fp->buffer) {`
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9,540, n4: 6,200)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9,540
- **n4 coverage**: T:15  F:6,200
- **Canonical identifiers**:
  - `htslib_bgzf.c:hwrite_296_9_T` — cmplog:0  n4:15
  - `htslib_bgzf.c:hwrite_296_9_F` — cmplog:9,540  n4:6,200

### 168. `bgzf.c:hwrite` @ 302:9
- **Statement**: `if (n > nbytes) n = nbytes;`
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9,540, n4: 6,200)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9,540  F:0
- **n4 coverage**: T:6,200  F:15
- **Canonical identifiers**:
  - `htslib_bgzf.c:hwrite_302_9_T` — cmplog:9,540  n4:6,200
  - `htslib_bgzf.c:hwrite_302_9_F` — cmplog:0  n4:15

### 169. `bgzf.c:hwrite` @ 305:12
- **Statement**: `return (n==nbytes)? (ssize_t) n : hwrite2(fp, buffer, nbytes, n);`
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9,540, n4: 6,200)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9,540  F:0
- **n4 coverage**: T:6,200  F:15
- **Canonical identifiers**:
  - `htslib_bgzf.c:hwrite_305_12_T` — cmplog:9,540  n4:6,200
  - `htslib_bgzf.c:hwrite_305_12_F` — cmplog:0  n4:15

### 170. `hts_detect_format2` @ 660:18
- **Statement**: `else if (memcmp(s, "BCF\2", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 6, n4: 2)
- **Flip strength**: 15 (blocked side hit 15× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:6
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_660_18_T` — cmplog:15  n4:0
  - `htslib_hts_detect_format2_660_18_F` — cmplog:6  n4:2

### 171. `hts_getline` @ 2036:5
- **Statement**: `case bgzf:`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 108,000, n4: 745,000)
- **Flip strength**: 15 (blocked side hit 15× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:108,000
- **n4 coverage**: T:0  F:745,000
- **Canonical identifiers**:
  - `htslib_hts_getline_2036_5_T` — cmplog:15  n4:0
  - `htslib_hts_getline_2036_5_F` — cmplog:108,000  n4:745,000

### 172. `sam.c:fastq_parse1` @ 4103:18
- **Statement**: `else if (ret < -1)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,630, n4: 5,680)
- **Flip strength**: 15 (blocked side hit 15× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:4,630
- **n4 coverage**: T:0  F:5,680
- **Canonical identifiers**:
  - `htslib_sam.c:fastq_parse1_4103_18_T` — cmplog:15  n4:0
  - `htslib_sam.c:fastq_parse1_4103_18_F` — cmplog:4,630  n4:5,680

### 173. `sam.c:kputll` @ 388:9
- **Statement**: `if (c < 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 17,000, n4: 195,000)
- **Flip strength**: 13 (blocked side hit 13× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:13  F:17,000
- **n4 coverage**: T:0  F:195,000
- **Canonical identifiers**:
  - `htslib_sam.c:kputll_388_9_T` — cmplog:13  n4:0
  - `htslib_sam.c:kputll_388_9_F` — cmplog:17,000  n4:195,000

### 174. `cram_free_compression_header` @ 4366:9
- **Statement**: `if (hdr->landmark)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,530, n4: 3,600)
- **Flip strength**: 12 (blocked side hit 12× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:4,530
- **n4 coverage**: T:0  F:3,600
- **Canonical identifiers**:
  - `htslib_cram_free_compression_header_4366_9_T` — cmplog:12  n4:0
  - `htslib_cram_free_compression_header_4366_9_F` — cmplog:4,530  n4:3,600

### 175. `cram_huffman_encode_init` @ 3301:13
- **Statement**: `if (codes[i].symbol >= -1 && codes[i].symbol < MAX_HUFF)`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 19,400, n4: 17,700)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:19,400  F:11
- **n4 coverage**: T:17,700  F:0
- **Canonical identifiers**:
  - `htslib_cram_huffman_encode_init_3301_13_T` — cmplog:19,400  n4:17,700
  - `htslib_cram_huffman_encode_init_3301_13_F` — cmplog:11  n4:0

### 176. `sam.c:sam_format1_append` @ 4462:9
- **Statement**: `if (c->mtid < 0) r |= kputsn_("*\t", 2, str); // mate chr`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,690, n4: 65,099)
- **Flip strength**: 11 (blocked side hit 11× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,690  F:11
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_sam.c:sam_format1_append_4462_9_T` — cmplog:5,690  n4:65,099
  - `htslib_sam.c:sam_format1_append_4462_9_F` — cmplog:11  n4:0

### 177. `bam_write1` @ 869:9
- **Statement**: `c->isize < INT_MIN || c->isize > INT_MAX) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,590, n4: 65,099)
- **Flip strength**: 10 (blocked side hit 10× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:5,590
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_bam_write1_869_9_T` — cmplog:10  n4:0
  - `htslib_bam_write1_869_9_F` — cmplog:5,590  n4:65,099

### 178. `cram_encode.c:process_one_read` @ 3780:19
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,350, n4: 65,099)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:5,350
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3780_19_T` — cmplog:9  n4:0
  - `htslib_cram_encode.c:process_one_read_3780_19_F` — cmplog:5,350  n4:65,099

### 179. `string_alloc` @ 127:13
- **Statement**: `if (str->used + length < a_str->max_length) {`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 25,700, n4: 90,200)
- **Flip strength**: 9 (blocked side hit 9× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:25,700  F:9
- **n4 coverage**: T:90,200  F:0
- **Canonical identifiers**:
  - `htslib_string_alloc_127_13_T` — cmplog:25,700  n4:90,200
  - `htslib_string_alloc_127_13_F` — cmplog:9  n4:0

### 180. `cram_encoder_init` @ 3928:13
- **Statement**: `if ((r = encode_init[codec](st, codec, option, dat, version, vv)))`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 34,200, n4: 35,100)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:34,200  F:8
- **n4 coverage**: T:35,100  F:0
- **Canonical identifiers**:
  - `htslib_cram_encoder_init_3928_13_T` — cmplog:34,200  n4:35,100
  - `htslib_cram_encoder_init_3928_13_F` — cmplog:8  n4:0

### 181. `cram_encoder_init` @ 3930:13
- **Statement**: `if (!r) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 34,200, n4: 35,100)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:34,200
- **n4 coverage**: T:0  F:35,100
- **Canonical identifiers**:
  - `htslib_cram_encoder_init_3930_13_T` — cmplog:8  n4:0
  - `htslib_cram_encoder_init_3930_13_F` — cmplog:34,200  n4:35,100

### 182. `cram_encode_container` @ 2039:17
- **Statement**: `if (process_one_read(fd, c, s, cr, b, r2, &MD, embed_ref,`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,360, n4: 65,099)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:5,360
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode_container_2039_17_T` — cmplog:8  n4:0
  - `htslib_cram_encode_container_2039_17_F` — cmplog:5,360  n4:65,099

### 183. `cram_encode_container` @ 2212:9
- **Statement**: `if (!h->codecs[DS_AP]) goto_err;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,680, n4: 1,770)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:1,680
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode_container_2212_9_T` — cmplog:8  n4:0
  - `htslib_cram_encode_container_2212_9_F` — cmplog:1,680  n4:1,770

### 184. `cram_encode.c:process_one_read` @ 3719:9
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,360, n4: 65,099)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:5,360
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3719_9_T` — cmplog:8  n4:0
  - `htslib_cram_encode.c:process_one_read_3719_9_F` — cmplog:5,360  n4:65,099

### 185. `cram_free_container` @ 3781:9
- **Statement**: `if (c->bams)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 9,160, n4: 3,600)
- **Flip strength**: 8 (blocked side hit 8× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:9,160
- **n4 coverage**: T:0  F:3,600
- **Canonical identifiers**:
  - `htslib_cram_free_container_3781_9_T` — cmplog:8  n4:0
  - `htslib_cram_free_container_3781_9_F` — cmplog:9,160  n4:3,600

### 186. `cram_encode.c:cram_compress_slice` @ 945:9
- **Statement**: `if (s->block[DS_NS] && s->block[DS_NS] != s->block[0])`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 1,670, n4: 1,770)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:1,670
- **n4 coverage**: T:0  F:1,770
- **Canonical identifiers**:
  - `htslib_cram_encode.c:cram_compress_slice_945_9_T` — cmplog:7  n4:0
  - `htslib_cram_encode.c:cram_compress_slice_945_9_F` — cmplog:1,670  n4:1,770

### 187. `rANS_static32x16pr_avx2.c:normalise_freq_shift` @ 153:9
- **Statement**: `return NULL;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,490, n4: 14,600)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:7,490
- **n4 coverage**: T:0  F:14,600
- **Canonical identifiers**:
  - `htslib_rANS_static32x16pr_avx2.c:normalise_freq_shift_153_9_T` — cmplog:7  n4:0
  - `htslib_rANS_static32x16pr_avx2.c:normalise_freq_shift_153_9_F` — cmplog:7,490  n4:14,600

### 188. `tokenise_name3.c:encode_name` @ 930:31
- **Statement**: `&& (5+ctx->token_dcount[ntok]) > ctx->token_icount[ntok]`
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 204, n4: 398)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:204  F:0
- **n4 coverage**: T:398  F:6
- **Canonical identifiers**:
  - `htslib_tokenise_name3.c:encode_name_930_31_T` — cmplog:204  n4:398
  - `htslib_tokenise_name3.c:encode_name_930_31_F` — cmplog:0  n4:6

### 189. `hts_detect_format2` @ 654:18
- **Statement**: `else if (memcmp(s, "BCF\4", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 21, n4: 2)
- **Flip strength**: 6 (blocked side hit 6× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:21
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_654_18_T` — cmplog:6  n4:0
  - `htslib_hts_detect_format2_654_18_F` — cmplog:21  n4:2

### 190. `sam_realloc_bam_data` @ 442:9
- **Statement**: `if (new_m_data > FUZZ_ALLOC_LIMIT) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 15,600, n4: 75,700)
- **Flip strength**: 5 (blocked side hit 5× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:15,600
- **n4 coverage**: T:0  F:75,700
- **Canonical identifiers**:
  - `htslib_sam_realloc_bam_data_442_9_T` — cmplog:5  n4:0
  - `htslib_sam_realloc_bam_data_442_9_F` — cmplog:15,600  n4:75,700

### 191. `tokenise_name3.c:create_context` @ 173:9
- **Statement**: `void *htscodecs_tls_calloc(size_t nmemb, size_t size) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,020, n4: 2,330)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:3,020
- **n4 coverage**: T:0  F:2,330
- **Canonical identifiers**:
  - `htslib_tokenise_name3.c:create_context_173_9_T` — cmplog:4  n4:0
  - `htslib_tokenise_name3.c:create_context_173_9_F` — cmplog:3,020  n4:2,330

### 192. `bam_write1` @ 868:9
- **Statement**: `c->mpos > INT_MAX ||`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,600, n4: 65,099)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:5,600
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_bam_write1_868_9_T` — cmplog:4  n4:0
  - `htslib_bam_write1_868_9_F` — cmplog:5,600  n4:65,099

### 193. `bgzf_hopen` @ 538:13
- **Statement**: `if (fp == NULL) return NULL;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 866, n4: 9)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:866
- **n4 coverage**: T:0  F:9
- **Canonical identifiers**:
  - `htslib_bgzf_hopen_538_13_T` — cmplog:3  n4:0
  - `htslib_bgzf_hopen_538_13_F` — cmplog:866  n4:9

### 194. `bgzf.c:bgzf_read_init` @ 404:46
- **Statement**: `}`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 182, n4: 5)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:182
- **n4 coverage**: T:0  F:5
- **Canonical identifiers**:
  - `htslib_bgzf.c:bgzf_read_init_404_46_T` — cmplog:3  n4:0
  - `htslib_bgzf.c:bgzf_read_init_404_46_F` — cmplog:182  n4:5

### 195. `string_alloc` @ 135:9
- **Statement**: `if (length > a_str->max_length) a_str->max_length = length;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 7,660, n4: 2,420)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:7,660
- **n4 coverage**: T:0  F:2,420
- **Canonical identifiers**:
  - `htslib_string_alloc_135_9_T` — cmplog:3  n4:0
  - `htslib_string_alloc_135_9_F` — cmplog:7,660  n4:2,420

### 196. `hts_detect_format2` @ 578:22
- **Statement**: `else if (memcmp(&s[12], "RAZF", 4) == 0)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 27, n4: 5)
- **Flip strength**: 3 (blocked side hit 3× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:27
- **n4 coverage**: T:0  F:5
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_578_22_T` — cmplog:3  n4:0
  - `htslib_hts_detect_format2_578_22_F` — cmplog:27  n4:5

### 197. `hts_detect_format2` @ 586:27
- **Statement**: `else if (len >= 10 && memcmp(s, "BZh", 3) == 0 &&`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 15,700, n4: 7,210)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:15,700
- **n4 coverage**: T:0  F:7,210
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_586_27_T` — cmplog:2  n4:0
  - `htslib_hts_detect_format2_586_27_F` — cmplog:15,700  n4:7,210

### 198. `hts_detect_format2` @ 598:26
- **Statement**: `else if (len >= 6 && memcmp(s, "\xfd""7zXZ\0", 6) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 15,900, n4: 7,350)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:15,900
- **n4 coverage**: T:0  F:7,350
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_598_26_T` — cmplog:2  n4:0
  - `htslib_hts_detect_format2_598_26_F` — cmplog:15,900  n4:7,350

### 199. `hts_detect_format2` @ 746:18
- **Statement**: `else if (fmt->compression == gzip && colmatch(columns, "iiiiii") == 6) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 86, n4: 69)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:86
- **n4 coverage**: T:0  F:69
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_746_18_T` — cmplog:2  n4:0
  - `htslib_hts_detect_format2_746_18_F` — cmplog:86  n4:69

### 200. `hts_hopen` @ 1587:17
- **Statement**: `if (fp->fp.bgzf == NULL) goto error;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 53, n4: 9)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:53
- **n4 coverage**: T:0  F:9
- **Canonical identifiers**:
  - `htslib_hts_hopen_1587_17_T` — cmplog:2  n4:0
  - `htslib_hts_hopen_1587_17_F` — cmplog:53  n4:9

### 201. `hts.c:decompress_peek_gz` @ 334:13
- **Statement**: `if (ret == Z_STREAM_END) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 251, n4: 14)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:251
- **n4 coverage**: T:0  F:14
- **Canonical identifiers**:
  - `htslib_hts.c:decompress_peek_gz_334_13_T` — cmplog:2  n4:0
  - `htslib_hts.c:decompress_peek_gz_334_13_F` — cmplog:251  n4:14

### 202. `sam_write1` @ 4732:17
- **Statement**: `if (sam_format1(h, b, &fp->line) < 0) return -1;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,700, n4: 65,099)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:5,700
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_sam_write1_4732_17_T` — cmplog:2  n4:0
  - `htslib_sam_write1_4732_17_F` — cmplog:5,700  n4:65,099

### 203. `cram_encode.c:process_one_read` @ 3380:9
- **Statement**: `if (!(md = bam_aux_get(b, "MD")))`
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 5,370, n4: 65,099)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,370  F:1
- **n4 coverage**: T:65,099  F:0
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3380_9_T` — cmplog:5,370  n4:65,099
  - `htslib_cram_encode.c:process_one_read_3380_9_F` — cmplog:1  n4:0

### 204. `cram_encode.c:process_one_read` @ 3826:17
- **Statement**: `if (((bam_flag(b) & BAM_FMREVERSE) != 0) !=`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 29, n4: 20,500)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:29
- **n4 coverage**: T:0  F:20,500
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3826_17_T` — cmplog:1  n4:0
  - `htslib_cram_encode.c:process_one_read_3826_17_F` — cmplog:29  n4:20,500

### 205. `cram_encode.c:process_one_read` @ 3950:17
- **Statement**: `if (bam_flag(b) & BAM_FMREVERSE)`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,360, n4: 65,099)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:5,360
- **n4 coverage**: T:0  F:65,099
- **Canonical identifiers**:
  - `htslib_cram_encode.c:process_one_read_3950_17_T` — cmplog:1  n4:0
  - `htslib_cram_encode.c:process_one_read_3950_17_F` — cmplog:5,360  n4:65,099

### 206. `hopen` @ 1310:16
- **Statement**: `|| handler->priority < 2000`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,200, n4: 7,510)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:16,200
- **n4 coverage**: T:0  F:7,510
- **Canonical identifiers**:
  - `htslib_hopen_1310_16_T` — cmplog:1  n4:0
  - `htslib_hopen_1310_16_F` — cmplog:16,200  n4:7,510

### 207. `hts_detect_format2` @ 607:26
- **Statement**: `else if (len >= 4 && memcmp(s, "\x28\xb5\x2f\xfd", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,000, n4: 7,440)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:16,000
- **n4 coverage**: T:0  F:7,440
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_607_26_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_607_26_F` — cmplog:16,000  n4:7,440

### 208. `hts_detect_format2` @ 614:9
- **Statement**: `if (len < 0) return -1;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,200, n4: 7,510)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:16,200
- **n4 coverage**: T:0  F:7,510
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_614_9_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_614_9_F` — cmplog:16,200  n4:7,510

### 209. `hts_detect_format2` @ 648:18
- **Statement**: `else if (memcmp(s, "BAI\1", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 27, n4: 2)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:27
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_648_18_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_648_18_F` — cmplog:27  n4:2

### 210. `hts_detect_format2` @ 667:18
- **Statement**: `else if (memcmp(s, "CSI\1", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5, n4: 2)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:5
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_667_18_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_667_18_F` — cmplog:5  n4:2

### 211. `hts_detect_format2` @ 673:18
- **Statement**: `else if (memcmp(s, "TBI\1", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4, n4: 2)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:4
- **n4 coverage**: T:0  F:2
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_673_18_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_673_18_F` — cmplog:4  n4:2

### 212. `hts_detect_format2` @ 707:26
- **Statement**: `else if (len >= 8 && memcmp(s, "d4\xdd\xdd", 4) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,910, n4: 7,270)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:5,910
- **n4 coverage**: T:0  F:7,270
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_707_26_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_707_26_F` — cmplog:5,910  n4:7,270

### 213. `hts_detect_format2` @ 719:25
- **Statement**: `else if (len > 8 && memcmp(s, "crypt4gh", 8) == 0) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 5,880, n4: 7,240)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:5,880
- **n4 coverage**: T:0  F:7,240
- **Canonical identifiers**:
  - `htslib_hts_detect_format2_719_25_T` — cmplog:1  n4:0
  - `htslib_hts_detect_format2_719_25_F` — cmplog:5,880  n4:7,240

### 214. `hts_hopen` @ 1479:13
- **Statement**: `if (hts_detect_format2(hfile, fn, &fp->format) < 0) goto error;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,200, n4: 7,510)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:16,200
- **n4 coverage**: T:0  F:7,510
- **Canonical identifiers**:
  - `htslib_hts_hopen_1479_13_T` — cmplog:1  n4:0
  - `htslib_hts_hopen_1479_13_F` — cmplog:16,200  n4:7,510

### 215. `hts_hopen` @ 1486:16
- **Statement**: `fp->format.format == hts_crypt4gh_format) {`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 16,200, n4: 7,510)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:16,200
- **n4 coverage**: T:0  F:7,510
- **Canonical identifiers**:
  - `htslib_hts_hopen_1486_16_T` — cmplog:1  n4:0
  - `htslib_hts_hopen_1486_16_F` — cmplog:16,200  n4:7,510

### 216. `hts_hopen` @ 1566:13
- **Statement**: `if (fp->fp.bgzf == NULL) goto error;`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 4,570, n4: 1,830)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:4,570
- **n4 coverage**: T:0  F:1,830
- **Canonical identifiers**:
  - `htslib_hts_hopen_1566_13_T` — cmplog:1  n4:0
  - `htslib_hts_hopen_1566_13_F` — cmplog:4,570  n4:1,830

### 217. `tokenise_name3.c:create_context` @ 177:9
- **Statement**: `void *ptr = htscodecs_tls_alloc(nmemb * size);`
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 3,020, n4: 2,330)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:3,020
- **n4 coverage**: T:0  F:2,330
- **Canonical identifiers**:
  - `htslib_tokenise_name3.c:create_context_177_9_T` — cmplog:1  n4:0
  - `htslib_tokenise_name3.c:create_context_177_9_F` — cmplog:3,020  n4:2,330
