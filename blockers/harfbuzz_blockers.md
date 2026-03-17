# Input-Dependent Blocking Branches — harfbuzz (All, Ranked by Flip Strength)

**Coverage sources:** `coverage/harfbuzz/cmplog.cov`, `coverage/harfbuzz/n4.cov`  
**Analysis date:** 2026-03-17  
**Ranking:** descending by *flip strength* = hitcount of the blocked side in the confirming fuzzer

## Summary

| Metric | Value |
|--------|-------|
| Branch pairs (cmplog) | 11,322 |
| Branch pairs (n4) | 12,476 |
| Asymmetric in cmplog | 4,076 |
| Asymmetric in n4 | 3,647 |
| **Confirmed input-dependent** | **1,023** |
| Unconfirmed candidates | 6,700 |

## Ranked Summary Table

| Rank | Function | Line:Col | Blocked | Flip Strength | cmplog T:F | n4 T:F | Confirmed By |
|------|----------|----------|---------|---------------|------------|------------|--------------|
| 1 | `hb-ot-layout.cc:_ZL32_hb_glyph_info_get_lig_num_comp...` | 518:7 | False | 2,550,000 | 9040:0 | 26200:2550000 | n4 |
| 2 | `hb-ot-font.cc:_ZNK4$_33clIR10hb_array_tIKiERK4$_18S7...` | 992:11 | False | 1,600,000 | 663:0 | 3640:1600000 | n4 |
| 3 | `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_...` | 700:14 | True | 739,000 | 0:28 | 739000:144000 | n4 |
| 4 | `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj...` | 347:7 | False | 627,000 | 14:0 | 724000:627000 | n4 |
| 5 | `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20c...` | 700:14 | True | 554,000 | 0:17 | 554000:108000 | n4 |
| 6 | `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_ap...` | 1528:11 | False | 520,000 | 68:0 | 35100:520000 | n4 |
| 7 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1262:11 | False | 351,000 | 66:0 | 583:351000 | n4 |
| 8 | `_ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driv...` | 497:11 | True | 351,000 | 0:66 | 351000:583 | n4 |
| 9 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1298:11 | False | 350,000 | 60:0 | 1370:350000 | n4 |
| 10 | `_Z20find_syllables_khmerP11hb_buffer_t` | 341:7 | True | 209,000 | 0:8260 | 209000:45900 | n4 |
| 11 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1287:60 | True | 195,000 | 0:2 | 195000:59 | n4 |
| 12 | `_ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driv...` | 490:6 | True | 194,000 | 0:6 | 194000:77800 | n4 |
| 13 | `_ZN2OT6Layout9GPOS_impl9PosLookup21dispatch_recurse_...` | 68:18 | False | 165,000 | 28000:0 | 102000:165000 | n4 |
| 14 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1287:32 | False | 155,000 | 2:0 | 195000:155000 | n4 |
| 15 | `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj...` | 370:11 | False | 150,000 | 8:0 | 334000:150000 | n4 |
| 16 | `_ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj` | 438:3 | True | 147,000 | 0:551000 | 147000:5860000 | n4 |
| 17 | `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_...` | 724:14 | True | 138,000 | 0:36 | 138000:25800 | n4 |
| 18 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21R...` | 1268:19 | True | 126,000 | 0:95 | 126000:1210 | n4 |
| 19 | `_ZN12hb_extents_tIfE6union_ERKS0_` | 49:9 | True | 116,000 | 0:4110 | 116000:33900 | n4 |
| 20 | `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_...` | 718:11 | True | 114,000 | 0:28 | 114000:30100 | n4 |
| 21 | `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20c...` | 724:14 | True | 103,000 | 0:13 | 103000:19300 | n4 |
| 22 | `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj...` | 358:47 | False | 97,000 | 6:0 | 143000:97000 | n4 |
| 23 | `hb-ot-layout.cc:_ZNK3$_0clIjjEEDTqugefp_fp0_fp_fp0_E...` | 76:55 | True | 92,700 | 0:490 | 92700:21500 | n4 |
| 24 | `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20c...` | 718:11 | True | 85,800 | 0:17 | 85800:22400 | n4 |
| 25 | `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj...` | 360:11 | True | 74,200 | 0:6 | 74200:166000 | n4 |
| 26 | `_ZNK14hb_transform_tIfE11is_identityEv` | 120:12 | False | 62,700 | 6:0 | 177000:62700 | n4 |
| 27 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_19Ke...` | 1262:11 | True | 55,400 | 0:110000 | 55400:166000 | n4 |
| 28 | `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeader...` | 557:23 | False | 55,300 | 110000:0 | 111000:55300 | n4 |
| 29 | `_ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT1...` | 176:11 | True | 44,500 | 0:18200 | 44500:92700 | n4 |
| 30 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3526:8 | False | 41,000 | 490:0 | 57000:41000 | n4 |
| 31 | `_ZNK14hb_transform_tIfE11is_identityEv` | 122:5 | False | 27,700 | 6:0 | 149000:27700 | n4 |
| 32 | `_ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT...` | 178:9 | False | 24,200 | 30:0 | 318:24200 | n4 |
| 33 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3511:11 | False | 13,700 | 490:0 | 100000:13700 | n4 |
| 34 | `_ZNK2OT18glyf_accelerator_t11get_path_atEP9hb_font_t...` | 514:9 | True | 12,200 | 0:6 | 12200:228000 | n4 |
| 35 | `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10...` | 104:6 | True | 12,000 | 0:462 | 12000:128000 | n4 |
| 36 | `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_b...` | 436:7 | False | 12,000 | 1:0 | 1210:12000 | n4 |
| 37 | `_ZNK2OT6Layout9GPOS_impl9MarkArray5applyEPNS_21hb_ot...` | 251:24 | False | 10,700 | 4:0 | 2400:10700 | n4 |
| 38 | `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context...` | 641:9 | True | 10,300 | 0:145000 | 10300:1480000 | n4 |
| 39 | `_Z20find_syllables_indicP11hb_buffer_t` | 1167:3 | False | 10,300 | 163:0 | 526000:10300 | n4 |
| 40 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3528:10 | True | 9,640 | 0:490 | 9640:47400 | n4 |
| 41 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixE...` | 251:24 | True | 8,830 | 0:4 | 8830:12900 | n4 |
| 42 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_17Inserti...` | 251:24 | True | 8,730 | 0:268 | 8730:46600 | n4 |
| 43 | `hb-ot-layout.cc:_ZN10hb_apply_tIZNK2OT6Layout9GSUB_i...` | 693:12 | True | 8,119 | 0:204 | 8119:2260 | n4 |
| 44 | `_ZNK2OT7ArrayOfINS_6Layout9GPOS_impl15EntryExitRecor...` | 251:24 | False | 7,660 | 3:0 | 1820:7660 | n4 |
| 45 | `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context...` | 652:9 | True | 7,380 | 0:144000 | 7380:1300000 | n4 |
| 46 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1090:11 | True | 7,200 | 0:3 | 7200:688 | n4 |
| 47 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1092:8 | True | 7,200 | 0:3 | 7200:688 | n4 |
| 48 | `_ZNK14hb_transform_tIfE11is_identityEv` | 122:16 | False | 6,440 | 6:0 | 143000:6440 | n4 |
| 49 | `hb-ot-layout.cc:_ZL14apply_backwardPN2OT21hb_ot_appl...` | 1952:2 | False | 5,260 | 2170:0 | 249000:5260 | n4 |
| 50 | `_ZNK2OT6Layout9GSUB_impl11SubstLookup11would_applyEP...` | 97:9 | False | 5,170 | 20:0 | 24100:5170 | n4 |
| 51 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 967:3 | False | 4,740 | 2100:0 | 74200:4740 | n4 |
| 52 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3519:7 | True | 4,550 | 0:466 | 4550:90700 | n4 |
| 53 | `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj...` | 344:18 | True | 4,480 | 0:14 | 4480:1340000 | n4 |
| 54 | `_ZNK2OT6Layout9GPOS_impl17CursivePosFormat15applyEPN...` | 129:9 | False | 3,980 | 3:0 | 1950:3980 | n4 |
| 55 | `hb-ot-layout.cc:_ZL22_hb_glyph_info_is_zwnjPK15hb_gl...` | 406:53 | True | 3,640 | 0:10300 | 3640:121000 | n4 |
| 56 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3515:6 | False | 3,610 | 490:0 | 18400:3610 | n4 |
| 57 | `_Z20find_syllables_indicP11hb_buffer_t` | 1241:2 | True | 3,460 | 0:96 | 3460:1230 | n4 |
| 58 | `_ZNK2OT20TupleVariationHeader16calculate_scalarE10hb...` | 149:11 | True | 3,210 | 0:250 | 3210:4830 | n4 |
| 59 | `hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj` | 74:25 | False | 3,120 | 2810:0 | 104000:3120 | n4 |
| 60 | `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_...` | 2700:9 | True | 3,040 | 0:36 | 3040:603 | n4 |
| 61 | `_Z20find_syllables_indicP11hb_buffer_t` | 1197:2 | True | 2,820 | 0:2060 | 2820:186000 | n4 |
| 62 | `hb-ot-shaper-indic.cc:_ZL33initial_reordering_syllab...` | 980:5 | True | 2,820 | 0:1900 | 2820:168000 | n4 |
| 63 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 604:2 | True | 2,810 | 0:354 | 2810:47200 | n4 |
| 64 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 309:7 | True | 2,720 | 0:6400000 | 2720:98500000 | n4 |
| 65 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3452:9 | True | 2,700 | 0:529 | 2700:58100 | n4 |
| 66 | `_ZNK2OT21hb_ot_apply_context_t21match_properties_mar...` | 794:21 | False | 2,460 | 52:0 | 52600:2460 | n4 |
| 67 | `hb-ot-shaper-myanmar.cc:_ZL17_hb_next_syllableP11hb_...` | 166:29 | True | 2,460 | 0:660 | 2460:97800 | n4 |
| 68 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3519:6 | False | 2,410 | 466:0 | 92800:2410 | n4 |
| 69 | `_ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_t...` | 207:11 | True | 2,280 | 0:8 | 2280:1440 | n4 |
| 70 | `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_...` | 820:7 | True | 2,280 | 0:22400 | 2280:64000 | n4 |
| 71 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 890:34 | True | 2,160 | 0:67 | 2160:1520 | n4 |
| 72 | `_Z20find_syllables_khmerP11hb_buffer_t` | 391:2 | True | 2,090 | 0:8260 | 2090:43800 | n4 |
| 73 | `_Z20find_syllables_khmerP11hb_buffer_t` | 373:2 | True | 2,060 | 0:8260 | 2060:43900 | n4 |
| 74 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 624:2 | True | 1,970 | 0:354 | 1970:48100 | n4 |
| 75 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 590:3 | False | 1,940 | 28:0 | 9500:1940 | n4 |
| 76 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 329:7 | True | 1,810 | 0:6400000 | 1810:98500000 | n4 |
| 77 | `_ZNK2OT18glyf_accelerator_t10get_pointsINS0_19points...` | 260:8 | False | 1,770 | 15:0 | 27700:1770 | n4 |
| 78 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 321:7 | True | 1,730 | 0:6400000 | 1730:98500000 | n4 |
| 79 | `_ZN11hb_vector_tIiLb0EE6resizeEibb` | 492:11 | True | 1,610 | 0:368 | 1610:389 | n4 |
| 80 | `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesi...` | 72:23 | True | 1,560 | 0:10300 | 1560:17900 | n4 |
| 81 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1057:2 | True | 1,440 | 0:2020 | 1440:72400 | n4 |
| 82 | `hb-ot-shaper-use.cc:_ZN15machine_index_tI13hb_zip_it...` | 879:46 | True | 1,440 | 0:130 | 1440:580 | n4 |
| 83 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1069:2 | True | 1,410 | 0:2020 | 1410:72400 | n4 |
| 84 | `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10...` | 107:6 | True | 1,390 | 0:462 | 1390:127000 | n4 |
| 85 | `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context...` | 591:8 | False | 1,370 | 1970:0 | 151000:1370 | n4 |
| 86 | `_ZNK2OT6Layout9GSUB_impl23AlternateSubstFormat1_2INS...` | 77:9 | True | 1,280 | 0:192 | 1280:19000 | n4 |
| 87 | `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_cons...` | 227:12 | True | 1,230 | 0:27 | 1230:3380 | n4 |
| 88 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 309:7 | True | 1,220 | 0:3800000 | 1220:71000000 | n4 |
| 89 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCE...` | 457:9 | False | 1,190 | 2:0 | 1130:1190 | n4 |
| 90 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCE...` | 459:11 | True | 1,100 | 0:2 | 1100:27 | n4 |
| 91 | `_ZNK2OT12CmapSubtable9get_glyphEjPj` | 1504:5 | True | 1,090 | 0:213000 | 1090:456000 | n4 |
| 92 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3523:8 | False | 1,070 | 466:0 | 89600:1070 | n4 |
| 93 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 317:7 | True | 1,050 | 0:6400000 | 1050:98500000 | n4 |
| 94 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 329:7 | True | 1,030 | 0:3800000 | 1030:71000000 | n4 |
| 95 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 325:7 | True | 1,020 | 0:6400000 | 1020:98500000 | n4 |
| 96 | `_ZNK3AAT10ClassTableIN2OT7NumTypeILb1EtLj2EEEE14coll...` | 1048:11 | False | 1,000 | 404:0 | 45200:1000 | n4 |
| 97 | `_ZN12hb_extents_tIfE6union_ERKS0_` | 50:9 | True | 882 | 0:4110 | 882:33000 | n4 |
| 98 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17In...` | 1267:18 | False | 879 | 646:0 | 75000:879 | n4 |
| 99 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 321:7 | True | 875 | 0:3800000 | 875:71000000 | n4 |
| 100 | `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836...` | 1415:30 | True | 821 | 0:6 | 821:423 | n4 |
| 101 | `_ZNK2OT9glyf_impl5Glyph10get_pointsINS_18glyf_accele...` | 386:11 | True | 800 | 0:663 | 800:2840 | n4 |
| 102 | `hb-ot-font.cc:_ZL24hb_ot_draw_glyph_or_failP9hb_font...` | 910:7 | True | 769 | 0:20400 | 769:45200 | n4 |
| 103 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 277:7 | True | 751 | 0:6400000 | 751:98500000 | n4 |
| 104 | `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5...` | 127:37 | True | 746 | 0:1 | 746:515 | n4 |
| 105 | `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallType...` | 3930:9 | True | 737 | 0:19400 | 737:400000 | n4 |
| 106 | `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallType...` | 3931:9 | True | 737 | 0:19400 | 737:400000 | n4 |
| 107 | `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallType...` | 3932:9 | True | 737 | 0:19400 | 737:400000 | n4 |
| 108 | `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallType...` | 3938:13 | True | 737 | 0:19400 | 737:400000 | n4 |
| 109 | `hb-ot-layout.cc:_ZN2OTL11match_inputINS_11HBGlyphID1...` | 1364:25 | True | 735 | 0:2330 | 735:50100 | n4 |
| 110 | `_ZNK2OT7ArrayOfINS_6Layout9GPOS_impl10MarkRecordENS_...` | 251:24 | False | 731 | 4:0 | 12300:731 | n4 |
| 111 | `_ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableH...` | 143:36 | False | 729 | 1:0 | 224:729 | n4 |
| 112 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 278:7 | True | 716 | 0:6400000 | 716:98500000 | n4 |
| 113 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 317:7 | True | 686 | 0:3800000 | 686:71000000 | n4 |
| 114 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 333:7 | True | 684 | 0:6400000 | 684:98500000 | n4 |
| 115 | `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBG...` | 1467:17 | True | 683 | 0:10100 | 683:17600 | n4 |
| 116 | `_ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTy...` | 50:9 | True | 667 | 0:36 | 667:965 | n4 |
| 117 | `_ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_1...` | 160:9 | False | 664 | 2029:0 | 165000:664 | n4 |
| 118 | `_ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_...` | 499:9 | False | 622 | 32:0 | 741:622 | n4 |
| 119 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 325:7 | True | 621 | 0:3800000 | 621:71000000 | n4 |
| 120 | `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5...` | 129:28 | True | 597 | 0:2 | 597:516 | n4 |
| 121 | `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5...` | 144:28 | True | 597 | 0:2 | 597:516 | n4 |
| 122 | `hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_...` | 456:18 | True | 594 | 0:38 | 594:851 | n4 |
| 123 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegme...` | 1181:11 | True | 565 | 0:16 | 565:609 | n4 |
| 124 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl6AnchorENS_7Num...` | 251:24 | False | 561 | 4:0 | 12500:561 | n4 |
| 125 | `_ZNK3AAT19KerxSubTableFormat0INS_18KerxSubTableHeade...` | 125:31 | True | 542 | 0:1 | 542:63 | n4 |
| 126 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 277:7 | True | 542 | 0:3800000 | 542:71000000 | n4 |
| 127 | `_ZN11hb_vector_tIfLb0EE5allocEjb` | 250:22 | False | 538 | 1260:0 | 1780000:538 | n4 |
| 128 | `_ZNK2OT8hmtxvmtxINS_4vmtxENS_4vheaENS_4VVAREE13accel...` | 251:24 | False | 514 | 7660:0 | 211000:514 | n4 |
| 129 | `hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj` | 57:7 | True | 503 | 0:2810 | 503:107000 | n4 |
| 130 | `_ZN2OT17hb_scalar_cache_t6createEjPS0_` | 2572:9 | True | 466 | 0:586 | 466:2460 | n4 |
| 131 | `_ZNK2OT18glyf_accelerator_t19points_aggregator_t16co...` | 330:56 | True | 462 | 0:3 | 462:28000 | n4 |
| 132 | `_ZN2OT17hb_scalar_cache_t7destroyEPS0_S1_` | 2590:46 | False | 460 | 586:0 | 2440:460 | n4 |
| 133 | `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836...` | 1389:30 | True | 457 | 0:3 | 457:224 | n4 |
| 134 | `_ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20c...` | 499:9 | False | 448 | 16:0 | 510:448 | n4 |
| 135 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 333:7 | True | 435 | 0:3800000 | 435:71000000 | n4 |
| 136 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 107:9 | True | 431 | 0:627 | 431:5380 | n4 |
| 137 | `_ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj` | 671:5 | True | 422 | 0:111000 | 422:873000 | n4 |
| 138 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 292:7 | True | 412 | 0:6400000 | 412:98500000 | n4 |
| 139 | `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_co...` | 874:5 | False | 405 | 15:0 | 66:405 | n4 |
| 140 | `_ZN2OT4cff132lookup_standard_encoding_for_sidEj` | 262:7 | True | 397 | 0:6 | 397:155 | n4 |
| 141 | `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_privat...` | 251:24 | False | 397 | 6:0 | 155:397 | n4 |
| 142 | `_ZNK2OT6Layout9GPOS_impl16SinglePosFormat15applyEPNS...` | 70:9 | False | 392 | 16:0 | 36800:392 | n4 |
| 143 | `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_ap...` | 1477:43 | False | 390 | 5270:0 | 87800:390 | n4 |
| 144 | `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_ap...` | 1520:7 | False | 390 | 5280:0 | 91500:390 | n4 |
| 145 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1194:28 | True | 389 | 0:1 | 389:31 | n4 |
| 146 | `_ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_...` | 519:9 | False | 371 | 26:0 | 739:371 | n4 |
| 147 | `_ZNK2OT6Layout9GSUB_impl20SingleSubstFormat2_4INS0_1...` | 251:24 | True | 349 | 0:68 | 349:610 | n4 |
| 148 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 278:7 | True | 340 | 0:3800000 | 340:71000000 | n4 |
| 149 | `_ZNK2OT8OffsetToINS_19OpenTypeOffsetTableENS_7NumTyp...` | 251:24 | True | 323 | 0:79 | 323:724 | n4 |
| 150 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVARE...` | 474:11 | True | 322 | 0:1 | 322:15 | n4 |
| 151 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVARE...` | 459:11 | True | 312 | 0:5 | 312:103 | n4 |
| 152 | `_ZN3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj18360...` | 1340:32 | True | 294 | 0:5860 | 294:15500 | n4 |
| 153 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 292:7 | True | 291 | 0:3800000 | 291:71000000 | n4 |
| 154 | `_ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20c...` | 519:9 | False | 272 | 12:0 | 487:272 | n4 |
| 155 | `hb-ot-shaper-use.cc:_ZL27_hb_glyph_info_get_lig_comp...` | 508:7 | True | 270 | 0:1 | 270:13000 | n4 |
| 156 | `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBG...` | 1469:9 | False | 268 | 10100:0 | 17300:268 | n4 |
| 157 | `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12i...` | 892:6 | False | 268 | 1730:0 | 2740:268 | n4 |
| 158 | `_ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat...` | 250:22 | False | 267 | 18:0 | 1170:267 | n4 |
| 159 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 123:9 | True | 263 | 0:6 | 263:332 | n4 |
| 160 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 268:7 | True | 262 | 0:6400000 | 262:98500000 | n4 |
| 161 | `hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1...` | 1364:9 | True | 252 | 0:239000 | 252:3200000 | n4 |
| 162 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 313:7 | True | 248 | 0:6400000 | 248:98500000 | n4 |
| 163 | `hb-ot-shaper-use.cc:_ZZL18find_syllables_useP11hb_bu...` | 916:10 | True | 245 | 0:13700 | 245:514000 | n4 |
| 164 | `_ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_s...` | 1279:9 | False | 237 | 13:0 | 215:237 | n4 |
| 165 | `_ZNK2OT8ClassDef9get_classEj` | 2074:5 | True | 237 | 0:40600 | 237:514000 | n4 |
| 166 | `_ZN2OT6Layout9GPOS_impl11ValueFormat10get_deviceEPKN...` | 251:24 | True | 234 | 0:6 | 234:725 | n4 |
| 167 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17In...` | 1284:11 | False | 230 | 646:0 | 75000:230 | n4 |
| 168 | `_ZN11hb_buffer_t14replace_glyphsIjEEbjjPKT_` | 302:34 | False | 227 | 803000:0 | 4000000:227 | n4 |
| 169 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 273:7 | True | 217 | 0:6400000 | 217:98500000 | n4 |
| 170 | `hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_i...` | 357:11 | True | 212 | 0:2029 | 212:242000 | n4 |
| 171 | `_ZNK2OT8OffsetToINS_13IndexSubtableENS_7NumTypeILb1E...` | 251:24 | False | 209 | 26:0 | 66:209 | n4 |
| 172 | `_ZNK2OT15VariationDevice11get_x_deltaEP9hb_font_tRKN...` | 4862:12 | False | 207 | 16:0 | 3:207 | n4 |
| 173 | `_ZNK21hb_sanitize_context_t11check_rangeIN2OT7NumTyp...` | 340:12 | False | 207 | 63:0 | 168000:207 | n4 |
| 174 | `hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1...` | 1404:11 | True | 203 | 0:239000 | 203:3200000 | n4 |
| 175 | `hb-ot-shape-normalize.cc:_ZL33handle_variation_selec...` | 233:14 | True | 203 | 0:13 | 203:206 | n4 |
| 176 | `_ZNK10hb_array_tIKiE11__item_at__Ej` | 251:24 | True | 201 | 0:250 | 201:7850 | n4 |
| 177 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 127:2 | True | 194 | 0:786 | 194:2680 | n4 |
| 178 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1271:14 | True | 191 | 0:2 | 191:953 | n4 |
| 179 | `_ZN2OT11TupleValues9decompileIiEEbRPKNS_7NumTypeILb1...` | 1760:16 | True | 182 | 0:170 | 182:59 | n4 |
| 180 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 268:7 | True | 181 | 0:3800000 | 181:71000000 | n4 |
| 181 | `_ZNK3AAT13LookupFormat0IN2OT7NumTypeILb1EtLj2EEEE9ge...` | 251:24 | True | 176 | 0:110000 | 176:741000 | n4 |
| 182 | `_ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21...` | 350:45 | False | 174 | 933:0 | 5100:174 | n4 |
| 183 | `_Z23hb_indic_get_categoriesj` | 506:11 | True | 172 | 0:1030 | 172:13800 | n4 |
| 184 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationReg...` | 251:24 | True | 168 | 0:42 | 168:1730 | n4 |
| 185 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13Ligatur...` | 864:42 | False | 166 | 40:0 | 793:166 | n4 |
| 186 | `_ZZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5appl...` | 350:45 | False | 156 | 38:0 | 930:156 | n4 |
| 187 | `_ZN11hb_buffer_t16try_allocate_varEjj` | 159:9 | True | 155 | 0:5 | 155:162 | n4 |
| 188 | `_ZNK2OT33hb_ot_layout_lookup_accelerator_t11cache_en...` | 4490:5 | False | 155 | 5:0 | 162:155 | n4 |
| 189 | `hb-ot-layout.cc:_ZN2OTL18context_cache_funcEPNS_21hb...` | 2040:11 | True | 155 | 0:5 | 155:162 | n4 |
| 190 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 313:7 | True | 153 | 0:3800000 | 153:71000000 | n4 |
| 191 | `_ZNK2OT8OffsetToINS_9ColorLineINS_8VariableEEENS_7Nu...` | 251:24 | True | 150 | 0:12 | 150:24 | n4 |
| 192 | `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallType...` | 3921:9 | True | 150 | 0:19400 | 150:401000 | n4 |
| 193 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 128:9 | True | 144 | 0:6 | 144:451 | n4 |
| 194 | `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8di...` | 147:5 | False | 139 | 111:0 | 220:139 | n4 |
| 195 | `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8di...` | 153:5 | True | 139 | 0:111 | 139:220 | n4 |
| 196 | `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_privat...` | 1303:4 | True | 137 | 0:2160 | 137:1640 | n4 |
| 197 | `_ZNK3CFF12CFF2FDSelect6get_fdEj` | 74:9 | False | 135 | 1300:0 | 4650:135 | n4 |
| 198 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 902:45 | True | 135 | 0:3 | 135:4130 | n4 |
| 199 | `_ZN14hb_transform_tIfE7skewingEff` | 271:42 | True | 132 | 0:32 | 132:59 | n4 |
| 200 | `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_co...` | 871:5 | True | 131 | 0:15 | 131:340 | n4 |
| 201 | `_ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15proces...` | 251:24 | False | 131 | 140:0 | 152:131 | n4 |
| 202 | `_ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15proces...` | 251:47 | False | 131 | 140:0 | 138:131 | n4 |
| 203 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17In...` | 1287:60 | False | 130 | 18000:0 | 116000:130 | n4 |
| 204 | `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_...` | 1059:49 | True | 130 | 0:111 | 130:229 | n4 |
| 205 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 127:2 | True | 129 | 0:258 | 129:1310 | n4 |
| 206 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3452:26 | True | 129 | 0:529 | 129:58000 | n4 |
| 207 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1284:11 | False | 126 | 64:0 | 450:126 | n4 |
| 208 | `_ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj` | 437:9 | True | 122 | 0:551000 | 122:6000000 | n4 |
| 209 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 273:7 | True | 120 | 0:3800000 | 120:71000000 | n4 |
| 210 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 138:9 | True | 117 | 0:6 | 117:478 | n4 |
| 211 | `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_co...` | 873:5 | True | 115 | 0:15 | 115:356 | n4 |
| 212 | `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11Mediu...` | 251:24 | False | 113 | 3:0 | 1050:113 | n4 |
| 213 | `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_co...` | 872:5 | True | 112 | 0:15 | 112:359 | n4 |
| 214 | `_ZN11hb_buffer_t18merge_out_clustersEjj` | 578:19 | True | 112 | 0:7 | 112:135 | n4 |
| 215 | `hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_fro...` | 250:22 | True | 112 | 0:41 | 112:522 | n4 |
| 216 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1032:4 | True | 108 | 0:100 | 108:4750 | n4 |
| 217 | `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_pl...` | 202:16 | False | 107 | 18:0 | 200:107 | n4 |
| 218 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSub...` | 886:18 | True | 106 | 0:110000 | 106:222000 | n4 |
| 219 | `_ZNK2OT6Layout9GSUB_impl8LigatureINS0_10SmallTypesEE...` | 165:9 | True | 103 | 0:5280 | 103:91700 | n4 |
| 220 | `_ZNK3AAT4ankr10get_anchorEjjj` | 68:9 | False | 102 | 110000:0 | 111000:102 | n4 |
| 221 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 670:5 | True | 102 | 0:110000 | 102:111000 | n4 |
| 222 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 675:5 | False | 102 | 110000:0 | 111000:102 | n4 |
| 223 | `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeader...` | 562:4 | True | 102 | 0:110000 | 102:111000 | n4 |
| 224 | `_ZNK2OT8OffsetToIN3AAT6LookupINS0_INS_7ArrayOfINS1_6...` | 251:24 | False | 102 | 110000:0 | 111000:102 | n4 |
| 225 | `_ZNK2OT19KernSubTableFormat3INS_20KernOTSubTableHead...` | 350:45 | True | 101 | 0:1 | 101:2 | n4 |
| 226 | `_Z35hb_aat_layout_remove_deleted_glyphsP11hb_buffer_t` | 339:7 | True | 98 | 0:461 | 98:2340 | n4 |
| 227 | `_ZN3CFF27cff2_priv_dict_interp_env_t15process_vsindexEv` | 250:22 | False | 98 | 2:0 | 19:98 | n4 |
| 228 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 314:5 | True | 97 | 0:8290 | 97:23900 | n4 |
| 229 | `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11Mediu...` | 165:27 | False | 96 | 3:0 | 1170:96 | n4 |
| 230 | `_ZNK2OT6Layout9GPOS_impl16PairPosFormat2_4INS0_10Sma...` | 258:30 | False | 96 | 104:0 | 138:96 | n4 |
| 231 | `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14c...` | 167:5 | True | 96 | 0:62 | 96:172 | n4 |
| 232 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 321:5 | False | 93 | 12:0 | 43:93 | n4 |
| 233 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13Ligatur...` | 251:24 | True | 90 | 0:210 | 90:354000 | n4 |
| 234 | `_ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT...` | 251:47 | True | 90 | 0:1880 | 90:5380 | n4 |
| 235 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1154:7 | True | 90 | 0:1 | 90:71 | n4 |
| 236 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 120:2 | True | 89 | 0:786 | 89:2780 | n4 |
| 237 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1866:5 | True | 88 | 0:1800 | 88:7930 | n4 |
| 238 | `_ZNK3AAT12LookupSingleIN2OT7NumTypeILb1EtLj2EEEE23co...` | 492:9 | True | 87 | 0:282 | 87:5910 | n4 |
| 239 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 251:24 | False | 87 | 1:0 | 49:87 | n4 |
| 240 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8...` | 359:9 | True | 87 | 0:624 | 87:671 | n4 |
| 241 | `_ZN14hb_transform_tIfE7skewingEff` | 271:16 | False | 83 | 32:0 | 108:83 | n4 |
| 242 | `hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_fil...` | 992:11 | False | 82 | 38:0 | 848:82 | n4 |
| 243 | `_ZN2OT9glyf_impl20CompositeGlyphRecord9transformERA4...` | 94:22 | True | 81 | 0:398 | 81:2850 | n4 |
| 244 | `_ZN3AAT21RearrangementSubtableINS_13ExtendedTypesEE1...` | 153:8 | True | 81 | 0:35900 | 81:441000 | n4 |
| 245 | `_ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEE...` | 797:11 | False | 80 | 3:0 | 227:80 | n4 |
| 246 | `_ZNK2OT15VariationDevice11get_y_deltaEP9hb_font_tRKN...` | 4867:12 | False | 79 | 11:0 | 4:79 | n4 |
| 247 | `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` | 334:5 | False | 78 | 14:0 | 61:78 | n4 |
| 248 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1872:5 | True | 76 | 0:1800 | 76:7950 | n4 |
| 249 | `_ZNK3AAT12KerxSubTable8dispatchI21hb_sanitize_contex...` | 873:5 | True | 75 | 0:105 | 75:328 | n4 |
| 250 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 251:24 | True | 75 | 0:344 | 75:1120 | n4 |
| 251 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7...` | 251:24 | True | 72 | 0:4 | 72:722 | n4 |
| 252 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 120:2 | True | 71 | 0:258 | 71:1370 | n4 |
| 253 | `hb-ot-layout.cc:_ZN2OTL12apply_lookupEPNS_21hb_ot_ap...` | 251:24 | True | 71 | 0:5040 | 71:56000 | n4 |
| 254 | `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_...` | 887:5 | True | 69 | 0:41 | 69:179 | n4 |
| 255 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat...` | 1038:4 | True | 66 | 0:6 | 66:235 | n4 |
| 256 | `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5apply...` | 3503:30 | False | 66 | 490:0 | 114000:66 | n4 |
| 257 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 920:9 | True | 66 | 0:847 | 66:22300 | n4 |
| 258 | `hb_ot_layout_lookup_would_substitute` | 1559:19 | True | 65 | 0:20 | 65:29200 | n4 |
| 259 | `_ZNK35hb_indic_would_substitute_feature_t16would_sub...` | 104:11 | True | 65 | 0:20 | 65:29200 | n4 |
| 260 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 553:9 | False | 65 | 49:0 | 4270:65 | n4 |
| 261 | `hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDS...` | 1206:14 | True | 64 | 0:2 | 64:69 | n4 |
| 262 | `_ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb...` | 263:9 | False | 64 | 2:0 | 69:64 | n4 |
| 263 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCE...` | 233:111 | False | 64 | 2:0 | 1130:64 | n4 |
| 264 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCE...` | 493:9 | False | 64 | 2:0 | 1130:64 | n4 |
| 265 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 1180:30 | False | 61 | 344:0 | 1120:61 | n4 |
| 266 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 1181:11 | False | 61 | 344:0 | 1060:61 | n4 |
| 267 | `hb-ot-layout.cc:_ZN2OT6LayoutL28propagate_attachment...` | 287:38 | False | 60 | 153:0 | 1530:60 | n4 |
| 268 | `_ZNK3AAT9KerxTableIN2OT6KernOTEE16has_cross_streamEv` | 969:11 | True | 60 | 0:8 | 60:199 | n4 |
| 269 | `hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_fro...` | 250:22 | True | 59 | 0:60 | 59:486 | n4 |
| 270 | `_ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTy...` | 251:24 | True | 58 | 0:36 | 58:1570 | n4 |
| 271 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 148:5 | True | 58 | 0:389 | 58:1590 | n4 |
| 272 | `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` | 333:5 | True | 57 | 0:14 | 57:82 | n4 |
| 273 | `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11h...` | 85:9 | True | 57 | 0:10 | 57:579 | n4 |
| 274 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT1...` | 251:24 | True | 57 | 0:38 | 57:192 | n4 |
| 275 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 320:13 | True | 56 | 0:12 | 56:80 | n4 |
| 276 | `_ZNK2OT9TTCHeader8get_faceEj` | 260:5 | True | 56 | 0:120 | 56:1030 | n4 |
| 277 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 128:2 | True | 55 | 0:786 | 55:2820 | n4 |
| 278 | `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_...` | 2705:8 | True | 55 | 0:36 | 55:548 | n4 |
| 279 | `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_...` | 2709:13 | True | 55 | 0:36 | 55:548 | n4 |
| 280 | `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11h...` | 84:9 | False | 55 | 10:0 | 636:55 | n4 |
| 281 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_ext...` | 250:22 | False | 53 | 18:0 | 13900:53 | n4 |
| 282 | `_ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tI...` | 251:47 | True | 52 | 0:83700 | 52:11800000 | n4 |
| 283 | `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_b...` | 397:7 | True | 52 | 0:1970 | 52:67300 | n4 |
| 284 | `_ZNK21hb_sanitize_context_t11check_rangeIN2OT8Offset...` | 340:12 | False | 52 | 2760:0 | 7910:52 | n4 |
| 285 | `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeader...` | 560:10 | True | 51 | 0:110000 | 51:111000 | n4 |
| 286 | `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeader...` | 618:10 | True | 51 | 0:51 | 51:51 | n4 |
| 287 | `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_...` | 886:5 | True | 50 | 0:41 | 50:198 | n4 |
| 288 | `_ZNK2OT7ArrayOfINS_19SparseVarRegionAxisENS_7NumType...` | 350:45 | False | 50 | 42:0 | 1090:50 | n4 |
| 289 | `_Z23hb_indic_get_categoriesj` | 500:11 | True | 50 | 0:3 | 50:14 | n4 |
| 290 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 1180:30 | False | 49 | 517:0 | 52400:49 | n4 |
| 291 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 1181:11 | False | 49 | 517:0 | 52300:49 | n4 |
| 292 | `hb-ot-shape-normalize.cc:_ZL33handle_variation_selec...` | 250:22 | True | 49 | 0:13 | 49:206 | n4 |
| 293 | `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_...` | 287:38 | False | 48 | 35:0 | 1080:48 | n4 |
| 294 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 56:2 | False | 48 | 1:0 | 1:48 | n4 |
| 295 | `_ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_t...` | 854:11 | False | 47 | 12:0 | 89:47 | n4 |
| 296 | `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_co...` | 875:5 | True | 47 | 0:15 | 47:424 | n4 |
| 297 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE16has_cross_streamEv` | 969:11 | True | 47 | 0:3 | 47:151 | n4 |
| 298 | `hb-face.cc:_ZL10hb_bsearchIKZN2OTL19unicode_to_macro...` | 1227:10 | True | 47 | 0:567 | 47:1370 | n4 |
| 299 | `hb-face.cc:_ZL15hb_bsearch_implIKZN2OTL19unicode_to_...` | 1206:14 | False | 47 | 2640:0 | 5710:47 | n4 |
| 300 | `hb-face.cc:_ZL16_hb_cmp_operatorIttEiPKvS1_` | 1180:7 | False | 47 | 2640:0 | 5710:47 | n4 |
| 301 | `_ZN2OT4cmap13accelerator_t23get_glyph_from_macromanI...` | 2218:14 | True | 47 | 0:567 | 47:1370 | n4 |
| 302 | `hb-face.cc:_ZN2OTL19unicode_to_macromanEj` | 184:10 | True | 47 | 0:567 | 47:1370 | n4 |
| 303 | `_ZNK2OT10SBIXStrike14get_glyph_blobEjP9hb_blob_tjPiS...` | 251:24 | True | 46 | 0:13 | 46:51 | n4 |
| 304 | `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8d...` | 153:5 | True | 46 | 0:6 | 46:255 | n4 |
| 305 | `_ZNK2OT16DeltaSetIndexMap3mapEj` | 3744:5 | True | 46 | 0:445 | 46:2009 | n4 |
| 306 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 462:38 | True | 45 | 0:12300 | 45:442000 | n4 |
| 307 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 462:44 | True | 45 | 0:11600 | 45:440000 | n4 |
| 308 | `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_cons...` | 189:9 | True | 45 | 0:27 | 45:3340 | n4 |
| 309 | `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_1...` | 137:12 | False | 44 | 2:0 | 50:44 | n4 |
| 310 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 133:9 | False | 43 | 6:0 | 552:43 | n4 |
| 311 | `hb-ot-shaper-khmer.cc:_ZL17_hb_next_syllableP11hb_bu...` | 166:29 | True | 42 | 0:15500 | 42:84600 | n4 |
| 312 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 704:24 | False | 41 | 236:0 | 126:41 | n4 |
| 313 | `_ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tI...` | 251:47 | True | 39 | 0:46800 | 39:8800000 | n4 |
| 314 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTabl...` | 251:24 | True | 39 | 0:79 | 39:1000 | n4 |
| 315 | `hb-ot-shaper-arabic.cc:_ZL12joining_typej` | 208:11 | True | 39 | 0:23 | 39:49 | n4 |
| 316 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1085:22 | True | 39 | 0:16 | 39:8960 | n4 |
| 317 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 128:2 | True | 38 | 0:258 | 38:1400 | n4 |
| 318 | `_ZNK2OT7Context8dispatchINS_33hb_accelerate_subtable...` | 2961:5 | True | 38 | 0:937 | 38:8690 | n4 |
| 319 | `_ZN11hb_vector_tIfLb0EE6resizeEibb` | 487:9 | True | 38 | 0:1630 | 38:1780000 | n4 |
| 320 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7...` | 350:45 | False | 37 | 51:0 | 574:37 | n4 |
| 321 | `hb-ot-shaper-hebrew.cc:_ZL20reorder_marks_hebrewPK18...` | 173:32 | True | 37 | 0:6 | 37:130 | n4 |
| 322 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 535:24 | True | 37 | 0:2 | 37:1020 | n4 |
| 323 | `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1...` | 428:9 | False | 37 | 51:0 | 574:37 | n4 |
| 324 | `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb...` | 322:31 | True | 36 | 0:1 | 36:61 | n4 |
| 325 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT1...` | 251:24 | True | 36 | 0:27 | 36:108 | n4 |
| 326 | `_ZNK3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2O...` | 136:12 | True | 35 | 0:10200000 | 35:169000000 | n4 |
| 327 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_pat...` | 250:22 | False | 35 | 12:0 | 10400:35 | n4 |
| 328 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 123:2 | True | 35 | 0:786 | 35:2840 | n4 |
| 329 | `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb...` | 349:9 | True | 35 | 0:1 | 35:33 | n4 |
| 330 | `_ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEE...` | 251:24 | False | 34 | 82:0 | 980:34 | n4 |
| 331 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1855:5 | True | 32 | 0:1800 | 32:7990 | n4 |
| 332 | `_ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj` | 675:5 | True | 32 | 0:111000 | 32:874000 | n4 |
| 333 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 163:6 | True | 32 | 0:466 | 32:646 | n4 |
| 334 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 171:11 | True | 32 | 0:466 | 32:646 | n4 |
| 335 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 141:7 | True | 32 | 0:5 | 32:181 | n4 |
| 336 | `_Z20find_syllables_khmerP11hb_buffer_t` | 361:2 | True | 32 | 0:8260 | 32:45900 | n4 |
| 337 | `hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_sh...` | 345:11 | True | 32 | 0:2080 | 32:231000 | n4 |
| 338 | `_ZNK2OT23MultiItemVariationStore8sanitizeEP21hb_sani...` | 350:45 | False | 31 | 2:0 | 537:31 | n4 |
| 339 | `_ZNK2OT20TupleVariationHeader16calculate_scalarE10hb...` | 159:13 | False | 31 | 2:0 | 19:31 | n4 |
| 340 | `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_app...` | 1038:4 | True | 30 | 0:15 | 30:441 | n4 |
| 341 | `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_app...` | 1054:11 | True | 30 | 0:15 | 30:441 | n4 |
| 342 | `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_app...` | 1063:11 | True | 30 | 0:15 | 30:441 | n4 |
| 343 | `hb-ot-shape.cc:_ZL20hb_set_unicode_propsP11hb_buffer_t` | 251:47 | True | 30 | 0:138000 | 30:373000 | n4 |
| 344 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1033:2 | True | 30 | 0:2020 | 30:73800 | n4 |
| 345 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1075:2 | True | 30 | 0:2020 | 30:73800 | n4 |
| 346 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13Ligatur...` | 872:9 | True | 29 | 0:6 | 29:92 | n4 |
| 347 | `_ZNK10hb_array_tIKN2OT22MathGlyphVariantRecordEEneER...` | 132:12 | True | 29 | 0:6150 | 29:16500 | n4 |
| 348 | `_ZNK13hb_zip_iter_tI10hb_array_tIKN2OT22MathGlyphVar...` | 581:12 | True | 29 | 0:6150 | 29:16500 | n4 |
| 349 | `_ZNK2OT21MathGlyphConstruction12get_variantsE14hb_di...` | 849:19 | True | 29 | 0:6150 | 29:16500 | n4 |
| 350 | `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_f...` | 394:7 | True | 29 | 0:10 | 29:882 | n4 |
| 351 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 711:6 | True | 29 | 0:147 | 29:35 | n4 |
| 352 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 798:6 | True | 29 | 0:147 | 29:35 | n4 |
| 353 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1268:19 | True | 28 | 0:6 | 28:34 | n4 |
| 354 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_...` | 1134:42 | True | 28 | 0:1 | 28:61 | n4 |
| 355 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 600:2 | True | 28 | 0:354 | 28:50000 | n4 |
| 356 | `_ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPK...` | 250:22 | True | 28 | 0:27 | 28:347 | n4 |
| 357 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 92:7 | True | 27 | 0:6410000 | 27:98500000 | n4 |
| 358 | `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14c...` | 166:5 | True | 27 | 0:62 | 27:241 | n4 |
| 359 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 581:8 | True | 27 | 0:844 | 27:20500 | n4 |
| 360 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 242:16 | True | 27 | 0:123 | 27:1790 | n4 |
| 361 | `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_...` | 889:5 | True | 26 | 0:41 | 26:222 | n4 |
| 362 | `_ZN3CFF14biased_subrs_tINS_5SubrsIN2OT7NumTypeILb1Et...` | 69:9 | False | 26 | 2270:0 | 9410:26 | n4 |
| 363 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 145:5 | True | 26 | 0:389 | 26:1630 | n4 |
| 364 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 776:10 | False | 26 | 6:0 | 4:26 | n4 |
| 365 | `_ZN22hb_serialize_context_t13check_successEb20hb_ser...` | 258:13 | False | 26 | 11800:0 | 17100:26 | n4 |
| 366 | `hb_script_get_horizontal_direction` | 619:5 | True | 25 | 0:29700 | 25:79800 | n4 |
| 367 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixE...` | 350:45 | False | 25 | 84:0 | 487:25 | n4 |
| 368 | `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1...` | 428:9 | False | 25 | 84:0 | 487:25 | n4 |
| 369 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1879:5 | True | 24 | 0:1800 | 24:8000 | n4 |
| 370 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7N...` | 251:24 | True | 24 | 0:5 | 24:1550 | n4 |
| 371 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 116:16 | True | 24 | 0:3 | 24:19 | n4 |
| 372 | `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11h...` | 60:7 | False | 24 | 6:0 | 93:24 | n4 |
| 373 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 123:2 | True | 23 | 0:258 | 23:1420 | n4 |
| 374 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1860:5 | True | 22 | 0:1800 | 22:8000 | n4 |
| 375 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1862:5 | True | 22 | 0:1800 | 22:8000 | n4 |
| 376 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 122:2 | True | 22 | 0:786 | 22:2850 | n4 |
| 377 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 260:5 | True | 22 | 0:237 | 22:969 | n4 |
| 378 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 292:5 | True | 22 | 0:237 | 22:969 | n4 |
| 379 | `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` | 332:5 | True | 21 | 0:14 | 21:118 | n4 |
| 380 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 320:5 | True | 21 | 0:12 | 21:115 | n4 |
| 381 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationReg...` | 350:45 | False | 21 | 2:0 | 640:21 | n4 |
| 382 | `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8d...` | 155:5 | True | 21 | 0:5 | 21:193 | n4 |
| 383 | `_ZNK2OT12MultiVarData8sanitizeEP21hb_sanitize_context_t` | 350:45 | False | 21 | 5:0 | 418:21 | n4 |
| 384 | `hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllabl...` | 226:38 | True | 21 | 0:504 | 21:1480 | n4 |
| 385 | `hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllabl...` | 231:36 | True | 21 | 0:504 | 21:1480 | n4 |
| 386 | `hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_...` | 455:9 | True | 21 | 0:130 | 21:552 | n4 |
| 387 | `_ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPK...` | 250:45 | False | 21 | 27:0 | 375:21 | n4 |
| 388 | `_ZN11hb_buffer_t13shift_forwardEj` | 251:24 | True | 20 | 0:18300 | 20:76400 | n4 |
| 389 | `_ZN11hb_buffer_t7move_toEj` | 251:24 | True | 20 | 0:3070000 | 20:15200000 | n4 |
| 390 | `_ZN11hb_buffer_t7move_toEj` | 251:47 | True | 20 | 0:18300 | 20:76400 | n4 |
| 391 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 92:7 | True | 20 | 0:3800000 | 20:71000000 | n4 |
| 392 | `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8d...` | 153:5 | True | 20 | 0:5 | 20:194 | n4 |
| 393 | `_ZN2OT17hb_scalar_cache_t6createEjPS0_` | 251:24 | True | 20 | 0:586 | 20:2440 | n4 |
| 394 | `_Z23hb_indic_get_categoriesj` | 496:11 | True | 20 | 0:19 | 20:423 | n4 |
| 395 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 450:10 | False | 20 | 15:0 | 160:20 | n4 |
| 396 | `_ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_1...` | 350:45 | False | 19 | 146:0 | 532:19 | n4 |
| 397 | `_ZN3CFF18dict_interpreter_tINS_22cff1_font_dict_opse...` | 251:24 | True | 19 | 0:2890 | 19:4590 | n4 |
| 398 | `_ZNK14hb_transform_tIfE11is_identityEv` | 120:23 | False | 19 | 6:0 | 177000:19 | n4 |
| 399 | `_ZNK14hb_transform_tIfE11is_identityEv` | 121:16 | False | 19 | 6:0 | 177000:19 | n4 |
| 400 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 824:11 | True | 19 | 0:9 | 19:6230 | n4 |
| 401 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1017:2 | True | 19 | 0:2020 | 19:73800 | n4 |
| 402 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 452:4 | True | 19 | 0:15 | 19:161 | n4 |
| 403 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1865:5 | True | 18 | 0:1800 | 18:8000 | n4 |
| 404 | `_ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_fo...` | 333:39 | True | 18 | 0:154 | 18:498 | n4 |
| 405 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0...` | 1134:10 | True | 18 | 0:1 | 18:71 | n4 |
| 406 | `_ZNK2OT8OffsetToINS_9ColorLineINS_10NoVariableEEENS_...` | 251:24 | False | 18 | 6:0 | 138:18 | n4 |
| 407 | `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14...` | 167:5 | True | 18 | 0:3 | 18:161 | n4 |
| 408 | `hb-ot-layout.cc:_ZL12apply_stringI9GSUBProxyEbPN2OT2...` | 1978:7 | False | 18 | 2410:0 | 16900:18 | n4 |
| 409 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 121:2 | True | 17 | 0:786 | 17:2860 | n4 |
| 410 | `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20...` | 124:2 | True | 17 | 0:786 | 17:2860 | n4 |
| 411 | `_ZN22hb_serialize_context_t4pushIN2OT6Layout9GSUB_im...` | 251:24 | True | 17 | 0:473 | 17:779 | n4 |
| 412 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1854:5 | True | 16 | 0:1800 | 16:8010 | n4 |
| 413 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1874:5 | True | 16 | 0:1800 | 16:8010 | n4 |
| 414 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18Context...` | 949:37 | False | 16 | 7:0 | 65:16 | n4 |
| 415 | `_ZNK3AAT18ContextualSubtableINS_13ObsoleteTypesEE8sa...` | 251:24 | False | 16 | 6:0 | 30:16 | n4 |
| 416 | `_ZNK10hb_array_tIKN2OT19MathGlyphPartRecordEEneERKS3_` | 132:12 | True | 16 | 0:6150 | 16:16500 | n4 |
| 417 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_ext...` | 338:7 | True | 16 | 0:77700 | 16:11700000 | n4 |
| 418 | `_ZNK13hb_zip_iter_tI10hb_array_tIKN2OT19MathGlyphPar...` | 581:12 | True | 16 | 0:6150 | 16:16500 | n4 |
| 419 | `_ZNK2OT8OffsetToINS_17MathGlyphAssemblyENS_7NumTypeI...` | 251:24 | False | 16 | 18400:0 | 49600:16 | n4 |
| 420 | `_ZNK2OT17MathGlyphAssembly9get_partsE14hb_direction_...` | 780:19 | True | 16 | 0:6150 | 16:16500 | n4 |
| 421 | `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_f...` | 393:7 | True | 16 | 0:10 | 16:911 | n4 |
| 422 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 687:6 | False | 16 | 240:0 | 159:16 | n4 |
| 423 | `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14...` | 168:5 | True | 15 | 0:3 | 15:164 | n4 |
| 424 | `hb-ot-shape-fallback.cc:_ZL20position_around_basePK1...` | 387:11 | False | 15 | 238:0 | 997:15 | n4 |
| 425 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1001:2 | True | 15 | 0:2020 | 15:73800 | n4 |
| 426 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1864:5 | True | 14 | 0:1800 | 14:8010 | n4 |
| 427 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1876:5 | True | 14 | 0:1800 | 14:8010 | n4 |
| 428 | `_ZNK2OT12LigCaretList14get_lig_caretsEP9hb_font_t14h...` | 380:9 | False | 14 | 6150:0 | 16500:14 | n4 |
| 429 | `_ZNK3AAT10StateTableINS_13ExtendedTypesEvE22collect_...` | 872:9 | True | 14 | 0:26 | 14:131 | n4 |
| 430 | `_ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableH...` | 251:24 | True | 14 | 0:7 | 14:160 | n4 |
| 431 | `hb-paint-extents.cc:_ZNK3$_0clIRfRKfEEDTqugefp_fp0_f...` | 76:55 | False | 14 | 4:0 | 10:14 | n4 |
| 432 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 129:5 | True | 14 | 0:389 | 14:1640 | n4 |
| 433 | `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_f...` | 391:7 | True | 14 | 0:10 | 14:927 | n4 |
| 434 | `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` | 77:7 | True | 14 | 0:225 | 14:2220 | n4 |
| 435 | `_ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_10...` | 116:11 | False | 13 | 3:0 | 515:13 | n4 |
| 436 | `_ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33...` | 37:5 | True | 13 | 0:554 | 13:3080 | n4 |
| 437 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13Ligatur...` | 251:24 | True | 13 | 0:15 | 13:324 | n4 |
| 438 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_12Format1...` | 251:24 | True | 13 | 0:1 | 13:122 | n4 |
| 439 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 122:2 | True | 13 | 0:258 | 13:1430 | n4 |
| 440 | `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12i...` | 251:24 | True | 13 | 0:1150 | 13:1850 | n4 |
| 441 | `hb-ot-shaper-arabic.cc:_ZL12joining_typej` | 207:11 | True | 13 | 0:23 | 13:88 | n4 |
| 442 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 640:2 | True | 13 | 0:354 | 13:50000 | n4 |
| 443 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 226:10 | False | 13 | 540:0 | 1720:13 | n4 |
| 444 | `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5Entry...` | 341:5 | False | 13 | 15:0 | 324:13 | n4 |
| 445 | `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5Entry...` | 341:5 | False | 13 | 1:0 | 122:13 | n4 |
| 446 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1880:5 | True | 12 | 0:1800 | 12:8010 | n4 |
| 447 | `_ZN2OT6Layout9GSUB_impl11LigatureSetINS0_10SmallType...` | 251:24 | True | 12 | 0:5980 | 12:7490 | n4 |
| 448 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat...` | 1014:34 | True | 12 | 0:9 | 12:506 | n4 |
| 449 | `_ZNK10hb_array_tIKcE11check_rangeIN2OT7NumTypeILb1Et...` | 291:5 | False | 12 | 1570:0 | 55000:12 | n4 |
| 450 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 121:2 | True | 12 | 0:258 | 12:1430 | n4 |
| 451 | `_ZN11hb_bounds_tIfE9intersectERKS0_` | 336:9 | True | 12 | 0:4520 | 12:512 | n4 |
| 452 | `_ZNK2OT9TTCHeader8sanitizeEP21hb_sanitize_context_t` | 272:5 | True | 12 | 0:5 | 12:101 | n4 |
| 453 | `_ZN2OT8OffsetToINS_6Layout9GSUB_impl8LigatureINS1_10...` | 469:9 | False | 12 | 5980:0 | 7490:12 | n4 |
| 454 | `_ZNK2OT6Device11get_x_deltaEP9hb_font_tRKNS_18ItemVa...` | 4933:13 | True | 12 | 0:43000 | 12:116000 | n4 |
| 455 | `_ZNK2OT9Condition8evaluateINS_21ItemVarStoreInstance...` | 4212:5 | True | 12 | 0:769 | 12:546 | n4 |
| 456 | `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_scri...` | 35:5 | True | 12 | 0:140 | 12:573 | n4 |
| 457 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 365:5 | True | 12 | 0:8290 | 12:24000 | n4 |
| 458 | `_ZNK2OT23IndexSubtableFormat1Or3INS_7NumTypeILb1EjLj...` | 350:45 | False | 11 | 21:0 | 38:11 | n4 |
| 459 | `_ZN12hb_bit_set_t9add_rangeEjj` | 251:47 | True | 11 | 0:99700 | 11:54900 | n4 |
| 460 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_pat...` | 338:7 | True | 11 | 0:43600 | 11:8790000 | n4 |
| 461 | `_ZNK14hb_transform_tIfE11is_identityEv` | 121:5 | False | 11 | 6:0 | 177000:11 | n4 |
| 462 | `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CF...` | 54:7 | True | 11 | 0:2 | 11:82 | n4 |
| 463 | `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_privat...` | 1312:11 | True | 11 | 0:1 | 11:1 | n4 |
| 464 | `_Z18data_create_arabicPK18hb_ot_shape_plan_t` | 251:24 | True | 11 | 0:299 | 11:668 | n4 |
| 465 | `_Z20find_syllables_indicP11hb_buffer_t` | 1209:2 | True | 11 | 0:2060 | 11:189000 | n4 |
| 466 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1448:2 | False | 11 | 2:0 | 38:11 | n4 |
| 467 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1009:2 | True | 11 | 0:2020 | 11:73800 | n4 |
| 468 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 113:10 | False | 11 | 75:0 | 933:11 | n4 |
| 469 | `_ZNK21hb_sanitize_context_t11check_rangeIN2OT6Offset...` | 341:5 | False | 11 | 21:0 | 38:11 | n4 |
| 470 | `_ZN11hb_vector_tI14hb_transform_tIfELb0EE6resizeEibb` | 487:9 | True | 11 | 0:11000 | 11:31500 | n4 |
| 471 | `_ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_contex...` | 251:24 | True | 11 | 0:473 | 11:785 | n4 |
| 472 | `_ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_contex...` | 251:47 | True | 11 | 0:473 | 11:785 | n4 |
| 473 | `_ZN11hb_vector_tIN11hb_ot_map_t12lookup_map_tELb0EE5...` | 462:11 | True | 11 | 0:28 | 11:92 | n4 |
| 474 | `_ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_t...` | 847:48 | True | 10 | 0:12 | 10:136 | n4 |
| 475 | `_ZNK2OT15PaintColrLayers11paint_glyphEPNS_18hb_paint...` | 251:24 | True | 10 | 0:428 | 10:5370 | n4 |
| 476 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1868:5 | True | 10 | 0:1800 | 10:8010 | n4 |
| 477 | `_ZNK2OT6Layout9GPOS_impl16PairPosFormat1_3INS0_11Med...` | 38:9 | True | 10 | 0:66 | 10:304 | n4 |
| 478 | `hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOrigin...` | 1204:9 | True | 10 | 0:8 | 10:23 | n4 |
| 479 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0...` | 1134:42 | True | 10 | 0:1 | 10:61 | n4 |
| 480 | `_ZN3CFF11cff_stack_tINS_8number_tELi513EE4pushEv` | 250:22 | False | 10 | 149000:0 | 19300000:10 | n4 |
| 481 | `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff...` | 124:2 | True | 10 | 0:258 | 10:1430 | n4 |
| 482 | `_ZN3CFF22cff2_font_dict_opset_t10process_opEjRNS_12i...` | 251:24 | True | 10 | 0:275 | 10:1150 | n4 |
| 483 | `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_...` | 814:7 | True | 10 | 0:23100 | 10:66900 | n4 |
| 484 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 48:2 | True | 10 | 0:1 | 10:39 | n4 |
| 485 | `hb-ot-shape-normalize.cc:_ZL27decompose_current_char...` | 178:9 | False | 10 | 471:0 | 1240:10 | n4 |
| 486 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 631:2 | True | 10 | 0:2 | 10:51 | n4 |
| 487 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 634:2 | False | 10 | 2:0 | 51:10 | n4 |
| 488 | `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` | 82:7 | True | 10 | 0:223 | 10:2160 | n4 |
| 489 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 236:32 | True | 10 | 0:540 | 10:1730 | n4 |
| 490 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 359:4 | True | 10 | 0:15 | 10:110 | n4 |
| 491 | `_ZNK2OT10avarV2Tail8sanitizeEP21hb_sanitize_context_...` | 350:45 | False | 10 | 32:0 | 69:10 | n4 |
| 492 | `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` | 224:7 | True | 10 | 0:471 | 10:1240 | n4 |
| 493 | `_ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_fo...` | 345:11 | True | 9 | 0:154 | 9:489 | n4 |
| 494 | `_ZN2OT6Layout9GSUB_impl11SubstLookup16serialize_sing...` | 251:24 | True | 9 | 0:188 | 9:375 | n4 |
| 495 | `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_s...` | 732:5 | True | 9 | 0:64 | 9:290 | n4 |
| 496 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeE...` | 949:12 | True | 9 | 0:44 | 9:356 | n4 |
| 497 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeE...` | 951:11 | True | 9 | 0:36 | 9:254 | n4 |
| 498 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 747:5 | True | 9 | 0:6 | 9:185 | n4 |
| 499 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_i...` | 456:12 | True | 9 | 0:130 | 9:573 | n4 |
| 500 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_i...` | 456:18 | True | 9 | 0:130 | 9:572 | n4 |
| 501 | `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_...` | 813:7 | True | 9 | 0:23100 | 9:66900 | n4 |
| 502 | `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesi...` | 101:10 | False | 9 | 188:0 | 375:9 | n4 |
| 503 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 542:9 | True | 9 | 0:2 | 9:42 | n4 |
| 504 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 977:2 | True | 9 | 0:2020 | 9:73800 | n4 |
| 505 | `_ZN13hb_utf16_xe_tItE10encode_lenEj` | 264:12 | False | 9 | 46300:0 | 69500:9 | n4 |
| 506 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1853:5 | True | 8 | 0:1800 | 8:8010 | n4 |
| 507 | `_ZN2OT6Layout9GSUB_impl11SubstLookup18serialize_liga...` | 251:24 | True | 8 | 0:285 | 8:404 | n4 |
| 508 | `_ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableH...` | 109:9 | True | 8 | 0:2 | 8:134 | n4 |
| 509 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_a...` | 1177:4 | True | 8 | 0:3 | 8:341 | n4 |
| 510 | `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBG...` | 1467:12 | False | 8 | 10100:0 | 18200:8 | n4 |
| 511 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_...` | 1134:10 | True | 8 | 0:1 | 8:89 | n4 |
| 512 | `_ZN11hb_bounds_tIfE9intersectERKS0_` | 345:6 | True | 8 | 0:2 | 8:4 | n4 |
| 513 | `hb-number.cc:_ZL9strtod_rlPKcPS0_` | 223:9 | True | 8 | 0:1 | 8:6 | n4 |
| 514 | `hb-ot-shaper-indic.cc:_ZL41_hb_glyph_info_ligated_an...` | 586:10 | True | 8 | 0:2 | 8:953 | n4 |
| 515 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 87:5 | True | 8 | 0:389 | 8:1640 | n4 |
| 516 | `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesi...` | 101:17 | False | 8 | 188:0 | 367:8 | n4 |
| 517 | `_Z23hb_indic_get_categoriesj` | 512:11 | True | 8 | 0:4 | 8:12 | n4 |
| 518 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 251:24 | True | 8 | 0:472 | 8:750 | n4 |
| 519 | `_ZN15hb_set_digest_t9add_rangeEjj` | 103:9 | True | 8 | 0:13000 | 8:37800 | n4 |
| 520 | `_ZNK2OT21SVGDocumentIndexEntry3cmpEj` | 46:36 | False | 7 | 9:0 | 24:7 | n4 |
| 521 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18Context...` | 949:12 | True | 7 | 0:7 | 7:81 | n4 |
| 522 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18Context...` | 951:11 | True | 7 | 0:7 | 7:65 | n4 |
| 523 | `_ZN3AAT13ObsoleteTypes13offsetToIndexIN2OT7NumTypeIL...` | 251:24 | True | 7 | 0:7 | 7:167 | n4 |
| 524 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat...` | 1017:11 | True | 7 | 0:9 | 7:499 | n4 |
| 525 | `hb-ot-color.cc:_ZL15hb_bsearch_implIKN2OT21SVGDocume...` | 1206:14 | False | 7 | 9:0 | 24:7 | n4 |
| 526 | `hb-ot-layout.cc:_ZL15hb_bsearch_implIKN2OT6RecordINS...` | 1206:14 | False | 7 | 247:0 | 2980:7 | n4 |
| 527 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S...` | 1134:42 | True | 7 | 0:1 | 7:61 | n4 |
| 528 | `_ZNK17hb_sorted_array_tIKN2OT6RecordINS0_7LangSysEEE...` | 414:9 | True | 7 | 0:16500 | 7:48000 | n4 |
| 529 | `_ZN17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryE...` | 399:12 | True | 7 | 0:6150 | 7:16500 | n4 |
| 530 | `_ZNK17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntry...` | 414:9 | True | 7 | 0:6150 | 7:16500 | n4 |
| 531 | `hb_script_get_horizontal_direction` | 629:5 | True | 7 | 0:29700 | 7:79800 | n4 |
| 532 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7N...` | 350:45 | False | 7 | 2:0 | 561:7 | n4 |
| 533 | `_ZNK2OT8OffsetToINS_9SBIXGlyphENS_7NumTypeILb1EjLj4E...` | 251:24 | True | 7 | 0:13 | 7:90 | n4 |
| 534 | `hb_ot_layout_script_select_language2` | 792:7 | True | 7 | 0:16500 | 7:48000 | n4 |
| 535 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 49:2 | True | 7 | 0:1 | 7:42 | n4 |
| 536 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 200:10 | False | 7 | 91:0 | 116:7 | n4 |
| 537 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 346:7 | True | 7 | 0:1 | 7:25 | n4 |
| 538 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 348:25 | False | 7 | 1:0 | 25:7 | n4 |
| 539 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 371:8 | False | 7 | 1:0 | 25:7 | n4 |
| 540 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 479:7 | True | 7 | 0:1 | 7:1550 | n4 |
| 541 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 337:11 | False | 7 | 80:0 | 1150:7 | n4 |
| 542 | `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb...` | 346:12 | False | 7 | 1:0 | 97:7 | n4 |
| 543 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 981:2 | True | 7 | 0:2020 | 7:73800 | n4 |
| 544 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 115:4 | True | 7 | 0:75 | 7:937 | n4 |
| 545 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 134:10 | False | 7 | 30:0 | 368:7 | n4 |
| 546 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 328:10 | False | 7 | 15:0 | 323:7 | n4 |
| 547 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 327:5 | True | 7 | 0:8290 | 7:24000 | n4 |
| 548 | `_ZNK2OT4VVAR23get_vorg_delta_unscaledEjPKijPNS_17hb_...` | 455:9 | True | 7 | 0:1 | 7:24 | n4 |
| 549 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCE...` | 474:25 | False | 7 | 7:0 | 50:7 | n4 |
| 550 | `hb-ucd.cc:_ZL14hb_ucd_composeP18hb_unicode_funcs_tjj...` | 251:24 | True | 7 | 0:84 | 7:144 | n4 |
| 551 | `hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj` | 98:26 | True | 7 | 0:1320 | 7:6420 | n4 |
| 552 | `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_pl...` | 121:56 | False | 7 | 6:7 | 24:0 | cmplog |
| 553 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 319:13 | True | 6 | 0:12 | 6:130 | n4 |
| 554 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1856:5 | True | 6 | 0:1800 | 6:8020 | n4 |
| 555 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1870:5 | True | 6 | 0:1800 | 6:8020 | n4 |
| 556 | `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEEN...` | 1878:5 | True | 6 | 0:1800 | 6:8020 | n4 |
| 557 | `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_1...` | 350:45 | False | 6 | 20:0 | 1020:6 | n4 |
| 558 | `_ZNK2OT6Layout9GSUB_impl22LigatureSubstFormat1_2INS0...` | 250:22 | False | 6 | 10:0 | 690:6 | n4 |
| 559 | `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18Context...` | 251:24 | True | 6 | 0:3 | 6:44 | n4 |
| 560 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_18Co...` | 1278:9 | False | 6 | 6:0 | 110:6 | n4 |
| 561 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_18Context...` | 251:24 | True | 6 | 0:169 | 6:1180 | n4 |
| 562 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17In...` | 251:24 | True | 6 | 0:36500 | 6:219000 | n4 |
| 563 | `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_...` | 1037:11 | False | 6 | 111:0 | 353:6 | n4 |
| 564 | `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836...` | 251:24 | True | 6 | 0:3 | 6:224 | n4 |
| 565 | `_ZNK3AAT8mortmorxINS_4morxENS_13ExtendedTypesELj1836...` | 251:24 | True | 6 | 0:385 | 6:1810 | n4 |
| 566 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_a...` | 251:24 | True | 6 | 0:190 | 6:1090 | n4 |
| 567 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_ext...` | 348:7 | True | 6 | 0:77700 | 6:11700000 | n4 |
| 568 | `hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_fil...` | 991:33 | False | 6 | 38:0 | 930:6 | n4 |
| 569 | `_ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat...` | 250:22 | False | 6 | 48:0 | 1370:6 | n4 |
| 570 | `_ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object...` | 251:47 | True | 6 | 0:606 | 6:980 | n4 |
| 571 | `_ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object...` | 251:24 | True | 6 | 0:607 | 6:981 | n4 |
| 572 | `hb-ot-math.cc:_ZNK3$_2clIRjS1_EEDTqulefp_fp0_fp_fp0_...` | 76:55 | False | 6 | 12300:0 | 33000:6 | n4 |
| 573 | `_ZNK2OT7ArrayOfIN3CFF17FDSelect3_4_RangeINS_7NumType...` | 251:24 | True | 6 | 0:553 | 6:1020 | n4 |
| 574 | `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cf...` | 800:7 | True | 6 | 0:13500 | 6:37000 | n4 |
| 575 | `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_conte...` | 98:5 | True | 6 | 0:2 | 6:86 | n4 |
| 576 | `_ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12Exte...` | 251:24 | True | 6 | 0:461 | 6:1190 | n4 |
| 577 | `hb_ot_layout_language_find_feature` | 1022:11 | False | 6 | 6:0 | 4:6 | n4 |
| 578 | `_ZN19hb_ot_map_builder_t11has_featureEj` | 116:9 | True | 6 | 0:574 | 6:1140 | n4 |
| 579 | `_ZNK2OT4meta8sanitizeEP21hb_sanitize_context_t` | 350:45 | False | 6 | 2:0 | 4:6 | n4 |
| 580 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 61:2 | True | 6 | 0:1 | 6:43 | n4 |
| 581 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 106:5 | True | 6 | 0:389 | 6:1650 | n4 |
| 582 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 200:10 | False | 6 | 94:0 | 132:6 | n4 |
| 583 | `hb-ot-shaper-arabic.cc:_ZL23collect_features_arabicP...` | 235:8 | False | 6 | 287:0 | 573:6 | n4 |
| 584 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 119:25 | True | 6 | 0:720 | 6:2490 | n4 |
| 585 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 150:7 | True | 6 | 0:5 | 6:207 | n4 |
| 586 | `_Z20find_syllables_indicP11hb_buffer_t` | 1217:2 | True | 6 | 0:2060 | 6:189000 | n4 |
| 587 | `_Z23hb_indic_get_categoriesj` | 510:11 | True | 6 | 0:4 | 6:21 | n4 |
| 588 | `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_f...` | 390:7 | True | 6 | 0:10 | 6:941 | n4 |
| 589 | `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11h...` | 81:11 | False | 6 | 10:0 | 634:6 | n4 |
| 590 | `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` | 80:7 | True | 6 | 0:223 | 6:2170 | n4 |
| 591 | `hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_acti...` | 146:5 | False | 6 | 2:0 | 65:6 | n4 |
| 592 | `hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_acti...` | 147:5 | True | 6 | 0:2 | 6:65 | n4 |
| 593 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 989:2 | True | 6 | 0:2020 | 6:73800 | n4 |
| 594 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1021:2 | True | 6 | 0:2020 | 6:73800 | n4 |
| 595 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 330:4 | True | 6 | 0:15 | 6:324 | n4 |
| 596 | `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint...` | 81:7 | True | 6 | 0:116 | 6:62 | n4 |
| 597 | `_ZN9hb_pool_tIN22hb_serialize_context_t8object_tELj3...` | 251:24 | True | 6 | 0:550 | 6:875 | n4 |
| 598 | `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5Entry...` | 341:5 | False | 6 | 3:0 | 44:6 | n4 |
| 599 | `_ZN21hb_sanitize_context_t12may_dispatchIN2OT16Exten...` | 138:12 | False | 6 | 461:0 | 1190:6 | n4 |
| 600 | `_ZN9hb_utf8_t6encodeEPhPKhj` | 157:14 | False | 6 | 35:0 | 86:6 | n4 |
| 601 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 319:5 | True | 5 | 0:12 | 5:131 | n4 |
| 602 | `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_exte...` | 320:21 | True | 5 | 0:12 | 5:131 | n4 |
| 603 | `_ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33...` | 36:5 | True | 5 | 0:554 | 5:3080 | n4 |
| 604 | `_ZNK2OT4VARC8sanitizeEP21hb_sanitize_context_t` | 350:45 | False | 5 | 2:0 | 2240:5 | n4 |
| 605 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 748:5 | True | 5 | 0:6 | 5:189 | n4 |
| 606 | `_ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature...` | 396:7 | True | 5 | 0:5730 | 5:15100 | n4 |
| 607 | `_ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature...` | 401:7 | True | 5 | 0:5730 | 5:15100 | n4 |
| 608 | `hb-buffer-verify.cc:_ZL29buffer_verify_unsafe_to_bre...` | 185:9 | True | 5 | 0:63 | 5:120 | n4 |
| 609 | `hb_buffer_set_length` | 1565:7 | False | 5 | 11400:0 | 30500:5 | n4 |
| 610 | `hb_buffer_set_length` | 1573:7 | True | 5 | 0:11400 | 5:30500 | n4 |
| 611 | `hb_buffer_get_glyph_infos` | 1619:7 | False | 5 | 17100:0 | 45400:5 | n4 |
| 612 | `hb_buffer_diff` | 2201:7 | True | 5 | 0:63 | 5:120 | n4 |
| 613 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 463:38 | True | 5 | 0:1980 | 5:73700 | n4 |
| 614 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 463:44 | True | 5 | 0:1980 | 5:73700 | n4 |
| 615 | `hb-ot-shaper-indic.cc:_ZNK3$_2clIRjjEEDTqulefp_fp0_f...` | 76:55 | False | 5 | 1:0 | 43:5 | n4 |
| 616 | `_ZNK2OT21ItemVarStoreInstancerclEjt` | 3828:8 | False | 5 | 1300:0 | 2780:5 | n4 |
| 617 | `hb-ot-shape-fallback.cc:_ZL32_hb_glyph_info_get_lig_...` | 518:7 | False | 5 | 4:0 | 4:5 | n4 |
| 618 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 565:2 | True | 5 | 0:28 | 5:310 | n4 |
| 619 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 126:12 | False | 5 | 1:0 | 70:5 | n4 |
| 620 | `_Z20find_syllables_indicP11hb_buffer_t` | 1213:2 | True | 5 | 0:2060 | 5:189000 | n4 |
| 621 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 251:24 | True | 5 | 0:8 | 5:4910 | n4 |
| 622 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 251:47 | True | 5 | 0:7 | 5:4230 | n4 |
| 623 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 774:6 | False | 5 | 829:0 | 13100:5 | n4 |
| 624 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1109:5 | True | 5 | 0:4 | 5:1060 | n4 |
| 625 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1447:9 | True | 5 | 0:2 | 5:49 | n4 |
| 626 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 608:2 | True | 5 | 0:354 | 5:50000 | n4 |
| 627 | `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` | 53:7 | True | 5 | 0:223 | 5:2150 | n4 |
| 628 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 249:10 | False | 5 | 30:0 | 985:5 | n4 |
| 629 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 381:5 | True | 5 | 0:8290 | 5:24000 | n4 |
| 630 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCE...` | 480:6 | False | 5 | 7:0 | 45:5 | n4 |
| 631 | `hb_shape_full` | 161:9 | True | 5 | 0:5730 | 5:15100 | n4 |
| 632 | `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` | 234:7 | True | 5 | 0:471 | 5:1250 | n4 |
| 633 | `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10...` | 102:6 | True | 4 | 0:462 | 4:140000 | n4 |
| 634 | `_ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_11...` | 350:45 | False | 4 | 7:0 | 830:4 | n4 |
| 635 | `_ZNK3AAT21SubtableGlyphCoverage8sanitizeEP21hb_sanit...` | 1085:26 | True | 4 | 0:17 | 4:305 | n4 |
| 636 | `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE14collect_glyphsI...` | 700:5 | True | 4 | 0:24 | 4:23 | n4 |
| 637 | `_ZN3AAT33hb_aat_layout_chain_accelerator_t6createINS...` | 251:24 | True | 4 | 0:134 | 4:618 | n4 |
| 638 | `_ZN10hb_array_tI15hb_glyph_info_tE8__next__Ev` | 251:24 | True | 4 | 0:12300 | 4:446000 | n4 |
| 639 | `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_ext...` | 348:7 | True | 4 | 0:6400000 | 4:98500000 | n4 |
| 640 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_pat...` | 348:7 | True | 4 | 0:43600 | 4:8790000 | n4 |
| 641 | `hb_script_get_horizontal_direction` | 605:5 | True | 4 | 0:29700 | 4:79800 | n4 |
| 642 | `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl13LigatureArray...` | 350:45 | False | 4 | 2:0 | 191:4 | n4 |
| 643 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTabl...` | 350:45 | False | 4 | 4:0 | 107:4 | n4 |
| 644 | `_ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE...` | 251:24 | True | 4 | 0:7 | 4:18 | n4 |
| 645 | `_ZNK3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEE...` | 350:45 | False | 4 | 553:0 | 1020:4 | n4 |
| 646 | `_ZNK3CFF8Encoding8sanitizeEP21hb_sanitize_context_t` | 350:45 | False | 4 | 1:0 | 10:4 | n4 |
| 647 | `_ZNK2OT4cff113accelerator_t14get_glyph_nameEjPcj` | 1401:11 | True | 4 | 0:261 | 4:766 | n4 |
| 648 | `_ZNK2OT7DataMap8sanitizeEP21hb_sanitize_context_tPKv` | 350:45 | False | 4 | 7:0 | 18:4 | n4 |
| 649 | `hb-ot-shaper-arabic.cc:_ZL29mongolian_variation_sele...` | 251:24 | True | 4 | 0:91 | 4:825 | n4 |
| 650 | `_Z20find_syllables_indicP11hb_buffer_t` | 1225:2 | True | 4 | 0:2060 | 4:189000 | n4 |
| 651 | `hb-ot-shaper-indic.cc:_ZL22final_reordering_indicPK1...` | 251:24 | True | 4 | 0:112 | 4:1780 | n4 |
| 652 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1150:56 | False | 4 | 2:0 | 1150:4 | n4 |
| 653 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1244:7 | False | 4 | 2:0 | 957:4 | n4 |
| 654 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1274:11 | True | 4 | 0:2 | 4:953 | n4 |
| 655 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1372:27 | False | 4 | 2:0 | 953:4 | n4 |
| 656 | `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_cons...` | 217:12 | True | 4 | 0:27 | 4:3380 | n4 |
| 657 | `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11h...` | 68:39 | False | 4 | 10800:0 | 296000:4 | n4 |
| 658 | `hb-ot-shaper-use.cc:_ZL15data_create_usePK18hb_ot_sh...` | 251:24 | True | 4 | 0:12 | 4:96 | n4 |
| 659 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 705:43 | False | 4 | 141:0 | 30:4 | n4 |
| 660 | `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint...` | 92:7 | True | 4 | 0:116 | 4:64 | n4 |
| 661 | `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint...` | 106:7 | True | 4 | 0:116 | 4:60 | n4 |
| 662 | `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint...` | 117:7 | True | 4 | 0:116 | 4:60 | n4 |
| 663 | `_ZNK21hb_sanitize_context_t11check_rangeIN2OT8Offset...` | 341:5 | False | 4 | 5:0 | 172:4 | n4 |
| 664 | `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1...` | 428:9 | False | 4 | 2:0 | 191:4 | n4 |
| 665 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVARE...` | 474:25 | False | 4 | 59:0 | 232:4 | n4 |
| 666 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVARE...` | 480:6 | False | 4 | 59:0 | 228:4 | n4 |
| 667 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 251:24 | True | 4 | 0:472 | 4:754 | n4 |
| 668 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 251:24 | True | 4 | 0:5980 | 4:7490 | n4 |
| 669 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 539:9 | True | 4 | 0:1930 | 4:2530 | n4 |
| 670 | `_ZN9hb_utf8_t10encode_lenEj` | 135:9 | False | 4 | 1190:0 | 2870:4 | n4 |
| 671 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:24 | True | 4 | 0:739 | 4:1150 | n4 |
| 672 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:47 | True | 4 | 0:739 | 4:1150 | n4 |
| 673 | `_ZN11hb_bounds_tIfE6union_ERKS0_` | 329:16 | False | 4 | 4110:4 | 202:0 | cmplog |
| 674 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 231:5 | True | 4 | 4:233 | 0:991 | cmplog |
| 675 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 269:5 | True | 4 | 4:233 | 0:991 | cmplog |
| 676 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 777:30 | True | 4 | 4:2 | 0:4 | cmplog |
| 677 | `_ZN11hb_vector_tI15contour_point_tLb0EE6extendE10hb_...` | 251:24 | True | 4 | 4:6180 | 0:165000 | cmplog |
| 678 | `_ZNK2OT6Layout9GSUB_impl11SubstLookup10is_reverseEv` | 251:24 | True | 3 | 0:2410 | 3:16900 | n4 |
| 679 | `_ZNK2OT9glyf_impl20CompositeGlyphRecord10get_pointsE...` | 251:24 | True | 3 | 0:3200 | 3:4410 | n4 |
| 680 | `_ZN2OT22hb_ot_name_convert_utfI10hb_ascii_t9hb_utf8_...` | 62:11 | True | 3 | 0:39 | 3:120 | n4 |
| 681 | `_ZNK3AAT19LookupSegmentSingleIN2OT7NumTypeILb1EtLj2E...` | 301:9 | True | 3 | 0:6 | 3:237 | n4 |
| 682 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 746:5 | True | 3 | 0:6 | 3:191 | n4 |
| 683 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE8sanitizeEP21hb_s...` | 1282:11 | False | 3 | 1:0 | 1:3 | n4 |
| 684 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE13compile_flagsEP...` | 1135:11 | True | 3 | 0:370 | 3:1620 | n4 |
| 685 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_a...` | 1173:30 | False | 3 | 416:0 | 2480:3 | n4 |
| 686 | `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_a...` | 1174:32 | False | 3 | 416:0 | 2480:3 | n4 |
| 687 | `hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0...` | 1134:10 | True | 3 | 0:91 | 3:826 | n4 |
| 688 | `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S...` | 1134:10 | True | 3 | 0:1 | 3:68 | n4 |
| 689 | `_ZNK10hb_array_tIKN2OT5IndexEE11__item_at__Ej` | 251:24 | True | 3 | 0:2 | 3:2 | n4 |
| 690 | `_ZN11hb_buffer_t11output_infoERK15hb_glyph_info_t` | 251:24 | True | 3 | 0:18100 | 3:73300 | n4 |
| 691 | `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_pat...` | 348:7 | True | 3 | 0:3800000 | 3:71000000 | n4 |
| 692 | `hb_language_matches` | 443:7 | True | 3 | 0:3 | 3:27 | n4 |
| 693 | `hb_script_get_horizontal_direction` | 588:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 694 | `hb_script_get_horizontal_direction` | 591:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 695 | `hb_script_get_horizontal_direction` | 606:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 696 | `hb_script_get_horizontal_direction` | 607:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 697 | `hb_script_get_horizontal_direction` | 622:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 698 | `hb_script_get_horizontal_direction` | 625:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 699 | `hb_script_get_horizontal_direction` | 626:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 700 | `hb_script_get_horizontal_direction` | 638:5 | True | 3 | 0:29700 | 3:79800 | n4 |
| 701 | `hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_...` | 456:12 | False | 3 | 38:0 | 1440:3 | n4 |
| 702 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 456:12 | True | 3 | 0:130 | 3:573 | n4 |
| 703 | `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zi...` | 456:18 | True | 3 | 0:130 | 3:572 | n4 |
| 704 | `_ZN2OT8OffsetToINS_6Layout6Common8CoverageENS_7NumTy...` | 469:9 | False | 3 | 284:0 | 383:3 | n4 |
| 705 | `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5Sub...` | 51:7 | True | 3 | 0:951 | 3:2110 | n4 |
| 706 | `_ZN3CFF18name_dict_values_t16name_op_to_indexEj` | 722:7 | True | 3 | 0:2120 | 3:4820 | n4 |
| 707 | `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cf...` | 784:7 | True | 3 | 0:13500 | 3:37000 | n4 |
| 708 | `_ZN2OT4cff119accelerator_templ_tIN3CFF25cff1_private...` | 251:47 | True | 3 | 0:563 | 3:768 | n4 |
| 709 | `_ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private...` | 251:47 | True | 3 | 0:232 | 3:949 | n4 |
| 710 | `hb-ot-font.cc:_ZL26hb_ot_get_glyph_v_advancesP9hb_fo...` | 251:24 | True | 3 | 0:1 | 3:258 | n4 |
| 711 | `_ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12Exte...` | 350:45 | False | 3 | 461:0 | 1190:3 | n4 |
| 712 | `_ZN2OT33hb_accelerate_subtables_context_t8dispatchIN...` | 1051:9 | True | 3 | 0:1 | 3:22 | n4 |
| 713 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 52:2 | True | 3 | 0:1 | 3:46 | n4 |
| 714 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 53:2 | True | 3 | 0:1 | 3:46 | n4 |
| 715 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 54:2 | True | 3 | 0:1 | 3:46 | n4 |
| 716 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 55:2 | True | 3 | 0:1 | 3:46 | n4 |
| 717 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 65:2 | True | 3 | 0:1 | 3:46 | n4 |
| 718 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 91:5 | True | 3 | 0:389 | 3:1650 | n4 |
| 719 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 107:5 | True | 3 | 0:389 | 3:1650 | n4 |
| 720 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 113:5 | True | 3 | 0:389 | 3:1650 | n4 |
| 721 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 244:5 | True | 3 | 0:237 | 3:988 | n4 |
| 722 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 259:5 | True | 3 | 0:237 | 3:988 | n4 |
| 723 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 272:5 | True | 3 | 0:237 | 3:988 | n4 |
| 724 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 298:5 | True | 3 | 0:237 | 3:988 | n4 |
| 725 | `_Z22_hb_ot_shape_normalizePK18hb_ot_shape_plan_tP11h...` | 411:5 | False | 3 | 3:0 | 10:3 | n4 |
| 726 | `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_scri...` | 32:5 | True | 3 | 0:140 | 3:582 | n4 |
| 727 | `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_scri...` | 33:5 | True | 3 | 0:140 | 3:582 | n4 |
| 728 | `hb-ot-shaper-arabic.cc:_ZL12joining_typej` | 200:11 | True | 3 | 0:1 | 3:10 | n4 |
| 729 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 107:7 | True | 3 | 0:5 | 3:210 | n4 |
| 730 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 127:4 | True | 3 | 0:1 | 3:72 | n4 |
| 731 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 716:6 | True | 3 | 0:978 | 3:24900 | n4 |
| 732 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1085:11 | False | 3 | 16:0 | 9000:3 | n4 |
| 733 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1087:8 | True | 3 | 0:16 | 3:8960 | n4 |
| 734 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 345:5 | True | 3 | 0:80 | 3:1160 | n4 |
| 735 | `hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_o...` | 330:9 | True | 3 | 0:22 | 3:166 | n4 |
| 736 | `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_cons...` | 280:9 | True | 3 | 0:27 | 3:4610 | n4 |
| 737 | `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` | 78:7 | True | 3 | 0:224 | 3:2200 | n4 |
| 738 | `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` | 55:23 | True | 3 | 0:220 | 3:2150 | n4 |
| 739 | `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` | 57:7 | True | 3 | 0:220 | 3:2140 | n4 |
| 740 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 121:4 | True | 3 | 0:75 | 3:941 | n4 |
| 741 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 144:4 | True | 3 | 0:30 | 3:372 | n4 |
| 742 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 152:4 | True | 3 | 0:30 | 3:372 | n4 |
| 743 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 199:4 | True | 3 | 0:45 | 3:2840 | n4 |
| 744 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 251:4 | True | 3 | 0:30 | 3:987 | n4 |
| 745 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 306:4 | True | 3 | 0:570 | 3:1060 | n4 |
| 746 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 370:4 | True | 3 | 0:15 | 3:117 | n4 |
| 747 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 301:5 | True | 3 | 0:8290 | 3:24000 | n4 |
| 748 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 397:5 | True | 3 | 0:8290 | 3:24000 | n4 |
| 749 | `_ZNK2OT11SegmentMaps9map_floatEfjj` | 188:14 | False | 3 | 381:0 | 1650:3 | n4 |
| 750 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj173581144...` | 755:10 | False | 3 | 141:0 | 31:3 | n4 |
| 751 | `_ZNK2OT4VVAR8sanitizeEP21hb_sanitize_context_t` | 350:45 | False | 3 | 5:0 | 727:3 | n4 |
| 752 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT16Open...` | 474:25 | False | 3 | 1:0 | 37:3 | n4 |
| 753 | `_ZN22hb_serialize_context_t8pop_packEb` | 251:24 | True | 3 | 0:5460 | 3:7840 | n4 |
| 754 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 539:9 | True | 3 | 0:472 | 3:751 | n4 |
| 755 | `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` | 232:7 | True | 3 | 0:471 | 3:1250 | n4 |
| 756 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:24 | True | 3 | 0:473 | 3:793 | n4 |
| 757 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:47 | True | 3 | 0:473 | 3:793 | n4 |
| 758 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:24 | True | 3 | 0:5460 | 3:7840 | n4 |
| 759 | `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_t...` | 251:47 | True | 3 | 0:266 | 3:362 | n4 |
| 760 | `_ZNK2OT3SVG13accelerator_t11paint_glyphEP9hb_font_tj...` | 104:11 | False | 2 | 4:0 | 17:2 | n4 |
| 761 | `_ZNK2OT6Layout6Common8Coverage16collect_coverageI12h...` | 241:5 | True | 2 | 0:1120 | 2:2490 | n4 |
| 762 | `_ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_t...` | 251:24 | True | 2 | 0:8 | 2:3730 | n4 |
| 763 | `_ZNK2OT4VARC13accelerator_t15acquire_scratchEv` | 251:24 | True | 2 | 0:2 | 2:1130 | n4 |
| 764 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13Li...` | 1274:7 | False | 2 | 6:0 | 32:2 | n4 |
| 765 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat...` | 1054:11 | True | 2 | 0:6 | 2:299 | n4 |
| 766 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat...` | 1063:11 | True | 2 | 0:6 | 2:299 | n4 |
| 767 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE23create_accelerato...` | 251:24 | True | 2 | 0:3 | 2:179 | n4 |
| 768 | `hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDS...` | 1204:9 | True | 2 | 0:2 | 2:133 | n4 |
| 769 | `_ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_gl...` | 661:11 | False | 2 | 60:0 | 167:2 | n4 |
| 770 | `hb_script_get_horizontal_direction` | 589:5 | True | 2 | 0:29700 | 2:79800 | n4 |
| 771 | `hb_script_get_horizontal_direction` | 608:5 | True | 2 | 0:29700 | 2:79800 | n4 |
| 772 | `hb_draw_funcs_set_close_path_func` | 148:7 | True | 2 | 0:2 | 2:1050 | n4 |
| 773 | `hb-font.cc:_ZL34hb_font_get_nominal_glyphs_defaultP9...` | 179:30 | False | 2 | 185:0 | 422:2 | n4 |
| 774 | `_ZN11hb_bounds_tIfE9intersectERKS0_` | 342:16 | False | 2 | 2:0 | 12:2 | n4 |
| 775 | `_ZN16hb_lazy_loader_tI15hb_draw_funcs_tN2OT39hb_tran...` | 209:14 | False | 2 | 2:0 | 1050:2 | n4 |
| 776 | `hb-paint-extents.cc:_ZNK3$_2clIRfRKfEEDTqulefp_fp0_f...` | 76:55 | False | 2 | 4:0 | 22:2 | n4 |
| 777 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingl...` | 251:24 | True | 2 | 0:517 | 2:52400 | n4 |
| 778 | `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_EixEi` | 251:24 | True | 2 | 0:1 | 2:10 | n4 |
| 779 | `_ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE...` | 350:45 | False | 2 | 2:0 | 8:2 | n4 |
| 780 | `_ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb...` | 262:9 | True | 2 | 0:2 | 2:133 | n4 |
| 781 | `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5Sub...` | 51:7 | True | 2 | 0:491 | 2:1960 | n4 |
| 782 | `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CF...` | 51:7 | True | 2 | 0:33 | 2:222 | n4 |
| 783 | `_ZNK3CFF8Encoding11suppEncDataEv` | 291:5 | False | 2 | 1:0 | 12:2 | n4 |
| 784 | `_ZNK3CFF8Encoding11suppEncDataEv` | 292:5 | True | 2 | 0:1 | 2:12 | n4 |
| 785 | `_ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_...` | 941:7 | True | 2 | 0:26600 | 2:48300 | n4 |
| 786 | `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_conte...` | 97:5 | True | 2 | 0:2 | 2:90 | n4 |
| 787 | `_ZNK2OT8ClassDef4costEv` | 2209:5 | True | 2 | 0:339 | 2:2080 | n4 |
| 788 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 583:2 | True | 2 | 0:28 | 2:313 | n4 |
| 789 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 595:2 | True | 2 | 0:28 | 2:313 | n4 |
| 790 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 281:11 | False | 2 | 5:0 | 12:2 | n4 |
| 791 | `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_pl...` | 167:26 | True | 2 | 0:52 | 2:358 | n4 |
| 792 | `hb-ot-shaper-arabic.cc:_ZL20reorder_marks_arabicPK18...` | 711:23 | False | 2 | 145:0 | 297:2 | n4 |
| 793 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 86:7 | True | 2 | 0:5 | 2:211 | n4 |
| 794 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 113:7 | True | 2 | 0:5 | 2:211 | n4 |
| 795 | `_Z20find_syllables_indicP11hb_buffer_t` | 1221:2 | True | 2 | 0:2060 | 2:189000 | n4 |
| 796 | `hb-ot-shaper-indic.cc:_ZL24initial_reordering_indicP...` | 155:25 | False | 2 | 119:0 | 1780:2 | n4 |
| 797 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 679:20 | True | 2 | 0:2 | 2:80 | n4 |
| 798 | `hb-ot-shaper-indic.cc:_ZL37initial_reordering_conson...` | 819:6 | False | 2 | 9:0 | 6230:2 | n4 |
| 799 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1105:7 | True | 2 | 0:91 | 2:4010 | n4 |
| 800 | `_Z20find_syllables_khmerP11hb_buffer_t` | 365:2 | True | 2 | 0:8260 | 2:45900 | n4 |
| 801 | `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb...` | 363:11 | False | 2 | 1:0 | 31:2 | n4 |
| 802 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 997:2 | True | 2 | 0:2020 | 2:73800 | n4 |
| 803 | `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_b...` | 437:7 | False | 2 | 1:0 | 1210:2 | n4 |
| 804 | `hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_i...` | 358:3 | False | 2 | 34:0 | 381:2 | n4 |
| 805 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 272:4 | True | 2 | 0:105 | 2:16900 | n4 |
| 806 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 303:32 | True | 2 | 0:570 | 2:1060 | n4 |
| 807 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 400:5 | True | 2 | 0:262 | 2:2370 | n4 |
| 808 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 320:5 | True | 2 | 0:8290 | 2:24000 | n4 |
| 809 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 341:5 | True | 2 | 0:8290 | 2:24000 | n4 |
| 810 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 374:5 | True | 2 | 0:8290 | 2:24000 | n4 |
| 811 | `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EjLj3EEELj119683515...` | 350:45 | False | 2 | 1:0 | 318:2 | n4 |
| 812 | `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint...` | 84:7 | True | 2 | 0:116 | 2:66 | n4 |
| 813 | `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint...` | 91:7 | True | 2 | 0:116 | 2:66 | n4 |
| 814 | `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint...` | 109:7 | True | 2 | 0:116 | 2:62 | n4 |
| 815 | `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint...` | 116:7 | True | 2 | 0:116 | 2:62 | n4 |
| 816 | `_ZN21hb_sanitize_context_t13sanitize_blobIN3AAT4ankr...` | 480:6 | False | 2 | 14:0 | 78:2 | n4 |
| 817 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN3AAT...` | 251:24 | True | 2 | 0:6 | 2:294 | n4 |
| 818 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8...` | 251:24 | True | 2 | 0:4 | 2:109 | n4 |
| 819 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT16Open...` | 480:6 | False | 2 | 1:0 | 35:2 | n4 |
| 820 | `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToIN...` | 539:9 | True | 2 | 0:472 | 2:748 | n4 |
| 821 | `_ZNK11hb_vector_tI12hb_bit_set_tLb0EEixEi` | 251:24 | False | 2 | 43:0 | 73100:2 | n4 |
| 822 | `_ZN11hb_vector_tIfLb0EE5allocEjb` | 251:24 | True | 2 | 0:87 | 2:789 | n4 |
| 823 | `_ZN11hb_vector_tIfLb0EE5allocEjb` | 251:47 | True | 2 | 0:87 | 2:789 | n4 |
| 824 | `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11Mediu...` | 73:12 | True | 2 | 2:64 | 0:82 | cmplog |
| 825 | `hb-face.cc:_ZL15hb_bsearch_implIKN2OT23VariationSele...` | 1206:14 | False | 2 | 28:2 | 68:0 | cmplog |
| 826 | `_ZN17hb_sorted_array_tIKN2OT23VariationSelectorRecor...` | 399:12 | True | 2 | 2:12200 | 0:33100 | cmplog |
| 827 | `_ZNK17hb_sorted_array_tIKN2OT23VariationSelectorReco...` | 414:9 | True | 2 | 2:12200 | 0:33100 | cmplog |
| 828 | `_ZNK2OT16OpenTypeFontFile8sanitizeEP21hb_sanitize_co...` | 520:5 | True | 2 | 2:6130 | 0:16500 | cmplog |
| 829 | `_ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21...` | 251:24 | True | 1 | 0:934 | 1:6280 | n4 |
| 830 | `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_1...` | 128:11 | False | 1 | 18:0 | 280:1 | n4 |
| 831 | `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEP...` | 89:9 | True | 1 | 0:627 | 1:5810 | n4 |
| 832 | `_ZNK3AAT14LookupFormat10IN2OT7NumTypeILb1EtLj2EEEE8s...` | 350:45 | False | 1 | 1:0 | 4:1 | n4 |
| 833 | `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_s...` | 731:5 | True | 1 | 0:64 | 1:298 | n4 |
| 834 | `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_s...` | 735:5 | True | 1 | 0:64 | 1:298 | n4 |
| 835 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13Ligatur...` | 251:47 | False | 1 | 7:0 | 176:1 | n4 |
| 836 | `_ZNK3AAT13LookupFormat8IN2OT7NumTypeILb1EtLj2EEEE23c...` | 251:24 | True | 1 | 0:84 | 1:215 | n4 |
| 837 | `_ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21R...` | 1278:9 | False | 1 | 1:0 | 19400:1 | n4 |
| 838 | `_ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT1...` | 251:24 | True | 1 | 0:18200 | 1:137000 | n4 |
| 839 | `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSub...` | 864:42 | True | 1 | 0:117 | 1:83 | n4 |
| 840 | `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6Ancho...` | 749:5 | True | 1 | 0:6 | 1:193 | n4 |
| 841 | `_ZNK3AAT9KerxTableINS_4kerxEE23create_accelerator_da...` | 251:24 | True | 1 | 0:41 | 1:248 | n4 |
| 842 | `_ZNK3AAT9KerxTableIN2OT7KernAATEE8sanitizeEP21hb_san...` | 251:47 | False | 1 | 10:0 | 138:1 | n4 |
| 843 | `_ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableH...` | 350:45 | False | 1 | 2:0 | 80:1 | n4 |
| 844 | `_ZNK3AAT16LigatureSubtableINS_13ExtendedTypesEE8sani...` | 350:45 | False | 1 | 6:0 | 150:1 | n4 |
| 845 | `_ZNK3AAT17InsertionSubtableINS_13ExtendedTypesEE8san...` | 350:45 | False | 1 | 75:0 | 423:1 | n4 |
| 846 | `_ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_s...` | 1260:11 | False | 1 | 52:0 | 586:1 | n4 |
| 847 | `_ZNK3AAT17InsertionSubtableINS_13ObsoleteTypesEE8san...` | 350:45 | False | 1 | 1:0 | 118:1 | n4 |
| 848 | `hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOrigin...` | 1206:14 | False | 1 | 8:0 | 22:1 | n4 |
| 849 | `hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0...` | 1134:42 | True | 1 | 0:91 | 1:825 | n4 |
| 850 | `hb-ot-shaper-hangul.cc:_ZL12hb_in_rangesIjJjjEEbT_S0...` | 1134:42 | True | 1 | 0:726 | 1:2520 | n4 |
| 851 | `_ZNK17hb_sorted_array_tIKN2OT16VertOriginMetricEE5bf...` | 414:9 | True | 1 | 0:18 | 1:305 | n4 |
| 852 | `_ZN12hb_bit_set_t9add_rangeEjj` | 251:24 | True | 1 | 0:807 | 1:5320 | n4 |
| 853 | `_ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPK...` | 251:24 | True | 1 | 0:18000 | 1:82900 | n4 |
| 854 | `_ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPK...` | 251:47 | True | 1 | 0:18000 | 1:82900 | n4 |
| 855 | `_ZN11hb_buffer_t19merge_clusters_implEjj` | 551:12 | True | 1 | 0:2 | 1:61 | n4 |
| 856 | `_ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_gl...` | 655:25 | False | 1 | 14:0 | 91:1 | n4 |
| 857 | `hb_buffer_diff` | 2193:7 | False | 1 | 63:0 | 124:1 | n4 |
| 858 | `_ZN3CFF12dict_opset_t9parse_bcdERNS_14byte_str_ref_tE` | 251:24 | True | 1 | 0:33 | 1:92 | n4 |
| 859 | `hb_language_matches` | 435:7 | True | 1 | 0:3 | 1:31 | n4 |
| 860 | `hb_language_matches` | 436:7 | True | 1 | 0:3 | 1:30 | n4 |
| 861 | `hb_script_get_horizontal_direction` | 596:5 | True | 1 | 0:29700 | 1:79800 | n4 |
| 862 | `hb-number.cc:_ZL9strtod_rlPKcPS0_` | 224:9 | True | 1 | 0:1 | 1:5 | n4 |
| 863 | `_ZNK2OT14ResourceRecord8sanitizeEP21hb_sanitize_cont...` | 350:45 | False | 1 | 1:0 | 48:1 | n4 |
| 864 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GSUB_impl19S...` | 350:45 | False | 1 | 53000:0 | 78000:1 | n4 |
| 865 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegme...` | 350:45 | False | 1 | 2:0 | 113:1 | n4 |
| 866 | `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegme...` | 251:24 | True | 1 | 0:8 | 1:845 | n4 |
| 867 | `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEENS1_ILb1EjLj4...` | 350:45 | False | 1 | 1:0 | 49:1 | n4 |
| 868 | `_ZNK2OT7ArrayOfINS_21SVGDocumentIndexEntryENS_7NumTy...` | 350:45 | False | 1 | 4:0 | 12:1 | n4 |
| 869 | `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_E16sanitiz...` | 350:45 | False | 1 | 2:0 | 18:1 | n4 |
| 870 | `_ZNK2OT7ArrayOfIN3CFF12SuppEncodingENS_7NumTypeILb1E...` | 350:45 | False | 1 | 1:0 | 10:1 | n4 |
| 871 | `_ZNK2OT7ArrayOfINS_15MathValueRecordENS_7NumTypeILb1...` | 251:24 | False | 1 | 6150:0 | 16500:1 | n4 |
| 872 | `_ZNK3CFF9FDSelect08sanitizeEP21hb_sanitize_context_tj` | 251:24 | True | 1 | 0:13 | 1:27 | n4 |
| 873 | `_ZNK3CFF8FDSelect8sanitizeEP21hb_sanitize_context_tj` | 251:24 | True | 1 | 0:33 | 1:221 | n4 |
| 874 | `_ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_IL...` | 251:24 | True | 1 | 0:17 | 1:254 | n4 |
| 875 | `_ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_IL...` | 251:47 | False | 1 | 17:0 | 254:1 | n4 |
| 876 | `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_8Enc...` | 51:7 | True | 1 | 0:8 | 1:29 | n4 |
| 877 | `_ZNK3CFF7Charset8sanitizeEP21hb_sanitize_context_tPj` | 251:24 | True | 1 | 0:382 | 1:1110 | n4 |
| 878 | `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cf...` | 794:7 | True | 1 | 0:13500 | 1:37000 | n4 |
| 879 | `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12i...` | 881:7 | True | 1 | 0:2890 | 1:4610 | n4 |
| 880 | `_ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_...` | 942:7 | True | 1 | 0:26600 | 1:48300 | n4 |
| 881 | `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_conte...` | 251:24 | True | 1 | 0:2 | 1:92 | n4 |
| 882 | `_ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_...` | 283:7 | True | 1 | 0:16600 | 1:98100 | n4 |
| 883 | `_ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_...` | 285:7 | True | 1 | 0:16600 | 1:98100 | n4 |
| 884 | `_ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private...` | 443:11 | True | 1 | 0:260 | 1:1090 | n4 |
| 885 | `_ZN2OT4cmap13accelerator_tC2EP9hb_face_t` | 2052:2 | True | 1 | 0:9 | 1:76 | n4 |
| 886 | `hb-ot-font.cc:_ZL25hb_ot_get_glyph_v_originsP9hb_fon...` | 251:24 | True | 1 | 0:26 | 1:487 | n4 |
| 887 | `_ZNK2OT13VarRegionAxis8evaluateEi` | 2481:22 | True | 1 | 0:1480 | 1:5640 | n4 |
| 888 | `_ZNK2OT23MathTopAccentAttachment9get_valueEjP9hb_font_t` | 287:9 | False | 1 | 6150:0 | 16500:1 | n4 |
| 889 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 566:2 | True | 1 | 0:28 | 1:314 | n4 |
| 890 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 567:2 | True | 1 | 0:28 | 1:314 | n4 |
| 891 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 568:2 | True | 1 | 0:28 | 1:314 | n4 |
| 892 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 569:2 | True | 1 | 0:28 | 1:314 | n4 |
| 893 | `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan...` | 606:2 | True | 1 | 0:28 | 1:314 | n4 |
| 894 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 46:15 | True | 1 | 0:1 | 1:48 | n4 |
| 895 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 50:2 | True | 1 | 0:1 | 1:48 | n4 |
| 896 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 51:2 | True | 1 | 0:1 | 1:48 | n4 |
| 897 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 60:2 | True | 1 | 0:1 | 1:48 | n4 |
| 898 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 62:2 | True | 1 | 0:1 | 1:48 | n4 |
| 899 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 63:2 | True | 1 | 0:1 | 1:48 | n4 |
| 900 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 64:2 | True | 1 | 0:1 | 1:48 | n4 |
| 901 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 66:2 | True | 1 | 0:1 | 1:48 | n4 |
| 902 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 67:2 | True | 1 | 0:1 | 1:48 | n4 |
| 903 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 71:2 | True | 1 | 0:1 | 1:48 | n4 |
| 904 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 88:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 905 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 89:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 906 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 92:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 907 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 93:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 908 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 94:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 909 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 95:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 910 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 96:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 911 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 136:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 912 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 139:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 913 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 154:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 914 | `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_...` | 157:5 | True | 1 | 0:389 | 1:1650 | n4 |
| 915 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 232:5 | True | 1 | 0:237 | 1:990 | n4 |
| 916 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 243:5 | True | 1 | 0:237 | 1:990 | n4 |
| 917 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 253:5 | True | 1 | 0:237 | 1:990 | n4 |
| 918 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 258:5 | True | 1 | 0:237 | 1:990 | n4 |
| 919 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 278:5 | True | 1 | 0:237 | 1:990 | n4 |
| 920 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 289:5 | True | 1 | 0:237 | 1:990 | n4 |
| 921 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 290:5 | True | 1 | 0:237 | 1:990 | n4 |
| 922 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 299:5 | True | 1 | 0:237 | 1:990 | n4 |
| 923 | `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_pl...` | 173:46 | True | 1 | 0:414 | 1:1990 | n4 |
| 924 | `hb-ot-shaper-arabic.cc:_ZL28arabic_fallback_plan_des...` | 358:11 | False | 1 | 472:0 | 746:1 | n4 |
| 925 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 200:17 | False | 1 | 99:0 | 134:1 | n4 |
| 926 | `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesi...` | 200:17 | False | 1 | 94:0 | 131:1 | n4 |
| 927 | `hb-ot-shaper-arabic.cc:_ZL26arabic_fallback_plan_sha...` | 377:11 | False | 1 | 472:0 | 746:1 | n4 |
| 928 | `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_scri...` | 26:5 | True | 1 | 0:140 | 1:584 | n4 |
| 929 | `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_scri...` | 34:5 | True | 1 | 0:140 | 1:584 | n4 |
| 930 | `hb-ot-shaper-arabic.cc:_ZL12joining_typej` | 205:11 | True | 1 | 0:25 | 1:151 | n4 |
| 931 | `hb-ot-shaper-arabic.cc:_ZL12joining_typej` | 212:11 | True | 1 | 0:2 | 1:23 | n4 |
| 932 | `hb-ot-shaper-hangul.cc:_ZL18data_create_hangulPK18hb...` | 251:24 | True | 1 | 0:45 | 1:158 | n4 |
| 933 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 317:4 | False | 1 | 7:0 | 36:1 | n4 |
| 934 | `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK...` | 377:23 | False | 1 | 6:0 | 23:1 | n4 |
| 935 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 92:7 | True | 1 | 0:5 | 1:212 | n4 |
| 936 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 101:7 | True | 1 | 0:5 | 1:212 | n4 |
| 937 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 131:4 | True | 1 | 0:1 | 1:74 | n4 |
| 938 | `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_...` | 135:4 | True | 1 | 0:1 | 1:74 | n4 |
| 939 | `_Z20find_syllables_indicP11hb_buffer_t` | 1151:7 | True | 1 | 0:119 | 1:1790 | n4 |
| 940 | `_Z23hb_indic_get_categoriesj` | 251:24 | True | 1 | 0:25 | 1:694 | n4 |
| 941 | `_Z23hb_indic_get_categoriesj` | 489:11 | True | 1 | 0:12 | 1:973 | n4 |
| 942 | `_Z23hb_indic_get_categoriesj` | 501:11 | True | 1 | 0:3 | 1:13 | n4 |
| 943 | `_Z23hb_indic_get_categoriesj` | 502:11 | True | 1 | 0:3 | 1:12 | n4 |
| 944 | `_Z23hb_indic_get_categoriesj` | 511:11 | True | 1 | 0:4 | 1:20 | n4 |
| 945 | `hb-ot-shaper-indic.cc:_ZL21setup_syllables_indicPK18...` | 155:25 | False | 1 | 119:0 | 1790:1 | n4 |
| 946 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1160:11 | True | 1 | 0:2 | 1:1150 | n4 |
| 947 | `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable...` | 1290:40 | False | 1 | 2:0 | 16800:1 | n4 |
| 948 | `hb-ot-shaper-indic.cc:_ZL15decompose_indicPK31hb_ot_...` | 1522:5 | True | 1 | 0:1970 | 1:29800 | n4 |
| 949 | `hb-ot-shaper-indic.cc:_ZL13compose_indicPK31hb_ot_sh...` | 1553:7 | True | 1 | 0:85 | 1:3150 | n4 |
| 950 | `_Z20find_syllables_khmerP11hb_buffer_t` | 319:7 | True | 1 | 0:5 | 1:72 | n4 |
| 951 | `_Z20find_syllables_khmerP11hb_buffer_t` | 369:2 | True | 1 | 0:8260 | 1:45900 | n4 |
| 952 | `hb-ot-shaper-khmer.cc:_ZL21setup_syllables_khmerPK18...` | 155:25 | False | 1 | 5:0 | 72:1 | n4 |
| 953 | `hb-ot-shaper-khmer.cc:_ZL13reorder_khmerPK18hb_ot_sh...` | 155:25 | False | 1 | 5:0 | 72:1 | n4 |
| 954 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 344:5 | True | 1 | 0:80 | 1:1160 | n4 |
| 955 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 346:5 | True | 1 | 0:80 | 1:1160 | n4 |
| 956 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 347:5 | True | 1 | 0:80 | 1:1160 | n4 |
| 957 | `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_...` | 348:5 | True | 1 | 0:80 | 1:1160 | n4 |
| 958 | `_Z22find_syllables_myanmarP11hb_buffer_t` | 574:7 | True | 1 | 0:22 | 1:168 | n4 |
| 959 | `hb-ot-shaper-myanmar.cc:_ZL23setup_syllables_myanmar...` | 155:25 | False | 1 | 22:0 | 168:1 | n4 |
| 960 | `hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_o...` | 155:25 | False | 1 | 22:0 | 168:1 | n4 |
| 961 | `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb...` | 370:47 | False | 1 | 14:0 | 137:1 | n4 |
| 962 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 951:7 | True | 1 | 0:130 | 1:572 | n4 |
| 963 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1005:2 | True | 1 | 0:2020 | 1:73800 | n4 |
| 964 | `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buf...` | 1053:2 | True | 1 | 0:2020 | 1:73800 | n4 |
| 965 | `hb-ot-shaper-use.cc:_ZL19setup_syllables_usePK18hb_o...` | 155:25 | False | 1 | 130:0 | 572:1 | n4 |
| 966 | `hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_sh...` | 155:25 | False | 1 | 130:0 | 572:1 | n4 |
| 967 | `hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_...` | 155:25 | False | 1 | 130:0 | 572:1 | n4 |
| 968 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 118:4 | True | 1 | 0:75 | 1:943 | n4 |
| 969 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 126:6 | True | 1 | 0:75 | 1:943 | n4 |
| 970 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 136:4 | True | 1 | 0:30 | 1:374 | n4 |
| 971 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 170:10 | False | 1 | 15:0 | 134:1 | n4 |
| 972 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 172:4 | True | 1 | 0:15 | 1:134 | n4 |
| 973 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 199:18 | True | 1 | 0:45 | 1:2840 | n4 |
| 974 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 212:6 | True | 1 | 0:15 | 1:164 | n4 |
| 975 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 228:4 | True | 1 | 0:540 | 1:1730 | n4 |
| 976 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 236:4 | True | 1 | 0:540 | 1:1730 | n4 |
| 977 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 236:18 | True | 1 | 0:540 | 1:1730 | n4 |
| 978 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 251:18 | True | 1 | 0:30 | 1:989 | n4 |
| 979 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 254:4 | True | 1 | 0:30 | 1:989 | n4 |
| 980 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 269:4 | True | 1 | 0:105 | 1:16900 | n4 |
| 981 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 275:4 | True | 1 | 0:105 | 1:16900 | n4 |
| 982 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 295:4 | True | 1 | 0:570 | 1:1060 | n4 |
| 983 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 303:4 | True | 1 | 0:570 | 1:1060 | n4 |
| 984 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 303:18 | True | 1 | 0:570 | 1:1060 | n4 |
| 985 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 333:4 | True | 1 | 0:15 | 1:329 | n4 |
| 986 | `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_s...` | 460:4 | True | 1 | 0:15 | 1:179 | n4 |
| 987 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 307:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 988 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 331:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 989 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 335:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 990 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 339:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 991 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 340:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 992 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 345:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 993 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 355:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 994 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 362:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 995 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 368:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 996 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 369:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 997 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 370:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 998 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 371:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 999 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 377:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1000 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 380:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1001 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 384:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1002 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 387:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1003 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 388:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1004 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 394:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1005 | `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_scri...` | 395:5 | True | 1 | 0:8290 | 1:24000 | n4 |
| 1006 | `_ZNK2OT11SegmentMaps9map_floatEfjj` | 176:67 | True | 1 | 0:356 | 1:1650 | n4 |
| 1007 | `_ZNK2OT4VORG12get_y_originEj` | 68:9 | False | 1 | 18:0 | 305:1 | n4 |
| 1008 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4sbixE...` | 474:25 | False | 1 | 7:0 | 24:1 | n4 |
| 1009 | `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT7...` | 251:24 | True | 1 | 0:2 | 1:9 | n4 |
| 1010 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4MATHE...` | 480:6 | False | 1 | 182:0 | 241:1 | n4 |
| 1011 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4avarE...` | 474:25 | False | 1 | 17:0 | 35:1 | n4 |
| 1012 | `_ZNK22hb_serialize_context_t10copy_bytesEv` | 251:24 | True | 1 | 0:472 | 1:747 | n4 |
| 1013 | `hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj` | 91:45 | True | 1 | 0:1 | 1:32 | n4 |
| 1014 | `hb-unicode.cc:_ZL34_hb_emoji_is_Extended_Pictographicj` | 71:10 | False | 1 | 5:0 | 299:1 | n4 |
| 1015 | `_ZN18hb_unicode_funcs_t24modified_combining_classEj` | 251:24 | True | 1 | 0:2009 | 1:12100 | n4 |
| 1016 | `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` | 239:7 | True | 1 | 0:471 | 1:1250 | n4 |
| 1017 | `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_bas...` | 487:9 | True | 1 | 0:260 | 1:1090 | n4 |
| 1018 | `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_bas...` | 251:24 | True | 1 | 0:251 | 1:903 | n4 |
| 1019 | `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_bas...` | 251:47 | True | 1 | 0:251 | 1:903 | n4 |
| 1020 | `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_bas...` | 250:22 | False | 1 | 251:0 | 903:1 | n4 |
| 1021 | `_ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GPOS_impl17P...` | 350:45 | False | 1 | 14000:1 | 23100:0 | cmplog |
| 1022 | `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_...` | 233:11 | False | 1 | 3:1 | 1:0 | cmplog |
| 1023 | `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4STATE...` | 251:24 | False | 1 | 20:1 | 26:0 | cmplog |

## Detail Listings

### 1. `hb-ot-layout.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t` @ 518:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9,040, n4: 26,200)
- **Flip strength**: 2,550,000 (blocked side hit 2,550,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9,040  F:0
- **n4 coverage**: T:26,200  F:2,550,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t_518_7_T` — cmplog:9,040  n4:26,200
  - `harfbuzz_hb-ot-layout.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t_518_7_F` — cmplog:0  n4:2,550,000

### 2. `hb-ot-font.cc:_ZNK4$_33clIR10hb_array_tIKiERK4$_18S7_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELPv0EEEbOS9_OT0_OT1_` @ 992:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 663, n4: 3,640)
- **Flip strength**: 1,600,000 (blocked side hit 1,600,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:663  F:0
- **n4 coverage**: T:3,640  F:1,600,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZNK4$_33clIR10hb_array_tIKiERK4$_18S7_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELPv0EEEbOS9_OT0_OT1__992_11_T` — cmplog:663  n4:3,640
  - `harfbuzz_hb-ot-font.cc:_ZNK4$_33clIR10hb_array_tIKiERK4$_18S7_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELPv0EEEbOS9_OT0_OT1__992_11_F` — cmplog:0  n4:1,600,000

### 3. `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5_` @ 700:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 144,000)
- **Flip strength**: 739,000 (blocked side hit 739,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:739,000  F:144,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__700_14_T` — cmplog:0  n4:739,000
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__700_14_F` — cmplog:28  n4:144,000

### 4. `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE` @ 347:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 14, n4: 724,000)
- **Flip strength**: 627,000 (blocked side hit 627,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14  F:0
- **n4 coverage**: T:724,000  F:627,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_347_7_T` — cmplog:14  n4:724,000
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_347_7_F` — cmplog:0  n4:627,000

### 5. `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5_` @ 700:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 17, n4: 108,000)
- **Flip strength**: 554,000 (blocked side hit 554,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:17
- **n4 coverage**: T:554,000  F:108,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__700_14_T` — cmplog:0  n4:554,000
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__700_14_F` — cmplog:17  n4:108,000

### 6. `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj` @ 1528:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 68, n4: 35,100)
- **Flip strength**: 520,000 (blocked side hit 520,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:68  F:0
- **n4 coverage**: T:35,100  F:520,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1528_11_T` — cmplog:68  n4:35,100
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1528_11_F` — cmplog:0  n4:520,000

### 7. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1262:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 66, n4: 583)
- **Flip strength**: 351,000 (blocked side hit 351,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:66  F:0
- **n4 coverage**: T:583  F:351,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1262_11_T` — cmplog:66  n4:583
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1262_11_F` — cmplog:0  n4:351,000

### 8. `_ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE` @ 497:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 66, n4: 583)
- **Flip strength**: 351,000 (blocked side hit 351,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:66
- **n4 coverage**: T:351,000  F:583
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE_497_11_T` — cmplog:0  n4:351,000
  - `harfbuzz__ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE_497_11_F` — cmplog:66  n4:583

### 9. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1298:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 60, n4: 1,370)
- **Flip strength**: 350,000 (blocked side hit 350,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:60  F:0
- **n4 coverage**: T:1,370  F:350,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1298_11_T` — cmplog:60  n4:1,370
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1298_11_F` — cmplog:0  n4:350,000

### 10. `_Z20find_syllables_khmerP11hb_buffer_t` @ 341:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 45,900)
- **Flip strength**: 209,000 (blocked side hit 209,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:209,000  F:45,900
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_341_7_T` — cmplog:0  n4:209,000
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_341_7_F` — cmplog:8,260  n4:45,900

### 11. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1287:60
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 59)
- **Flip strength**: 195,000 (blocked side hit 195,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:195,000  F:59
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_60_T` — cmplog:0  n4:195,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_60_F` — cmplog:2  n4:59

### 12. `_ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE` @ 490:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 77,800)
- **Flip strength**: 194,000 (blocked side hit 194,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:194,000  F:77,800
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE_490_6_T` — cmplog:0  n4:194,000
  - `harfbuzz__ZN3AAT16LigatureSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_NS_13LigatureEntryILb1EE9EntryDataENS2_5FlagsEEERKNS_5EntryIS9_EE_490_6_F` — cmplog:6  n4:77,800

### 13. `_ZN2OT6Layout9GPOS_impl9PosLookup21dispatch_recurse_funcINS_21hb_ot_apply_context_tEEENT_8return_tEPS5_j` @ 68:18
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 28,000, n4: 102,000)
- **Flip strength**: 165,000 (blocked side hit 165,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:28,000  F:0
- **n4 coverage**: T:102,000  F:165,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GPOS_impl9PosLookup21dispatch_recurse_funcINS_21hb_ot_apply_context_tEEENT_8return_tEPS5_j_68_18_T` — cmplog:28,000  n4:102,000
  - `harfbuzz__ZN2OT6Layout9GPOS_impl9PosLookup21dispatch_recurse_funcINS_21hb_ot_apply_context_tEEENT_8return_tEPS5_j_68_18_F` — cmplog:0  n4:165,000

### 14. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1287:32
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 195,000)
- **Flip strength**: 155,000 (blocked side hit 155,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:195,000  F:155,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_32_T` — cmplog:2  n4:195,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_32_F` — cmplog:0  n4:155,000

### 15. `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE` @ 370:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 8, n4: 334,000)
- **Flip strength**: 150,000 (blocked side hit 150,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:0
- **n4 coverage**: T:334,000  F:150,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_370_11_T` — cmplog:8  n4:334,000
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_370_11_F` — cmplog:0  n4:150,000

### 16. `_ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj` @ 438:3
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 551,000, n4: 5,860,000)
- **Flip strength**: 147,000 (blocked side hit 147,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:551,000
- **n4 coverage**: T:147,000  F:5,860,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj_438_3_T` — cmplog:0  n4:147,000
  - `harfbuzz__ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj_438_3_F` — cmplog:551,000  n4:5,860,000

### 17. `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5_` @ 724:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 25,800)
- **Flip strength**: 138,000 (blocked side hit 138,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:138,000  F:25,800
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__724_14_T` — cmplog:0  n4:138,000
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__724_14_F` — cmplog:36  n4:25,800

### 18. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1268:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 95, n4: 1,210)
- **Flip strength**: 126,000 (blocked side hit 126,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:95
- **n4 coverage**: T:126,000  F:1,210
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1268_19_T` — cmplog:0  n4:126,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1268_19_F` — cmplog:95  n4:1,210

### 19. `_ZN12hb_extents_tIfE6union_ERKS0_` @ 49:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4,110, n4: 33,900)
- **Flip strength**: 116,000 (blocked side hit 116,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4,110
- **n4 coverage**: T:116,000  F:33,900
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_extents_tIfE6union_ERKS0__49_9_T` — cmplog:0  n4:116,000
  - `harfbuzz__ZN12hb_extents_tIfE6union_ERKS0__49_9_F` — cmplog:4,110  n4:33,900

### 20. `_ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5_` @ 718:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 30,100)
- **Flip strength**: 114,000 (blocked side hit 114,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:114,000  F:30,100
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__718_11_T` — cmplog:0  n4:114,000
  - `harfbuzz__ZN3CFF12path_procs_tI25cff2_path_procs_extents_tNS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_extents_param_tE9hvcurvetoERS4_RS5__718_11_F` — cmplog:28  n4:30,100

### 21. `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5_` @ 724:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 19,300)
- **Flip strength**: 103,000 (blocked side hit 103,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:103,000  F:19,300
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__724_14_T` — cmplog:0  n4:103,000
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__724_14_F` — cmplog:13  n4:19,300

### 22. `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE` @ 358:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 143,000)
- **Flip strength**: 97,000 (blocked side hit 97,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:143,000  F:97,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_358_47_T` — cmplog:6  n4:143,000
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_358_47_F` — cmplog:0  n4:97,000

### 23. `hb-ot-layout.cc:_ZNK3$_0clIjjEEDTqugefp_fp0_fp_fp0_EOT_OT0_` @ 76:55
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 490, n4: 21,500)
- **Flip strength**: 92,700 (blocked side hit 92,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:490
- **n4 coverage**: T:92,700  F:21,500
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZNK3$_0clIjjEEDTqugefp_fp0_fp_fp0_EOT_OT0__76_55_T` — cmplog:0  n4:92,700
  - `harfbuzz_hb-ot-layout.cc:_ZNK3$_0clIjjEEDTqugefp_fp0_fp_fp0_EOT_OT0__76_55_F` — cmplog:490  n4:21,500

### 24. `_ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5_` @ 718:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 17, n4: 22,400)
- **Flip strength**: 85,800 (blocked side hit 85,800× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:17
- **n4 coverage**: T:85,800  F:22,400
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__718_11_T` — cmplog:0  n4:85,800
  - `harfbuzz__ZN3CFF12path_procs_tI22cff2_path_procs_path_tNS_20cff2_cs_interp_env_tINS_8number_tEEE17cff2_path_param_tE9hvcurvetoERS4_RS5__718_11_F` — cmplog:17  n4:22,400

### 25. `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE` @ 360:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 166,000)
- **Flip strength**: 74,200 (blocked side hit 74,200× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:74,200  F:166,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_360_11_T` — cmplog:0  n4:74,200
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_360_11_F` — cmplog:6  n4:166,000

### 26. `_ZNK14hb_transform_tIfE11is_identityEv` @ 120:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 177,000)
- **Flip strength**: 62,700 (blocked side hit 62,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:177,000  F:62,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_120_12_T` — cmplog:6  n4:177,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_120_12_F` — cmplog:0  n4:62,700

### 27. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataENS4_5FlagsEE5driveINS4_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1262:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 166,000)
- **Flip strength**: 55,400 (blocked side hit 55,400× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:55,400  F:166,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataENS4_5FlagsEE5driveINS4_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1262_11_T` — cmplog:0  n4:55,400
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataENS4_5FlagsEE5driveINS4_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1262_11_F` — cmplog:110,000  n4:166,000

### 28. `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE` @ 557:23
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 55,300 (blocked side hit 55,300× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:110,000  F:0
- **n4 coverage**: T:111,000  F:55,300
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_557_23_T` — cmplog:110,000  n4:111,000
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_557_23_F` — cmplog:0  n4:55,300

### 29. `_ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT_` @ 176:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,200, n4: 92,700)
- **Flip strength**: 44,500 (blocked side hit 44,500× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,200
- **n4 coverage**: T:44,500  F:92,700
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT__176_11_T` — cmplog:0  n4:44,500
  - `harfbuzz__ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT__176_11_F` — cmplog:18,200  n4:92,700

### 30. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3526:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 490, n4: 57,000)
- **Flip strength**: 41,000 (blocked side hit 41,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:490  F:0
- **n4 coverage**: T:57,000  F:41,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3526_8_T` — cmplog:490  n4:57,000
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3526_8_F` — cmplog:0  n4:41,000

### 31. `_ZNK14hb_transform_tIfE11is_identityEv` @ 122:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 149,000)
- **Flip strength**: 27,700 (blocked side hit 27,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:149,000  F:27,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_122_5_T` — cmplog:6  n4:149,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_122_5_F` — cmplog:0  n4:27,700

### 32. `_ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEE23determine_hintmask_sizeEv` @ 178:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 30, n4: 318)
- **Flip strength**: 24,200 (blocked side hit 24,200× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:30  F:0
- **n4 coverage**: T:318  F:24,200
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEE23determine_hintmask_sizeEv_178_9_T` — cmplog:30  n4:318
  - `harfbuzz__ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEE23determine_hintmask_sizeEv_178_9_F` — cmplog:0  n4:24,200

### 33. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3511:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 490, n4: 100,000)
- **Flip strength**: 13,700 (blocked side hit 13,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:490  F:0
- **n4 coverage**: T:100,000  F:13,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3511_11_T` — cmplog:490  n4:100,000
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3511_11_F` — cmplog:0  n4:13,700

### 34. `_ZNK2OT18glyf_accelerator_t11get_path_atEP9hb_font_tjR17hb_draw_session_t10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE` @ 514:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 228,000)
- **Flip strength**: 12,200 (blocked side hit 12,200× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:12,200  F:228,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT18glyf_accelerator_t11get_path_atEP9hb_font_tjR17hb_draw_session_t10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE_514_9_T` — cmplog:0  n4:12,200
  - `harfbuzz__ZNK2OT18glyf_accelerator_t11get_path_atEP9hb_font_tjR17hb_draw_session_t10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE_514_9_F` — cmplog:6  n4:228,000

### 35. `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj` @ 104:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 462, n4: 128,000)
- **Flip strength**: 12,000 (blocked side hit 12,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:462
- **n4 coverage**: T:12,000  F:128,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_104_6_T` — cmplog:0  n4:12,000
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_104_6_F` — cmplog:462  n4:128,000

### 36. `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj` @ 436:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 1,210)
- **Flip strength**: 12,000 (blocked side hit 12,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:1,210  F:12,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_436_7_T` — cmplog:1  n4:1,210
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_436_7_F` — cmplog:0  n4:12,000

### 37. `_ZNK2OT6Layout9GPOS_impl9MarkArray5applyEPNS_21hb_ot_apply_context_tEjjRKNS1_12AnchorMatrixEjj` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 2,400)
- **Flip strength**: 10,700 (blocked side hit 10,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:2,400  F:10,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl9MarkArray5applyEPNS_21hb_ot_apply_context_tEjjRKNS1_12AnchorMatrixEjj_251_24_T` — cmplog:4  n4:2,400
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl9MarkArray5applyEPNS_21hb_ot_apply_context_tEjjRKNS1_12AnchorMatrixEjj_251_24_F` — cmplog:0  n4:10,700

### 38. `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE14get_glyph_dataEv` @ 641:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 145,000, n4: 1,480,000)
- **Flip strength**: 10,300 (blocked side hit 10,300× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:145,000
- **n4 coverage**: T:10,300  F:1,480,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE14get_glyph_dataEv_641_9_T` — cmplog:0  n4:10,300
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE14get_glyph_dataEv_641_9_F` — cmplog:145,000  n4:1,480,000

### 39. `_Z20find_syllables_indicP11hb_buffer_t` @ 1167:3
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 163, n4: 526,000)
- **Flip strength**: 10,300 (blocked side hit 10,300× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:163  F:0
- **n4 coverage**: T:526,000  F:10,300
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1167_3_T` — cmplog:163  n4:526,000
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1167_3_F` — cmplog:0  n4:10,300

### 40. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3528:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 490, n4: 47,400)
- **Flip strength**: 9,640 (blocked side hit 9,640× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:490
- **n4 coverage**: T:9,640  F:47,400
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3528_10_T` — cmplog:0  n4:9,640
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3528_10_F` — cmplog:490  n4:47,400

### 41. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 12,900)
- **Flip strength**: 8,830 (blocked side hit 8,830× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:8,830  F:12,900
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_T` — cmplog:0  n4:8,830
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_F` — cmplog:4  n4:12,900

### 42. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 268, n4: 46,600)
- **Flip strength**: 8,730 (blocked side hit 8,730× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:268
- **n4 coverage**: T:8,730  F:46,600
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_251_24_T` — cmplog:0  n4:8,730
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_251_24_F` — cmplog:268  n4:46,600

### 43. `hb-ot-layout.cc:_ZN10hb_apply_tIZNK2OT6Layout9GSUB_impl11LigatureSetINS1_11MediumTypesEE15collect_secondsI15hb_set_digest_tEEvRT_EUlRKNS2_8LigatureIS4_EEE_EclI13hb_map_iter_tI10hb_array_tIKNS0_8OffsetToISB_NS0_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKS5_EL24hb_function_sortedness_t0ELPv0EETnPN12hb_enable_ifIXsr17hb_is_iterator_ofIS8_NS8_6item_tEEE5valueEvE4typeELSX_0EEEvS8_` @ 693:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 204, n4: 2,260)
- **Flip strength**: 8,119 (blocked side hit 8,119× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:204
- **n4 coverage**: T:8,119  F:2,260
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN10hb_apply_tIZNK2OT6Layout9GSUB_impl11LigatureSetINS1_11MediumTypesEE15collect_secondsI15hb_set_digest_tEEvRT_EUlRKNS2_8LigatureIS4_EEE_EclI13hb_map_iter_tI10hb_array_tIKNS0_8OffsetToISB_NS0_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKS5_EL24hb_function_sortedness_t0ELPv0EETnPN12hb_enable_ifIXsr17hb_is_iterator_ofIS8_NS8_6item_tEEE5valueEvE4typeELSX_0EEEvS8__693_12_T` — cmplog:0  n4:8,119
  - `harfbuzz_hb-ot-layout.cc:_ZN10hb_apply_tIZNK2OT6Layout9GSUB_impl11LigatureSetINS1_11MediumTypesEE15collect_secondsI15hb_set_digest_tEEvRT_EUlRKNS2_8LigatureIS4_EEE_EclI13hb_map_iter_tI10hb_array_tIKNS0_8OffsetToISB_NS0_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKS5_EL24hb_function_sortedness_t0ELPv0EETnPN12hb_enable_ifIXsr17hb_is_iterator_ofIS8_NS8_6item_tEEE5valueEvE4typeELSX_0EEEvS8__693_12_F` — cmplog:204  n4:2,260

### 44. `_ZNK2OT7ArrayOfINS_6Layout9GPOS_impl15EntryExitRecordENS_7NumTypeILb1EtLj2EEEEixEi` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 1,820)
- **Flip strength**: 7,660 (blocked side hit 7,660× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:1,820  F:7,660
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_6Layout9GPOS_impl15EntryExitRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_T` — cmplog:3  n4:1,820
  - `harfbuzz__ZNK2OT7ArrayOfINS_6Layout9GPOS_impl15EntryExitRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_F` — cmplog:0  n4:7,660

### 45. `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE18advance_glyph_dataEv` @ 652:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 144,000, n4: 1,300,000)
- **Flip strength**: 7,380 (blocked side hit 7,380× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:144,000
- **n4 coverage**: T:7,380  F:1,300,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE18advance_glyph_dataEv_652_9_T` — cmplog:0  n4:7,380
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE18advance_glyph_dataEv_652_9_F` — cmplog:144,000  n4:1,300,000

### 46. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1090:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 688)
- **Flip strength**: 7,200 (blocked side hit 7,200× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:7,200  F:688
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1090_11_T` — cmplog:0  n4:7,200
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1090_11_F` — cmplog:3  n4:688

### 47. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1092:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 688)
- **Flip strength**: 7,200 (blocked side hit 7,200× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:7,200  F:688
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1092_8_T` — cmplog:0  n4:7,200
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1092_8_F` — cmplog:3  n4:688

### 48. `_ZNK14hb_transform_tIfE11is_identityEv` @ 122:16
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 143,000)
- **Flip strength**: 6,440 (blocked side hit 6,440× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:143,000  F:6,440
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_122_16_T` — cmplog:6  n4:143,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_122_16_F` — cmplog:0  n4:6,440

### 49. `hb-ot-layout.cc:_ZL14apply_backwardPN2OT21hb_ot_apply_context_tERKNS_33hb_ot_layout_lookup_accelerator_tE` @ 1952:2
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,170, n4: 249,000)
- **Flip strength**: 5,260 (blocked side hit 5,260× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,170  F:0
- **n4 coverage**: T:249,000  F:5,260
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZL14apply_backwardPN2OT21hb_ot_apply_context_tERKNS_33hb_ot_layout_lookup_accelerator_tE_1952_2_T` — cmplog:2,170  n4:249,000
  - `harfbuzz_hb-ot-layout.cc:_ZL14apply_backwardPN2OT21hb_ot_apply_context_tERKNS_33hb_ot_layout_lookup_accelerator_tE_1952_2_F` — cmplog:0  n4:5,260

### 50. `_ZNK2OT6Layout9GSUB_impl11SubstLookup11would_applyEPNS_24hb_would_apply_context_tEPKNS_33hb_ot_layout_lookup_accelerator_tE` @ 97:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 20, n4: 24,100)
- **Flip strength**: 5,170 (blocked side hit 5,170× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:0
- **n4 coverage**: T:24,100  F:5,170
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SubstLookup11would_applyEPNS_24hb_would_apply_context_tEPKNS_33hb_ot_layout_lookup_accelerator_tE_97_9_T` — cmplog:20  n4:24,100
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SubstLookup11would_applyEPNS_24hb_would_apply_context_tEPKNS_33hb_ot_layout_lookup_accelerator_tE_97_9_F` — cmplog:0  n4:5,170

### 51. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 967:3
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,100, n4: 74,200)
- **Flip strength**: 4,740 (blocked side hit 4,740× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,100  F:0
- **n4 coverage**: T:74,200  F:4,740
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_967_3_T` — cmplog:2,100  n4:74,200
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_967_3_F` — cmplog:0  n4:4,740

### 52. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3519:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 466, n4: 90,700)
- **Flip strength**: 4,550 (blocked side hit 4,550× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:466
- **n4 coverage**: T:4,550  F:90,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3519_7_T` — cmplog:0  n4:4,550
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3519_7_F` — cmplog:466  n4:90,700

### 53. `_ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE` @ 344:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 14, n4: 1,340,000)
- **Flip strength**: 4,480 (blocked side hit 4,480× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:14
- **n4 coverage**: T:4,480  F:1,340,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_344_18_T` — cmplog:0  n4:4,480
  - `harfbuzz__ZNK2OT4VARC11get_path_atERKNS_17hb_varc_context_tEj10hb_array_tIKiE14hb_transform_tIfEjPNS_17hb_scalar_cache_tE_344_18_F` — cmplog:14  n4:1,340,000

### 54. `_ZNK2OT6Layout9GPOS_impl17CursivePosFormat15applyEPNS_21hb_ot_apply_context_tE` @ 129:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 1,950)
- **Flip strength**: 3,980 (blocked side hit 3,980× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:1,950  F:3,980
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl17CursivePosFormat15applyEPNS_21hb_ot_apply_context_tE_129_9_T` — cmplog:3  n4:1,950
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl17CursivePosFormat15applyEPNS_21hb_ot_apply_context_tE_129_9_F` — cmplog:0  n4:3,980

### 55. `hb-ot-layout.cc:_ZL22_hb_glyph_info_is_zwnjPK15hb_glyph_info_t` @ 406:53
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10,300, n4: 121,000)
- **Flip strength**: 3,640 (blocked side hit 3,640× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10,300
- **n4 coverage**: T:3,640  F:121,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZL22_hb_glyph_info_is_zwnjPK15hb_glyph_info_t_406_53_T` — cmplog:0  n4:3,640
  - `harfbuzz_hb-ot-layout.cc:_ZL22_hb_glyph_info_is_zwnjPK15hb_glyph_info_t_406_53_F` — cmplog:10,300  n4:121,000

### 56. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3515:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 490, n4: 18,400)
- **Flip strength**: 3,610 (blocked side hit 3,610× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:490  F:0
- **n4 coverage**: T:18,400  F:3,610
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3515_6_T` — cmplog:490  n4:18,400
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3515_6_F` — cmplog:0  n4:3,610

### 57. `_Z20find_syllables_indicP11hb_buffer_t` @ 1241:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 96, n4: 1,230)
- **Flip strength**: 3,460 (blocked side hit 3,460× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:96
- **n4 coverage**: T:3,460  F:1,230
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1241_2_T` — cmplog:0  n4:3,460
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1241_2_F` — cmplog:96  n4:1,230

### 58. `_ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE` @ 149:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 250, n4: 4,830)
- **Flip strength**: 3,210 (blocked side hit 3,210× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:250
- **n4 coverage**: T:3,210  F:4,830
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE_149_11_T` — cmplog:0  n4:3,210
  - `harfbuzz__ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE_149_11_F` — cmplog:250  n4:4,830

### 59. `hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj` @ 74:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,810, n4: 104,000)
- **Flip strength**: 3,120 (blocked side hit 3,120× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,810  F:0
- **n4 coverage**: T:104,000  F:3,120
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj_74_25_T` — cmplog:2,810  n4:104,000
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj_74_25_F` — cmplog:0  n4:3,120

### 60. `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 2700:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 603)
- **Flip strength**: 3,040 (blocked side hit 3,040× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:3,040  F:603
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2700_9_T` — cmplog:0  n4:3,040
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2700_9_F` — cmplog:36  n4:603

### 61. `_Z20find_syllables_indicP11hb_buffer_t` @ 1197:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 186,000)
- **Flip strength**: 2,820 (blocked side hit 2,820× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:2,820  F:186,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1197_2_T` — cmplog:0  n4:2,820
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1197_2_F` — cmplog:2,060  n4:186,000

### 62. `hb-ot-shaper-indic.cc:_ZL33initial_reordering_syllable_indicPK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 980:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,900, n4: 168,000)
- **Flip strength**: 2,820 (blocked side hit 2,820× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,900
- **n4 coverage**: T:2,820  F:168,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL33initial_reordering_syllable_indicPK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_980_5_T` — cmplog:0  n4:2,820
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL33initial_reordering_syllable_indicPK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_980_5_F` — cmplog:1,900  n4:168,000

### 63. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 604:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 354, n4: 47,200)
- **Flip strength**: 2,810 (blocked side hit 2,810× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:354
- **n4 coverage**: T:2,810  F:47,200
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_604_2_T` — cmplog:0  n4:2,810
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_604_2_F` — cmplog:354  n4:47,200

### 64. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 309:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 2,720 (blocked side hit 2,720× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:2,720  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__309_7_T` — cmplog:0  n4:2,720
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__309_7_F` — cmplog:6,400,000  n4:98,500,000

### 65. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3452:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 529, n4: 58,100)
- **Flip strength**: 2,700 (blocked side hit 2,700× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:529
- **n4 coverage**: T:2,700  F:58,100
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3452_9_T` — cmplog:0  n4:2,700
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3452_9_F` — cmplog:529  n4:58,100

### 66. `_ZNK2OT21hb_ot_apply_context_t21match_properties_markEPK15hb_glyph_info_tjjb` @ 794:21
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 52, n4: 52,600)
- **Flip strength**: 2,460 (blocked side hit 2,460× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:52  F:0
- **n4 coverage**: T:52,600  F:2,460
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21hb_ot_apply_context_t21match_properties_markEPK15hb_glyph_info_tjjb_794_21_T` — cmplog:52  n4:52,600
  - `harfbuzz__ZNK2OT21hb_ot_apply_context_t21match_properties_markEPK15hb_glyph_info_tjjb_794_21_F` — cmplog:0  n4:2,460

### 67. `hb-ot-shaper-myanmar.cc:_ZL17_hb_next_syllableP11hb_buffer_tj` @ 166:29
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 660, n4: 97,800)
- **Flip strength**: 2,460 (blocked side hit 2,460× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:660
- **n4 coverage**: T:2,460  F:97,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL17_hb_next_syllableP11hb_buffer_tj_166_29_T` — cmplog:0  n4:2,460
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL17_hb_next_syllableP11hb_buffer_tj_166_29_F` — cmplog:660  n4:97,800

### 68. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3519:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 466, n4: 92,800)
- **Flip strength**: 2,410 (blocked side hit 2,410× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:466  F:0
- **n4 coverage**: T:92,800  F:2,410
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3519_6_T` — cmplog:466  n4:92,800
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3519_6_F` — cmplog:0  n4:2,410

### 69. `_ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t` @ 207:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 1,440)
- **Flip strength**: 2,280 (blocked side hit 2,280× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:2,280  F:1,440
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t_207_11_T` — cmplog:0  n4:2,280
  - `harfbuzz__ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t_207_11_F` — cmplog:8  n4:1,440

### 70. `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1_` @ 820:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 22,400, n4: 64,000)
- **Flip strength**: 2,280 (blocked side hit 2,280× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:22,400
- **n4 coverage**: T:2,280  F:64,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__820_7_T` — cmplog:0  n4:2,280
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__820_7_F` — cmplog:22,400  n4:64,000

### 71. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 890:34
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 67, n4: 1,520)
- **Flip strength**: 2,160 (blocked side hit 2,160× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:67
- **n4 coverage**: T:2,160  F:1,520
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_890_34_T` — cmplog:0  n4:2,160
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_890_34_F` — cmplog:67  n4:1,520

### 72. `_Z20find_syllables_khmerP11hb_buffer_t` @ 391:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 43,800)
- **Flip strength**: 2,090 (blocked side hit 2,090× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:2,090  F:43,800
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_391_2_T` — cmplog:0  n4:2,090
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_391_2_F` — cmplog:8,260  n4:43,800

### 73. `_Z20find_syllables_khmerP11hb_buffer_t` @ 373:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 43,900)
- **Flip strength**: 2,060 (blocked side hit 2,060× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:2,060  F:43,900
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_373_2_T` — cmplog:0  n4:2,060
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_373_2_F` — cmplog:8,260  n4:43,900

### 74. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 624:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 354, n4: 48,100)
- **Flip strength**: 1,970 (blocked side hit 1,970× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:354
- **n4 coverage**: T:1,970  F:48,100
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_624_2_T` — cmplog:0  n4:1,970
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_624_2_F` — cmplog:354  n4:48,100

### 75. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 590:3
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 28, n4: 9,500)
- **Flip strength**: 1,940 (blocked side hit 1,940× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:28  F:0
- **n4 coverage**: T:9,500  F:1,940
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_590_3_T` — cmplog:28  n4:9,500
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_590_3_F` — cmplog:0  n4:1,940

### 76. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 329:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 1,810 (blocked side hit 1,810× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:1,810  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__329_7_T` — cmplog:0  n4:1,810
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__329_7_F` — cmplog:6,400,000  n4:98,500,000

### 77. `_ZNK2OT18glyf_accelerator_t10get_pointsINS0_19points_aggregator_tEEEbP9hb_font_tjT_10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE` @ 260:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 27,700)
- **Flip strength**: 1,770 (blocked side hit 1,770× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:27,700  F:1,770
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT18glyf_accelerator_t10get_pointsINS0_19points_aggregator_tEEEbP9hb_font_tjT_10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE_260_8_T` — cmplog:15  n4:27,700
  - `harfbuzz__ZNK2OT18glyf_accelerator_t10get_pointsINS0_19points_aggregator_tEEEbP9hb_font_tjT_10hb_array_tIKiER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tE_260_8_F` — cmplog:0  n4:1,770

### 78. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 321:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 1,730 (blocked side hit 1,730× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:1,730  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__321_7_T` — cmplog:0  n4:1,730
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__321_7_F` — cmplog:6,400,000  n4:98,500,000

### 79. `_ZN11hb_vector_tIiLb0EE6resizeEibb` @ 492:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 368, n4: 389)
- **Flip strength**: 1,610 (blocked side hit 1,610× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:368
- **n4 coverage**: T:1,610  F:389
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIiLb0EE6resizeEibb_492_11_T` — cmplog:0  n4:1,610
  - `harfbuzz__ZN11hb_vector_tIiLb0EE6resizeEibb_492_11_F` — cmplog:368  n4:389

### 80. `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj` @ 72:23
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10,300, n4: 17,900)
- **Flip strength**: 1,560 (blocked side hit 1,560× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10,300
- **n4 coverage**: T:1,560  F:17,900
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_72_23_T` — cmplog:0  n4:1,560
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_72_23_F` — cmplog:10,300  n4:17,900

### 81. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1057:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 72,400)
- **Flip strength**: 1,440 (blocked side hit 1,440× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:1,440  F:72,400
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1057_2_T` — cmplog:0  n4:1,440
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1057_2_F` — cmplog:2,020  n4:72,400

### 82. `hb-ot-shaper-use.cc:_ZN15machine_index_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE16hb_filter_iter_tIS3_IS0_IS2_10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS5_E_RK4$_30LPv0EEZL18find_syllables_useS9_EUl9hb_pair_tIjSB_EE_RK4$_17LSG_0EEEEaSERKSQ_` @ 879:46
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 580)
- **Flip strength**: 1,440 (blocked side hit 1,440× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:1,440  F:580
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN15machine_index_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE16hb_filter_iter_tIS3_IS0_IS2_10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS5_E_RK4$_30LPv0EEZL18find_syllables_useS9_EUl9hb_pair_tIjSB_EE_RK4$_17LSG_0EEEEaSERKSQ__879_46_T` — cmplog:0  n4:1,440
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN15machine_index_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE16hb_filter_iter_tIS3_IS0_IS2_10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS5_E_RK4$_30LPv0EEZL18find_syllables_useS9_EUl9hb_pair_tIjSB_EE_RK4$_17LSG_0EEEEaSERKSQ__879_46_F` — cmplog:130  n4:580

### 83. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1069:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 72,400)
- **Flip strength**: 1,410 (blocked side hit 1,410× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:1,410  F:72,400
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1069_2_T` — cmplog:0  n4:1,410
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1069_2_F` — cmplog:2,020  n4:72,400

### 84. `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj` @ 107:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 462, n4: 127,000)
- **Flip strength**: 1,390 (blocked side hit 1,390× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:462
- **n4 coverage**: T:1,390  F:127,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_107_6_T` — cmplog:0  n4:1,390
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_107_6_F` — cmplog:462  n4:127,000

### 85. `_ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE4nextEPj` @ 591:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,970, n4: 151,000)
- **Flip strength**: 1,370 (blocked side hit 1,370× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,970  F:0
- **n4 coverage**: T:151,000  F:1,370
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE4nextEPj_591_8_T` — cmplog:1,970  n4:151,000
  - `harfbuzz__ZN2OT19skipping_iterator_tINS_21hb_ot_apply_context_tEE4nextEPj_591_8_F` — cmplog:0  n4:1,370

### 86. `_ZNK2OT6Layout9GSUB_impl23AlternateSubstFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 77:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 192, n4: 19,000)
- **Flip strength**: 1,280 (blocked side hit 1,280× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:192
- **n4 coverage**: T:1,280  F:19,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl23AlternateSubstFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_77_9_T` — cmplog:0  n4:1,280
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl23AlternateSubstFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_77_9_F` — cmplog:192  n4:19,000

### 87. `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj` @ 227:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 3,380)
- **Flip strength**: 1,230 (blocked side hit 1,230× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:1,230  F:3,380
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_227_12_T` — cmplog:0  n4:1,230
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_227_12_F` — cmplog:27  n4:3,380

### 88. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 309:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 1,220 (blocked side hit 1,220× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:1,220  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__309_7_T` — cmplog:0  n4:1,220
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__309_7_F` — cmplog:3,800,000  n4:71,000,000

### 89. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4_` @ 457:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 1,130)
- **Flip strength**: 1,190 (blocked side hit 1,190× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:1,130  F:1,190
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__457_9_T` — cmplog:2  n4:1,130
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__457_9_F` — cmplog:0  n4:1,190

### 90. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4_` @ 459:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 27)
- **Flip strength**: 1,100 (blocked side hit 1,100× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1,100  F:27
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__459_11_T` — cmplog:0  n4:1,100
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__459_11_F` — cmplog:2  n4:27

### 91. `_ZNK2OT12CmapSubtable9get_glyphEjPj` @ 1504:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 213,000, n4: 456,000)
- **Flip strength**: 1,090 (blocked side hit 1,090× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:213,000
- **n4 coverage**: T:1,090  F:456,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12CmapSubtable9get_glyphEjPj_1504_5_T` — cmplog:0  n4:1,090
  - `harfbuzz__ZNK2OT12CmapSubtable9get_glyphEjPj_1504_5_F` — cmplog:213,000  n4:456,000

### 92. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3523:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 466, n4: 89,600)
- **Flip strength**: 1,070 (blocked side hit 1,070× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:466  F:0
- **n4 coverage**: T:89,600  F:1,070
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3523_8_T` — cmplog:466  n4:89,600
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3523_8_F` — cmplog:0  n4:1,070

### 93. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 317:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 1,050 (blocked side hit 1,050× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:1,050  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__317_7_T` — cmplog:0  n4:1,050
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__317_7_F` — cmplog:6,400,000  n4:98,500,000

### 94. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 329:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 1,030 (blocked side hit 1,030× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:1,030  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__329_7_T` — cmplog:0  n4:1,030
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__329_7_F` — cmplog:3,800,000  n4:71,000,000

### 95. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 325:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 1,020 (blocked side hit 1,020× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:1,020  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__325_7_T` — cmplog:0  n4:1,020
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__325_7_F` — cmplog:6,400,000  n4:98,500,000

### 96. `_ZNK3AAT10ClassTableIN2OT7NumTypeILb1EtLj2EEEE14collect_glyphsI12hb_bit_set_tEEvRT_j` @ 1048:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 404, n4: 45,200)
- **Flip strength**: 1,000 (blocked side hit 1,000× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:404  F:0
- **n4 coverage**: T:45,200  F:1,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10ClassTableIN2OT7NumTypeILb1EtLj2EEEE14collect_glyphsI12hb_bit_set_tEEvRT_j_1048_11_T` — cmplog:404  n4:45,200
  - `harfbuzz__ZNK3AAT10ClassTableIN2OT7NumTypeILb1EtLj2EEEE14collect_glyphsI12hb_bit_set_tEEvRT_j_1048_11_F` — cmplog:0  n4:1,000

### 97. `_ZN12hb_extents_tIfE6union_ERKS0_` @ 50:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4,110, n4: 33,000)
- **Flip strength**: 882 (blocked side hit 882× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4,110
- **n4 coverage**: T:882  F:33,000
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_extents_tIfE6union_ERKS0__50_9_T` — cmplog:0  n4:882
  - `harfbuzz__ZN12hb_extents_tIfE6union_ERKS0__50_9_F` — cmplog:4,110  n4:33,000

### 98. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1267:18
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 646, n4: 75,000)
- **Flip strength**: 879 (blocked side hit 879× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:646  F:0
- **n4 coverage**: T:75,000  F:879
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1267_18_T` — cmplog:646  n4:75,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1267_18_F` — cmplog:0  n4:879

### 99. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 321:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 875 (blocked side hit 875× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:875  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__321_7_T` — cmplog:0  n4:875
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__321_7_F` — cmplog:3,800,000  n4:71,000,000

### 100. `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE` @ 1415:30
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 423)
- **Flip strength**: 821 (blocked side hit 821× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:821  F:423
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE_1415_30_T` — cmplog:0  n4:821
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE_1415_30_F` — cmplog:6  n4:423

### 101. `_ZNK2OT9glyf_impl5Glyph10get_pointsINS_18glyf_accelerator_tEEEbP9hb_font_tRKT_R22contour_point_vector_tR17hb_glyf_scratch_tPS9_P16head_maxp_info_tPjbbb10hb_array_tIKiEPNS_17hb_scalar_cache_tEjSG_` @ 386:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 663, n4: 2,840)
- **Flip strength**: 800 (blocked side hit 800× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:663
- **n4 coverage**: T:800  F:2,840
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9glyf_impl5Glyph10get_pointsINS_18glyf_accelerator_tEEEbP9hb_font_tRKT_R22contour_point_vector_tR17hb_glyf_scratch_tPS9_P16head_maxp_info_tPjbbb10hb_array_tIKiEPNS_17hb_scalar_cache_tEjSG__386_11_T` — cmplog:0  n4:800
  - `harfbuzz__ZNK2OT9glyf_impl5Glyph10get_pointsINS_18glyf_accelerator_tEEEbP9hb_font_tRKT_R22contour_point_vector_tR17hb_glyf_scratch_tPS9_P16head_maxp_info_tPjbbb10hb_array_tIKiEPNS_17hb_scalar_cache_tEjSG__386_11_F` — cmplog:663  n4:2,840

### 102. `hb-ot-font.cc:_ZL24hb_ot_draw_glyph_or_failP9hb_font_tPvjP15hb_draw_funcs_tS1_S1_` @ 910:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 20,400, n4: 45,200)
- **Flip strength**: 769 (blocked side hit 769× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:20,400
- **n4 coverage**: T:769  F:45,200
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL24hb_ot_draw_glyph_or_failP9hb_font_tPvjP15hb_draw_funcs_tS1_S1__910_7_T` — cmplog:0  n4:769
  - `harfbuzz_hb-ot-font.cc:_ZL24hb_ot_draw_glyph_or_failP9hb_font_tPvjP15hb_draw_funcs_tS1_S1__910_7_F` — cmplog:20,400  n4:45,200

### 103. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 277:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 751 (blocked side hit 751× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:751  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__277_7_T` — cmplog:0  n4:751
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__277_7_F` — cmplog:6,400,000  n4:98,500,000

### 104. `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj` @ 127:37
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 515)
- **Flip strength**: 746 (blocked side hit 746× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:746  F:515
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_127_37_T` — cmplog:0  n4:746
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_127_37_F` — cmplog:1  n4:515

### 105. `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 3930:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19,400, n4: 400,000)
- **Flip strength**: 737 (blocked side hit 737× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19,400
- **n4 coverage**: T:737  F:400,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3930_9_T` — cmplog:0  n4:737
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3930_9_F` — cmplog:19,400  n4:400,000

### 106. `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 3931:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19,400, n4: 400,000)
- **Flip strength**: 737 (blocked side hit 737× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19,400
- **n4 coverage**: T:737  F:400,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3931_9_T` — cmplog:0  n4:737
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3931_9_F` — cmplog:19,400  n4:400,000

### 107. `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 3932:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19,400, n4: 400,000)
- **Flip strength**: 737 (blocked side hit 737× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19,400
- **n4 coverage**: T:737  F:400,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3932_9_T` — cmplog:0  n4:737
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3932_9_F` — cmplog:19,400  n4:400,000

### 108. `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 3938:13
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19,400, n4: 400,000)
- **Flip strength**: 737 (blocked side hit 737× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19,400
- **n4 coverage**: T:737  F:400,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3938_13_T` — cmplog:0  n4:737
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3938_13_F` — cmplog:19,400  n4:400,000

### 109. `hb-ot-layout.cc:_ZN2OTL11match_inputINS_11HBGlyphID16EEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESA_PjSD_SD_` @ 1364:25
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,330, n4: 50,100)
- **Flip strength**: 735 (blocked side hit 735× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,330
- **n4 coverage**: T:735  F:50,100
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_11HBGlyphID16EEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESA_PjSD_SD__1364_25_T` — cmplog:0  n4:735
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_11HBGlyphID16EEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESA_PjSD_SD__1364_25_F` — cmplog:2,330  n4:50,100

### 110. `_ZNK2OT7ArrayOfINS_6Layout9GPOS_impl10MarkRecordENS_7NumTypeILb1EtLj2EEEEixEi` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 12,300)
- **Flip strength**: 731 (blocked side hit 731× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:12,300  F:731
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_6Layout9GPOS_impl10MarkRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_T` — cmplog:4  n4:12,300
  - `harfbuzz__ZNK2OT7ArrayOfINS_6Layout9GPOS_impl10MarkRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_F` — cmplog:0  n4:731

### 111. `_ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE13accelerator_t11get_kerningEjj` @ 143:36
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 224)
- **Flip strength**: 729 (blocked side hit 729× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:224  F:729
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE13accelerator_t11get_kerningEjj_143_36_T` — cmplog:1  n4:224
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE13accelerator_t11get_kerningEjj_143_36_F` — cmplog:0  n4:729

### 112. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 278:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 716 (blocked side hit 716× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:716  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__278_7_T` — cmplog:0  n4:716
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__278_7_F` — cmplog:6,400,000  n4:98,500,000

### 113. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 317:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 686 (blocked side hit 686× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:686  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__317_7_T` — cmplog:0  n4:686
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__317_7_F` — cmplog:3,800,000  n4:71,000,000

### 114. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 333:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 684 (blocked side hit 684× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:684  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__333_7_T` — cmplog:0  n4:684
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__333_7_F` — cmplog:6,400,000  n4:98,500,000

### 115. `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1_` @ 1467:17
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10,100, n4: 17,600)
- **Flip strength**: 683 (blocked side hit 683× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10,100
- **n4 coverage**: T:683  F:17,600
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1467_17_T` — cmplog:0  n4:683
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1467_17_F` — cmplog:10,100  n4:17,600

### 116. `_ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 50:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 965)
- **Flip strength**: 667 (blocked side hit 667× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:667  F:965
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_50_9_T` — cmplog:0  n4:667
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_50_9_F` — cmplog:36  n4:965

### 117. `_ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 160:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,029, n4: 165,000)
- **Flip strength**: 664 (blocked side hit 664× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,029  F:0
- **n4 coverage**: T:165,000  F:664
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_160_9_T` — cmplog:2,029  n4:165,000
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_160_9_F` — cmplog:0  n4:664

### 118. `_ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7hlinetoERS2_RS3_` @ 499:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 32, n4: 741)
- **Flip strength**: 622 (blocked side hit 622× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:32  F:0
- **n4 coverage**: T:741  F:622
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7hlinetoERS2_RS3__499_9_T` — cmplog:32  n4:741
  - `harfbuzz__ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7hlinetoERS2_RS3__499_9_F` — cmplog:0  n4:622

### 119. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 325:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 621 (blocked side hit 621× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:621  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__325_7_T` — cmplog:0  n4:621
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__325_7_F` — cmplog:3,800,000  n4:71,000,000

### 120. `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj` @ 129:28
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 516)
- **Flip strength**: 597 (blocked side hit 597× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:597  F:516
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_129_28_T` — cmplog:0  n4:597
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_129_28_F` — cmplog:2  n4:516

### 121. `_ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj` @ 144:28
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 516)
- **Flip strength**: 597 (blocked side hit 597× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:597  F:516
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_144_28_T` — cmplog:0  n4:597
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl7PairSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPKNS1_11ValueFormatEj_144_28_F` — cmplog:2  n4:516

### 122. `hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ_` @ 456:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 38, n4: 851)
- **Flip strength**: 594 (blocked side hit 594× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:38
- **n4 coverage**: T:594  F:851
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ__456_18_T` — cmplog:0  n4:594
  - `harfbuzz_hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ__456_18_F` — cmplog:38  n4:851

### 123. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv` @ 1181:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16, n4: 609)
- **Flip strength**: 565 (blocked side hit 565× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16
- **n4 coverage**: T:565  F:609
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1181_11_T` — cmplog:0  n4:565
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1181_11_F` — cmplog:16  n4:609

### 124. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl6AnchorENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 12,500)
- **Flip strength**: 561 (blocked side hit 561× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:12,500  F:561
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl6AnchorENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_T` — cmplog:4  n4:12,500
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl6AnchorENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_F` — cmplog:0  n4:561

### 125. `_ZNK3AAT19KerxSubTableFormat0INS_18KerxSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j` @ 125:31
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 63)
- **Flip strength**: 542 (blocked side hit 542× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:542  F:63
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0INS_18KerxSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_125_31_T` — cmplog:0  n4:542
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0INS_18KerxSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_125_31_F` — cmplog:1  n4:63

### 126. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 277:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 542 (blocked side hit 542× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:542  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__277_7_T` — cmplog:0  n4:542
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__277_7_F` — cmplog:3,800,000  n4:71,000,000

### 127. `_ZN11hb_vector_tIfLb0EE5allocEjb` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,260, n4: 1,780,000)
- **Flip strength**: 538 (blocked side hit 538× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,260  F:0
- **n4 coverage**: T:1,780,000  F:538
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_250_22_T` — cmplog:1,260  n4:1,780,000
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_250_22_F` — cmplog:0  n4:538

### 128. `_ZNK2OT8hmtxvmtxINS_4vmtxENS_4vheaENS_4VVAREE13accelerator_t40get_leading_bearing_without_var_unscaledEjPi` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7,660, n4: 211,000)
- **Flip strength**: 514 (blocked side hit 514× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7,660  F:0
- **n4 coverage**: T:211,000  F:514
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8hmtxvmtxINS_4vmtxENS_4vheaENS_4VVAREE13accelerator_t40get_leading_bearing_without_var_unscaledEjPi_251_24_T` — cmplog:7,660  n4:211,000
  - `harfbuzz__ZNK2OT8hmtxvmtxINS_4vmtxENS_4vheaENS_4VVAREE13accelerator_t40get_leading_bearing_without_var_unscaledEjPi_251_24_F` — cmplog:0  n4:514

### 129. `hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj` @ 57:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,810, n4: 107,000)
- **Flip strength**: 503 (blocked side hit 503× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,810
- **n4 coverage**: T:503  F:107,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj_57_7_T` — cmplog:0  n4:503
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL9is_one_ofRK15hb_glyph_info_tj_57_7_F` — cmplog:2,810  n4:107,000

### 130. `_ZN2OT17hb_scalar_cache_t6createEjPS0_` @ 2572:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 586, n4: 2,460)
- **Flip strength**: 466 (blocked side hit 466× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:586
- **n4 coverage**: T:466  F:2,460
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT17hb_scalar_cache_t6createEjPS0__2572_9_T` — cmplog:0  n4:466
  - `harfbuzz__ZN2OT17hb_scalar_cache_t6createEjPS0__2572_9_F` — cmplog:586  n4:2,460

### 131. `_ZNK2OT18glyf_accelerator_t19points_aggregator_t16contour_bounds_t5emptyEv` @ 330:56
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 28,000)
- **Flip strength**: 462 (blocked side hit 462× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:462  F:28,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT18glyf_accelerator_t19points_aggregator_t16contour_bounds_t5emptyEv_330_56_T` — cmplog:0  n4:462
  - `harfbuzz__ZNK2OT18glyf_accelerator_t19points_aggregator_t16contour_bounds_t5emptyEv_330_56_F` — cmplog:3  n4:28,000

### 132. `_ZN2OT17hb_scalar_cache_t7destroyEPS0_S1_` @ 2590:46
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 586, n4: 2,440)
- **Flip strength**: 460 (blocked side hit 460× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:586  F:0
- **n4 coverage**: T:2,440  F:460
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT17hb_scalar_cache_t7destroyEPS0_S1__2590_46_T` — cmplog:586  n4:2,440
  - `harfbuzz__ZN2OT17hb_scalar_cache_t7destroyEPS0_S1__2590_46_F` — cmplog:0  n4:460

### 133. `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t` @ 1389:30
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 224)
- **Flip strength**: 457 (blocked side hit 457× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:457  F:224
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t_1389_30_T` — cmplog:0  n4:457
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t_1389_30_F` — cmplog:3  n4:224

### 134. `_ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7hlinetoERS2_RS3_` @ 499:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 16, n4: 510)
- **Flip strength**: 448 (blocked side hit 448× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:0
- **n4 coverage**: T:510  F:448
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7hlinetoERS2_RS3__499_9_T` — cmplog:16  n4:510
  - `harfbuzz__ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7hlinetoERS2_RS3__499_9_F` — cmplog:0  n4:448

### 135. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 333:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 435 (blocked side hit 435× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:435  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__333_7_T` — cmplog:0  n4:435
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__333_7_F` — cmplog:3,800,000  n4:71,000,000

### 136. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 107:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 627, n4: 5,380)
- **Flip strength**: 431 (blocked side hit 431× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:627
- **n4 coverage**: T:431  F:5,380
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_107_9_T` — cmplog:0  n4:431
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_107_9_F` — cmplog:627  n4:5,380

### 137. `_ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj` @ 671:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 111,000, n4: 873,000)
- **Flip strength**: 422 (blocked side hit 422× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:111,000
- **n4 coverage**: T:422  F:873,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_671_5_T` — cmplog:0  n4:422
  - `harfbuzz__ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_671_5_F` — cmplog:111,000  n4:873,000

### 138. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 292:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 412 (blocked side hit 412× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:412  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__292_7_T` — cmplog:0  n4:412
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__292_7_F` — cmplog:6,400,000  n4:98,500,000

### 139. `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 874:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 66)
- **Flip strength**: 405 (blocked side hit 405× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:66  F:405
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__874_5_T` — cmplog:15  n4:66
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__874_5_F` — cmplog:0  n4:405

### 140. `_ZN2OT4cff132lookup_standard_encoding_for_sidEj` @ 262:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 155)
- **Flip strength**: 397 (blocked side hit 397× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:397  F:155
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cff132lookup_standard_encoding_for_sidEj_262_7_T` — cmplog:0  n4:397
  - `harfbuzz__ZN2OT4cff132lookup_standard_encoding_for_sidEj_262_7_F` — cmplog:6  n4:155

### 141. `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE17std_code_to_glyphEj` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 155)
- **Flip strength**: 397 (blocked side hit 397× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:155  F:397
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE17std_code_to_glyphEj_251_24_T` — cmplog:6  n4:155
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE17std_code_to_glyphEj_251_24_F` — cmplog:0  n4:397

### 142. `_ZNK2OT6Layout9GPOS_impl16SinglePosFormat15applyEPNS_21hb_ot_apply_context_tE` @ 70:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 16, n4: 36,800)
- **Flip strength**: 392 (blocked side hit 392× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:0
- **n4 coverage**: T:36,800  F:392
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16SinglePosFormat15applyEPNS_21hb_ot_apply_context_tE_70_9_T` — cmplog:16  n4:36,800
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16SinglePosFormat15applyEPNS_21hb_ot_apply_context_tE_70_9_F` — cmplog:0  n4:392

### 143. `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj` @ 1477:43
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5,270, n4: 87,800)
- **Flip strength**: 390 (blocked side hit 390× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,270  F:0
- **n4 coverage**: T:87,800  F:390
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1477_43_T` — cmplog:5,270  n4:87,800
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1477_43_F` — cmplog:0  n4:390

### 144. `hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj` @ 1520:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5,280, n4: 91,500)
- **Flip strength**: 390 (blocked side hit 390× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,280  F:0
- **n4 coverage**: T:91,500  F:390
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1520_7_T` — cmplog:5,280  n4:91,500
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12ligate_inputEPNS_21hb_ot_apply_context_tEjPKjjjj_1520_7_F` — cmplog:0  n4:390

### 145. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1194:28
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 31)
- **Flip strength**: 389 (blocked side hit 389× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:389  F:31
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1194_28_T` — cmplog:0  n4:389
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1194_28_F` — cmplog:1  n4:31

### 146. `_ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7vlinetoERS2_RS3_` @ 519:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 26, n4: 739)
- **Flip strength**: 371 (blocked side hit 371× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:26  F:0
- **n4 coverage**: T:739  F:371
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7vlinetoERS2_RS3__519_9_T` — cmplog:26  n4:739
  - `harfbuzz__ZN3CFF12path_procs_tI25cff1_path_procs_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_tE7vlinetoERS2_RS3__519_9_F` — cmplog:0  n4:371

### 147. `_ZNK2OT6Layout9GSUB_impl20SingleSubstFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 68, n4: 610)
- **Flip strength**: 349 (blocked side hit 349× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:68
- **n4 coverage**: T:349  F:610
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl20SingleSubstFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_251_24_T` — cmplog:0  n4:349
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl20SingleSubstFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_251_24_F` — cmplog:68  n4:610

### 148. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 278:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 340 (blocked side hit 340× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:340  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__278_7_T` — cmplog:0  n4:340
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__278_7_F` — cmplog:3,800,000  n4:71,000,000

### 149. `_ZNK2OT8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 79, n4: 724)
- **Flip strength**: 323 (blocked side hit 323× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:79
- **n4 coverage**: T:323  F:724
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_T` — cmplog:0  n4:323
  - `harfbuzz__ZNK2OT8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_F` — cmplog:79  n4:724

### 150. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4_` @ 474:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 15)
- **Flip strength**: 322 (blocked side hit 322× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:322  F:15
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4__474_11_T` — cmplog:0  n4:322
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4__474_11_F` — cmplog:1  n4:15

### 151. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4_` @ 459:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 103)
- **Flip strength**: 312 (blocked side hit 312× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:312  F:103
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4__459_11_T` — cmplog:0  n4:312
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VVAREEEP9hb_blob_tS4__459_11_F` — cmplog:5  n4:103

### 152. `_ZN3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13accelerator_tD2Ev` @ 1340:32
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,860, n4: 15,500)
- **Flip strength**: 294 (blocked side hit 294× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,860
- **n4 coverage**: T:294  F:15,500
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13accelerator_tD2Ev_1340_32_T` — cmplog:0  n4:294
  - `harfbuzz__ZN3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13accelerator_tD2Ev_1340_32_F` — cmplog:5,860  n4:15,500

### 153. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 292:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 291 (blocked side hit 291× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:291  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__292_7_T` — cmplog:0  n4:291
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__292_7_F` — cmplog:3,800,000  n4:71,000,000

### 154. `_ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7vlinetoERS2_RS3_` @ 519:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 12, n4: 487)
- **Flip strength**: 272 (blocked side hit 272× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:0
- **n4 coverage**: T:487  F:272
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7vlinetoERS2_RS3__519_9_T` — cmplog:12  n4:487
  - `harfbuzz__ZN3CFF12path_procs_tI22cff1_path_procs_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_tE7vlinetoERS2_RS3__519_9_F` — cmplog:0  n4:272

### 155. `hb-ot-shaper-use.cc:_ZL27_hb_glyph_info_get_lig_compPK15hb_glyph_info_t` @ 508:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 13,000)
- **Flip strength**: 270 (blocked side hit 270× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:270  F:13,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL27_hb_glyph_info_get_lig_compPK15hb_glyph_info_t_508_7_T` — cmplog:0  n4:270
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL27_hb_glyph_info_get_lig_compPK15hb_glyph_info_t_508_7_F` — cmplog:1  n4:13,000

### 156. `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1_` @ 1469:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10,100, n4: 17,300)
- **Flip strength**: 268 (blocked side hit 268× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10,100  F:0
- **n4 coverage**: T:17,300  F:268
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1469_9_T` — cmplog:10,100  n4:17,300
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1469_9_F` — cmplog:0  n4:268

### 157. `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE` @ 892:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,730, n4: 2,740)
- **Flip strength**: 268 (blocked side hit 268× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,730  F:0
- **n4 coverage**: T:2,740  F:268
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_892_6_T` — cmplog:1,730  n4:2,740
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_892_6_F` — cmplog:0  n4:268

### 158. `_ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat0INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18, n4: 1,170)
- **Flip strength**: 267 (blocked side hit 267× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:0
- **n4 coverage**: T:1,170  F:267
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat0INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb_250_22_T` — cmplog:18  n4:1,170
  - `harfbuzz__ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat0INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb_250_22_F` — cmplog:0  n4:267

### 159. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 123:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 332)
- **Flip strength**: 263 (blocked side hit 263× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:263  F:332
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_123_9_T` — cmplog:0  n4:263
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_123_9_F` — cmplog:6  n4:332

### 160. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 268:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 262 (blocked side hit 262× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:262  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__268_7_T` — cmplog:0  n4:262
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__268_7_F` — cmplog:6,400,000  n4:98,500,000

### 161. `hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE_` @ 1364:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 239,000, n4: 3,200,000)
- **Flip strength**: 252 (blocked side hit 252× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:239,000
- **n4 coverage**: T:252  F:3,200,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE__1364_9_T` — cmplog:0  n4:252
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE__1364_9_F` — cmplog:239,000  n4:3,200,000

### 162. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 313:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 248 (blocked side hit 248× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:248  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__313_7_T` — cmplog:0  n4:248
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__313_7_F` — cmplog:6,400,000  n4:98,500,000

### 163. `hb-ot-shaper-use.cc:_ZZL18find_syllables_useP11hb_buffer_tENKUl9hb_pair_tIjRK15hb_glyph_info_tEE_clES5_` @ 916:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13,700, n4: 514,000)
- **Flip strength**: 245 (blocked side hit 245× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13,700
- **n4 coverage**: T:245  F:514,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZZL18find_syllables_useP11hb_buffer_tENKUl9hb_pair_tIjRK15hb_glyph_info_tEE_clES5__916_10_T` — cmplog:0  n4:245
  - `harfbuzz_hb-ot-shaper-use.cc:_ZZL18find_syllables_useP11hb_buffer_tENKUl9hb_pair_tIjRK15hb_glyph_info_tEE_clES5__916_10_F` — cmplog:13,700  n4:514,000

### 164. `_ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj` @ 1279:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 13, n4: 215)
- **Flip strength**: 237 (blocked side hit 237× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:13  F:0
- **n4 coverage**: T:215  F:237
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj_1279_9_T` — cmplog:13  n4:215
  - `harfbuzz__ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj_1279_9_F` — cmplog:0  n4:237

### 165. `_ZNK2OT8ClassDef9get_classEj` @ 2074:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 40,600, n4: 514,000)
- **Flip strength**: 237 (blocked side hit 237× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:40,600
- **n4 coverage**: T:237  F:514,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8ClassDef9get_classEj_2074_5_T` — cmplog:0  n4:237
  - `harfbuzz__ZNK2OT8ClassDef9get_classEj_2074_5_F` — cmplog:40,600  n4:514,000

### 166. `_ZN2OT6Layout9GPOS_impl11ValueFormat10get_deviceEPKNS_7NumTypeILb1EtLj2EEEPbPKNS1_9ValueBaseER21hb_sanitize_context_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 725)
- **Flip strength**: 234 (blocked side hit 234× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:234  F:725
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GPOS_impl11ValueFormat10get_deviceEPKNS_7NumTypeILb1EtLj2EEEPbPKNS1_9ValueBaseER21hb_sanitize_context_t_251_24_T` — cmplog:0  n4:234
  - `harfbuzz__ZN2OT6Layout9GPOS_impl11ValueFormat10get_deviceEPKNS_7NumTypeILb1EtLj2EEEPbPKNS1_9ValueBaseER21hb_sanitize_context_t_251_24_F` — cmplog:6  n4:725

### 167. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1284:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 646, n4: 75,000)
- **Flip strength**: 230 (blocked side hit 230× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:646  F:0
- **n4 coverage**: T:75,000  F:230
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1284_11_T` — cmplog:646  n4:75,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1284_11_F` — cmplog:0  n4:230

### 168. `_ZN11hb_buffer_t14replace_glyphsIjEEbjjPKT_` @ 302:34
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 803,000, n4: 4,000,000)
- **Flip strength**: 227 (blocked side hit 227× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:803,000  F:0
- **n4 coverage**: T:4,000,000  F:227
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t14replace_glyphsIjEEbjjPKT__302_34_T` — cmplog:803,000  n4:4,000,000
  - `harfbuzz__ZN11hb_buffer_t14replace_glyphsIjEEbjjPKT__302_34_F` — cmplog:0  n4:227

### 169. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 273:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 217 (blocked side hit 217× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:217  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__273_7_T` — cmplog:0  n4:217
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__273_7_F` — cmplog:6,400,000  n4:98,500,000

### 170. `hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t` @ 357:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,029, n4: 242,000)
- **Flip strength**: 212 (blocked side hit 212× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,029
- **n4 coverage**: T:212  F:242,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t_357_11_T` — cmplog:0  n4:212
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t_357_11_F` — cmplog:2,029  n4:242,000

### 171. `_ZNK2OT8OffsetToINS_13IndexSubtableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 26, n4: 66)
- **Flip strength**: 209 (blocked side hit 209× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:26  F:0
- **n4 coverage**: T:66  F:209
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_13IndexSubtableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_T` — cmplog:26  n4:66
  - `harfbuzz__ZNK2OT8OffsetToINS_13IndexSubtableENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_F` — cmplog:0  n4:209

### 172. `_ZNK2OT15VariationDevice11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE` @ 4862:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 16, n4: 3)
- **Flip strength**: 207 (blocked side hit 207× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:0
- **n4 coverage**: T:3  F:207
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT15VariationDevice11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4862_12_T` — cmplog:16  n4:3
  - `harfbuzz__ZNK2OT15VariationDevice11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4862_12_F` — cmplog:0  n4:207

### 173. `_ZNK21hb_sanitize_context_t11check_rangeIN2OT7NumTypeILb1EsLj2EEEEEbPKT_jj` @ 340:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 63, n4: 168,000)
- **Flip strength**: 207 (blocked side hit 207× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:63  F:0
- **n4 coverage**: T:168,000  F:207
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT7NumTypeILb1EsLj2EEEEEbPKT_jj_340_12_T` — cmplog:63  n4:168,000
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT7NumTypeILb1EsLj2EEEEEbPKT_jj_340_12_F` — cmplog:0  n4:207

### 174. `hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE_` @ 1404:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 239,000, n4: 3,200,000)
- **Flip strength**: 203 (blocked side hit 203× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:239,000
- **n4 coverage**: T:203  F:3,200,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE__1404_11_T` — cmplog:0  n4:203
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL11match_inputINS_7NumTypeILb1EtLj2EEEEEbPNS_21hb_ot_apply_context_tEjPKT_PFbR15hb_glyph_info_tjPKvESB_PjSE_SE__1404_11_F` — cmplog:239,000  n4:3,200,000

### 175. `hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb` @ 233:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 206)
- **Flip strength**: 203 (blocked side hit 203× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:203  F:206
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb_233_14_T` — cmplog:0  n4:203
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb_233_14_F` — cmplog:13  n4:206

### 176. `_ZNK10hb_array_tIKiE11__item_at__Ej` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 250, n4: 7,850)
- **Flip strength**: 201 (blocked side hit 201× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:250
- **n4 coverage**: T:201  F:7,850
- **Canonical identifiers**:
  - `harfbuzz__ZNK10hb_array_tIKiE11__item_at__Ej_251_24_T` — cmplog:0  n4:201
  - `harfbuzz__ZNK10hb_array_tIKiE11__item_at__Ej_251_24_F` — cmplog:250  n4:7,850

### 177. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 127:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,680)
- **Flip strength**: 194 (blocked side hit 194× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:194  F:2,680
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__127_2_T` — cmplog:0  n4:194
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__127_2_F` — cmplog:786  n4:2,680

### 178. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1271:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 953)
- **Flip strength**: 191 (blocked side hit 191× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:191  F:953
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1271_14_T` — cmplog:0  n4:191
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1271_14_F` — cmplog:2  n4:953

### 179. `_ZN2OT11TupleValues9decompileIiEEbRPKNS_7NumTypeILb1EhLj1EEER11hb_vector_tIT_Lb0EES5_bj` @ 1760:16
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 170, n4: 59)
- **Flip strength**: 182 (blocked side hit 182× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:170
- **n4 coverage**: T:182  F:59
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT11TupleValues9decompileIiEEbRPKNS_7NumTypeILb1EhLj1EEER11hb_vector_tIT_Lb0EES5_bj_1760_16_T` — cmplog:0  n4:182
  - `harfbuzz__ZN2OT11TupleValues9decompileIiEEbRPKNS_7NumTypeILb1EhLj1EEER11hb_vector_tIT_Lb0EES5_bj_1760_16_F` — cmplog:170  n4:59

### 180. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 268:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 181 (blocked side hit 181× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:181  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__268_7_T` — cmplog:0  n4:181
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__268_7_F` — cmplog:3,800,000  n4:71,000,000

### 181. `_ZNK3AAT13LookupFormat0IN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 741,000)
- **Flip strength**: 176 (blocked side hit 176× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:176  F:741,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT13LookupFormat0IN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_251_24_T` — cmplog:0  n4:176
  - `harfbuzz__ZNK3AAT13LookupFormat0IN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_251_24_F` — cmplog:110,000  n4:741,000

### 182. `_ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 933, n4: 5,100)
- **Flip strength**: 174 (blocked side hit 174× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:933  F:0
- **n4 coverage**: T:5,100  F:174
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:933  n4:5,100
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:174

### 183. `_Z23hb_indic_get_categoriesj` @ 506:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,030, n4: 13,800)
- **Flip strength**: 172 (blocked side hit 172× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,030
- **n4 coverage**: T:172  F:13,800
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_506_11_T` — cmplog:0  n4:172
  - `harfbuzz__Z23hb_indic_get_categoriesj_506_11_F` — cmplog:1,030  n4:13,800

### 184. `_ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_19SparseVarRegionListEEEEbP21hb_sanitize_context_tDpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 42, n4: 1,730)
- **Flip strength**: 168 (blocked side hit 168× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:42
- **n4 coverage**: T:168  F:1,730
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_19SparseVarRegionListEEEEbP21hb_sanitize_context_tDpOT__251_24_T` — cmplog:0  n4:168
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_19SparseVarRegionListEEEEbP21hb_sanitize_context_tDpOT__251_24_F` — cmplog:42  n4:1,730

### 185. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0_` @ 864:42
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 40, n4: 793)
- **Flip strength**: 166 (blocked side hit 166× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:40  F:0
- **n4 coverage**: T:793  F:166
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0__864_42_T` — cmplog:40  n4:793
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0__864_42_F` — cmplog:0  n4:166

### 186. `_ZZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextEENKUlRKNS_9ChainRuleIS2_EEE0_clESC_` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 38, n4: 930)
- **Flip strength**: 156 (blocked side hit 156× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:38  F:0
- **n4 coverage**: T:930  F:156
- **Canonical identifiers**:
  - `harfbuzz__ZZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextEENKUlRKNS_9ChainRuleIS2_EEE0_clESC__350_45_T` — cmplog:38  n4:930
  - `harfbuzz__ZZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextEENKUlRKNS_9ChainRuleIS2_EEE0_clESC__350_45_F` — cmplog:0  n4:156

### 187. `_ZN11hb_buffer_t16try_allocate_varEjj` @ 159:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 162)
- **Flip strength**: 155 (blocked side hit 155× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:155  F:162
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t16try_allocate_varEjj_159_9_T` — cmplog:0  n4:155
  - `harfbuzz__ZN11hb_buffer_t16try_allocate_varEjj_159_9_F` — cmplog:5  n4:162

### 188. `_ZNK2OT33hb_ot_layout_lookup_accelerator_t11cache_enterEPNS_21hb_ot_apply_context_tE` @ 4490:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 162)
- **Flip strength**: 155 (blocked side hit 155× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:162  F:155
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT33hb_ot_layout_lookup_accelerator_t11cache_enterEPNS_21hb_ot_apply_context_tE_4490_5_T` — cmplog:5  n4:162
  - `harfbuzz__ZNK2OT33hb_ot_layout_lookup_accelerator_t11cache_enterEPNS_21hb_ot_apply_context_tE_4490_5_F` — cmplog:0  n4:155

### 189. `hb-ot-layout.cc:_ZN2OTL18context_cache_funcEPNS_21hb_ot_apply_context_tENS_25hb_ot_subtable_cache_op_tE` @ 2040:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 162)
- **Flip strength**: 155 (blocked side hit 155× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:155  F:162
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL18context_cache_funcEPNS_21hb_ot_apply_context_tENS_25hb_ot_subtable_cache_op_tE_2040_11_T` — cmplog:0  n4:155
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL18context_cache_funcEPNS_21hb_ot_apply_context_tENS_25hb_ot_subtable_cache_op_tE_2040_11_F` — cmplog:5  n4:162

### 190. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 313:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 153 (blocked side hit 153× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:153  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__313_7_T` — cmplog:0  n4:153
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__313_7_F` — cmplog:3,800,000  n4:71,000,000

### 191. `_ZNK2OT8OffsetToINS_9ColorLineINS_8VariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 24)
- **Flip strength**: 150 (blocked side hit 150× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:150  F:24
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_9ColorLineINS_8VariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv_251_24_T` — cmplog:0  n4:150
  - `harfbuzz__ZNK2OT8OffsetToINS_9ColorLineINS_8VariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv_251_24_F` — cmplog:12  n4:24

### 192. `_ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 3921:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19,400, n4: 401,000)
- **Flip strength**: 150 (blocked side hit 150× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19,400
- **n4 coverage**: T:150  F:401,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3921_9_T` — cmplog:0  n4:150
  - `harfbuzz__ZNK2OT21ChainContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_3921_9_F` — cmplog:19,400  n4:401,000

### 193. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 128:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 451)
- **Flip strength**: 144 (blocked side hit 144× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:144  F:451
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_128_9_T` — cmplog:0  n4:144
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_128_9_F` — cmplog:6  n4:451

### 194. `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0_` @ 147:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 111, n4: 220)
- **Flip strength**: 139 (blocked side hit 139× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:111  F:0
- **n4 coverage**: T:220  F:139
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__147_5_T` — cmplog:111  n4:220
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__147_5_F` — cmplog:0  n4:139

### 195. `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0_` @ 153:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 111, n4: 220)
- **Flip strength**: 139 (blocked side hit 139× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:111
- **n4 coverage**: T:139  F:220
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__153_5_T` — cmplog:0  n4:139
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__153_5_F` — cmplog:111  n4:220

### 196. `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12glyph_to_sidEjPNS2_11code_pair_tE` @ 1303:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,160, n4: 1,640)
- **Flip strength**: 137 (blocked side hit 137× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,160
- **n4 coverage**: T:137  F:1,640
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12glyph_to_sidEjPNS2_11code_pair_tE_1303_4_T` — cmplog:0  n4:137
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12glyph_to_sidEjPNS2_11code_pair_tE_1303_4_F` — cmplog:2,160  n4:1,640

### 197. `_ZNK3CFF12CFF2FDSelect6get_fdEj` @ 74:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,300, n4: 4,650)
- **Flip strength**: 135 (blocked side hit 135× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,300  F:0
- **n4 coverage**: T:4,650  F:135
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF12CFF2FDSelect6get_fdEj_74_9_T` — cmplog:1,300  n4:4,650
  - `harfbuzz__ZNK3CFF12CFF2FDSelect6get_fdEj_74_9_F` — cmplog:0  n4:135

### 198. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 902:45
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 4,130)
- **Flip strength**: 135 (blocked side hit 135× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:135  F:4,130
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_902_45_T` — cmplog:0  n4:135
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_902_45_F` — cmplog:3  n4:4,130

### 199. `_ZN14hb_transform_tIfE7skewingEff` @ 271:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 32, n4: 59)
- **Flip strength**: 132 (blocked side hit 132× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:32
- **n4 coverage**: T:132  F:59
- **Canonical identifiers**:
  - `harfbuzz__ZN14hb_transform_tIfE7skewingEff_271_42_T` — cmplog:0  n4:132
  - `harfbuzz__ZN14hb_transform_tIfE7skewingEff_271_42_F` — cmplog:32  n4:59

### 200. `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 871:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 340)
- **Flip strength**: 131 (blocked side hit 131× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:131  F:340
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__871_5_T` — cmplog:0  n4:131
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__871_5_F` — cmplog:15  n4:340

### 201. `_ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 140, n4: 152)
- **Flip strength**: 131 (blocked side hit 131× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:140  F:0
- **n4 coverage**: T:152  F:131
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv_251_24_T` — cmplog:140  n4:152
  - `harfbuzz__ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv_251_24_F` — cmplog:0  n4:131

### 202. `_ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv` @ 251:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 140, n4: 138)
- **Flip strength**: 131 (blocked side hit 131× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:140  F:0
- **n4 coverage**: T:138  F:131
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv_251_47_T` — cmplog:140  n4:138
  - `harfbuzz__ZN3CFF20cff2_cs_interp_env_tINS_8number_tEE15process_vsindexEv_251_47_F` — cmplog:0  n4:131

### 203. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1287:60
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18,000, n4: 116,000)
- **Flip strength**: 130 (blocked side hit 130× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18,000  F:0
- **n4 coverage**: T:116,000  F:130
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_60_T` — cmplog:18,000  n4:116,000
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1287_60_F` — cmplog:0  n4:130

### 204. `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1059:49
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 111, n4: 229)
- **Flip strength**: 130 (blocked side hit 130× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:111
- **n4 coverage**: T:130  F:229
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1059_49_T` — cmplog:0  n4:130
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1059_49_F` — cmplog:111  n4:229

### 205. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 127:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,310)
- **Flip strength**: 129 (blocked side hit 129× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:129  F:1,310
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__127_2_T` — cmplog:0  n4:129
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__127_2_F` — cmplog:258  n4:1,310

### 206. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3452:26
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 529, n4: 58,000)
- **Flip strength**: 129 (blocked side hit 129× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:529
- **n4 coverage**: T:129  F:58,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3452_26_T` — cmplog:0  n4:129
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3452_26_F` — cmplog:529  n4:58,000

### 207. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1284:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 64, n4: 450)
- **Flip strength**: 126 (blocked side hit 126× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:64  F:0
- **n4 coverage**: T:450  F:126
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1284_11_T` — cmplog:64  n4:450
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1284_11_F` — cmplog:0  n4:126

### 208. `_ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj` @ 437:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 551,000, n4: 6,000,000)
- **Flip strength**: 122 (blocked side hit 122× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:551,000
- **n4 coverage**: T:122  F:6,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj_437_9_T` — cmplog:0  n4:122
  - `harfbuzz__ZNK2OT9matcher_t9may_matchER15hb_glyph_info_tj_437_9_F` — cmplog:551,000  n4:6,000,000

### 209. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 273:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 120 (blocked side hit 120× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:120  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__273_7_T` — cmplog:0  n4:120
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__273_7_F` — cmplog:3,800,000  n4:71,000,000

### 210. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 138:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 478)
- **Flip strength**: 117 (blocked side hit 117× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:117  F:478
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_138_9_T` — cmplog:0  n4:117
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_138_9_F` — cmplog:6  n4:478

### 211. `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 873:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 356)
- **Flip strength**: 115 (blocked side hit 115× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:115  F:356
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__873_5_T` — cmplog:0  n4:115
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__873_5_F` — cmplog:15  n4:356

### 212. `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT_` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 1,050)
- **Flip strength**: 113 (blocked side hit 113× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:1,050  F:113
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT__251_24_T` — cmplog:3  n4:1,050
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT__251_24_F` — cmplog:0  n4:113

### 213. `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 872:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 359)
- **Flip strength**: 112 (blocked side hit 112× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:112  F:359
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__872_5_T` — cmplog:0  n4:112
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__872_5_F` — cmplog:15  n4:359

### 214. `_ZN11hb_buffer_t18merge_out_clustersEjj` @ 578:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 135)
- **Flip strength**: 112 (blocked side hit 112× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:112  F:135
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t18merge_out_clustersEjj_578_19_T` — cmplog:0  n4:112
  - `harfbuzz__ZN11hb_buffer_t18merge_out_clustersEjj_578_19_F` — cmplog:7  n4:135

### 215. `hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_simp_mapjEEEEbPKvjPj` @ 250:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 41, n4: 522)
- **Flip strength**: 112 (blocked side hit 112× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:41
- **n4 coverage**: T:112  F:522
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_simp_mapjEEEEbPKvjPj_250_22_T` — cmplog:0  n4:112
  - `harfbuzz_hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_simp_mapjEEEEbPKvjPj_250_22_F` — cmplog:41  n4:522

### 216. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1032:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 100, n4: 4,750)
- **Flip strength**: 108 (blocked side hit 108× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:100
- **n4 coverage**: T:108  F:4,750
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1032_4_T` — cmplog:0  n4:108
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1032_4_F` — cmplog:100  n4:4,750

### 217. `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t` @ 202:16
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18, n4: 200)
- **Flip strength**: 107 (blocked side hit 107× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:0
- **n4 coverage**: T:200  F:107
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_202_16_T` — cmplog:18  n4:200
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_202_16_F` — cmplog:0  n4:107

### 218. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE` @ 886:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 222,000)
- **Flip strength**: 106 (blocked side hit 106× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:106  F:222,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_886_18_T` — cmplog:0  n4:106
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_886_18_F` — cmplog:110,000  n4:222,000

### 219. `_ZNK2OT6Layout9GSUB_impl8LigatureINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 165:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,280, n4: 91,700)
- **Flip strength**: 103 (blocked side hit 103× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,280
- **n4 coverage**: T:103  F:91,700
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl8LigatureINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_165_9_T` — cmplog:0  n4:103
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl8LigatureINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_165_9_F` — cmplog:5,280  n4:91,700

### 220. `_ZNK3AAT4ankr10get_anchorEjjj` @ 68:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 102 (blocked side hit 102× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:110,000  F:0
- **n4 coverage**: T:111,000  F:102
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT4ankr10get_anchorEjjj_68_9_T` — cmplog:110,000  n4:111,000
  - `harfbuzz__ZNK3AAT4ankr10get_anchorEjjj_68_9_F` — cmplog:0  n4:102

### 221. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj` @ 670:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 102 (blocked side hit 102× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:102  F:111,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj_670_5_T` — cmplog:0  n4:102
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj_670_5_F` — cmplog:110,000  n4:111,000

### 222. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj` @ 675:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 102 (blocked side hit 102× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:110,000  F:0
- **n4 coverage**: T:111,000  F:102
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj_675_5_T` — cmplog:110,000  n4:111,000
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE9get_valueEjj_675_5_F` — cmplog:0  n4:102

### 223. `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE` @ 562:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 102 (blocked side hit 102× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:102  F:111,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_562_4_T` — cmplog:0  n4:102
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_562_4_F` — cmplog:110,000  n4:111,000

### 224. `_ZNK2OT8OffsetToIN3AAT6LookupINS0_INS_7ArrayOfINS1_6AnchorENS_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEEES6_vLb1EEclEPKv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 102 (blocked side hit 102× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:110,000  F:0
- **n4 coverage**: T:111,000  F:102
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToIN3AAT6LookupINS0_INS_7ArrayOfINS1_6AnchorENS_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEEES6_vLb1EEclEPKv_251_24_T` — cmplog:110,000  n4:111,000
  - `harfbuzz__ZNK2OT8OffsetToIN3AAT6LookupINS0_INS_7ArrayOfINS1_6AnchorENS_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEEES6_vLb1EEclEPKv_251_24_F` — cmplog:0  n4:102

### 225. `_ZNK2OT19KernSubTableFormat3INS_20KernOTSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 2)
- **Flip strength**: 101 (blocked side hit 101× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:101  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT19KernSubTableFormat3INS_20KernOTSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:0  n4:101
  - `harfbuzz__ZNK2OT19KernSubTableFormat3INS_20KernOTSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:1  n4:2

### 226. `_Z35hb_aat_layout_remove_deleted_glyphsP11hb_buffer_t` @ 339:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 461, n4: 2,340)
- **Flip strength**: 98 (blocked side hit 98× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:461
- **n4 coverage**: T:98  F:2,340
- **Canonical identifiers**:
  - `harfbuzz__Z35hb_aat_layout_remove_deleted_glyphsP11hb_buffer_t_339_7_T` — cmplog:0  n4:98
  - `harfbuzz__Z35hb_aat_layout_remove_deleted_glyphsP11hb_buffer_t_339_7_F` — cmplog:461  n4:2,340

### 227. `_ZN3CFF27cff2_priv_dict_interp_env_t15process_vsindexEv` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 19)
- **Flip strength**: 98 (blocked side hit 98× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:19  F:98
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF27cff2_priv_dict_interp_env_t15process_vsindexEv_250_22_T` — cmplog:2  n4:19
  - `harfbuzz__ZN3CFF27cff2_priv_dict_interp_env_t15process_vsindexEv_250_22_F` — cmplog:0  n4:98

### 228. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 314:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 23,900)
- **Flip strength**: 97 (blocked side hit 97× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:97  F:23,900
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_314_5_T` — cmplog:0  n4:97
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_314_5_F` — cmplog:8,290  n4:23,900

### 229. `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT_` @ 165:27
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 1,170)
- **Flip strength**: 96 (blocked side hit 96× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:1,170  F:96
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT__165_27_T` — cmplog:3  n4:1,170
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE16collect_coverageI15hb_set_digest_tEEbPT__165_27_F` — cmplog:0  n4:96

### 230. `_ZNK2OT6Layout9GPOS_impl16PairPosFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPv` @ 258:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 104, n4: 138)
- **Flip strength**: 96 (blocked side hit 96× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:104  F:0
- **n4 coverage**: T:138  F:96
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16PairPosFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPv_258_30_T` — cmplog:104  n4:138
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16PairPosFormat2_4INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tEPv_258_30_F` — cmplog:0  n4:96

### 231. `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j` @ 167:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 62, n4: 172)
- **Flip strength**: 96 (blocked side hit 96× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:62
- **n4 coverage**: T:96  F:172
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_167_5_T` — cmplog:0  n4:96
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_167_5_F` — cmplog:62  n4:172

### 232. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 321:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 12, n4: 43)
- **Flip strength**: 93 (blocked side hit 93× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:0
- **n4 coverage**: T:43  F:93
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_321_5_T` — cmplog:12  n4:43
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_321_5_F` — cmplog:0  n4:93

### 233. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE9get_entryEij` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 210, n4: 354,000)
- **Flip strength**: 90 (blocked side hit 90× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:210
- **n4 coverage**: T:90  F:354,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE9get_entryEij_251_24_T` — cmplog:0  n4:90
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE9get_entryEij_251_24_F` — cmplog:210  n4:354,000

### 234. `_ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE9call_subrERKNS_14biased_subrs_tIS6_EENS_9cs_type_tE` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,880, n4: 5,380)
- **Flip strength**: 90 (blocked side hit 90× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,880
- **n4 coverage**: T:90  F:5,380
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE9call_subrERKNS_14biased_subrs_tIS6_EENS_9cs_type_tE_251_47_T` — cmplog:0  n4:90
  - `harfbuzz__ZN3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE9call_subrERKNS_14biased_subrs_tIS6_EENS_9cs_type_tE_251_47_F` — cmplog:1,880  n4:5,380

### 235. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1154:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 71)
- **Flip strength**: 90 (blocked side hit 90× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:90  F:71
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1154_7_T` — cmplog:0  n4:90
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1154_7_F` — cmplog:1  n4:71

### 236. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 120:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,780)
- **Flip strength**: 89 (blocked side hit 89× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:89  F:2,780
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__120_2_T` — cmplog:0  n4:89
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__120_2_F` — cmplog:786  n4:2,780

### 237. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1866:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 7,930)
- **Flip strength**: 88 (blocked side hit 88× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:88  F:7,930
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1866_5_T` — cmplog:0  n4:88
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1866_5_F` — cmplog:1,800  n4:7,930

### 238. `_ZNK3AAT12LookupSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0_` @ 492:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 282, n4: 5,910)
- **Flip strength**: 87 (blocked side hit 87× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:282
- **n4 coverage**: T:87  F:5,910
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12LookupSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__492_9_T` — cmplog:0  n4:87
  - `harfbuzz__ZNK3AAT12LookupSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__492_9_F` — cmplog:282  n4:5,910

### 239. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 49)
- **Flip strength**: 87 (blocked side hit 87× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:49  F:87
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_251_24_T` — cmplog:1  n4:49
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_251_24_F` — cmplog:0  n4:87

### 240. `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_9ConditionENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj` @ 359:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 624, n4: 671)
- **Flip strength**: 87 (blocked side hit 87× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:624
- **n4 coverage**: T:87  F:671
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_9ConditionENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj_359_9_T` — cmplog:0  n4:87
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_9ConditionENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj_359_9_F` — cmplog:624  n4:671

### 241. `_ZN14hb_transform_tIfE7skewingEff` @ 271:16
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 32, n4: 108)
- **Flip strength**: 83 (blocked side hit 83× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:32  F:0
- **n4 coverage**: T:108  F:83
- **Canonical identifiers**:
  - `harfbuzz__ZN14hb_transform_tIfE7skewingEff_271_16_T` — cmplog:32  n4:108
  - `harfbuzz__ZN14hb_transform_tIfE7skewingEff_271_16_F` — cmplog:0  n4:83

### 242. `hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1_` @ 992:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 38, n4: 848)
- **Flip strength**: 82 (blocked side hit 82× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:38  F:0
- **n4 coverage**: T:848  F:82
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1__992_11_T` — cmplog:38  n4:848
  - `harfbuzz_hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1__992_11_F` — cmplog:0  n4:82

### 243. `_ZN2OT9glyf_impl20CompositeGlyphRecord9transformERA4_Kf10hb_array_tI15contour_point_tE` @ 94:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 398, n4: 2,850)
- **Flip strength**: 81 (blocked side hit 81× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:398
- **n4 coverage**: T:81  F:2,850
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT9glyf_impl20CompositeGlyphRecord9transformERA4_Kf10hb_array_tI15contour_point_tE_94_22_T` — cmplog:0  n4:81
  - `harfbuzz__ZN2OT9glyf_impl20CompositeGlyphRecord9transformERA4_Kf10hb_array_tI15contour_point_tE_94_22_F` — cmplog:398  n4:2,850

### 244. `_ZN3AAT21RearrangementSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_vNS2_5FlagsEEERKNS_5EntryIvEE` @ 153:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 35,900, n4: 441,000)
- **Flip strength**: 81 (blocked side hit 81× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:35,900
- **n4 coverage**: T:81  F:441,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT21RearrangementSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_vNS2_5FlagsEEERKNS_5EntryIvEE_153_8_T` — cmplog:0  n4:81
  - `harfbuzz__ZN3AAT21RearrangementSubtableINS_13ExtendedTypesEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverIS1_vNS2_5FlagsEEERKNS_5EntryIvEE_153_8_F` — cmplog:35,900  n4:441,000

### 245. `_ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE16collect_unicodesEP8hb_set_t` @ 797:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 227)
- **Flip strength**: 80 (blocked side hit 80× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:227  F:80
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE16collect_unicodesEP8hb_set_t_797_11_T` — cmplog:3  n4:227
  - `harfbuzz__ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE16collect_unicodesEP8hb_set_t_797_11_F` — cmplog:0  n4:80

### 246. `_ZNK2OT15VariationDevice11get_y_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE` @ 4867:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 11, n4: 4)
- **Flip strength**: 79 (blocked side hit 79× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11  F:0
- **n4 coverage**: T:4  F:79
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT15VariationDevice11get_y_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4867_12_T` — cmplog:11  n4:4
  - `harfbuzz__ZNK2OT15VariationDevice11get_y_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4867_12_F` — cmplog:0  n4:79

### 247. `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` @ 334:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 14, n4: 61)
- **Flip strength**: 78 (blocked side hit 78× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14  F:0
- **n4 coverage**: T:61  F:78
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__334_5_T` — cmplog:14  n4:61
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__334_5_F` — cmplog:0  n4:78

### 248. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1872:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 7,950)
- **Flip strength**: 76 (blocked side hit 76× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:76  F:7,950
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1872_5_T` — cmplog:0  n4:76
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1872_5_F` — cmplog:1,800  n4:7,950

### 249. `_ZNK3AAT12KerxSubTable8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS3_DpOT0_` @ 873:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 105, n4: 328)
- **Flip strength**: 75 (blocked side hit 75× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:105
- **n4 coverage**: T:75  F:328
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS3_DpOT0__873_5_T` — cmplog:0  n4:75
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS3_DpOT0__873_5_F` — cmplog:105  n4:328

### 250. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 344, n4: 1,120)
- **Flip strength**: 75 (blocked side hit 75× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:344
- **n4 coverage**: T:75  F:1,120
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_251_24_T` — cmplog:0  n4:75
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_251_24_F` — cmplog:344  n4:1,120

### 251. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 722)
- **Flip strength**: 72 (blocked side hit 72× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:72  F:722
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_T` — cmplog:0  n4:72
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_F` — cmplog:4  n4:722

### 252. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 120:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,370)
- **Flip strength**: 71 (blocked side hit 71× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:71  F:1,370
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__120_2_T` — cmplog:0  n4:71
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__120_2_F` — cmplog:258  n4:1,370

### 253. `hb-ot-layout.cc:_ZN2OTL12apply_lookupEPNS_21hb_ot_apply_context_tEjPjjPKNS_12LookupRecordEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,040, n4: 56,000)
- **Flip strength**: 71 (blocked side hit 71× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,040
- **n4 coverage**: T:71  F:56,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12apply_lookupEPNS_21hb_ot_apply_context_tEjPjjPKNS_12LookupRecordEj_251_24_T` — cmplog:0  n4:71
  - `harfbuzz_hb-ot-layout.cc:_ZN2OTL12apply_lookupEPNS_21hb_ot_apply_context_tEjPjjPKNS_12LookupRecordEj_251_24_F` — cmplog:5,040  n4:56,000

### 254. `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j` @ 887:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 41, n4: 179)
- **Flip strength**: 69 (blocked side hit 69× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:41
- **n4 coverage**: T:69  F:179
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_887_5_T` — cmplog:0  n4:69
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_887_5_F` — cmplog:41  n4:179

### 255. `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1038:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 235)
- **Flip strength**: 66 (blocked side hit 66× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:66  F:235
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1038_4_T` — cmplog:0  n4:66
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1038_4_F` — cmplog:6  n4:235

### 256. `_ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE` @ 3503:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 490, n4: 114,000)
- **Flip strength**: 66 (blocked side hit 66× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:490  F:0
- **n4 coverage**: T:114,000  F:66
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3503_30_T` — cmplog:490  n4:114,000
  - `harfbuzz__ZNK2OT12ChainRuleSetINS_6Layout10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tERKNS_30ChainContextApplyLookupContextE_3503_30_F` — cmplog:0  n4:66

### 257. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 920:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 847, n4: 22,300)
- **Flip strength**: 66 (blocked side hit 66× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:847
- **n4 coverage**: T:66  F:22,300
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_920_9_T` — cmplog:0  n4:66
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_920_9_F` — cmplog:847  n4:22,300

### 258. `hb_ot_layout_lookup_would_substitute` @ 1559:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 20, n4: 29,200)
- **Flip strength**: 65 (blocked side hit 65× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:20
- **n4 coverage**: T:65  F:29,200
- **Canonical identifiers**:
  - `harfbuzz_hb_ot_layout_lookup_would_substitute_1559_19_T` — cmplog:0  n4:65
  - `harfbuzz_hb_ot_layout_lookup_would_substitute_1559_19_F` — cmplog:20  n4:29,200

### 259. `_ZNK35hb_indic_would_substitute_feature_t16would_substituteEPKjjP9hb_face_t` @ 104:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 20, n4: 29,200)
- **Flip strength**: 65 (blocked side hit 65× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:20
- **n4 coverage**: T:65  F:29,200
- **Canonical identifiers**:
  - `harfbuzz__ZNK35hb_indic_would_substitute_feature_t16would_substituteEPKjjP9hb_face_t_104_11_T` — cmplog:0  n4:65
  - `harfbuzz__ZNK35hb_indic_would_substitute_feature_t16would_substituteEPKjjP9hb_face_t_104_11_F` — cmplog:20  n4:29,200

### 260. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 553:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 49, n4: 4,270)
- **Flip strength**: 65 (blocked side hit 65× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:49  F:0
- **n4 coverage**: T:4,270  F:65
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_553_9_T` — cmplog:49  n4:4,270
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_553_9_F` — cmplog:0  n4:65

### 261. `hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH_` @ 1206:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 69)
- **Flip strength**: 64 (blocked side hit 64× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:64  F:69
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH__1206_14_T` — cmplog:0  n4:64
  - `harfbuzz_hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH__1206_14_F` — cmplog:2  n4:69

### 262. `_ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7_` @ 263:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 69)
- **Flip strength**: 64 (blocked side hit 64× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:69  F:64
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7__263_9_T` — cmplog:2  n4:69
  - `harfbuzz__ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7__263_9_F` — cmplog:0  n4:64

### 263. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4_` @ 233:111
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 1,130)
- **Flip strength**: 64 (blocked side hit 64× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:1,130  F:64
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__233_111_T` — cmplog:2  n4:1,130
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__233_111_F` — cmplog:0  n4:64

### 264. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4_` @ 493:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 1,130)
- **Flip strength**: 64 (blocked side hit 64× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:1,130  F:64
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__493_9_T` — cmplog:2  n4:1,130
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4VARCEEEP9hb_blob_tS4__493_9_F` — cmplog:0  n4:64

### 265. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv` @ 1180:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 344, n4: 1,120)
- **Flip strength**: 61 (blocked side hit 61× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:344  F:0
- **n4 coverage**: T:1,120  F:61
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_1180_30_T` — cmplog:344  n4:1,120
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_1180_30_F` — cmplog:0  n4:61

### 266. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv` @ 1181:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 344, n4: 1,060)
- **Flip strength**: 61 (blocked side hit 61× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:344  F:0
- **n4 coverage**: T:1,060  F:61
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_1181_11_T` — cmplog:344  n4:1,060
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_11HBGlyphID16EEEE18last_is_terminatorEv_1181_11_F` — cmplog:0  n4:61

### 267. `hb-ot-layout.cc:_ZN2OT6LayoutL28propagate_attachment_offsetsEP19hb_glyph_position_tjj14hb_direction_tj` @ 287:38
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 153, n4: 1,530)
- **Flip strength**: 60 (blocked side hit 60× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:153  F:0
- **n4 coverage**: T:1,530  F:60
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN2OT6LayoutL28propagate_attachment_offsetsEP19hb_glyph_position_tjj14hb_direction_tj_287_38_T` — cmplog:153  n4:1,530
  - `harfbuzz_hb-ot-layout.cc:_ZN2OT6LayoutL28propagate_attachment_offsetsEP19hb_glyph_position_tjj14hb_direction_tj_287_38_F` — cmplog:0  n4:60

### 268. `_ZNK3AAT9KerxTableIN2OT6KernOTEE16has_cross_streamEv` @ 969:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 199)
- **Flip strength**: 60 (blocked side hit 60× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:60  F:199
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE16has_cross_streamEv_969_11_T` — cmplog:0  n4:60
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE16has_cross_streamEv_969_11_F` — cmplog:8  n4:199

### 269. `hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_trad_mapjEEEEbPKvjPj` @ 250:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 60, n4: 486)
- **Flip strength**: 59 (blocked side hit 59× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:60
- **n4 coverage**: T:59  F:486
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_trad_mapjEEEEbPKvjPj_250_22_T` — cmplog:0  n4:59
  - `harfbuzz_hb-face.cc:_ZN2OT4cmap13accelerator_t21get_glyph_from_symbolINS_12CmapSubtableEXadL_ZL23_hb_arabic_pua_trad_mapjEEEEbPKvjPj_250_22_F` — cmplog:60  n4:486

### 270. `_ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 1,570)
- **Flip strength**: 58 (blocked side hit 58× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:58  F:1,570
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_251_24_T` — cmplog:0  n4:58
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl12AlternateSetINS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_251_24_F` — cmplog:36  n4:1,570

### 271. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 148:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,590)
- **Flip strength**: 58 (blocked side hit 58× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:58  F:1,590
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_148_5_T` — cmplog:0  n4:58
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_148_5_F` — cmplog:389  n4:1,590

### 272. `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` @ 333:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 14, n4: 82)
- **Flip strength**: 57 (blocked side hit 57× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:14
- **n4 coverage**: T:57  F:82
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__333_5_T` — cmplog:0  n4:57
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__333_5_F` — cmplog:14  n4:82

### 273. `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii` @ 85:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10, n4: 579)
- **Flip strength**: 57 (blocked side hit 57× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10
- **n4 coverage**: T:57  F:579
- **Canonical identifiers**:
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_85_9_T` — cmplog:0  n4:57
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_85_9_F` — cmplog:10  n4:579

### 274. `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT17UnicodeValueRangeEEEbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 38, n4: 192)
- **Flip strength**: 57 (blocked side hit 57× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:38
- **n4 coverage**: T:57  F:192
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT17UnicodeValueRangeEEEbPKT_jj_251_24_T` — cmplog:0  n4:57
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT17UnicodeValueRangeEEEbPKT_jj_251_24_F` — cmplog:38  n4:192

### 275. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 320:13
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 80)
- **Flip strength**: 56 (blocked side hit 56× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:56  F:80
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_13_T` — cmplog:0  n4:56
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_13_F` — cmplog:12  n4:80

### 276. `_ZNK2OT9TTCHeader8get_faceEj` @ 260:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 120, n4: 1,030)
- **Flip strength**: 56 (blocked side hit 56× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:120
- **n4 coverage**: T:56  F:1,030
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9TTCHeader8get_faceEj_260_5_T` — cmplog:0  n4:56
  - `harfbuzz__ZNK2OT9TTCHeader8get_faceEj_260_5_F` — cmplog:120  n4:1,030

### 277. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 128:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,820)
- **Flip strength**: 55 (blocked side hit 55× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:55  F:2,820
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__128_2_T` — cmplog:0  n4:55
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__128_2_F` — cmplog:786  n4:2,820

### 278. `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 2705:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 548)
- **Flip strength**: 55 (blocked side hit 55× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:55  F:548
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2705_8_T` — cmplog:0  n4:55
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2705_8_F` — cmplog:36  n4:548

### 279. `_ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb` @ 2709:13
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 548)
- **Flip strength**: 55 (blocked side hit 55× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:55  F:548
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2709_13_T` — cmplog:0  n4:55
  - `harfbuzz__ZNK2OT16ContextFormat2_5INS_6Layout10SmallTypesEE6_applyEPNS_21hb_ot_apply_context_tEb_2709_13_F` — cmplog:36  n4:548

### 280. `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii` @ 84:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10, n4: 636)
- **Flip strength**: 55 (blocked side hit 55× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:0
- **n4 coverage**: T:636  F:55
- **Canonical identifiers**:
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_84_9_T` — cmplog:10  n4:636
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_84_9_F` — cmplog:0  n4:55

### 281. `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE16process_hintmaskEjRS4_RS5_` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18, n4: 13,900)
- **Flip strength**: 53 (blocked side hit 53× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:0
- **n4 coverage**: T:13,900  F:53
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE16process_hintmaskEjRS4_RS5__250_22_T` — cmplog:18  n4:13,900
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE16process_hintmaskEjRS4_RS5__250_22_F` — cmplog:0  n4:53

### 282. `_ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE23cff2_cs_opset_extents_t20cff2_extents_param_tE9interpretERS5_` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 83,700, n4: 11,800,000)
- **Flip strength**: 52 (blocked side hit 52× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:83,700
- **n4 coverage**: T:52  F:11,800,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE23cff2_cs_opset_extents_t20cff2_extents_param_tE9interpretERS5__251_47_T` — cmplog:0  n4:52
  - `harfbuzz__ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE23cff2_cs_opset_extents_t20cff2_extents_param_tE9interpretERS5__251_47_F` — cmplog:83,700  n4:11,800,000

### 283. `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj` @ 397:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,970, n4: 67,300)
- **Flip strength**: 52 (blocked side hit 52× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,970
- **n4 coverage**: T:52  F:67,300
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_397_7_T` — cmplog:0  n4:52
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_397_7_F` — cmplog:1,970  n4:67,300

### 284. `_ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_6Layout9GPOS_impl6AnchorENS1_7NumTypeILb1EtLj2EEENS4_12AnchorMatrixELb1EEEEEbPKT_jj` @ 340:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,760, n4: 7,910)
- **Flip strength**: 52 (blocked side hit 52× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,760  F:0
- **n4 coverage**: T:7,910  F:52
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_6Layout9GPOS_impl6AnchorENS1_7NumTypeILb1EtLj2EEENS4_12AnchorMatrixELb1EEEEEbPKT_jj_340_12_T` — cmplog:2,760  n4:7,910
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_6Layout9GPOS_impl6AnchorENS1_7NumTypeILb1EtLj2EEENS4_12AnchorMatrixELb1EEEEEbPKT_jj_340_12_F` — cmplog:0  n4:52

### 285. `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE` @ 560:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 110,000, n4: 111,000)
- **Flip strength**: 51 (blocked side hit 51× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:110,000
- **n4 coverage**: T:51  F:111,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_560_10_T` — cmplog:0  n4:51
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_560_10_F` — cmplog:110,000  n4:111,000

### 286. `_ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE` @ 618:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 51, n4: 51)
- **Flip strength**: 51 (blocked side hit 51× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:51
- **n4 coverage**: T:51  F:51
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_618_10_T` — cmplog:0  n4:51
  - `harfbuzz__ZN3AAT19KerxSubTableFormat4INS_18KerxSubTableHeaderEE16driver_context_t10transitionEP11hb_buffer_tPNS_16StateTableDriverINS_13ExtendedTypesENS2_9EntryDataENS2_5FlagsEEERKNS_5EntryIS8_EE_618_10_F` — cmplog:51  n4:51

### 287. `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j` @ 886:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 41, n4: 198)
- **Flip strength**: 50 (blocked side hit 50× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:41
- **n4 coverage**: T:50  F:198
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_886_5_T` — cmplog:0  n4:50
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_886_5_F` — cmplog:41  n4:198

### 288. `_ZNK2OT7ArrayOfINS_19SparseVarRegionAxisENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 42, n4: 1,090)
- **Flip strength**: 50 (blocked side hit 50× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:42  F:0
- **n4 coverage**: T:1,090  F:50
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_19SparseVarRegionAxisENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:42  n4:1,090
  - `harfbuzz__ZNK2OT7ArrayOfINS_19SparseVarRegionAxisENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:50

### 289. `_Z23hb_indic_get_categoriesj` @ 500:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 14)
- **Flip strength**: 50 (blocked side hit 50× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:50  F:14
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_500_11_T` — cmplog:0  n4:50
  - `harfbuzz__Z23hb_indic_get_categoriesj_500_11_F` — cmplog:3  n4:14

### 290. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv` @ 1180:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 517, n4: 52,400)
- **Flip strength**: 49 (blocked side hit 49× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:517  F:0
- **n4 coverage**: T:52,400  F:49
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1180_30_T` — cmplog:517  n4:52,400
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1180_30_F` — cmplog:0  n4:49

### 291. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv` @ 1181:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 517, n4: 52,300)
- **Flip strength**: 49 (blocked side hit 49× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:517  F:0
- **n4 coverage**: T:52,300  F:49
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1181_11_T` — cmplog:517  n4:52,300
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_1181_11_F` — cmplog:0  n4:49

### 292. `hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb` @ 250:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 206)
- **Flip strength**: 49 (blocked side hit 49× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:49  F:206
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb_250_22_T` — cmplog:0  n4:49
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL33handle_variation_selector_clusterPK31hb_ot_shape_normalize_context_tjb_250_22_F` — cmplog:13  n4:206

### 293. `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 287:38
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 35, n4: 1,080)
- **Flip strength**: 48 (blocked side hit 48× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:35  F:0
- **n4 coverage**: T:1,080  F:48
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_287_38_T` — cmplog:35  n4:1,080
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_287_38_F` — cmplog:0  n4:48

### 294. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 56:2
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 1)
- **Flip strength**: 48 (blocked side hit 48× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_56_2_T` — cmplog:1  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_56_2_F` — cmplog:0  n4:48

### 295. `_ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb` @ 854:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 12, n4: 89)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:0
- **n4 coverage**: T:89  F:47
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb_854_11_T` — cmplog:12  n4:89
  - `harfbuzz__ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb_854_11_F` — cmplog:0  n4:47

### 296. `_ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 875:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 424)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:47  F:424
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__875_5_T` — cmplog:0  n4:47
  - `harfbuzz__ZNK3AAT12KerxSubTable8dispatchINS_22hb_aat_apply_context_tEJEEENT_8return_tEPS3_DpOT0__875_5_F` — cmplog:15  n4:424

### 297. `_ZNK3AAT9KerxTableIN2OT7KernAATEE16has_cross_streamEv` @ 969:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 151)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:47  F:151
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE16has_cross_streamEv_969_11_T` — cmplog:0  n4:47
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE16has_cross_streamEv_969_11_F` — cmplog:3  n4:151

### 298. `hb-face.cc:_ZL10hb_bsearchIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjEPT_RKT0_S4_mmPFiPKvS9_E` @ 1227:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 567, n4: 1,370)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:567
- **n4 coverage**: T:47  F:1,370
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZL10hb_bsearchIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjEPT_RKT0_S4_mmPFiPKvS9_E_1227_10_T` — cmplog:0  n4:47
  - `harfbuzz_hb-face.cc:_ZL10hb_bsearchIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjEPT_RKT0_S4_mmPFiPKvS9_E_1227_10_F` — cmplog:567  n4:1,370

### 299. `hb-face.cc:_ZL15hb_bsearch_implIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC_` @ 1206:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,640, n4: 5,710)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,640  F:0
- **n4 coverage**: T:5,710  F:47
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZL15hb_bsearch_implIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_T` — cmplog:2,640  n4:5,710
  - `harfbuzz_hb-face.cc:_ZL15hb_bsearch_implIKZN2OTL19unicode_to_macromanEjE21unicode_to_macroman_tjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_F` — cmplog:0  n4:47

### 300. `hb-face.cc:_ZL16_hb_cmp_operatorIttEiPKvS1_` @ 1180:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,640, n4: 5,710)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,640  F:0
- **n4 coverage**: T:5,710  F:47
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZL16_hb_cmp_operatorIttEiPKvS1__1180_7_T` — cmplog:2,640  n4:5,710
  - `harfbuzz_hb-face.cc:_ZL16_hb_cmp_operatorIttEiPKvS1__1180_7_F` — cmplog:0  n4:47

### 301. `_ZN2OT4cmap13accelerator_t23get_glyph_from_macromanINS_12CmapSubtableEEEbPKvjPj` @ 2218:14
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 567, n4: 1,370)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:567
- **n4 coverage**: T:47  F:1,370
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cmap13accelerator_t23get_glyph_from_macromanINS_12CmapSubtableEEEbPKvjPj_2218_14_T` — cmplog:0  n4:47
  - `harfbuzz__ZN2OT4cmap13accelerator_t23get_glyph_from_macromanINS_12CmapSubtableEEEbPKvjPj_2218_14_F` — cmplog:567  n4:1,370

### 302. `hb-face.cc:_ZN2OTL19unicode_to_macromanEj` @ 184:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 567, n4: 1,370)
- **Flip strength**: 47 (blocked side hit 47× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:567
- **n4 coverage**: T:47  F:1,370
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZN2OTL19unicode_to_macromanEj_184_10_T` — cmplog:0  n4:47
  - `harfbuzz_hb-face.cc:_ZN2OTL19unicode_to_macromanEj_184_10_F` — cmplog:567  n4:1,370

### 303. `_ZNK2OT10SBIXStrike14get_glyph_blobEjP9hb_blob_tjPiS3_jPj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 51)
- **Flip strength**: 46 (blocked side hit 46× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:46  F:51
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT10SBIXStrike14get_glyph_blobEjP9hb_blob_tjPiS3_jPj_251_24_T` — cmplog:0  n4:46
  - `harfbuzz__ZNK2OT10SBIXStrike14get_glyph_blobEjP9hb_blob_tjPiS3_jPj_251_24_F` — cmplog:13  n4:51

### 304. `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0_` @ 153:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 255)
- **Flip strength**: 46 (blocked side hit 46× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:46  F:255
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__153_5_T` — cmplog:0  n4:46
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchIN3AAT22hb_aat_apply_context_tEJEEENT_8return_tEPS6_DpOT0__153_5_F` — cmplog:6  n4:255

### 305. `_ZNK2OT16DeltaSetIndexMap3mapEj` @ 3744:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 445, n4: 2,009)
- **Flip strength**: 46 (blocked side hit 46× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:445
- **n4 coverage**: T:46  F:2,009
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16DeltaSetIndexMap3mapEj_3744_5_T` — cmplog:0  n4:46
  - `harfbuzz__ZNK2OT16DeltaSetIndexMap3mapEj_3744_5_F` — cmplog:445  n4:2,009

### 306. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev` @ 462:38
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12,300, n4: 442,000)
- **Flip strength**: 45 (blocked side hit 45× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12,300
- **n4 coverage**: T:45  F:442,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev_462_38_T` — cmplog:0  n4:45
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev_462_38_F` — cmplog:12,300  n4:442,000

### 307. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev` @ 462:44
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 11,600, n4: 440,000)
- **Flip strength**: 45 (blocked side hit 45× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:11,600
- **n4 coverage**: T:45  F:440,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev_462_44_T` — cmplog:0  n4:45
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__next__Ev_462_44_F` — cmplog:11,600  n4:440,000

### 308. `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj` @ 189:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 3,340)
- **Flip strength**: 45 (blocked side hit 45× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:45  F:3,340
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_189_9_T` — cmplog:0  n4:45
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_189_9_F` — cmplog:27  n4:3,340

### 309. `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 137:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 50)
- **Flip strength**: 44 (blocked side hit 44× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:50  F:44
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_137_12_T` — cmplog:2  n4:50
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_137_12_F` — cmplog:0  n4:44

### 310. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 133:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 552)
- **Flip strength**: 43 (blocked side hit 43× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:552  F:43
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_133_9_T` — cmplog:6  n4:552
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_133_9_F` — cmplog:0  n4:43

### 311. `hb-ot-shaper-khmer.cc:_ZL17_hb_next_syllableP11hb_buffer_tj` @ 166:29
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15,500, n4: 84,600)
- **Flip strength**: 42 (blocked side hit 42× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15,500
- **n4 coverage**: T:42  F:84,600
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL17_hb_next_syllableP11hb_buffer_tj_166_29_T` — cmplog:0  n4:42
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL17_hb_next_syllableP11hb_buffer_tj_166_29_F` — cmplog:15,500  n4:84,600

### 312. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 704:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 236, n4: 126)
- **Flip strength**: 41 (blocked side hit 41× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:236  F:0
- **n4 coverage**: T:126  F:41
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_704_24_T` — cmplog:236  n4:126
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_704_24_F` — cmplog:0  n4:41

### 313. `_ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_cs_opset_path_t17cff2_path_param_tE9interpretERS5_` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 46,800, n4: 8,800,000)
- **Flip strength**: 39 (blocked side hit 39× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:46,800
- **n4 coverage**: T:39  F:8,800,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_cs_opset_path_t17cff2_path_param_tE9interpretERS5__251_47_T` — cmplog:0  n4:39
  - `harfbuzz__ZN3CFF16cs_interpreter_tINS_20cff2_cs_interp_env_tINS_8number_tEEE20cff2_cs_opset_path_t17cff2_path_param_tE9interpretERS5__251_47_F` — cmplog:46,800  n4:8,800,000

### 314. `_ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_EixEi` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 79, n4: 1,000)
- **Flip strength**: 39 (blocked side hit 39× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:79
- **n4 coverage**: T:39  F:1,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_EixEi_251_24_T` — cmplog:0  n4:39
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_EixEi_251_24_F` — cmplog:79  n4:1,000

### 315. `hb-ot-shaper-arabic.cc:_ZL12joining_typej` @ 208:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 23, n4: 49)
- **Flip strength**: 39 (blocked side hit 39× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:23
- **n4 coverage**: T:39  F:49
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_208_11_T` — cmplog:0  n4:39
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_208_11_F` — cmplog:23  n4:49

### 316. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1085:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16, n4: 8,960)
- **Flip strength**: 39 (blocked side hit 39× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16
- **n4 coverage**: T:39  F:8,960
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1085_22_T` — cmplog:0  n4:39
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1085_22_F` — cmplog:16  n4:8,960

### 317. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 128:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,400)
- **Flip strength**: 38 (blocked side hit 38× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:38  F:1,400
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__128_2_T` — cmplog:0  n4:38
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__128_2_F` — cmplog:258  n4:1,400

### 318. `_ZNK2OT7Context8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 2961:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 937, n4: 8,690)
- **Flip strength**: 38 (blocked side hit 38× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:937
- **n4 coverage**: T:38  F:8,690
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7Context8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS3_DpOT0__2961_5_T` — cmplog:0  n4:38
  - `harfbuzz__ZNK2OT7Context8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS3_DpOT0__2961_5_F` — cmplog:937  n4:8,690

### 319. `_ZN11hb_vector_tIfLb0EE6resizeEibb` @ 487:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,630, n4: 1,780,000)
- **Flip strength**: 38 (blocked side hit 38× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,630
- **n4 coverage**: T:38  F:1,780,000
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIfLb0EE6resizeEibb_487_9_T` — cmplog:0  n4:38
  - `harfbuzz__ZN11hb_vector_tIfLb0EE6resizeEibb_487_9_F` — cmplog:1,630  n4:1,780,000

### 320. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJEEEbP21hb_sanitize_context_tPKvDpOT_` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 51, n4: 574)
- **Flip strength**: 37 (blocked side hit 37× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:51  F:0
- **n4 coverage**: T:574  F:37
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJEEEbP21hb_sanitize_context_tPKvDpOT__350_45_T` — cmplog:51  n4:574
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl9MarkArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJEEEbP21hb_sanitize_context_tPKvDpOT__350_45_F` — cmplog:0  n4:37

### 321. `hb-ot-shaper-hebrew.cc:_ZL20reorder_marks_hebrewPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 173:32
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 130)
- **Flip strength**: 37 (blocked side hit 37× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:37  F:130
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL20reorder_marks_hebrewPK18hb_ot_shape_plan_tP11hb_buffer_tjj_173_32_T` — cmplog:0  n4:37
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL20reorder_marks_hebrewPK18hb_ot_shape_plan_tP11hb_buffer_tjj_173_32_F` — cmplog:6  n4:130

### 322. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 535:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 1,020)
- **Flip strength**: 37 (blocked side hit 37× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:37  F:1,020
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_535_24_T` — cmplog:0  n4:37
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_535_24_F` — cmplog:2  n4:1,020

### 323. `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl9MarkArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0_` @ 428:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 51, n4: 574)
- **Flip strength**: 37 (blocked side hit 37× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:51  F:0
- **n4 coverage**: T:574  F:37
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl9MarkArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_T` — cmplog:51  n4:574
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl9MarkArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_F` — cmplog:0  n4:37

### 324. `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 322:31
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 61)
- **Flip strength**: 36 (blocked side hit 36× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:36  F:61
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_322_31_T` — cmplog:0  n4:36
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_322_31_F` — cmplog:1  n4:61

### 325. `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT10UVSMappingEEEbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 108)
- **Flip strength**: 36 (blocked side hit 36× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:36  F:108
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT10UVSMappingEEEbPKT_jj_251_24_T` — cmplog:0  n4:36
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT10UVSMappingEEEbPKT_jj_251_24_F` — cmplog:27  n4:108

### 326. `_ZNK3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE8in_errorEv` @ 136:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10,200,000, n4: 169,000,000)
- **Flip strength**: 35 (blocked side hit 35× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10,200,000
- **n4 coverage**: T:35  F:169,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE8in_errorEv_136_12_T` — cmplog:0  n4:35
  - `harfbuzz__ZNK3CFF15cs_interp_env_tINS_8number_tENS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE8in_errorEv_136_12_F` — cmplog:10,200,000  n4:169,000,000

### 327. `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE16process_hintmaskEjRS4_RS5_` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 12, n4: 10,400)
- **Flip strength**: 35 (blocked side hit 35× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12  F:0
- **n4 coverage**: T:10,400  F:35
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE16process_hintmaskEjRS4_RS5__250_22_T` — cmplog:12  n4:10,400
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE16process_hintmaskEjRS4_RS5__250_22_F` — cmplog:0  n4:35

### 328. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 123:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,840)
- **Flip strength**: 35 (blocked side hit 35× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:35  F:2,840
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__123_2_T` — cmplog:0  n4:35
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__123_2_F` — cmplog:786  n4:2,840

### 329. `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 349:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 33)
- **Flip strength**: 35 (blocked side hit 35× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:35  F:33
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_349_9_T` — cmplog:0  n4:35
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_349_9_F` — cmplog:1  n4:33

### 330. `_ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE9get_glyphEjPj` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 82, n4: 980)
- **Flip strength**: 34 (blocked side hit 34× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:82  F:0
- **n4 coverage**: T:980  F:34
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE9get_glyphEjPj_251_24_T` — cmplog:82  n4:980
  - `harfbuzz__ZNK2OT19CmapSubtableTrimmedINS_7NumTypeILb1EjLj4EEEE9get_glyphEjPj_251_24_F` — cmplog:0  n4:34

### 331. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1855:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 7,990)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:32  F:7,990
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1855_5_T` — cmplog:0  n4:32
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1855_5_F` — cmplog:1,800  n4:7,990

### 332. `_ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj` @ 675:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 111,000, n4: 874,000)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:111,000
- **n4 coverage**: T:32  F:874,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_675_5_T` — cmplog:0  n4:32
  - `harfbuzz__ZNK3AAT6LookupIN2OT7NumTypeILb1EtLj2EEEE9get_valueEjj_675_5_F` — cmplog:111,000  n4:874,000

### 333. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 163:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 466, n4: 646)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:466
- **n4 coverage**: T:32  F:646
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_163_6_T` — cmplog:0  n4:32
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_163_6_F` — cmplog:466  n4:646

### 334. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 171:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 466, n4: 646)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:466
- **n4 coverage**: T:32  F:646
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_171_11_T` — cmplog:0  n4:32
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_171_11_F` — cmplog:466  n4:646

### 335. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 141:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 181)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:32  F:181
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_141_7_T` — cmplog:0  n4:32
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_141_7_F` — cmplog:5  n4:181

### 336. `_Z20find_syllables_khmerP11hb_buffer_t` @ 361:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 45,900)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:32  F:45,900
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_361_2_T` — cmplog:0  n4:32
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_361_2_F` — cmplog:8,260  n4:45,900

### 337. `hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 345:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,080, n4: 231,000)
- **Flip strength**: 32 (blocked side hit 32× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,080
- **n4 coverage**: T:32  F:231,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_345_11_T` — cmplog:0  n4:32
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_345_11_F` — cmplog:2,080  n4:231,000

### 338. `_ZNK2OT23MultiItemVariationStore8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 537)
- **Flip strength**: 31 (blocked side hit 31× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:537  F:31
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT23MultiItemVariationStore8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:537
  - `harfbuzz__ZNK2OT23MultiItemVariationStore8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:31

### 339. `_ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE` @ 159:13
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 19)
- **Flip strength**: 31 (blocked side hit 31× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:19  F:31
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE_159_13_T` — cmplog:2  n4:19
  - `harfbuzz__ZNK2OT20TupleVariationHeader16calculate_scalarE10hb_array_tIKiEjS1_IKNS_7HBFixedINS_7NumTypeILb1EsLj2EEELj14EEEEPNS_17hb_scalar_cache_tE_159_13_F` — cmplog:0  n4:31

### 340. `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1038:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 441)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:30  F:441
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1038_4_T` — cmplog:0  n4:30
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1038_4_F` — cmplog:15  n4:441

### 341. `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1054:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 441)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:30  F:441
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1054_11_T` — cmplog:0  n4:30
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1054_11_F` — cmplog:15  n4:441

### 342. `_ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1063:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 441)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:30  F:441
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1063_11_T` — cmplog:0  n4:30
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1063_11_F` — cmplog:15  n4:441

### 343. `hb-ot-shape.cc:_ZL20hb_set_unicode_propsP11hb_buffer_t` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 138,000, n4: 373,000)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:138,000
- **n4 coverage**: T:30  F:373,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL20hb_set_unicode_propsP11hb_buffer_t_251_47_T` — cmplog:0  n4:30
  - `harfbuzz_hb-ot-shape.cc:_ZL20hb_set_unicode_propsP11hb_buffer_t_251_47_F` — cmplog:138,000  n4:373,000

### 344. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1033:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:30  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1033_2_T` — cmplog:0  n4:30
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1033_2_F` — cmplog:2,020  n4:73,800

### 345. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1075:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 30 (blocked side hit 30× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:30  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1075_2_T` — cmplog:0  n4:30
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1075_2_F` — cmplog:2,020  n4:73,800

### 346. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0_` @ 872:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 92)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:29  F:92
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0__872_9_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tNS_16LigatureSubtableIS1_EEEEvRT_jRKT0__872_9_F` — cmplog:6  n4:92

### 347. `_ZNK10hb_array_tIKN2OT22MathGlyphVariantRecordEEneERKS3_` @ 132:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:29  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK10hb_array_tIKN2OT22MathGlyphVariantRecordEEneERKS3__132_12_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK10hb_array_tIKN2OT22MathGlyphVariantRecordEEneERKS3__132_12_F` — cmplog:6,150  n4:16,500

### 348. `_ZNK13hb_zip_iter_tI10hb_array_tIKN2OT22MathGlyphVariantRecordEES0_I26hb_ot_math_glyph_variant_tEEneERKS7_` @ 581:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:29  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK13hb_zip_iter_tI10hb_array_tIKN2OT22MathGlyphVariantRecordEES0_I26hb_ot_math_glyph_variant_tEEneERKS7__581_12_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK13hb_zip_iter_tI10hb_array_tIKN2OT22MathGlyphVariantRecordEES0_I26hb_ot_math_glyph_variant_tEEneERKS7__581_12_F` — cmplog:6,150  n4:16,500

### 349. `_ZNK2OT21MathGlyphConstruction12get_variantsE14hb_direction_tP9hb_font_tjPjP26hb_ot_math_glyph_variant_t` @ 849:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:29  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21MathGlyphConstruction12get_variantsE14hb_direction_tP9hb_font_tjPjP26hb_ot_math_glyph_variant_t_849_19_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK2OT21MathGlyphConstruction12get_variantsE14hb_direction_tP9hb_font_tjPjP26hb_ot_math_glyph_variant_t_849_19_F` — cmplog:6,150  n4:16,500

### 350. `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t` @ 394:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10, n4: 882)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10
- **n4 coverage**: T:29  F:882
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_394_7_T` — cmplog:0  n4:29
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_394_7_F` — cmplog:10  n4:882

### 351. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 711:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 147, n4: 35)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:147
- **n4 coverage**: T:29  F:35
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_711_6_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_711_6_F` — cmplog:147  n4:35

### 352. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 798:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 147, n4: 35)
- **Flip strength**: 29 (blocked side hit 29× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:147
- **n4 coverage**: T:29  F:35
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_798_6_T` — cmplog:0  n4:29
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_798_6_F` — cmplog:147  n4:35

### 353. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1268:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 34)
- **Flip strength**: 28 (blocked side hit 28× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:28  F:34
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1268_19_T` — cmplog:0  n4:28
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1268_19_F` — cmplog:6  n4:34

### 354. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0_` @ 1134:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 61)
- **Flip strength**: 28 (blocked side hit 28× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:28  F:61
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0__1134_42_T` — cmplog:0  n4:28
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0__1134_42_F` — cmplog:1  n4:61

### 355. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 600:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 354, n4: 50,000)
- **Flip strength**: 28 (blocked side hit 28× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:354
- **n4 coverage**: T:28  F:50,000
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_600_2_T` — cmplog:0  n4:28
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_600_2_F` — cmplog:354  n4:50,000

### 356. `_ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj` @ 250:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 347)
- **Flip strength**: 28 (blocked side hit 28× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:28  F:347
- **Canonical identifiers**:
  - `harfbuzz__ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj_250_22_T` — cmplog:0  n4:28
  - `harfbuzz__ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj_250_22_F` — cmplog:27  n4:347

### 357. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2_` @ 92:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,410,000, n4: 98,500,000)
- **Flip strength**: 27 (blocked side hit 27× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,410,000
- **n4 coverage**: T:27  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2__92_7_T` — cmplog:0  n4:27
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2__92_7_F` — cmplog:6,410,000  n4:98,500,000

### 358. `_ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j` @ 166:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 62, n4: 241)
- **Flip strength**: 27 (blocked side hit 27× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:62
- **n4 coverage**: T:27  F:241
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_166_5_T` — cmplog:0  n4:27
  - `harfbuzz__ZNK2OT12KernSubTableINS_20KernOTSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_166_5_F` — cmplog:62  n4:241

### 359. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 581:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 844, n4: 20,500)
- **Flip strength**: 27 (blocked side hit 27× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:844
- **n4 coverage**: T:27  F:20,500
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_581_8_T` — cmplog:0  n4:27
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_581_8_F` — cmplog:844  n4:20,500

### 360. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 242:16
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 123, n4: 1,790)
- **Flip strength**: 27 (blocked side hit 27× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:123
- **n4 coverage**: T:27  F:1,790
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_242_16_T` — cmplog:0  n4:27
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_242_16_F` — cmplog:123  n4:1,790

### 361. `_ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j` @ 889:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 41, n4: 222)
- **Flip strength**: 26 (blocked side hit 26× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:41
- **n4 coverage**: T:26  F:222
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_889_5_T` — cmplog:0  n4:26
  - `harfbuzz__ZNK3AAT12KerxSubTable14collect_glyphsI12hb_bit_set_tEEvRT_S4_j_889_5_F` — cmplog:41  n4:222

### 362. `_ZN3CFF14biased_subrs_tINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE4initEPKS5_` @ 69:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,270, n4: 9,410)
- **Flip strength**: 26 (blocked side hit 26× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,270  F:0
- **n4 coverage**: T:9,410  F:26
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF14biased_subrs_tINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE4initEPKS5__69_9_T` — cmplog:2,270  n4:9,410
  - `harfbuzz__ZN3CFF14biased_subrs_tINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEE4initEPKS5__69_9_F` — cmplog:0  n4:26

### 363. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 145:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,630)
- **Flip strength**: 26 (blocked side hit 26× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:26  F:1,630
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_145_5_T` — cmplog:0  n4:26
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_145_5_F` — cmplog:389  n4:1,630

### 364. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 776:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 4)
- **Flip strength**: 26 (blocked side hit 26× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:4  F:26
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_776_10_T` — cmplog:6  n4:4
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_776_10_F` — cmplog:0  n4:26

### 365. `_ZN22hb_serialize_context_t13check_successEb20hb_serialize_error_t` @ 258:13
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 11,800, n4: 17,100)
- **Flip strength**: 26 (blocked side hit 26× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11,800  F:0
- **n4 coverage**: T:17,100  F:26
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t13check_successEb20hb_serialize_error_t_258_13_T` — cmplog:11,800  n4:17,100
  - `harfbuzz__ZN22hb_serialize_context_t13check_successEb20hb_serialize_error_t_258_13_F` — cmplog:0  n4:26

### 366. `hb_script_get_horizontal_direction` @ 619:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 25 (blocked side hit 25× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:25  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_619_5_T` — cmplog:0  n4:25
  - `harfbuzz_hb_script_get_horizontal_direction_619_5_F` — cmplog:29,700  n4:79,800

### 367. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT_` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 84, n4: 487)
- **Flip strength**: 25 (blocked side hit 25× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:0
- **n4 coverage**: T:487  F:25
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT__350_45_T` — cmplog:84  n4:487
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl12AnchorMatrixENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT__350_45_F` — cmplog:0  n4:25

### 368. `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl12AnchorMatrixENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0_` @ 428:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 84, n4: 487)
- **Flip strength**: 25 (blocked side hit 25× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:84  F:0
- **n4 coverage**: T:487  F:25
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl12AnchorMatrixENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_T` — cmplog:84  n4:487
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl12AnchorMatrixENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_F` — cmplog:0  n4:25

### 369. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1879:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,000)
- **Flip strength**: 24 (blocked side hit 24× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:24  F:8,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1879_5_T` — cmplog:0  n4:24
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1879_5_F` — cmplog:1,800  n4:8,000

### 370. `_ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_23MultiItemVariationStoreEEEEbP21hb_sanitize_context_tDpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 1,550)
- **Flip strength**: 24 (blocked side hit 24× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:24  F:1,550
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_23MultiItemVariationStoreEEEEbP21hb_sanitize_context_tDpOT__251_24_T` — cmplog:0  n4:24
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE8sanitizeIJPKNS_23MultiItemVariationStoreEEEEbP21hb_sanitize_context_tDpOT__251_24_F` — cmplog:5  n4:1,550

### 371. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 116:16
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 19)
- **Flip strength**: 24 (blocked side hit 24× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:24  F:19
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_116_16_T` — cmplog:0  n4:24
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_116_16_F` — cmplog:3  n4:19

### 372. `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii` @ 60:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 93)
- **Flip strength**: 24 (blocked side hit 24× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:93  F:24
- **Canonical identifiers**:
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_60_7_T` — cmplog:6  n4:93
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_60_7_F` — cmplog:0  n4:24

### 373. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 123:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,420)
- **Flip strength**: 23 (blocked side hit 23× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:23  F:1,420
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__123_2_T` — cmplog:0  n4:23
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__123_2_F` — cmplog:258  n4:1,420

### 374. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1860:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,000)
- **Flip strength**: 22 (blocked side hit 22× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:22  F:8,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1860_5_T` — cmplog:0  n4:22
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1860_5_F` — cmplog:1,800  n4:8,000

### 375. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1862:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,000)
- **Flip strength**: 22 (blocked side hit 22× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:22  F:8,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1862_5_T` — cmplog:0  n4:22
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1862_5_F` — cmplog:1,800  n4:8,000

### 376. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 122:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,850)
- **Flip strength**: 22 (blocked side hit 22× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:22  F:2,850
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__122_2_T` — cmplog:0  n4:22
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__122_2_F` — cmplog:786  n4:2,850

### 377. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 260:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 969)
- **Flip strength**: 22 (blocked side hit 22× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:22  F:969
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_260_5_T` — cmplog:0  n4:22
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_260_5_F` — cmplog:237  n4:969

### 378. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 292:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 969)
- **Flip strength**: 22 (blocked side hit 22× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:22  F:969
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_292_5_T` — cmplog:0  n4:22
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_292_5_F` — cmplog:237  n4:969

### 379. `_ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1_` @ 332:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 14, n4: 118)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:14
- **n4 coverage**: T:21  F:118
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__332_5_T` — cmplog:0  n4:21
  - `harfbuzz__ZNK2OT13IndexSubtable14get_image_dataEjPjS1_S1__332_5_F` — cmplog:14  n4:118

### 380. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 320:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 115)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:21  F:115
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_5_T` — cmplog:0  n4:21
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_5_F` — cmplog:12  n4:115

### 381. `_ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 640)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:640  F:21
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:640
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_21SparseVariationRegionENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:21

### 382. `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0_` @ 155:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 193)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:21  F:193
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0__155_5_T` — cmplog:0  n4:21
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0__155_5_F` — cmplog:5  n4:193

### 383. `_ZNK2OT12MultiVarData8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 418)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:418  F:21
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12MultiVarData8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:5  n4:418
  - `harfbuzz__ZNK2OT12MultiVarData8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:21

### 384. `hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 226:38
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 504, n4: 1,480)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:504
- **n4 coverage**: T:21  F:1,480
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_226_38_T` — cmplog:0  n4:21
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_226_38_F` — cmplog:504  n4:1,480

### 385. `hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 231:36
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 504, n4: 1,480)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:504
- **n4 coverage**: T:21  F:1,480
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_231_36_T` — cmplog:0  n4:21
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL26reorder_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_231_36_F` — cmplog:504  n4:1,480

### 386. `hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 455:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 552)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:21  F:552
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_455_9_T` — cmplog:0  n4:21
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_455_9_F` — cmplog:130  n4:552

### 387. `_ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj` @ 250:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 27, n4: 375)
- **Flip strength**: 21 (blocked side hit 21× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:27  F:0
- **n4 coverage**: T:375  F:21
- **Canonical identifiers**:
  - `harfbuzz__ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj_250_45_T` — cmplog:27  n4:375
  - `harfbuzz__ZN13hb_utf16_xe_tIN2OT7NumTypeILb1EtLj2EEEE4nextEPKS2_S5_Pjj_250_45_F` — cmplog:0  n4:21

### 388. `_ZN11hb_buffer_t13shift_forwardEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,300, n4: 76,400)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,300
- **n4 coverage**: T:20  F:76,400
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t13shift_forwardEj_251_24_T` — cmplog:0  n4:20
  - `harfbuzz__ZN11hb_buffer_t13shift_forwardEj_251_24_F` — cmplog:18,300  n4:76,400

### 389. `_ZN11hb_buffer_t7move_toEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,070,000, n4: 15,200,000)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,070,000
- **n4 coverage**: T:20  F:15,200,000
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t7move_toEj_251_24_T` — cmplog:0  n4:20
  - `harfbuzz__ZN11hb_buffer_t7move_toEj_251_24_F` — cmplog:3,070,000  n4:15,200,000

### 390. `_ZN11hb_buffer_t7move_toEj` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,300, n4: 76,400)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,300
- **n4 coverage**: T:20  F:76,400
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t7move_toEj_251_47_T` — cmplog:0  n4:20
  - `harfbuzz__ZN11hb_buffer_t7move_toEj_251_47_F` — cmplog:18,300  n4:76,400

### 391. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2_` @ 92:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:20  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2__92_7_T` — cmplog:0  n4:20
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRNS_20cff1_cs_interp_env_tERS2__92_7_F` — cmplog:3,800,000  n4:71,000,000

### 392. `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0_` @ 153:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 194)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:20  F:194
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0__153_5_T` — cmplog:0  n4:20
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS5_DpOT0__153_5_F` — cmplog:5  n4:194

### 393. `_ZN2OT17hb_scalar_cache_t6createEjPS0_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 586, n4: 2,440)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:586
- **n4 coverage**: T:20  F:2,440
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT17hb_scalar_cache_t6createEjPS0__251_24_T` — cmplog:0  n4:20
  - `harfbuzz__ZN2OT17hb_scalar_cache_t6createEjPS0__251_24_F` — cmplog:586  n4:2,440

### 394. `_Z23hb_indic_get_categoriesj` @ 496:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 19, n4: 423)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:19
- **n4 coverage**: T:20  F:423
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_496_11_T` — cmplog:0  n4:20
  - `harfbuzz__Z23hb_indic_get_categoriesj_496_11_F` — cmplog:19  n4:423

### 395. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 450:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 160)
- **Flip strength**: 20 (blocked side hit 20× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:160  F:20
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_450_10_T` — cmplog:15  n4:160
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_450_10_F` — cmplog:0  n4:20

### 396. `_ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 146, n4: 532)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:146  F:0
- **n4 coverage**: T:532  F:19
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:146  n4:532
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:19

### 397. `_ZN3CFF18dict_interpreter_tINS_22cff1_font_dict_opset_tENS_23cff1_font_dict_values_tENS_12interp_env_tINS_8number_tEEEE9interpretERS2_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,890, n4: 4,590)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,890
- **n4 coverage**: T:19  F:4,590
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF18dict_interpreter_tINS_22cff1_font_dict_opset_tENS_23cff1_font_dict_values_tENS_12interp_env_tINS_8number_tEEEE9interpretERS2__251_24_T` — cmplog:0  n4:19
  - `harfbuzz__ZN3CFF18dict_interpreter_tINS_22cff1_font_dict_opset_tENS_23cff1_font_dict_values_tENS_12interp_env_tINS_8number_tEEEE9interpretERS2__251_24_F` — cmplog:2,890  n4:4,590

### 398. `_ZNK14hb_transform_tIfE11is_identityEv` @ 120:23
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 177,000)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:177,000  F:19
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_120_23_T` — cmplog:6  n4:177,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_120_23_F` — cmplog:0  n4:19

### 399. `_ZNK14hb_transform_tIfE11is_identityEv` @ 121:16
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 177,000)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:177,000  F:19
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_121_16_T` — cmplog:6  n4:177,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_121_16_F` — cmplog:0  n4:19

### 400. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 824:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9, n4: 6,230)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9
- **n4 coverage**: T:19  F:6,230
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_824_11_T` — cmplog:0  n4:19
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_824_11_F` — cmplog:9  n4:6,230

### 401. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1017:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:19  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1017_2_T` — cmplog:0  n4:19
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1017_2_F` — cmplog:2,020  n4:73,800

### 402. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 452:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 161)
- **Flip strength**: 19 (blocked side hit 19× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:19  F:161
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_452_4_T` — cmplog:0  n4:19
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_452_4_F` — cmplog:15  n4:161

### 403. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1865:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,000)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:18  F:8,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1865_5_T` — cmplog:0  n4:18
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1865_5_F` — cmplog:1,800  n4:8,000

### 404. `_ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb` @ 333:39
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 154, n4: 498)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:154
- **n4 coverage**: T:18  F:498
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb_333_39_T` — cmplog:0  n4:18
  - `harfbuzz__ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb_333_39_F` — cmplog:154  n4:498

### 405. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0_` @ 1134:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 71)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:18  F:71
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0__1134_10_T` — cmplog:0  n4:18
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0__1134_10_F` — cmplog:1  n4:71

### 406. `_ZNK2OT8OffsetToINS_9ColorLineINS_10NoVariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 138)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:138  F:18
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_9ColorLineINS_10NoVariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv_251_24_T` — cmplog:6  n4:138
  - `harfbuzz__ZNK2OT8OffsetToINS_9ColorLineINS_10NoVariableEEENS_7NumTypeILb1EjLj3EEEvLb1EEclEPKv_251_24_F` — cmplog:0  n4:18

### 407. `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j` @ 167:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 161)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:18  F:161
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_167_5_T` — cmplog:0  n4:18
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_167_5_F` — cmplog:3  n4:161

### 408. `hb-ot-layout.cc:_ZL12apply_stringI9GSUBProxyEbPN2OT21hb_ot_apply_context_tERKNT_6LookupERKNS1_33hb_ot_layout_lookup_accelerator_tE` @ 1978:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2,410, n4: 16,900)
- **Flip strength**: 18 (blocked side hit 18× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2,410  F:0
- **n4 coverage**: T:16,900  F:18
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZL12apply_stringI9GSUBProxyEbPN2OT21hb_ot_apply_context_tERKNT_6LookupERKNS1_33hb_ot_layout_lookup_accelerator_tE_1978_7_T` — cmplog:2,410  n4:16,900
  - `harfbuzz_hb-ot-layout.cc:_ZL12apply_stringI9GSUBProxyEbPN2OT21hb_ot_apply_context_tERKNT_6LookupERKNS1_33hb_ot_layout_lookup_accelerator_tE_1978_7_F` — cmplog:0  n4:18

### 409. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 121:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,860)
- **Flip strength**: 17 (blocked side hit 17× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:17  F:2,860
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__121_2_T` — cmplog:0  n4:17
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__121_2_F` — cmplog:786  n4:2,860

### 410. `_ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 124:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 786, n4: 2,860)
- **Flip strength**: 17 (blocked side hit 17× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:786
- **n4 coverage**: T:17  F:2,860
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__124_2_T` — cmplog:0  n4:17
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI23cff1_cs_opset_extents_t20cff1_extents_param_t25cff1_path_procs_extents_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__124_2_F` — cmplog:786  n4:2,860

### 411. `_ZN22hb_serialize_context_t4pushIN2OT6Layout9GSUB_impl11SubstLookupEEEPT_v` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 473, n4: 779)
- **Flip strength**: 17 (blocked side hit 17× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:473
- **n4 coverage**: T:17  F:779
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t4pushIN2OT6Layout9GSUB_impl11SubstLookupEEEPT_v_251_24_T` — cmplog:0  n4:17
  - `harfbuzz__ZN22hb_serialize_context_t4pushIN2OT6Layout9GSUB_impl11SubstLookupEEEPT_v_251_24_F` — cmplog:473  n4:779

### 412. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1854:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:16  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1854_5_T` — cmplog:0  n4:16
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1854_5_F` — cmplog:1,800  n4:8,010

### 413. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1874:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:16  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1874_5_T` — cmplog:0  n4:16
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1874_5_F` — cmplog:1,800  n4:8,010

### 414. `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 949:37
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 65)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:65  F:16
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_949_37_T` — cmplog:7  n4:65
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_949_37_F` — cmplog:0  n4:16

### 415. `_ZNK3AAT18ContextualSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 30)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:30  F:16
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT18ContextualSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t_251_24_T` — cmplog:6  n4:30
  - `harfbuzz__ZNK3AAT18ContextualSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t_251_24_F` — cmplog:0  n4:16

### 416. `_ZNK10hb_array_tIKN2OT19MathGlyphPartRecordEEneERKS3_` @ 132:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:16  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK10hb_array_tIKN2OT19MathGlyphPartRecordEEneERKS3__132_12_T` — cmplog:0  n4:16
  - `harfbuzz__ZNK10hb_array_tIKN2OT19MathGlyphPartRecordEEneERKS3__132_12_F` — cmplog:6,150  n4:16,500

### 417. `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5_` @ 338:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 77,700, n4: 11,700,000)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:77,700
- **n4 coverage**: T:16  F:11,700,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5__338_7_T` — cmplog:0  n4:16
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5__338_7_F` — cmplog:77,700  n4:11,700,000

### 418. `_ZNK13hb_zip_iter_tI10hb_array_tIKN2OT19MathGlyphPartRecordEES0_I23hb_ot_math_glyph_part_tEEneERKS7_` @ 581:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:16  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK13hb_zip_iter_tI10hb_array_tIKN2OT19MathGlyphPartRecordEES0_I23hb_ot_math_glyph_part_tEEneERKS7__581_12_T` — cmplog:0  n4:16
  - `harfbuzz__ZNK13hb_zip_iter_tI10hb_array_tIKN2OT19MathGlyphPartRecordEES0_I23hb_ot_math_glyph_part_tEEneERKS7__581_12_F` — cmplog:6,150  n4:16,500

### 419. `_ZNK2OT8OffsetToINS_17MathGlyphAssemblyENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18,400, n4: 49,600)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18,400  F:0
- **n4 coverage**: T:49,600  F:16
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_17MathGlyphAssemblyENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_T` — cmplog:18,400  n4:49,600
  - `harfbuzz__ZNK2OT8OffsetToINS_17MathGlyphAssemblyENS_7NumTypeILb1EtLj2EEEvLb1EEclEPKv_251_24_F` — cmplog:0  n4:16

### 420. `_ZNK2OT17MathGlyphAssembly9get_partsE14hb_direction_tP9hb_font_tjPjP23hb_ot_math_glyph_part_tPi` @ 780:19
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:16  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT17MathGlyphAssembly9get_partsE14hb_direction_tP9hb_font_tjPjP23hb_ot_math_glyph_part_tPi_780_19_T` — cmplog:0  n4:16
  - `harfbuzz__ZNK2OT17MathGlyphAssembly9get_partsE14hb_direction_tP9hb_font_tjPjP23hb_ot_math_glyph_part_tPi_780_19_F` — cmplog:6,150  n4:16,500

### 421. `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t` @ 393:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10, n4: 911)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10
- **n4 coverage**: T:16  F:911
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_393_7_T` — cmplog:0  n4:16
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_393_7_F` — cmplog:10  n4:911

### 422. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 687:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 240, n4: 159)
- **Flip strength**: 16 (blocked side hit 16× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:240  F:0
- **n4 coverage**: T:159  F:16
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_687_6_T` — cmplog:240  n4:159
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_687_6_F` — cmplog:0  n4:16

### 423. `_ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j` @ 168:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 164)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:15  F:164
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_168_5_T` — cmplog:0  n4:15
  - `harfbuzz__ZNK2OT12KernSubTableINS_21KernAATSubTableHeaderEE14collect_glyphsI12hb_bit_set_tEEvRT_S6_j_168_5_F` — cmplog:3  n4:164

### 424. `hb-ot-shape-fallback.cc:_ZL20position_around_basePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tjjb` @ 387:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 238, n4: 997)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:238  F:0
- **n4 coverage**: T:997  F:15
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL20position_around_basePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tjjb_387_11_T` — cmplog:238  n4:997
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL20position_around_basePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tjjb_387_11_F` — cmplog:0  n4:15

### 425. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1001:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 15 (blocked side hit 15× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:15  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1001_2_T` — cmplog:0  n4:15
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1001_2_F` — cmplog:2,020  n4:73,800

### 426. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1864:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:14  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1864_5_T` — cmplog:0  n4:14
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1864_5_F` — cmplog:1,800  n4:8,010

### 427. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1876:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:14  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1876_5_T` — cmplog:0  n4:14
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1876_5_F` — cmplog:1,800  n4:8,010

### 428. `_ZNK2OT12LigCaretList14get_lig_caretsEP9hb_font_t14hb_direction_tjRKNS_18ItemVariationStoreEjPjPi` @ 380:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,150  F:0
- **n4 coverage**: T:16,500  F:14
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT12LigCaretList14get_lig_caretsEP9hb_font_t14hb_direction_tjRKNS_18ItemVariationStoreEjPjPi_380_9_T` — cmplog:6,150  n4:16,500
  - `harfbuzz__ZNK2OT12LigCaretList14get_lig_caretsEP9hb_font_t14hb_direction_tjRKNS_18ItemVariationStoreEjPjPi_380_9_F` — cmplog:0  n4:14

### 429. `_ZNK3AAT10StateTableINS_13ExtendedTypesEvE22collect_initial_glyphsI12hb_bit_set_tNS_21RearrangementSubtableIS1_EEEEvRT_jRKT0_` @ 872:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 26, n4: 131)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:26
- **n4 coverage**: T:14  F:131
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesEvE22collect_initial_glyphsI12hb_bit_set_tNS_21RearrangementSubtableIS1_EEEEvRT_jRKT0__872_9_T` — cmplog:0  n4:14
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesEvE22collect_initial_glyphsI12hb_bit_set_tNS_21RearrangementSubtableIS1_EEEEvRT_jRKT0__872_9_F` — cmplog:26  n4:131

### 430. `_ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE11get_kerningEjjPNS_22hb_aat_apply_context_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 160)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:14  F:160
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE11get_kerningEjjPNS_22hb_aat_apply_context_tE_251_24_T` — cmplog:0  n4:14
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE11get_kerningEjjPNS_22hb_aat_apply_context_tE_251_24_F` — cmplog:7  n4:160

### 431. `hb-paint-extents.cc:_ZNK3$_0clIRfRKfEEDTqugefp_fp0_fp_fp0_EOT_OT0_` @ 76:55
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 10)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:10  F:14
- **Canonical identifiers**:
  - `harfbuzz_hb-paint-extents.cc:_ZNK3$_0clIRfRKfEEDTqugefp_fp0_fp_fp0_EOT_OT0__76_55_T` — cmplog:4  n4:10
  - `harfbuzz_hb-paint-extents.cc:_ZNK3$_0clIRfRKfEEDTqugefp_fp0_fp_fp0_EOT_OT0__76_55_F` — cmplog:0  n4:14

### 432. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 129:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,640)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:14  F:1,640
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_129_5_T` — cmplog:0  n4:14
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_129_5_F` — cmplog:389  n4:1,640

### 433. `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t` @ 391:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10, n4: 927)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10
- **n4 coverage**: T:14  F:927
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_391_7_T` — cmplog:0  n4:14
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_391_7_F` — cmplog:10  n4:927

### 434. `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` @ 77:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 225, n4: 2,220)
- **Flip strength**: 14 (blocked side hit 14× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:225
- **n4 coverage**: T:14  F:2,220
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_77_7_T` — cmplog:0  n4:14
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_77_7_F` — cmplog:225  n4:2,220

### 435. `_ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 116:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 515)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:515  F:13
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_116_11_T` — cmplog:3  n4:515
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_116_11_F` — cmplog:0  n4:13

### 436. `_ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0_` @ 37:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 554, n4: 3,080)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:554
- **n4 coverage**: T:13  F:3,080
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0__37_5_T` — cmplog:0  n4:13
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0__37_5_F` — cmplog:554  n4:3,080

### 437. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 324)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:13  F:324
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_T` — cmplog:0  n4:13
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_F` — cmplog:15  n4:324

### 438. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_12Format1EntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 122)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:13  F:122
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_12Format1EntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_T` — cmplog:0  n4:13
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_12Format1EntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_F` — cmplog:1  n4:122

### 439. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 122:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,430)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:13  F:1,430
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__122_2_T` — cmplog:0  n4:13
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__122_2_F` — cmplog:258  n4:1,430

### 440. `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,150, n4: 1,850)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,150
- **n4 coverage**: T:13  F:1,850
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_251_24_T` — cmplog:0  n4:13
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_251_24_F` — cmplog:1,150  n4:1,850

### 441. `hb-ot-shaper-arabic.cc:_ZL12joining_typej` @ 207:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 23, n4: 88)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:23
- **n4 coverage**: T:13  F:88
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_207_11_T` — cmplog:0  n4:13
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_207_11_F` — cmplog:23  n4:88

### 442. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 640:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 354, n4: 50,000)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:354
- **n4 coverage**: T:13  F:50,000
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_640_2_T` — cmplog:0  n4:13
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_640_2_F` — cmplog:354  n4:50,000

### 443. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 226:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 540, n4: 1,720)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:540  F:0
- **n4 coverage**: T:1,720  F:13
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_226_10_T` — cmplog:540  n4:1,720
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_226_10_F` — cmplog:0  n4:13

### 444. `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_13LigatureEntryILb1EE9EntryDataEEEEEbPKT_jj` @ 341:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 324)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:324  F:13
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_13LigatureEntryILb1EE9EntryDataEEEEEbPKT_jj_341_5_T` — cmplog:15  n4:324
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_13LigatureEntryILb1EE9EntryDataEEEEEbPKT_jj_341_5_F` — cmplog:0  n4:13

### 445. `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_12Format1EntryILb1EE9EntryDataEEEEEbPKT_jj` @ 341:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 122)
- **Flip strength**: 13 (blocked side hit 13× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:122  F:13
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_12Format1EntryILb1EE9EntryDataEEEEEbPKT_jj_341_5_T` — cmplog:1  n4:122
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_12Format1EntryILb1EE9EntryDataEEEEEbPKT_jj_341_5_F` — cmplog:0  n4:13

### 446. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1880:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:12  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1880_5_T` — cmplog:0  n4:12
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1880_5_F` — cmplog:1,800  n4:8,010

### 447. `_ZN2OT6Layout9GSUB_impl11LigatureSetINS0_10SmallTypesEE9serializeEP22hb_serialize_context_t10hb_array_tIKNS_11HBGlyphID16EES7_IKjERSA_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,980, n4: 7,490)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,980
- **n4 coverage**: T:12  F:7,490
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11LigatureSetINS0_10SmallTypesEE9serializeEP22hb_serialize_context_t10hb_array_tIKNS_11HBGlyphID16EES7_IKjERSA__251_24_T` — cmplog:0  n4:12
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11LigatureSetINS0_10SmallTypesEE9serializeEP22hb_serialize_context_t10hb_array_tIKNS_11HBGlyphID16EES7_IKjERSA__251_24_F` — cmplog:5,980  n4:7,490

### 448. `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1014:34
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9, n4: 506)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9
- **n4 coverage**: T:12  F:506
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1014_34_T` — cmplog:0  n4:12
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1014_34_F` — cmplog:9  n4:506

### 449. `_ZNK10hb_array_tIKcE11check_rangeIN2OT7NumTypeILb1EtLj2EEELj1ETnPN12hb_enable_ifIXeqT0_Li1EEvE4typeELPv0EEEbPKT_j` @ 291:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,570, n4: 55,000)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,570  F:0
- **n4 coverage**: T:55,000  F:12
- **Canonical identifiers**:
  - `harfbuzz__ZNK10hb_array_tIKcE11check_rangeIN2OT7NumTypeILb1EtLj2EEELj1ETnPN12hb_enable_ifIXeqT0_Li1EEvE4typeELPv0EEEbPKT_j_291_5_T` — cmplog:1,570  n4:55,000
  - `harfbuzz__ZNK10hb_array_tIKcE11check_rangeIN2OT7NumTypeILb1EtLj2EEELj1ETnPN12hb_enable_ifIXeqT0_Li1EEvE4typeELPv0EEEbPKT_j_291_5_F` — cmplog:0  n4:12

### 450. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 121:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,430)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:12  F:1,430
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__121_2_T` — cmplog:0  n4:12
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__121_2_F` — cmplog:258  n4:1,430

### 451. `_ZN11hb_bounds_tIfE9intersectERKS0_` @ 336:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4,520, n4: 512)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4,520
- **n4 coverage**: T:12  F:512
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__336_9_T` — cmplog:0  n4:12
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__336_9_F` — cmplog:4,520  n4:512

### 452. `_ZNK2OT9TTCHeader8sanitizeEP21hb_sanitize_context_t` @ 272:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 101)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:12  F:101
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9TTCHeader8sanitizeEP21hb_sanitize_context_t_272_5_T` — cmplog:0  n4:12
  - `harfbuzz__ZNK2OT9TTCHeader8sanitizeEP21hb_sanitize_context_t_272_5_F` — cmplog:5  n4:101

### 453. `_ZN2OT8OffsetToINS_6Layout9GSUB_impl8LigatureINS1_10SmallTypesEEENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJRKNS_11HBGlyphID16E10hb_array_tISB_EEEEbP22hb_serialize_context_tDpOT_` @ 469:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5,980, n4: 7,490)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5,980  F:0
- **n4 coverage**: T:7,490  F:12
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT8OffsetToINS_6Layout9GSUB_impl8LigatureINS1_10SmallTypesEEENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJRKNS_11HBGlyphID16E10hb_array_tISB_EEEEbP22hb_serialize_context_tDpOT__469_9_T` — cmplog:5,980  n4:7,490
  - `harfbuzz__ZN2OT8OffsetToINS_6Layout9GSUB_impl8LigatureINS1_10SmallTypesEEENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJRKNS_11HBGlyphID16E10hb_array_tISB_EEEEbP22hb_serialize_context_tDpOT__469_9_F` — cmplog:0  n4:12

### 454. `_ZNK2OT6Device11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE` @ 4933:13
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 43,000, n4: 116,000)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:43,000
- **n4 coverage**: T:12  F:116,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Device11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4933_13_T` — cmplog:0  n4:12
  - `harfbuzz__ZNK2OT6Device11get_x_deltaEP9hb_font_tRKNS_18ItemVariationStoreEPNS_17hb_scalar_cache_tE_4933_13_F` — cmplog:43,000  n4:116,000

### 455. `_ZNK2OT9Condition8evaluateINS_21ItemVarStoreInstancerEEEbPKijPT_` @ 4212:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 769, n4: 546)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:769
- **n4 coverage**: T:12  F:546
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9Condition8evaluateINS_21ItemVarStoreInstancerEEEbPKijPT__4212_5_T` — cmplog:0  n4:12
  - `harfbuzz__ZNK2OT9Condition8evaluateINS_21ItemVarStoreInstancerEEEbPKijPT__4212_5_F` — cmplog:769  n4:546

### 456. `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t` @ 35:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 140, n4: 573)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:140
- **n4 coverage**: T:12  F:573
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_35_5_T` — cmplog:0  n4:12
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_35_5_F` — cmplog:140  n4:573

### 457. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 365:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 12 (blocked side hit 12× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:12  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_365_5_T` — cmplog:0  n4:12
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_365_5_F` — cmplog:8,290  n4:24,000

### 458. `_ZNK2OT23IndexSubtableFormat1Or3INS_7NumTypeILb1EjLj4EEEE8sanitizeEP21hb_sanitize_context_tj` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 21, n4: 38)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:21  F:0
- **n4 coverage**: T:38  F:11
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT23IndexSubtableFormat1Or3INS_7NumTypeILb1EjLj4EEEE8sanitizeEP21hb_sanitize_context_tj_350_45_T` — cmplog:21  n4:38
  - `harfbuzz__ZNK2OT23IndexSubtableFormat1Or3INS_7NumTypeILb1EjLj4EEEE8sanitizeEP21hb_sanitize_context_tj_350_45_F` — cmplog:0  n4:11

### 459. `_ZN12hb_bit_set_t9add_rangeEjj` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 99,700, n4: 54,900)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:99,700
- **n4 coverage**: T:11  F:54,900
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_bit_set_t9add_rangeEjj_251_47_T` — cmplog:0  n4:11
  - `harfbuzz__ZN12hb_bit_set_t9add_rangeEjj_251_47_F` — cmplog:99,700  n4:54,900

### 460. `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5_` @ 338:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 43,600, n4: 8,790,000)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:43,600
- **n4 coverage**: T:11  F:8,790,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5__338_7_T` — cmplog:0  n4:11
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5__338_7_F` — cmplog:43,600  n4:8,790,000

### 461. `_ZNK14hb_transform_tIfE11is_identityEv` @ 121:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 177,000)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:177,000  F:11
- **Canonical identifiers**:
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_121_5_T` — cmplog:6  n4:177,000
  - `harfbuzz__ZNK14hb_transform_tIfE11is_identityEv_121_5_F` — cmplog:0  n4:11

### 462. `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF2FDSelectEJRKN2OT7NumTypeILb1EjLj4EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0_` @ 54:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 82)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:11  F:82
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF2FDSelectEJRKN2OT7NumTypeILb1EjLj4EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0__54_7_T` — cmplog:0  n4:11
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF2FDSelectEJRKN2OT7NumTypeILb1EjLj4EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0__54_7_F` — cmplog:2  n4:82

### 463. `_ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12sid_to_glyphEj` @ 1312:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 1)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:11  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12sid_to_glyphEj_1312_11_T` — cmplog:0  n4:11
  - `harfbuzz__ZNK2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEE12sid_to_glyphEj_1312_11_F` — cmplog:1  n4:1

### 464. `_Z18data_create_arabicPK18hb_ot_shape_plan_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 299, n4: 668)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:299
- **n4 coverage**: T:11  F:668
- **Canonical identifiers**:
  - `harfbuzz__Z18data_create_arabicPK18hb_ot_shape_plan_t_251_24_T` — cmplog:0  n4:11
  - `harfbuzz__Z18data_create_arabicPK18hb_ot_shape_plan_t_251_24_F` — cmplog:299  n4:668

### 465. `_Z20find_syllables_indicP11hb_buffer_t` @ 1209:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 189,000)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:11  F:189,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1209_2_T` — cmplog:0  n4:11
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1209_2_F` — cmplog:2,060  n4:189,000

### 466. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1448:2
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 38)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:38  F:11
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1448_2_T` — cmplog:2  n4:38
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1448_2_F` — cmplog:0  n4:11

### 467. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1009:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:11  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1009_2_T` — cmplog:0  n4:11
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1009_2_F` — cmplog:2,020  n4:73,800

### 468. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 113:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 75, n4: 933)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:75  F:0
- **n4 coverage**: T:933  F:11
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_113_10_T` — cmplog:75  n4:933
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_113_10_F` — cmplog:0  n4:11

### 469. `_ZNK21hb_sanitize_context_t11check_rangeIN2OT6OffsetINS1_7NumTypeILb1EjLj4EEELb1EEEEEbPKT_jj` @ 341:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 21, n4: 38)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:21  F:0
- **n4 coverage**: T:38  F:11
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT6OffsetINS1_7NumTypeILb1EjLj4EEELb1EEEEEbPKT_jj_341_5_T` — cmplog:21  n4:38
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT6OffsetINS1_7NumTypeILb1EjLj4EEELb1EEEEEbPKT_jj_341_5_F` — cmplog:0  n4:11

### 470. `_ZN11hb_vector_tI14hb_transform_tIfELb0EE6resizeEibb` @ 487:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 11,000, n4: 31,500)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:11,000
- **n4 coverage**: T:11  F:31,500
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tI14hb_transform_tIfELb0EE6resizeEibb_487_9_T` — cmplog:0  n4:11
  - `harfbuzz__ZN11hb_vector_tI14hb_transform_tIfELb0EE6resizeEibb_487_9_F` — cmplog:11,000  n4:31,500

### 471. `_ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 473, n4: 785)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:473
- **n4 coverage**: T:11  F:785
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb_251_24_T` — cmplog:0  n4:11
  - `harfbuzz__ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb_251_24_F` — cmplog:473  n4:785

### 472. `_ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 473, n4: 785)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:473
- **n4 coverage**: T:11  F:785
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb_251_47_T` — cmplog:0  n4:11
  - `harfbuzz__ZN11hb_vector_tIPN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE7chunk_tELb0EE5allocEjb_251_47_F` — cmplog:473  n4:785

### 473. `_ZN11hb_vector_tIN11hb_ot_map_t12lookup_map_tELb0EE5allocEjb` @ 462:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 92)
- **Flip strength**: 11 (blocked side hit 11× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:11  F:92
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIN11hb_ot_map_t12lookup_map_tELb0EE5allocEjb_462_11_T` — cmplog:0  n4:11
  - `harfbuzz__ZN11hb_vector_tIN11hb_ot_map_t12lookup_map_tELb0EE5allocEjb_462_11_F` — cmplog:28  n4:92

### 474. `_ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb` @ 847:48
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 136)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:10  F:136
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb_847_48_T` — cmplog:0  n4:10
  - `harfbuzz__ZNK2OT4CBDT13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_tb_847_48_F` — cmplog:12  n4:136

### 475. `_ZNK2OT15PaintColrLayers11paint_glyphEPNS_18hb_paint_context_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 428, n4: 5,370)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:428
- **n4 coverage**: T:10  F:5,370
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT15PaintColrLayers11paint_glyphEPNS_18hb_paint_context_tE_251_24_T` — cmplog:0  n4:10
  - `harfbuzz__ZNK2OT15PaintColrLayers11paint_glyphEPNS_18hb_paint_context_tE_251_24_F` — cmplog:428  n4:5,370

### 476. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1868:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:10  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1868_5_T` — cmplog:0  n4:10
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1868_5_F` — cmplog:1,800  n4:8,010

### 477. `_ZNK2OT6Layout9GPOS_impl16PairPosFormat1_3INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t` @ 38:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 66, n4: 304)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:66
- **n4 coverage**: T:10  F:304
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16PairPosFormat1_3INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_38_9_T` — cmplog:0  n4:10
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl16PairPosFormat1_3INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_38_9_F` — cmplog:66  n4:304

### 478. `hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC_` @ 1204:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 23)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:10  F:23
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1204_9_T` — cmplog:0  n4:10
  - `harfbuzz_hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1204_9_F` — cmplog:8  n4:23

### 479. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0_` @ 1134:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 61)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:10  F:61
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0__1134_42_T` — cmplog:0  n4:10
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjEEbT_S0_S0_DpT0__1134_42_F` — cmplog:1  n4:61

### 480. `_ZN3CFF11cff_stack_tINS_8number_tELi513EE4pushEv` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 149,000, n4: 19,300,000)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:149,000  F:0
- **n4 coverage**: T:19,300,000  F:10
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF11cff_stack_tINS_8number_tELi513EE4pushEv_250_22_T` — cmplog:149,000  n4:19,300,000
  - `harfbuzz__ZN3CFF11cff_stack_tINS_8number_tELi513EE4pushEv_250_22_F` — cmplog:0  n4:10

### 481. `_ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2_` @ 124:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 258, n4: 1,430)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:258
- **n4 coverage**: T:10  F:1,430
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__124_2_T` — cmplog:0  n4:10
  - `harfbuzz__ZN3CFF15cff1_cs_opset_tI20cff1_cs_opset_path_t17cff1_path_param_t22cff1_path_procs_path_tE11check_widthEjRNS_20cff1_cs_interp_env_tERS2__124_2_F` — cmplog:258  n4:1,430

### 482. `_ZN3CFF22cff2_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff2_font_dict_values_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 275, n4: 1,150)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:275
- **n4 coverage**: T:10  F:1,150
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF22cff2_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff2_font_dict_values_tE_251_24_T` — cmplog:0  n4:10
  - `harfbuzz__ZN3CFF22cff2_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff2_font_dict_values_tE_251_24_F` — cmplog:275  n4:1,150

### 483. `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1_` @ 814:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 23,100, n4: 66,900)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:23,100
- **n4 coverage**: T:10  F:66,900
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__814_7_T` — cmplog:0  n4:10
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__814_7_F` — cmplog:23,100  n4:66,900

### 484. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 48:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 39)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:10  F:39
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_48_2_T` — cmplog:0  n4:10
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_48_2_F` — cmplog:1  n4:39

### 485. `hb-ot-shape-normalize.cc:_ZL27decompose_current_characterPK31hb_ot_shape_normalize_context_tb` @ 178:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 471, n4: 1,240)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:471  F:0
- **n4 coverage**: T:1,240  F:10
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL27decompose_current_characterPK31hb_ot_shape_normalize_context_tb_178_9_T` — cmplog:471  n4:1,240
  - `harfbuzz_hb-ot-shape-normalize.cc:_ZL27decompose_current_characterPK31hb_ot_shape_normalize_context_tb_178_9_F` — cmplog:0  n4:10

### 486. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 631:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 51)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:10  F:51
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_631_2_T` — cmplog:0  n4:10
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_631_2_F` — cmplog:2  n4:51

### 487. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 634:2
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 51)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:51  F:10
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_634_2_T` — cmplog:2  n4:51
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_634_2_F` — cmplog:0  n4:10

### 488. `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` @ 82:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 223, n4: 2,160)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:223
- **n4 coverage**: T:10  F:2,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_82_7_T` — cmplog:0  n4:10
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_82_7_F` — cmplog:223  n4:2,160

### 489. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 236:32
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 540, n4: 1,730)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:540
- **n4 coverage**: T:10  F:1,730
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_32_T` — cmplog:0  n4:10
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_32_F` — cmplog:540  n4:1,730

### 490. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 359:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 110)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:10  F:110
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_359_4_T` — cmplog:0  n4:10
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_359_4_F` — cmplog:15  n4:110

### 491. `_ZNK2OT10avarV2Tail8sanitizeEP21hb_sanitize_context_tPKv` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 32, n4: 69)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:32  F:0
- **n4 coverage**: T:69  F:10
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT10avarV2Tail8sanitizeEP21hb_sanitize_context_tPKv_350_45_T` — cmplog:32  n4:69
  - `harfbuzz__ZNK2OT10avarV2Tail8sanitizeEP21hb_sanitize_context_tPKv_350_45_F` — cmplog:0  n4:10

### 492. `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` @ 224:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 471, n4: 1,240)
- **Flip strength**: 10 (blocked side hit 10× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:471
- **n4 coverage**: T:10  F:1,240
- **Canonical identifiers**:
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_224_7_T` — cmplog:0  n4:10
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_224_7_F` — cmplog:471  n4:1,240

### 493. `_ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb` @ 345:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 154, n4: 489)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:154
- **n4 coverage**: T:9  F:489
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb_345_11_T` — cmplog:0  n4:9
  - `harfbuzz__ZNK2OT4sbix13accelerator_t15get_png_extentsEP9hb_font_tjP18hb_glyph_extents_tb_345_11_F` — cmplog:154  n4:489

### 494. `_ZN2OT6Layout9GSUB_impl11SubstLookup16serialize_singleI17hb_sorted_array_tINS_11HBGlyphID16EE10hb_array_tIS5_ETnPN12hb_enable_ifIXaaaasr15hb_is_source_ofIT_KjEE5valuesrSA_18is_sorted_iteratorsr15hb_is_source_ofIT0_SB_EE5valueEvE4typeELPv0EEEbP22hb_serialize_context_tjSA_SC_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 188, n4: 375)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:188
- **n4 coverage**: T:9  F:375
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11SubstLookup16serialize_singleI17hb_sorted_array_tINS_11HBGlyphID16EE10hb_array_tIS5_ETnPN12hb_enable_ifIXaaaasr15hb_is_source_ofIT_KjEE5valuesrSA_18is_sorted_iteratorsr15hb_is_source_ofIT0_SB_EE5valueEvE4typeELPv0EEEbP22hb_serialize_context_tjSA_SC__251_24_T` — cmplog:0  n4:9
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11SubstLookup16serialize_singleI17hb_sorted_array_tINS_11HBGlyphID16EE10hb_array_tIS5_ETnPN12hb_enable_ifIXaaaasr15hb_is_source_ofIT_KjEE5valuesrSA_18is_sorted_iteratorsr15hb_is_source_ofIT0_SB_EE5valueEvE4typeELPv0EEEbP22hb_serialize_context_tjSA_SC__251_24_F` — cmplog:188  n4:375

### 495. `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t` @ 732:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 64, n4: 290)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:64
- **n4 coverage**: T:9  F:290
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_732_5_T` — cmplog:0  n4:9
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_732_5_F` — cmplog:64  n4:290

### 496. `_ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj` @ 949:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 44, n4: 356)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:44
- **n4 coverage**: T:9  F:356
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj_949_12_T` — cmplog:0  n4:9
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj_949_12_F` — cmplog:44  n4:356

### 497. `_ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj` @ 951:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36, n4: 254)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36
- **n4 coverage**: T:9  F:254
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj_951_11_T` — cmplog:0  n4:9
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesEvE8sanitizeEP21hb_sanitize_context_tPj_951_11_F` — cmplog:36  n4:254

### 498. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv` @ 747:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 185)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:9  F:185
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_747_5_T` — cmplog:0  n4:9
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_747_5_F` — cmplog:6  n4:185

### 499. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE_` @ 456:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 573)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:9  F:573
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE__456_12_T` — cmplog:0  n4:9
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE__456_12_F` — cmplog:130  n4:573

### 500. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE_` @ 456:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 572)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:9  F:572
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE__456_18_T` — cmplog:0  n4:9
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tI13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEC2ERKS6_SB_SE__456_18_F` — cmplog:130  n4:572

### 501. `hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1_` @ 813:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 23,100, n4: 66,900)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:23,100
- **n4 coverage**: T:9  F:66,900
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__813_7_T` — cmplog:0  n4:9
  - `harfbuzz_hb-ot-font.cc:_ZL23hb_ot_get_glyph_extentsP9hb_font_tPvjP18hb_glyph_extents_tS1__813_7_F` — cmplog:23,100  n4:66,900

### 502. `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj` @ 101:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 188, n4: 375)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:188  F:0
- **n4 coverage**: T:375  F:9
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_101_10_T` — cmplog:188  n4:375
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_101_10_F` — cmplog:0  n4:9

### 503. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 542:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 42)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:9  F:42
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_542_9_T` — cmplog:0  n4:9
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_542_9_F` — cmplog:2  n4:42

### 504. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 977:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:9  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_977_2_T` — cmplog:0  n4:9
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_977_2_F` — cmplog:2,020  n4:73,800

### 505. `_ZN13hb_utf16_xe_tItE10encode_lenEj` @ 264:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 46,300, n4: 69,500)
- **Flip strength**: 9 (blocked side hit 9× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:46,300  F:0
- **n4 coverage**: T:69,500  F:9
- **Canonical identifiers**:
  - `harfbuzz__ZN13hb_utf16_xe_tItE10encode_lenEj_264_12_T` — cmplog:46,300  n4:69,500
  - `harfbuzz__ZN13hb_utf16_xe_tItE10encode_lenEj_264_12_F` — cmplog:0  n4:9

### 506. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1853:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,010)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:8  F:8,010
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1853_5_T` — cmplog:0  n4:8
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1853_5_F` — cmplog:1,800  n4:8,010

### 507. `_ZN2OT6Layout9GSUB_impl11SubstLookup18serialize_ligatureEP22hb_serialize_context_tj17hb_sorted_array_tIKNS_11HBGlyphID16EE10hb_array_tIKjES9_IS7_ESB_SC_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 285, n4: 404)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:285
- **n4 coverage**: T:8  F:404
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11SubstLookup18serialize_ligatureEP22hb_serialize_context_tj17hb_sorted_array_tIKNS_11HBGlyphID16EE10hb_array_tIKjES9_IS7_ESB_SC__251_24_T` — cmplog:0  n4:8
  - `harfbuzz__ZN2OT6Layout9GSUB_impl11SubstLookup18serialize_ligatureEP22hb_serialize_context_tj17hb_sorted_array_tIKNS_11HBGlyphID16EE10hb_array_tIKjES9_IS7_ESB_SC__251_24_F` — cmplog:285  n4:404

### 508. `_ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE5applyEPNS_22hb_aat_apply_context_tE` @ 109:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 134)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:8  F:134
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE5applyEPNS_22hb_aat_apply_context_tE_109_9_T` — cmplog:0  n4:8
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat0IN2OT21KernAATSubTableHeaderEE5applyEPNS_22hb_aat_apply_context_tE_109_9_F` — cmplog:2  n4:134

### 509. `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE` @ 1177:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 341)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:8  F:341
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1177_4_T` — cmplog:0  n4:8
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1177_4_F` — cmplog:3  n4:341

### 510. `hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1_` @ 1467:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10,100, n4: 18,200)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10,100  F:0
- **n4 coverage**: T:18,200  F:8
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1467_12_T` — cmplog:10,100  n4:18,200
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL14hb_stable_sortIN2OT11HBGlyphID16ENS0_7NumTypeILb1EtLj2EEES1_EvPT_jPFiPKT0_S8_EPT1__1467_12_F` — cmplog:0  n4:8

### 511. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0_` @ 1134:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 89)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:8  F:89
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0__1134_10_T` — cmplog:0  n4:8
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjjjjjEEbT_S0_S0_DpT0__1134_10_F` — cmplog:1  n4:89

### 512. `_ZN11hb_bounds_tIfE9intersectERKS0_` @ 345:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 4)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:8  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__345_6_T` — cmplog:0  n4:8
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__345_6_F` — cmplog:2  n4:4

### 513. `hb-number.cc:_ZL9strtod_rlPKcPS0_` @ 223:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 6)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:8  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-number.cc:_ZL9strtod_rlPKcPS0__223_9_T` — cmplog:0  n4:8
  - `harfbuzz_hb-number.cc:_ZL9strtod_rlPKcPS0__223_9_F` — cmplog:1  n4:6

### 514. `hb-ot-shaper-indic.cc:_ZL41_hb_glyph_info_ligated_and_didnt_multiplyPK15hb_glyph_info_t` @ 586:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 953)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:8  F:953
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL41_hb_glyph_info_ligated_and_didnt_multiplyPK15hb_glyph_info_t_586_10_T` — cmplog:0  n4:8
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL41_hb_glyph_info_ligated_and_didnt_multiplyPK15hb_glyph_info_t_586_10_F` — cmplog:2  n4:953

### 515. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 87:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,640)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:8  F:1,640
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_87_5_T` — cmplog:0  n4:8
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_87_5_F` — cmplog:389  n4:1,640

### 516. `hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj` @ 101:17
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 188, n4: 367)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:188  F:0
- **n4 coverage**: T:367  F:8
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_101_17_T` — cmplog:188  n4:367
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL40arabic_fallback_synthesize_lookup_singlePK18hb_ot_shape_plan_tP9hb_font_tj_101_17_F` — cmplog:0  n4:8

### 517. `_Z23hb_indic_get_categoriesj` @ 512:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 12)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:8  F:12
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_512_11_T` — cmplog:0  n4:8
  - `harfbuzz__Z23hb_indic_get_categoriesj_512_11_F` — cmplog:4  n4:12

### 518. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 472, n4: 750)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:472
- **n4 coverage**: T:8  F:750
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_T` — cmplog:0  n4:8
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_F` — cmplog:472  n4:750

### 519. `_ZN15hb_set_digest_t9add_rangeEjj` @ 103:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13,000, n4: 37,800)
- **Flip strength**: 8 (blocked side hit 8× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13,000
- **n4 coverage**: T:8  F:37,800
- **Canonical identifiers**:
  - `harfbuzz__ZN15hb_set_digest_t9add_rangeEjj_103_9_T` — cmplog:0  n4:8
  - `harfbuzz__ZN15hb_set_digest_t9add_rangeEjj_103_9_F` — cmplog:13,000  n4:37,800

### 520. `_ZNK2OT21SVGDocumentIndexEntry3cmpEj` @ 46:36
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9, n4: 24)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:0
- **n4 coverage**: T:24  F:7
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21SVGDocumentIndexEntry3cmpEj_46_36_T` — cmplog:9  n4:24
  - `harfbuzz__ZNK2OT21SVGDocumentIndexEntry3cmpEj_46_36_F` — cmplog:0  n4:7

### 521. `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 949:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 81)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:7  F:81
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_949_12_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_949_12_F` — cmplog:7  n4:81

### 522. `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 951:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 65)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:7  F:65
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_951_11_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_951_11_F` — cmplog:7  n4:65

### 523. `_ZN3AAT13ObsoleteTypes13offsetToIndexIN2OT7NumTypeILb1EsLj2EEEEEjjPKvPKT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 167)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:7  F:167
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT13ObsoleteTypes13offsetToIndexIN2OT7NumTypeILb1EsLj2EEEEEjjPKvPKT__251_24_T` — cmplog:0  n4:7
  - `harfbuzz__ZN3AAT13ObsoleteTypes13offsetToIndexIN2OT7NumTypeILb1EsLj2EEEEEjjPKvPKT__251_24_F` — cmplog:7  n4:167

### 524. `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1017:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9, n4: 499)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9
- **n4 coverage**: T:7  F:499
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1017_11_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1017_11_F` — cmplog:9  n4:499

### 525. `hb-ot-color.cc:_ZL15hb_bsearch_implIKN2OT21SVGDocumentIndexEntryEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC_` @ 1206:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9, n4: 24)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:0
- **n4 coverage**: T:24  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-color.cc:_ZL15hb_bsearch_implIKN2OT21SVGDocumentIndexEntryEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_T` — cmplog:9  n4:24
  - `harfbuzz_hb-ot-color.cc:_ZL15hb_bsearch_implIKN2OT21SVGDocumentIndexEntryEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_F` — cmplog:0  n4:7

### 526. `hb-ot-layout.cc:_ZL15hb_bsearch_implIKN2OT6RecordINS0_7LangSysEEEjJEEbPjRKT0_PT_mmPFiPKvSC_DpT1_ESE_` @ 1206:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 247, n4: 2,980)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:247  F:0
- **n4 coverage**: T:2,980  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZL15hb_bsearch_implIKN2OT6RecordINS0_7LangSysEEEjJEEbPjRKT0_PT_mmPFiPKvSC_DpT1_ESE__1206_14_T` — cmplog:247  n4:2,980
  - `harfbuzz_hb-ot-layout.cc:_ZL15hb_bsearch_implIKN2OT6RecordINS0_7LangSysEEEjJEEbPjRKT0_PT_mmPFiPKvSC_DpT1_ESE__1206_14_F` — cmplog:0  n4:7

### 527. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0_` @ 1134:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 61)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:7  F:61
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_F` — cmplog:1  n4:61

### 528. `_ZNK17hb_sorted_array_tIKN2OT6RecordINS0_7LangSysEEEE5bfindIjEEbRKT_Pj14hb_not_found_tj` @ 414:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16,500, n4: 48,000)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16,500
- **n4 coverage**: T:7  F:48,000
- **Canonical identifiers**:
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT6RecordINS0_7LangSysEEEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT6RecordINS0_7LangSysEEEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_F` — cmplog:16,500  n4:48,000

### 529. `_ZN17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE7bsearchIjEEPS2_RKT_S5_` @ 399:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:7  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZN17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE7bsearchIjEEPS2_RKT_S5__399_12_T` — cmplog:0  n4:7
  - `harfbuzz__ZN17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE7bsearchIjEEPS2_RKT_S5__399_12_F` — cmplog:6,150  n4:16,500

### 530. `_ZNK17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE5bfindIjEEbRKT_Pj14hb_not_found_tj` @ 414:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,150
- **n4 coverage**: T:7  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT21SVGDocumentIndexEntryEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_F` — cmplog:6,150  n4:16,500

### 531. `hb_script_get_horizontal_direction` @ 629:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:7  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_629_5_T` — cmplog:0  n4:7
  - `harfbuzz_hb_script_get_horizontal_direction_629_5_F` — cmplog:29,700  n4:79,800

### 532. `_ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 561)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:561  F:7
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:561
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_12MultiVarDataENS_7NumTypeILb1EjLj4EEEvLb1EEENS3_ILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:7

### 533. `_ZNK2OT8OffsetToINS_9SBIXGlyphENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 90)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:7  F:90
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_9SBIXGlyphENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK2OT8OffsetToINS_9SBIXGlyphENS_7NumTypeILb1EjLj4EEEvLb1EEclEPKv_251_24_F` — cmplog:13  n4:90

### 534. `hb_ot_layout_script_select_language2` @ 792:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16,500, n4: 48,000)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16,500
- **n4 coverage**: T:7  F:48,000
- **Canonical identifiers**:
  - `harfbuzz_hb_ot_layout_script_select_language2_792_7_T` — cmplog:0  n4:7
  - `harfbuzz_hb_ot_layout_script_select_language2_792_7_F` — cmplog:16,500  n4:48,000

### 535. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 49:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 42)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:7  F:42
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_49_2_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_49_2_F` — cmplog:1  n4:42

### 536. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_16ligature_3_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 200:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 91, n4: 116)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:91  F:0
- **n4 coverage**: T:116  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_16ligature_3_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_10_T` — cmplog:91  n4:116
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_16ligature_3_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_10_F` — cmplog:0  n4:7

### 537. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 346:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 25)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:7  F:25
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_346_7_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_346_7_F` — cmplog:1  n4:25

### 538. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 348:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 25)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:25  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_348_25_T` — cmplog:1  n4:25
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_348_25_F` — cmplog:0  n4:7

### 539. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 371:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 25)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:25  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_371_8_T` — cmplog:1  n4:25
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_371_8_F` — cmplog:0  n4:7

### 540. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 479:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 1,550)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:7  F:1,550
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_479_7_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_479_7_F` — cmplog:1  n4:1,550

### 541. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 337:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 80, n4: 1,150)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:80  F:0
- **n4 coverage**: T:1,150  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__337_11_T` — cmplog:80  n4:1,150
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__337_11_F` — cmplog:0  n4:7

### 542. `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 346:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 97)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:97  F:7
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_346_12_T` — cmplog:1  n4:97
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_346_12_F` — cmplog:0  n4:7

### 543. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 981:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:7  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_981_2_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_981_2_F` — cmplog:2,020  n4:73,800

### 544. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 115:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 75, n4: 937)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:75
- **n4 coverage**: T:7  F:937
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_115_4_T` — cmplog:0  n4:7
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_115_4_F` — cmplog:75  n4:937

### 545. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 134:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 30, n4: 368)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:30  F:0
- **n4 coverage**: T:368  F:7
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_134_10_T` — cmplog:30  n4:368
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_134_10_F` — cmplog:0  n4:7

### 546. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 328:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 323)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:323  F:7
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_328_10_T` — cmplog:15  n4:323
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_328_10_F` — cmplog:0  n4:7

### 547. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 327:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:7  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_327_5_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_327_5_F` — cmplog:8,290  n4:24,000

### 548. `_ZNK2OT4VVAR23get_vorg_delta_unscaledEjPKijPNS_17hb_scalar_cache_tE` @ 455:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 24)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:7  F:24
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VVAR23get_vorg_delta_unscaledEjPKijPNS_17hb_scalar_cache_tE_455_9_T` — cmplog:0  n4:7
  - `harfbuzz__ZNK2OT4VVAR23get_vorg_delta_unscaledEjPKijPNS_17hb_scalar_cache_tE_455_9_F` — cmplog:1  n4:24

### 549. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4_` @ 474:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 50)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:50  F:7
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4__474_25_T` — cmplog:7  n4:50
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4__474_25_F` — cmplog:0  n4:7

### 550. `hb-ucd.cc:_ZL14hb_ucd_composeP18hb_unicode_funcs_tjjPjPv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 84, n4: 144)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:84
- **n4 coverage**: T:7  F:144
- **Canonical identifiers**:
  - `harfbuzz_hb-ucd.cc:_ZL14hb_ucd_composeP18hb_unicode_funcs_tjjPjPv_251_24_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ucd.cc:_ZL14hb_ucd_composeP18hb_unicode_funcs_tjjPjPv_251_24_F` — cmplog:84  n4:144

### 551. `hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj` @ 98:26
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,320, n4: 6,420)
- **Flip strength**: 7 (blocked side hit 7× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,320
- **n4 coverage**: T:7  F:6,420
- **Canonical identifiers**:
  - `harfbuzz_hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj_98_26_T` — cmplog:0  n4:7
  - `harfbuzz_hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj_98_26_F` — cmplog:1,320  n4:6,420

### 552. `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t` @ 121:56
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 6, n4: 24)
- **Flip strength**: 7 (blocked side hit 7× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:7
- **n4 coverage**: T:24  F:0
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_121_56_T` — cmplog:6  n4:24
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_121_56_F` — cmplog:7  n4:0

### 553. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 319:13
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 130)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:6  F:130
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_319_13_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_319_13_F` — cmplog:12  n4:130

### 554. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1856:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,020)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:6  F:8,020
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1856_5_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1856_5_F` — cmplog:1,800  n4:8,020

### 555. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1870:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,020)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:6  F:8,020
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1870_5_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1870_5_F` — cmplog:1,800  n4:8,020

### 556. `_ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0_` @ 1878:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,800, n4: 8,020)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,800
- **n4 coverage**: T:6  F:8,020
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1878_5_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT5Paint8dispatchINS_18hb_paint_context_tEJEEENT_8return_tEPS3_DpOT0__1878_5_F` — cmplog:1,800  n4:8,020

### 557. `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 20, n4: 1,020)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:0
- **n4 coverage**: T:1,020  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:20  n4:1,020
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:6

### 558. `_ZNK2OT6Layout9GSUB_impl22LigatureSubstFormat1_2INS0_11MediumTypesEE21external_cache_createEv` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10, n4: 690)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:0
- **n4 coverage**: T:690  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl22LigatureSubstFormat1_2INS0_11MediumTypesEE21external_cache_createEv_250_22_T` — cmplog:10  n4:690
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl22LigatureSubstFormat1_2INS0_11MediumTypesEE21external_cache_createEv_250_22_F` — cmplog:0  n4:6

### 559. `_ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 44)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:6  F:44
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3AAT10StateTableINS_13ObsoleteTypesENS_18ContextualSubtableIS1_E9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_24_F` — cmplog:3  n4:44

### 560. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1278:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 110)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:110  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1278_9_T` — cmplog:6  n4:110
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1278_9_F` — cmplog:0  n4:6

### 561. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 169, n4: 1,180)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:169
- **n4 coverage**: T:6  F:1,180
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_18ContextualSubtableIS1_E9EntryDataEE9get_classEjjP10hb_cache_tILj15ELj8ELj7ELb1EE_251_24_F` — cmplog:169  n4:1,180

### 562. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 36,500, n4: 219,000)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:36,500
- **n4 coverage**: T:6  F:219,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_17InsertionSubtableIS1_E9EntryDataENS3_5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_251_24_F` — cmplog:36,500  n4:219,000

### 563. `_ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1037:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 111, n4: 353)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:111  F:0
- **n4 coverage**: T:353  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1037_11_T` — cmplog:111  n4:353
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT6KernOTEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1037_11_F` — cmplog:0  n4:6

### 564. `_ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 224)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:6  F:224
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3AAT8mortmorxINS_4mortENS_13ObsoleteTypesELj1836020340EE13compile_flagsEPK20hb_aat_map_builder_tP12hb_aat_map_t_251_24_F` — cmplog:3  n4:224

### 565. `_ZNK3AAT8mortmorxINS_4morxENS_13ExtendedTypesELj1836020344EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 385, n4: 1,810)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:385
- **n4 coverage**: T:6  F:1,810
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT8mortmorxINS_4morxENS_13ExtendedTypesELj1836020344EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3AAT8mortmorxINS_4morxENS_13ExtendedTypesELj1836020344EE5applyEPNS_22hb_aat_apply_context_tERK12hb_aat_map_tRKNS3_13accelerator_tE_251_24_F` — cmplog:385  n4:1,810

### 566. `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 190, n4: 1,090)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:190
- **n4 coverage**: T:6  F:1,090
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_251_24_F` — cmplog:190  n4:1,090

### 567. `_ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5_` @ 348:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 77,700, n4: 11,700,000)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:77,700
- **n4 coverage**: T:6  F:11,700,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5__348_7_T` — cmplog:0  n4:6
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff2_cs_opset_extents_tNS_20cff2_cs_interp_env_tIS1_EE20cff2_extents_param_t25cff2_path_procs_extents_tE10process_opEjRS4_RS5__348_7_F` — cmplog:77,700  n4:11,700,000

### 568. `hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1_` @ 991:33
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 38, n4: 930)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:38  F:0
- **n4 coverage**: T:930  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1__991_33_T` — cmplog:38  n4:930
  - `harfbuzz_hb-ot-layout.cc:_ZNK4$_33clI13hb_map_iter_tI16hb_filter_iter_tIS1_I10hb_array_tIKN2OT8OffsetToINS4_9ChainRuleINS4_6Layout10SmallTypesEEENS4_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS4_12ChainRuleSetIS8_EEEL24hb_function_sortedness_t0ELPv0EEZNKSK_5applyEPNS4_21hb_ot_apply_context_tERKNS4_30ChainContextApplyLookupContextEEUlRKS9_E0_RK4$_19LSP_0EEZNKSK_5applyESS_SV_EUlSX_E1_LSO_0ELSP_0EES11_S11_TnPN12hb_enable_ifIXsr14hb_is_iterableIT_EE5valueEvE4typeELSP_0EEEbOS16_OT0_OT1__991_33_F` — cmplog:0  n4:6

### 569. `_ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat2INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 48, n4: 1,370)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:48  F:0
- **n4 coverage**: T:1,370  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat2INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb_250_22_T` — cmplog:48  n4:1,370
  - `harfbuzz__ZNK2OT17hb_kern_machine_tIN3AAT19KerxSubTableFormat2INS_21KernAATSubTableHeaderEE13accelerator_tEE4kernEP9hb_font_tP11hb_buffer_tjb_250_22_F` — cmplog:0  n4:6

### 570. `_ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE13set_with_hashIRPS1_RjEEbOT_jOT0_b` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 606, n4: 980)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:606
- **n4 coverage**: T:6  F:980
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE13set_with_hashIRPS1_RjEEbOT_jOT0_b_251_47_T` — cmplog:0  n4:6
  - `harfbuzz__ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE13set_with_hashIRPS1_RjEEbOT_jOT0_b_251_47_F` — cmplog:606  n4:980

### 571. `_ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE5allocEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 607, n4: 981)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:607
- **n4 coverage**: T:6  F:981
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE5allocEj_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZN12hb_hashmap_tIPKN22hb_serialize_context_t8object_tEjLb0EE5allocEj_251_24_F` — cmplog:607  n4:981

### 572. `hb-ot-math.cc:_ZNK3$_2clIRjS1_EEDTqulefp_fp0_fp_fp0_EOT_OT0_` @ 76:55
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 12,300, n4: 33,000)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:12,300  F:0
- **n4 coverage**: T:33,000  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-math.cc:_ZNK3$_2clIRjS1_EEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_T` — cmplog:12,300  n4:33,000
  - `harfbuzz_hb-ot-math.cc:_ZNK3$_2clIRjS1_EEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_F` — cmplog:0  n4:6

### 573. `_ZNK2OT7ArrayOfIN3CFF17FDSelect3_4_RangeINS_7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEES4_E8sanitizeIJDnRjEEEbP21hb_sanitize_context_tDpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 553, n4: 1,020)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:553
- **n4 coverage**: T:6  F:1,020
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfIN3CFF17FDSelect3_4_RangeINS_7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEES4_E8sanitizeIJDnRjEEEbP21hb_sanitize_context_tDpOT__251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT7ArrayOfIN3CFF17FDSelect3_4_RangeINS_7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEES4_E8sanitizeIJDnRjEEEbP21hb_sanitize_context_tDpOT__251_24_F` — cmplog:553  n4:1,020

### 574. `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE` @ 800:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13,500, n4: 37,000)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13,500
- **n4 coverage**: T:6  F:37,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_800_7_T` — cmplog:0  n4:6
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_800_7_F` — cmplog:13,500  n4:37,000

### 575. `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj` @ 98:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 86)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:6  F:86
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_98_5_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_98_5_F` — cmplog:2  n4:86

### 576. `_ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS7_DpOT0_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 461, n4: 1,190)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:461
- **n4 coverage**: T:6  F:1,190
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS7_DpOT0__251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8dispatchI21hb_sanitize_context_tJEEENT_8return_tEPS7_DpOT0__251_24_F` — cmplog:461  n4:1,190

### 577. `hb_ot_layout_language_find_feature` @ 1022:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 4)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:4  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb_ot_layout_language_find_feature_1022_11_T` — cmplog:6  n4:4
  - `harfbuzz_hb_ot_layout_language_find_feature_1022_11_F` — cmplog:0  n4:6

### 578. `_ZN19hb_ot_map_builder_t11has_featureEj` @ 116:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 574, n4: 1,140)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:574
- **n4 coverage**: T:6  F:1,140
- **Canonical identifiers**:
  - `harfbuzz__ZN19hb_ot_map_builder_t11has_featureEj_116_9_T` — cmplog:0  n4:6
  - `harfbuzz__ZN19hb_ot_map_builder_t11has_featureEj_116_9_F` — cmplog:574  n4:1,140

### 579. `_ZNK2OT4meta8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 4)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:4  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4meta8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:4
  - `harfbuzz__ZNK2OT4meta8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:6

### 580. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 61:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 43)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:6  F:43
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_61_2_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_61_2_F` — cmplog:1  n4:43

### 581. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 106:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:6  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_106_5_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_106_5_F` — cmplog:389  n4:1,650

### 582. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 200:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 94, n4: 132)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:94  F:0
- **n4 coverage**: T:132  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_10_T` — cmplog:94  n4:132
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_10_F` — cmplog:0  n4:6

### 583. `hb-ot-shaper-arabic.cc:_ZL23collect_features_arabicP21hb_ot_shape_planner_t` @ 235:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 287, n4: 573)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:287  F:0
- **n4 coverage**: T:573  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL23collect_features_arabicP21hb_ot_shape_planner_t_235_8_T` — cmplog:287  n4:573
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL23collect_features_arabicP21hb_ot_shape_planner_t_235_8_F` — cmplog:0  n4:6

### 584. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 119:25
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 720, n4: 2,490)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:720
- **n4 coverage**: T:6  F:2,490
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_119_25_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_119_25_F` — cmplog:720  n4:2,490

### 585. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 150:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 207)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:6  F:207
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_150_7_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_150_7_F` — cmplog:5  n4:207

### 586. `_Z20find_syllables_indicP11hb_buffer_t` @ 1217:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 189,000)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:6  F:189,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1217_2_T` — cmplog:0  n4:6
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1217_2_F` — cmplog:2,060  n4:189,000

### 587. `_Z23hb_indic_get_categoriesj` @ 510:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 21)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:6  F:21
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_510_11_T` — cmplog:0  n4:6
  - `harfbuzz__Z23hb_indic_get_categoriesj_510_11_F` — cmplog:4  n4:21

### 588. `hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t` @ 390:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 10, n4: 941)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:10
- **n4 coverage**: T:6  F:941
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_390_7_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL28consonant_position_from_facePK18indic_shape_plan_tjjP9hb_face_t_390_7_F` — cmplog:10  n4:941

### 589. `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii` @ 81:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10, n4: 634)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:0
- **n4 coverage**: T:634  F:6
- **Canonical identifiers**:
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_81_11_T` — cmplog:10  n4:634
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_81_11_F` — cmplog:0  n4:6

### 590. `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` @ 80:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 223, n4: 2,170)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:223
- **n4 coverage**: T:6  F:2,170
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_80_7_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_80_7_F` — cmplog:223  n4:2,170

### 591. `hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t` @ 146:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 65)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:65  F:6
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t_146_5_T` — cmplog:2  n4:65
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t_146_5_F` — cmplog:0  n4:6

### 592. `hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t` @ 147:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 65)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:6  F:65
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t_147_5_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL14thai_pua_shapej13thai_action_tP9hb_font_t_147_5_F` — cmplog:2  n4:65

### 593. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 989:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:6  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_989_2_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_989_2_F` — cmplog:2,020  n4:73,800

### 594. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1021:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:6  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1021_2_T` — cmplog:0  n4:6
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1021_2_F` — cmplog:2,020  n4:73,800

### 595. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 330:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 324)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:6  F:324
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_330_4_T` — cmplog:0  n4:6
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_330_4_F` — cmplog:15  n4:324

### 596. `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t` @ 81:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 62)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:6  F:62
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_81_7_T` — cmplog:0  n4:6
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_81_7_F` — cmplog:116  n4:62

### 597. `_ZN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE5allocEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 550, n4: 875)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:550
- **n4 coverage**: T:6  F:875
- **Canonical identifiers**:
  - `harfbuzz__ZN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE5allocEv_251_24_T` — cmplog:0  n4:6
  - `harfbuzz__ZN9hb_pool_tIN22hb_serialize_context_t8object_tELj32EE5allocEv_251_24_F` — cmplog:550  n4:875

### 598. `_ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_18ContextualSubtableINS1_13ObsoleteTypesEE9EntryDataEEEEEbPKT_jj` @ 341:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 44)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:44  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_18ContextualSubtableINS1_13ObsoleteTypesEE9EntryDataEEEEEbPKT_jj_341_5_T` — cmplog:3  n4:44
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN3AAT5EntryINS1_18ContextualSubtableINS1_13ObsoleteTypesEE9EntryDataEEEEEbPKT_jj_341_5_F` — cmplog:0  n4:6

### 599. `_ZN21hb_sanitize_context_t12may_dispatchIN2OT16ExtensionFormat1INS1_6Layout9GPOS_impl12ExtensionPosEEES6_EEbPKT_PKT0_` @ 138:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 461, n4: 1,190)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:461  F:0
- **n4 coverage**: T:1,190  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t12may_dispatchIN2OT16ExtensionFormat1INS1_6Layout9GPOS_impl12ExtensionPosEEES6_EEbPKT_PKT0__138_12_T` — cmplog:461  n4:1,190
  - `harfbuzz__ZN21hb_sanitize_context_t12may_dispatchIN2OT16ExtensionFormat1INS1_6Layout9GPOS_impl12ExtensionPosEEES6_EEbPKT_PKT0__138_12_F` — cmplog:0  n4:6

### 600. `_ZN9hb_utf8_t6encodeEPhPKhj` @ 157:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 35, n4: 86)
- **Flip strength**: 6 (blocked side hit 6× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:35  F:0
- **n4 coverage**: T:86  F:6
- **Canonical identifiers**:
  - `harfbuzz__ZN9hb_utf8_t6encodeEPhPKhj_157_14_T` — cmplog:35  n4:86
  - `harfbuzz__ZN9hb_utf8_t6encodeEPhPKhj_157_14_F` — cmplog:0  n4:6

### 601. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 319:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 131)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:5  F:131
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_319_5_T` — cmplog:0  n4:5
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_319_5_F` — cmplog:12  n4:131

### 602. `_ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb` @ 320:21
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 131)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:5  F:131
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_21_T` — cmplog:0  n4:5
  - `harfbuzz__ZNK2OT13IndexSubtable11get_extentsEP18hb_glyph_extents_tb_320_21_F` — cmplog:12  n4:131

### 603. `_ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0_` @ 36:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 554, n4: 3,080)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:554
- **n4 coverage**: T:5  F:3,080
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0__36_5_T` — cmplog:0  n4:5
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SingleSubst8dispatchINS_33hb_accelerate_subtables_context_tEJEEENT_8return_tEPS5_DpOT0__36_5_F` — cmplog:554  n4:3,080

### 604. `_ZNK2OT4VARC8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 2,240)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:2,240  F:5
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:2,240
  - `harfbuzz__ZNK2OT4VARC8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:5

### 605. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv` @ 748:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 189)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:5  F:189
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_748_5_T` — cmplog:0  n4:5
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_748_5_F` — cmplog:6  n4:189

### 606. `_ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc` @ 396:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,730, n4: 15,100)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,730
- **n4 coverage**: T:5  F:15,100
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc_396_7_T` — cmplog:0  n4:5
  - `harfbuzz__ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc_396_7_F` — cmplog:5,730  n4:15,100

### 607. `_ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc` @ 401:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,730, n4: 15,100)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,730
- **n4 coverage**: T:5  F:15,100
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc_401_7_T` — cmplog:0  n4:5
  - `harfbuzz__ZN11hb_buffer_t6verifyEPS_P9hb_font_tPK12hb_feature_tjPKPKc_401_7_F` — cmplog:5,730  n4:15,100

### 608. `hb-buffer-verify.cc:_ZL29buffer_verify_unsafe_to_breakP11hb_buffer_tS0_P9hb_font_tPK12hb_feature_tjPKPKc` @ 185:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 63, n4: 120)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:63
- **n4 coverage**: T:5  F:120
- **Canonical identifiers**:
  - `harfbuzz_hb-buffer-verify.cc:_ZL29buffer_verify_unsafe_to_breakP11hb_buffer_tS0_P9hb_font_tPK12hb_feature_tjPKPKc_185_9_T` — cmplog:0  n4:5
  - `harfbuzz_hb-buffer-verify.cc:_ZL29buffer_verify_unsafe_to_breakP11hb_buffer_tS0_P9hb_font_tPK12hb_feature_tjPKPKc_185_9_F` — cmplog:63  n4:120

### 609. `hb_buffer_set_length` @ 1565:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 11,400, n4: 30,500)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:11,400  F:0
- **n4 coverage**: T:30,500  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb_buffer_set_length_1565_7_T` — cmplog:11,400  n4:30,500
  - `harfbuzz_hb_buffer_set_length_1565_7_F` — cmplog:0  n4:5

### 610. `hb_buffer_set_length` @ 1573:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 11,400, n4: 30,500)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:11,400
- **n4 coverage**: T:5  F:30,500
- **Canonical identifiers**:
  - `harfbuzz_hb_buffer_set_length_1573_7_T` — cmplog:0  n4:5
  - `harfbuzz_hb_buffer_set_length_1573_7_F` — cmplog:11,400  n4:30,500

### 611. `hb_buffer_get_glyph_infos` @ 1619:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 17,100, n4: 45,400)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:17,100  F:0
- **n4 coverage**: T:45,400  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb_buffer_get_glyph_infos_1619_7_T` — cmplog:17,100  n4:45,400
  - `harfbuzz_hb_buffer_get_glyph_infos_1619_7_F` — cmplog:0  n4:5

### 612. `hb_buffer_diff` @ 2201:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 63, n4: 120)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:63
- **n4 coverage**: T:5  F:120
- **Canonical identifiers**:
  - `harfbuzz_hb_buffer_diff_2201_7_T` — cmplog:0  n4:5
  - `harfbuzz_hb_buffer_diff_2201_7_F` — cmplog:63  n4:120

### 613. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev` @ 463:38
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,980, n4: 73,700)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,980
- **n4 coverage**: T:5  F:73,700
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev_463_38_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev_463_38_F` — cmplog:1,980  n4:73,700

### 614. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev` @ 463:44
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,980, n4: 73,700)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,980
- **n4 coverage**: T:5  F:73,700
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev_463_44_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EE8__prev__Ev_463_44_F` — cmplog:1,980  n4:73,700

### 615. `hb-ot-shaper-indic.cc:_ZNK3$_2clIRjjEEDTqulefp_fp0_fp_fp0_EOT_OT0_` @ 76:55
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 43)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:43  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZNK3$_2clIRjjEEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_T` — cmplog:1  n4:43
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZNK3$_2clIRjjEEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_F` — cmplog:0  n4:5

### 616. `_ZNK2OT21ItemVarStoreInstancerclEjt` @ 3828:8
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,300, n4: 2,780)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,300  F:0
- **n4 coverage**: T:2,780  F:5
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT21ItemVarStoreInstancerclEjt_3828_8_T` — cmplog:1,300  n4:2,780
  - `harfbuzz__ZNK2OT21ItemVarStoreInstancerclEjt_3828_8_F` — cmplog:0  n4:5

### 617. `hb-ot-shape-fallback.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t` @ 518:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 4)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:4  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t_518_7_T` — cmplog:4  n4:4
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL32_hb_glyph_info_get_lig_num_compsPK15hb_glyph_info_t_518_7_F` — cmplog:0  n4:5

### 618. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 565:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 310)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:5  F:310
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_565_2_T` — cmplog:0  n4:5
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_565_2_F` — cmplog:28  n4:310

### 619. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 126:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 70)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:70  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_126_12_T` — cmplog:1  n4:70
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_126_12_F` — cmplog:0  n4:5

### 620. `_Z20find_syllables_indicP11hb_buffer_t` @ 1213:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 189,000)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:5  F:189,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1213_2_T` — cmplog:0  n4:5
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1213_2_F` — cmplog:2,060  n4:189,000

### 621. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 4,910)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:5  F:4,910
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_251_24_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_251_24_F` — cmplog:8  n4:4,910

### 622. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 4,230)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:5  F:4,230
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_251_47_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_251_47_F` — cmplog:7  n4:4,230

### 623. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 774:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 829, n4: 13,100)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:829  F:0
- **n4 coverage**: T:13,100  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_774_6_T` — cmplog:829  n4:13,100
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_774_6_F` — cmplog:0  n4:5

### 624. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1109:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 1,060)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:5  F:1,060
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1109_5_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1109_5_F` — cmplog:4  n4:1,060

### 625. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1447:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 49)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:5  F:49
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1447_9_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1447_9_F` — cmplog:2  n4:49

### 626. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 608:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 354, n4: 50,000)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:354
- **n4 coverage**: T:5  F:50,000
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_608_2_T` — cmplog:0  n4:5
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_608_2_F` — cmplog:354  n4:50,000

### 627. `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` @ 53:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 223, n4: 2,150)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:223
- **n4 coverage**: T:5  F:2,150
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_53_7_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_53_7_F` — cmplog:223  n4:2,150

### 628. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 249:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 30, n4: 985)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:30  F:0
- **n4 coverage**: T:985  F:5
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_249_10_T` — cmplog:30  n4:985
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_249_10_F` — cmplog:0  n4:5

### 629. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 381:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:5  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_381_5_T` — cmplog:0  n4:5
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_381_5_F` — cmplog:8,290  n4:24,000

### 630. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4_` @ 480:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 45)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:45  F:5
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4__480_6_T` — cmplog:7  n4:45
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4CBLCEEEP9hb_blob_tS4__480_6_F` — cmplog:0  n4:5

### 631. `hb_shape_full` @ 161:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,730, n4: 15,100)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,730
- **n4 coverage**: T:5  F:15,100
- **Canonical identifiers**:
  - `harfbuzz_hb_shape_full_161_9_T` — cmplog:0  n4:5
  - `harfbuzz_hb_shape_full_161_9_F` — cmplog:5,730  n4:15,100

### 632. `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` @ 234:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 471, n4: 1,250)
- **Flip strength**: 5 (blocked side hit 5× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:471
- **n4 coverage**: T:5  F:1,250
- **Canonical identifiers**:
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_234_7_T` — cmplog:0  n4:5
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_234_7_F` — cmplog:471  n4:1,250

### 633. `_ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj` @ 102:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 462, n4: 140,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:462
- **n4 coverage**: T:4  F:140,000
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_102_6_T` — cmplog:0  n4:4
  - `harfbuzz__ZN2OT6Layout9GPOS_impl20MarkBasePosFormat1_2INS0_10SmallTypesEE6acceptEP11hb_buffer_tj_102_6_F` — cmplog:462  n4:140,000

### 634. `_ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 830)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:830  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:7  n4:830
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl19MarkLigPosFormat1_2INS0_11MediumTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:4

### 635. `_ZNK3AAT21SubtableGlyphCoverage8sanitizeEP21hb_sanitize_context_tj` @ 1085:26
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 17, n4: 305)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:17
- **n4 coverage**: T:4  F:305
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT21SubtableGlyphCoverage8sanitizeEP21hb_sanitize_context_tj_1085_26_T` — cmplog:0  n4:4
  - `harfbuzz__ZNK3AAT21SubtableGlyphCoverage8sanitizeEP21hb_sanitize_context_tj_1085_26_F` — cmplog:17  n4:305

### 636. `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE14collect_glyphsI12hb_bit_set_tEEvRT_j` @ 700:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 24, n4: 23)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:24
- **n4 coverage**: T:4  F:23
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE14collect_glyphsI12hb_bit_set_tEEvRT_j_700_5_T` — cmplog:0  n4:4
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE14collect_glyphsI12hb_bit_set_tEEvRT_j_700_5_F` — cmplog:24  n4:23

### 637. `_ZN3AAT33hb_aat_layout_chain_accelerator_t6createINS_5ChainINS_13ExtendedTypesEEEEEPS0_RKT_j` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 134, n4: 618)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:134
- **n4 coverage**: T:4  F:618
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT33hb_aat_layout_chain_accelerator_t6createINS_5ChainINS_13ExtendedTypesEEEEEPS0_RKT_j_251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZN3AAT33hb_aat_layout_chain_accelerator_t6createINS_5ChainINS_13ExtendedTypesEEEEEPS0_RKT_j_251_24_F` — cmplog:134  n4:618

### 638. `_ZN10hb_array_tI15hb_glyph_info_tE8__next__Ev` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12,300, n4: 446,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12,300
- **n4 coverage**: T:4  F:446,000
- **Canonical identifiers**:
  - `harfbuzz__ZN10hb_array_tI15hb_glyph_info_tE8__next__Ev_251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZN10hb_array_tI15hb_glyph_info_tE8__next__Ev_251_24_F` — cmplog:12,300  n4:446,000

### 639. `_ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4_` @ 348:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6,400,000, n4: 98,500,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6,400,000
- **n4 coverage**: T:4  F:98,500,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__348_7_T` — cmplog:0  n4:4
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE23cff1_cs_opset_extents_tNS_20cff1_cs_interp_env_tE20cff1_extents_param_t25cff1_path_procs_extents_tE10process_opEjRS3_RS4__348_7_F` — cmplog:6,400,000  n4:98,500,000

### 640. `_ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5_` @ 348:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 43,600, n4: 8,790,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:43,600
- **n4 coverage**: T:4  F:8,790,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5__348_7_T` — cmplog:0  n4:4
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff2_cs_opset_path_tNS_20cff2_cs_interp_env_tIS1_EE17cff2_path_param_t22cff2_path_procs_path_tE10process_opEjRS4_RS5__348_7_F` — cmplog:43,600  n4:8,790,000

### 641. `hb_script_get_horizontal_direction` @ 605:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:4  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_605_5_T` — cmplog:0  n4:4
  - `harfbuzz_hb_script_get_horizontal_direction_605_5_F` — cmplog:29,700  n4:79,800

### 642. `_ZNK2OT8OffsetToINS_6Layout9GPOS_impl13LigatureArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT_` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 191)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:191  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl13LigatureArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT__350_45_T` — cmplog:2  n4:191
  - `harfbuzz__ZNK2OT8OffsetToINS_6Layout9GPOS_impl13LigatureArrayENS_7NumTypeILb1EjLj3EEEvLb1EE8sanitizeIJjEEEbP21hb_sanitize_context_tPKvDpOT__350_45_F` — cmplog:0  n4:4

### 643. `_ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_E16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 107)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:107  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:4  n4:107
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_19OpenTypeOffsetTableENS_7NumTypeILb1EjLj4EEEvLb1EEES4_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:4

### 644. `_ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE8sanitizeIJPKNS_4metaEEEEbP21hb_sanitize_context_tDpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 7, n4: 18)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:7
- **n4 coverage**: T:4  F:18
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE8sanitizeIJPKNS_4metaEEEEbP21hb_sanitize_context_tDpOT__251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE8sanitizeIJPKNS_4metaEEEEbP21hb_sanitize_context_tDpOT__251_24_F` — cmplog:7  n4:18

### 645. `_ZNK3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tPKvj` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 553, n4: 1,020)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:553  F:0
- **n4 coverage**: T:1,020  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tPKvj_350_45_T` — cmplog:553  n4:1,020
  - `harfbuzz__ZNK3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tPKvj_350_45_F` — cmplog:0  n4:4

### 646. `_ZNK3CFF8Encoding8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 10)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:10  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF8Encoding8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:10
  - `harfbuzz__ZNK3CFF8Encoding8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:4

### 647. `_ZNK2OT4cff113accelerator_t14get_glyph_nameEjPcj` @ 1401:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 261, n4: 766)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:261
- **n4 coverage**: T:4  F:766
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4cff113accelerator_t14get_glyph_nameEjPcj_1401_11_T` — cmplog:0  n4:4
  - `harfbuzz__ZNK2OT4cff113accelerator_t14get_glyph_nameEjPcj_1401_11_F` — cmplog:261  n4:766

### 648. `_ZNK2OT7DataMap8sanitizeEP21hb_sanitize_context_tPKv` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 18)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:18  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7DataMap8sanitizeEP21hb_sanitize_context_tPKv_350_45_T` — cmplog:7  n4:18
  - `harfbuzz__ZNK2OT7DataMap8sanitizeEP21hb_sanitize_context_tPKv_350_45_F` — cmplog:0  n4:4

### 649. `hb-ot-shaper-arabic.cc:_ZL29mongolian_variation_selectorsP11hb_buffer_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91, n4: 825)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91
- **n4 coverage**: T:4  F:825
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL29mongolian_variation_selectorsP11hb_buffer_t_251_24_T` — cmplog:0  n4:4
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL29mongolian_variation_selectorsP11hb_buffer_t_251_24_F` — cmplog:91  n4:825

### 650. `_Z20find_syllables_indicP11hb_buffer_t` @ 1225:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 189,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:4  F:189,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1225_2_T` — cmplog:0  n4:4
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1225_2_F` — cmplog:2,060  n4:189,000

### 651. `hb-ot-shaper-indic.cc:_ZL22final_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 112, n4: 1,780)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:112
- **n4 coverage**: T:4  F:1,780
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL22final_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_251_24_T` — cmplog:0  n4:4
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL22final_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_251_24_F` — cmplog:112  n4:1,780

### 652. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1150:56
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 1,150)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:1,150  F:4
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1150_56_T` — cmplog:2  n4:1,150
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1150_56_F` — cmplog:0  n4:4

### 653. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1244:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 957)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:957  F:4
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1244_7_T` — cmplog:2  n4:957
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1244_7_F` — cmplog:0  n4:4

### 654. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1274:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 953)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:4  F:953
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1274_11_T` — cmplog:0  n4:4
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1274_11_F` — cmplog:2  n4:953

### 655. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1372:27
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 953)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:953  F:4
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1372_27_T` — cmplog:2  n4:953
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1372_27_F` — cmplog:0  n4:4

### 656. `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj` @ 217:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 3,380)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:4  F:3,380
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_217_12_T` — cmplog:0  n4:4
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_217_12_F` — cmplog:27  n4:3,380

### 657. `_Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii` @ 68:39
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10,800, n4: 296,000)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10,800  F:0
- **n4 coverage**: T:296,000  F:4
- **Canonical identifiers**:
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_68_39_T` — cmplog:10,800  n4:296,000
  - `harfbuzz__Z33hb_syllabic_insert_dotted_circlesP9hb_font_tP11hb_buffer_tjjii_68_39_F` — cmplog:0  n4:4

### 658. `hb-ot-shaper-use.cc:_ZL15data_create_usePK18hb_ot_shape_plan_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 96)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:4  F:96
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15data_create_usePK18hb_ot_shape_plan_t_251_24_T` — cmplog:0  n4:4
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15data_create_usePK18hb_ot_shape_plan_t_251_24_F` — cmplog:12  n4:96

### 659. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 705:43
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 141, n4: 30)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:141  F:0
- **n4 coverage**: T:30  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_705_43_T` — cmplog:141  n4:30
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_705_43_F` — cmplog:0  n4:4

### 660. `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t` @ 92:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 64)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:4  F:64
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_92_7_T` — cmplog:0  n4:4
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_92_7_F` — cmplog:116  n4:64

### 661. `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t` @ 106:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 60)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:4  F:60
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_106_7_T` — cmplog:0  n4:4
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_106_7_F` — cmplog:116  n4:60

### 662. `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t` @ 117:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 60)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:4  F:60
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_117_7_T` — cmplog:0  n4:4
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_117_7_F` — cmplog:116  n4:60

### 663. `_ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_7ArrayOfIN3AAT6AnchorENS1_7NumTypeILb1EjLj4EEEEENS6_ILb1EtLj2EEEvLb0EEEEEbPKT_jj` @ 341:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 172)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:172  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_7ArrayOfIN3AAT6AnchorENS1_7NumTypeILb1EjLj4EEEEENS6_ILb1EtLj2EEEvLb0EEEEEbPKT_jj_341_5_T` — cmplog:5  n4:172
  - `harfbuzz__ZNK21hb_sanitize_context_t11check_rangeIN2OT8OffsetToINS1_7ArrayOfIN3AAT6AnchorENS1_7NumTypeILb1EjLj4EEEEENS6_ILb1EtLj2EEEvLb0EEEEEbPKT_jj_341_5_F` — cmplog:0  n4:4

### 664. `_ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl13LigatureArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0_` @ 428:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 191)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:191  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl13LigatureArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_T` — cmplog:2  n4:191
  - `harfbuzz__ZN21hb_sanitize_context_t7try_setIN2OT8OffsetToINS1_6Layout9GPOS_impl13LigatureArrayENS1_7NumTypeILb1EjLj3EEEvLb1EEEiEEbPKT_RKT0__428_9_F` — cmplog:0  n4:4

### 665. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4_` @ 474:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 59, n4: 232)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:59  F:0
- **n4 coverage**: T:232  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4__474_25_T` — cmplog:59  n4:232
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4__474_25_F` — cmplog:0  n4:4

### 666. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4_` @ 480:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 59, n4: 228)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:59  F:0
- **n4 coverage**: T:228  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4__480_6_T` — cmplog:59  n4:228
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4HVAREEEP9hb_blob_tS4__480_6_F` — cmplog:0  n4:4

### 667. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 472, n4: 754)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:472
- **n4 coverage**: T:4  F:754
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_F` — cmplog:472  n4:754

### 668. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl8LigatureINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,980, n4: 7,490)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,980
- **n4 coverage**: T:4  F:7,490
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl8LigatureINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl8LigatureINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_251_24_F` — cmplog:5,980  n4:7,490

### 669. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl11LigatureSetINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 539:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,930, n4: 2,530)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,930
- **n4 coverage**: T:4  F:2,530
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl11LigatureSetINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_T` — cmplog:0  n4:4
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl11LigatureSetINS3_10SmallTypesEEENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_F` — cmplog:1,930  n4:2,530

### 670. `_ZN9hb_utf8_t10encode_lenEj` @ 135:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1,190, n4: 2,870)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1,190  F:0
- **n4 coverage**: T:2,870  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZN9hb_utf8_t10encode_lenEj_135_9_T` — cmplog:1,190  n4:2,870
  - `harfbuzz__ZN9hb_utf8_t10encode_lenEj_135_9_F` — cmplog:0  n4:4

### 671. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 739, n4: 1,150)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:739
- **n4 coverage**: T:4  F:1,150
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb_251_24_T` — cmplog:0  n4:4
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb_251_24_F` — cmplog:739  n4:1,150

### 672. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 739, n4: 1,150)
- **Flip strength**: 4 (blocked side hit 4× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:739
- **n4 coverage**: T:4  F:1,150
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb_251_47_T` — cmplog:0  n4:4
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE5allocEjb_251_47_F` — cmplog:739  n4:1,150

### 673. `_ZN11hb_bounds_tIfE6union_ERKS0_` @ 329:16
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 4,110, n4: 202)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4,110  F:4
- **n4 coverage**: T:202  F:0
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_bounds_tIfE6union_ERKS0__329_16_T` — cmplog:4,110  n4:202
  - `harfbuzz__ZN11hb_bounds_tIfE6union_ERKS0__329_16_F` — cmplog:4  n4:0

### 674. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 231:5
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 233, n4: 991)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:233
- **n4 coverage**: T:0  F:991
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_231_5_T` — cmplog:4  n4:0
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_231_5_F` — cmplog:233  n4:991

### 675. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 269:5
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 233, n4: 991)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:233
- **n4 coverage**: T:0  F:991
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_269_5_T` — cmplog:4  n4:0
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_269_5_F` — cmplog:233  n4:991

### 676. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 777:30
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 2, n4: 4)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:2
- **n4 coverage**: T:0  F:4
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_777_30_T` — cmplog:4  n4:0
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_777_30_F` — cmplog:2  n4:4

### 677. `_ZN11hb_vector_tI15contour_point_tLb0EE6extendE10hb_array_tIS0_E` @ 251:24
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 6,180, n4: 165,000)
- **Flip strength**: 4 (blocked side hit 4× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:6,180
- **n4 coverage**: T:0  F:165,000
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tI15contour_point_tLb0EE6extendE10hb_array_tIS0_E_251_24_T` — cmplog:4  n4:0
  - `harfbuzz__ZN11hb_vector_tI15contour_point_tLb0EE6extendE10hb_array_tIS0_E_251_24_F` — cmplog:6,180  n4:165,000

### 678. `_ZNK2OT6Layout9GSUB_impl11SubstLookup10is_reverseEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,410, n4: 16,900)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,410
- **n4 coverage**: T:3  F:16,900
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SubstLookup10is_reverseEv_251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK2OT6Layout9GSUB_impl11SubstLookup10is_reverseEv_251_24_F` — cmplog:2,410  n4:16,900

### 679. `_ZNK2OT9glyf_impl20CompositeGlyphRecord10get_pointsER22contour_point_vector_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,200, n4: 4,410)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,200
- **n4 coverage**: T:3  F:4,410
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9glyf_impl20CompositeGlyphRecord10get_pointsER22contour_point_vector_t_251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK2OT9glyf_impl20CompositeGlyphRecord10get_pointsER22contour_point_vector_t_251_24_F` — cmplog:3,200  n4:4,410

### 680. `_ZN2OT22hb_ot_name_convert_utfI10hb_ascii_t9hb_utf8_tEEj10hb_array_tIKcEPjPNT0_11codepoint_tE` @ 62:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 39, n4: 120)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:39
- **n4 coverage**: T:3  F:120
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT22hb_ot_name_convert_utfI10hb_ascii_t9hb_utf8_tEEj10hb_array_tIKcEPjPNT0_11codepoint_tE_62_11_T` — cmplog:0  n4:3
  - `harfbuzz__ZN2OT22hb_ot_name_convert_utfI10hb_ascii_t9hb_utf8_tEEj10hb_array_tIKcEPjPNT0_11codepoint_tE_62_11_F` — cmplog:39  n4:120

### 681. `_ZNK3AAT19LookupSegmentSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0_` @ 301:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 237)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:3  F:237
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19LookupSegmentSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__301_9_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK3AAT19LookupSegmentSingleIN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__301_9_F` — cmplog:6  n4:237

### 682. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv` @ 746:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 191)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:3  F:191
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_746_5_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_746_5_F` — cmplog:6  n4:191

### 683. `_ZNK3AAT5ChainINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_tj` @ 1282:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 1)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:1  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_tj_1282_11_T` — cmplog:1  n4:1
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_tj_1282_11_F` — cmplog:0  n4:3

### 684. `_ZNK3AAT5ChainINS_13ExtendedTypesEE13compile_flagsEPK20hb_aat_map_builder_t` @ 1135:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 370, n4: 1,620)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:370
- **n4 coverage**: T:3  F:1,620
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE13compile_flagsEPK20hb_aat_map_builder_t_1135_11_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE13compile_flagsEPK20hb_aat_map_builder_t_1135_11_F` — cmplog:370  n4:1,620

### 685. `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE` @ 1173:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 416, n4: 2,480)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:416  F:0
- **n4 coverage**: T:2,480  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1173_30_T` — cmplog:416  n4:2,480
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1173_30_F` — cmplog:0  n4:3

### 686. `_ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE` @ 1174:32
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 416, n4: 2,480)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:416  F:0
- **n4 coverage**: T:2,480  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1174_32_T` — cmplog:416  n4:2,480
  - `harfbuzz__ZNK3AAT5ChainINS_13ExtendedTypesEE5applyEPNS_22hb_aat_apply_context_tEPKNS_33hb_aat_layout_chain_accelerator_tE_1174_32_F` — cmplog:0  n4:3

### 687. `hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0_` @ 1134:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91, n4: 826)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91
- **n4 coverage**: T:3  F:826
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_10_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_10_F` — cmplog:91  n4:826

### 688. `hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0_` @ 1134:10
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 68)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:68
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_10_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_10_F` — cmplog:1  n4:68

### 689. `_ZNK10hb_array_tIKN2OT5IndexEE11__item_at__Ej` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 2)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:3  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK10hb_array_tIKN2OT5IndexEE11__item_at__Ej_251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZNK10hb_array_tIKN2OT5IndexEE11__item_at__Ej_251_24_F` — cmplog:2  n4:2

### 690. `_ZN11hb_buffer_t11output_infoERK15hb_glyph_info_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,100, n4: 73,300)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,100
- **n4 coverage**: T:3  F:73,300
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t11output_infoERK15hb_glyph_info_t_251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZN11hb_buffer_t11output_infoERK15hb_glyph_info_t_251_24_F` — cmplog:18,100  n4:73,300

### 691. `_ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4_` @ 348:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3,800,000, n4: 71,000,000)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3,800,000
- **n4 coverage**: T:3  F:71,000,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__348_7_T` — cmplog:0  n4:3
  - `harfbuzz__ZN3CFF10cs_opset_tINS_8number_tE20cff1_cs_opset_path_tNS_20cff1_cs_interp_env_tE17cff1_path_param_t22cff1_path_procs_path_tE10process_opEjRS3_RS4__348_7_F` — cmplog:3,800,000  n4:71,000,000

### 692. `hb_language_matches` @ 443:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 27)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:3  F:27
- **Canonical identifiers**:
  - `harfbuzz_hb_language_matches_443_7_T` — cmplog:0  n4:3
  - `harfbuzz_hb_language_matches_443_7_F` — cmplog:3  n4:27

### 693. `hb_script_get_horizontal_direction` @ 588:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_588_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_588_5_F` — cmplog:29,700  n4:79,800

### 694. `hb_script_get_horizontal_direction` @ 591:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_591_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_591_5_F` — cmplog:29,700  n4:79,800

### 695. `hb_script_get_horizontal_direction` @ 606:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_606_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_606_5_F` — cmplog:29,700  n4:79,800

### 696. `hb_script_get_horizontal_direction` @ 607:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_607_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_607_5_F` — cmplog:29,700  n4:79,800

### 697. `hb_script_get_horizontal_direction` @ 622:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_622_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_622_5_F` — cmplog:29,700  n4:79,800

### 698. `hb_script_get_horizontal_direction` @ 625:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_625_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_625_5_F` — cmplog:29,700  n4:79,800

### 699. `hb_script_get_horizontal_direction` @ 626:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_626_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_626_5_F` — cmplog:29,700  n4:79,800

### 700. `hb_script_get_horizontal_direction` @ 638:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:3  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_638_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb_script_get_horizontal_direction_638_5_F` — cmplog:29,700  n4:79,800

### 701. `hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ_` @ 456:12
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 38, n4: 1,440)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:38  F:0
- **n4 coverage**: T:1,440  F:3
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ__456_12_T` — cmplog:38  n4:1,440
  - `harfbuzz_hb-ot-layout.cc:_ZN16hb_filter_iter_tI13hb_map_iter_tI10hb_array_tIKN2OT8OffsetToINS2_9ChainRuleINS2_6Layout10SmallTypesEEENS2_7NumTypeILb1EtLj2EEEvLb1EEEE12hb_partial_tILj2EPK4$_39PKNS2_12ChainRuleSetIS6_EEEL24hb_function_sortedness_t0ELPv0EEZNKSI_5applyEPNS2_21hb_ot_apply_context_tERKNS2_30ChainContextApplyLookupContextEEUlRKS7_E0_RK4$_19LSN_0EEC2ERKSO_SW_SZ__456_12_F` — cmplog:0  n4:3

### 702. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM_` @ 456:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 573)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:3  F:573
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM__456_12_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM__456_12_F` — cmplog:130  n4:573

### 703. `hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM_` @ 456:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 572)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:3  F:572
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM__456_18_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-use.cc:_ZN16hb_filter_iter_tIS_I13hb_zip_iter_tI14hb_iota_iter_tIjjE10hb_array_tI15hb_glyph_info_tEEZL18find_syllables_useP11hb_buffer_tEUlRKS4_E_RK4$_30LPv0EEZL18find_syllables_useS8_EUl9hb_pair_tIjSA_EE_RK4$_17LSF_0EEC2ERKSG_SJ_SM__456_18_F` — cmplog:130  n4:572

### 704. `_ZN2OT8OffsetToINS_6Layout6Common8CoverageENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJR17hb_sorted_array_tIKNS_11HBGlyphID16EEEEEbP22hb_serialize_context_tDpOT_` @ 469:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 284, n4: 383)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:284  F:0
- **n4 coverage**: T:383  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT8OffsetToINS_6Layout6Common8CoverageENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJR17hb_sorted_array_tIKNS_11HBGlyphID16EEEEEbP22hb_serialize_context_tDpOT__469_9_T` — cmplog:284  n4:383
  - `harfbuzz__ZN2OT8OffsetToINS_6Layout6Common8CoverageENS_7NumTypeILb1EtLj2EEEvLb1EE19serialize_serializeIJR17hb_sorted_array_tIKNS_11HBGlyphID16EEEEEbP22hb_serialize_context_tDpOT__469_9_F` — cmplog:0  n4:3

### 705. `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0_` @ 51:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 951, n4: 2,110)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:951
- **n4 coverage**: T:3  F:2,110
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EtLj2EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_F` — cmplog:951  n4:2,110

### 706. `_ZN3CFF18name_dict_values_t16name_op_to_indexEj` @ 722:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,120, n4: 4,820)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,120
- **n4 coverage**: T:3  F:4,820
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF18name_dict_values_t16name_op_to_indexEj_722_7_T` — cmplog:0  n4:3
  - `harfbuzz__ZN3CFF18name_dict_values_t16name_op_to_indexEj_722_7_F` — cmplog:2,120  n4:4,820

### 707. `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE` @ 784:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13,500, n4: 37,000)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13,500
- **n4 coverage**: T:3  F:37,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_784_7_T` — cmplog:0  n4:3
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_784_7_F` — cmplog:13,500  n4:37,000

### 708. `_ZN2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 563, n4: 768)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:563
- **n4 coverage**: T:3  F:768
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_251_47_T` — cmplog:0  n4:3
  - `harfbuzz__ZN2OT4cff119accelerator_templ_tIN3CFF25cff1_private_dict_opset_tENS2_31cff1_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_251_47_F` — cmplog:563  n4:768

### 709. `_ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 232, n4: 949)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:232
- **n4 coverage**: T:3  F:949
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_251_47_T` — cmplog:0  n4:3
  - `harfbuzz__ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_251_47_F` — cmplog:232  n4:949

### 710. `hb-ot-font.cc:_ZL26hb_ot_get_glyph_v_advancesP9hb_font_tPvjPKjjPijS1_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 258)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:258
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL26hb_ot_get_glyph_v_advancesP9hb_font_tPvjPKjjPijS1__251_24_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-font.cc:_ZL26hb_ot_get_glyph_v_advancesP9hb_font_tPvjPKjjPijS1__251_24_F` — cmplog:1  n4:258

### 711. `_ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 461, n4: 1,190)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:461  F:0
- **n4 coverage**: T:1,190  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:461  n4:1,190
  - `harfbuzz__ZNK2OT16ExtensionFormat1INS_6Layout9GPOS_impl12ExtensionPosEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:3

### 712. `_ZN2OT33hb_accelerate_subtables_context_t8dispatchINS_21ChainContextFormat2_5INS_6Layout11MediumTypesEEEEE10hb_empty_tRKT_` @ 1051:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 22)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:22
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT33hb_accelerate_subtables_context_t8dispatchINS_21ChainContextFormat2_5INS_6Layout11MediumTypesEEEEE10hb_empty_tRKT__1051_9_T` — cmplog:0  n4:3
  - `harfbuzz__ZN2OT33hb_accelerate_subtables_context_t8dispatchINS_21ChainContextFormat2_5INS_6Layout11MediumTypesEEEEE10hb_empty_tRKT__1051_9_F` — cmplog:1  n4:22

### 713. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 52:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 46)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:46
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_52_2_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_52_2_F` — cmplog:1  n4:46

### 714. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 53:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 46)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:46
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_53_2_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_53_2_F` — cmplog:1  n4:46

### 715. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 54:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 46)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:46
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_54_2_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_54_2_F` — cmplog:1  n4:46

### 716. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 55:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 46)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:46
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_55_2_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_55_2_F` — cmplog:1  n4:46

### 717. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 65:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 46)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:46
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_65_2_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_65_2_F` — cmplog:1  n4:46

### 718. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 91:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:3  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_91_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_91_5_F` — cmplog:389  n4:1,650

### 719. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 107:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:3  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_107_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_107_5_F` — cmplog:389  n4:1,650

### 720. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 113:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:3  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_113_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_113_5_F` — cmplog:389  n4:1,650

### 721. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 244:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 988)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:3  F:988
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_244_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_244_5_F` — cmplog:237  n4:988

### 722. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 259:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 988)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:3  F:988
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_259_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_259_5_F` — cmplog:237  n4:988

### 723. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 272:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 988)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:3  F:988
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_272_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_272_5_F` — cmplog:237  n4:988

### 724. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 298:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 988)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:3  F:988
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_298_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_298_5_F` — cmplog:237  n4:988

### 725. `_Z22_hb_ot_shape_normalizePK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 411:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 3, n4: 10)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:0
- **n4 coverage**: T:10  F:3
- **Canonical identifiers**:
  - `harfbuzz__Z22_hb_ot_shape_normalizePK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_411_5_T` — cmplog:3  n4:10
  - `harfbuzz__Z22_hb_ot_shape_normalizePK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_411_5_F` — cmplog:0  n4:3

### 726. `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t` @ 32:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 140, n4: 582)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:140
- **n4 coverage**: T:3  F:582
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_32_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_32_5_F` — cmplog:140  n4:582

### 727. `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t` @ 33:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 140, n4: 582)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:140
- **n4 coverage**: T:3  F:582
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_33_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_33_5_F` — cmplog:140  n4:582

### 728. `hb-ot-shaper-arabic.cc:_ZL12joining_typej` @ 200:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 10)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:10
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_200_11_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_200_11_F` — cmplog:1  n4:10

### 729. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 107:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 210)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:3  F:210
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_107_7_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_107_7_F` — cmplog:5  n4:210

### 730. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 127:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 72)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:3  F:72
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_127_4_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_127_4_F` — cmplog:1  n4:72

### 731. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 716:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 978, n4: 24,900)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:978
- **n4 coverage**: T:3  F:24,900
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_716_6_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_716_6_F` — cmplog:978  n4:24,900

### 732. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1085:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 16, n4: 9,000)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:16  F:0
- **n4 coverage**: T:9,000  F:3
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1085_11_T` — cmplog:16  n4:9,000
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1085_11_F` — cmplog:0  n4:3

### 733. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1087:8
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16, n4: 8,960)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16
- **n4 coverage**: T:3  F:8,960
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1087_8_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1087_8_F` — cmplog:16  n4:8,960

### 734. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 345:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 80, n4: 1,160)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:80
- **n4 coverage**: T:3  F:1,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__345_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__345_5_F` — cmplog:80  n4:1,160

### 735. `hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 330:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 22, n4: 166)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:22
- **n4 coverage**: T:3  F:166
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_330_9_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_330_9_F` — cmplog:22  n4:166

### 736. `hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj` @ 280:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 27, n4: 4,610)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:27
- **n4 coverage**: T:3  F:4,610
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_280_9_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL37initial_reordering_consonant_syllableP11hb_buffer_tjj_280_9_F` — cmplog:27  n4:4,610

### 737. `hb-ot-shaper-thai.cc:_ZL13get_mark_typej` @ 78:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 224, n4: 2,200)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:224
- **n4 coverage**: T:3  F:2,200
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_78_7_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL13get_mark_typej_78_7_F` — cmplog:224  n4:2,200

### 738. `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` @ 55:23
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 220, n4: 2,150)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:220
- **n4 coverage**: T:3  F:2,150
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_55_23_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_55_23_F` — cmplog:220  n4:2,150

### 739. `hb-ot-shaper-thai.cc:_ZL18get_consonant_typej` @ 57:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 220, n4: 2,140)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:220
- **n4 coverage**: T:3  F:2,140
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_57_7_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL18get_consonant_typej_57_7_F` — cmplog:220  n4:2,140

### 740. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 121:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 75, n4: 941)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:75
- **n4 coverage**: T:3  F:941
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_121_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_121_4_F` — cmplog:75  n4:941

### 741. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 144:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 372)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:3  F:372
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_144_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_144_4_F` — cmplog:30  n4:372

### 742. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 152:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 372)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:3  F:372
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_152_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_152_4_F` — cmplog:30  n4:372

### 743. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 199:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 45, n4: 2,840)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:45
- **n4 coverage**: T:3  F:2,840
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_199_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_199_4_F` — cmplog:45  n4:2,840

### 744. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 251:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 987)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:3  F:987
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_251_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_251_4_F` — cmplog:30  n4:987

### 745. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 306:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 570, n4: 1,060)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:570
- **n4 coverage**: T:3  F:1,060
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_306_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_306_4_F` — cmplog:570  n4:1,060

### 746. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 370:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 117)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:3  F:117
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_370_4_T` — cmplog:0  n4:3
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_370_4_F` — cmplog:15  n4:117

### 747. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 301:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:3  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_301_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_301_5_F` — cmplog:8,290  n4:24,000

### 748. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 397:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:3  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_397_5_T` — cmplog:0  n4:3
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_397_5_F` — cmplog:8,290  n4:24,000

### 749. `_ZNK2OT11SegmentMaps9map_floatEfjj` @ 188:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 381, n4: 1,650)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:381  F:0
- **n4 coverage**: T:1,650  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT11SegmentMaps9map_floatEfjj_188_14_T` — cmplog:381  n4:1,650
  - `harfbuzz__ZNK2OT11SegmentMaps9map_floatEfjj_188_14_F` — cmplog:0  n4:3

### 750. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb` @ 755:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 141, n4: 31)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:141  F:0
- **n4 coverage**: T:31  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_755_10_T` — cmplog:141  n4:31
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EtLj2EEELj1735811442EE13accelerator_t22apply_deltas_to_pointsEj10hb_array_tIKiES5_I15contour_point_tER17hb_glyf_scratch_tPNS_17hb_scalar_cache_tEb_755_10_F` — cmplog:0  n4:3

### 751. `_ZNK2OT4VVAR8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 727)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:727  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VVAR8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:5  n4:727
  - `harfbuzz__ZNK2OT4VVAR8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:3

### 752. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4_` @ 474:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 37)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:37  F:3
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4__474_25_T` — cmplog:1  n4:37
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4__474_25_F` — cmplog:0  n4:3

### 753. `_ZN22hb_serialize_context_t8pop_packEb` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,460, n4: 7,840)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,460
- **n4 coverage**: T:3  F:7,840
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8pop_packEb_251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZN22hb_serialize_context_t8pop_packEb_251_24_F` — cmplog:5,460  n4:7,840

### 754. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 539:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 472, n4: 751)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:472
- **n4 coverage**: T:3  F:751
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_T` — cmplog:0  n4:3
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout6Common8CoverageENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_F` — cmplog:472  n4:751

### 755. `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` @ 232:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 471, n4: 1,250)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:471
- **n4 coverage**: T:3  F:1,250
- **Canonical identifiers**:
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_232_7_T` — cmplog:0  n4:3
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_232_7_F` — cmplog:471  n4:1,250

### 756. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 473, n4: 793)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:473
- **n4 coverage**: T:3  F:793
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT__251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT__251_24_F` — cmplog:473  n4:793

### 757. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT_` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 473, n4: 793)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:473
- **n4 coverage**: T:3  F:793
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT__251_47_T` — cmplog:0  n4:3
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJDnEEEPS2_DpOT__251_47_F` — cmplog:473  n4:793

### 758. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5,460, n4: 7,840)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5,460
- **n4 coverage**: T:3  F:7,840
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT__251_24_T` — cmplog:0  n4:3
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT__251_24_F` — cmplog:5,460  n4:7,840

### 759. `_ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT_` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 266, n4: 362)
- **Flip strength**: 3 (blocked side hit 3× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:266
- **n4 coverage**: T:3  F:362
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT__251_47_T` — cmplog:0  n4:3
  - `harfbuzz__ZN11hb_vector_tIPN22hb_serialize_context_t8object_tELb0EE4pushIJRS2_EEEPS2_DpOT__251_47_F` — cmplog:266  n4:362

### 760. `_ZNK2OT3SVG13accelerator_t11paint_glyphEP9hb_font_tjP16hb_paint_funcs_tPv` @ 104:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 17)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:17  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT3SVG13accelerator_t11paint_glyphEP9hb_font_tjP16hb_paint_funcs_tPv_104_11_T` — cmplog:4  n4:17
  - `harfbuzz__ZNK2OT3SVG13accelerator_t11paint_glyphEP9hb_font_tjP16hb_paint_funcs_tPv_104_11_F` — cmplog:0  n4:2

### 761. `_ZNK2OT6Layout6Common8Coverage16collect_coverageI12hb_bit_set_tEEbPT_` @ 241:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,120, n4: 2,490)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,120
- **n4 coverage**: T:2  F:2,490
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout6Common8Coverage16collect_coverageI12hb_bit_set_tEEbPT__241_5_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT6Layout6Common8Coverage16collect_coverageI12hb_bit_set_tEEbPT__241_5_F` — cmplog:1,120  n4:2,490

### 762. `_ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 3,730)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:2  F:3,730
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT4VARC13accelerator_t11get_extentsEP9hb_font_tjP18hb_glyph_extents_t_251_24_F` — cmplog:8  n4:3,730

### 763. `_ZNK2OT4VARC13accelerator_t15acquire_scratchEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 1,130)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:1,130
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VARC13accelerator_t15acquire_scratchEv_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT4VARC13accelerator_t15acquire_scratchEv_251_24_F` — cmplog:2  n4:1,130

### 764. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1274:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 32)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:32  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1274_7_T` — cmplog:6  n4:32
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataENS_16LigatureSubtableIS1_E5FlagsEE5driveINS6_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1274_7_F` — cmplog:0  n4:2

### 765. `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1054:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 299)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:2  F:299
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1054_11_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1054_11_F` — cmplog:6  n4:299

### 766. `_ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE` @ 1063:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 299)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:2  F:299
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1063_11_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE5applyEPNS_22hb_aat_apply_context_tERKNS_23kern_accelerator_data_tE_1063_11_F` — cmplog:6  n4:299

### 767. `_ZNK3AAT9KerxTableIN2OT7KernAATEE23create_accelerator_dataEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 179)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:2  F:179
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE23create_accelerator_dataEj_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE23create_accelerator_dataEj_251_24_F` — cmplog:3  n4:179

### 768. `hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH_` @ 1204:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 133)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:133
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH__1204_9_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-cff1-table.cc:_ZL15hb_bsearch_implIKN3CFF17FDSelect3_4_RangeIN2OT7NumTypeILb1EtLj2EEENS3_ILb1EhLj1EEEEEjJEEbPjRKT0_PT_mmPFiPKvSF_DpT1_ESH__1204_9_F` — cmplog:2  n4:133

### 769. `_ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE` @ 661:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 60, n4: 167)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:60  F:0
- **n4 coverage**: T:167  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE_661_11_T` — cmplog:60  n4:167
  - `harfbuzz__ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE_661_11_F` — cmplog:0  n4:2

### 770. `hb_script_get_horizontal_direction` @ 589:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:2  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_589_5_T` — cmplog:0  n4:2
  - `harfbuzz_hb_script_get_horizontal_direction_589_5_F` — cmplog:29,700  n4:79,800

### 771. `hb_script_get_horizontal_direction` @ 608:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:2  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_608_5_T` — cmplog:0  n4:2
  - `harfbuzz_hb_script_get_horizontal_direction_608_5_F` — cmplog:29,700  n4:79,800

### 772. `hb_draw_funcs_set_close_path_func` @ 148:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 1,050)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:1,050
- **Canonical identifiers**:
  - `harfbuzz_hb_draw_funcs_set_close_path_func_148_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb_draw_funcs_set_close_path_func_148_7_F` — cmplog:2  n4:1,050

### 773. `hb-font.cc:_ZL34hb_font_get_nominal_glyphs_defaultP9hb_font_tPvjPKjjPjjS1_` @ 179:30
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 185, n4: 422)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:185  F:0
- **n4 coverage**: T:422  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-font.cc:_ZL34hb_font_get_nominal_glyphs_defaultP9hb_font_tPvjPKjjPjjS1__179_30_T` — cmplog:185  n4:422
  - `harfbuzz_hb-font.cc:_ZL34hb_font_get_nominal_glyphs_defaultP9hb_font_tPvjPKjjPjjS1__179_30_F` — cmplog:0  n4:2

### 774. `_ZN11hb_bounds_tIfE9intersectERKS0_` @ 342:16
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 12)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:12  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__342_16_T` — cmplog:2  n4:12
  - `harfbuzz__ZN11hb_bounds_tIfE9intersectERKS0__342_16_F` — cmplog:0  n4:2

### 775. `_ZN16hb_lazy_loader_tI15hb_draw_funcs_tN2OT39hb_transforming_pen_funcs_lazy_loader_tEvLj0ES0_E10do_destroyEPS0_` @ 209:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 1,050)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:1,050  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN16hb_lazy_loader_tI15hb_draw_funcs_tN2OT39hb_transforming_pen_funcs_lazy_loader_tEvLj0ES0_E10do_destroyEPS0__209_14_T` — cmplog:2  n4:1,050
  - `harfbuzz__ZN16hb_lazy_loader_tI15hb_draw_funcs_tN2OT39hb_transforming_pen_funcs_lazy_loader_tEvLj0ES0_E10do_destroyEPS0__209_14_F` — cmplog:0  n4:2

### 776. `hb-paint-extents.cc:_ZNK3$_2clIRfRKfEEDTqulefp_fp0_fp_fp0_EOT_OT0_` @ 76:55
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 22)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:22  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-paint-extents.cc:_ZNK3$_2clIRfRKfEEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_T` — cmplog:4  n4:22
  - `harfbuzz_hb-paint-extents.cc:_ZNK3$_2clIRfRKfEEDTqulefp_fp0_fp_fp0_EOT_OT0__76_55_F` — cmplog:0  n4:2

### 777. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 517, n4: 52,400)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:517
- **n4 coverage**: T:2  F:52,400
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT12LookupSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_251_24_F` — cmplog:517  n4:52,400

### 778. `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_EixEi` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 10)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:2  F:10
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_EixEi_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_EixEi_251_24_F` — cmplog:1  n4:10

### 779. `_ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 8)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:8  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:8
  - `harfbuzz__ZNK2OT7ArrayOfINS_7DataMapENS_7NumTypeILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:2

### 780. `_ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7_` @ 262:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 133)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:133
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7__262_9_T` — cmplog:0  n4:2
  - `harfbuzz__ZN3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE10_cmp_rangeEPKvS7__262_9_F` — cmplog:2  n4:133

### 781. `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0_` @ 51:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 491, n4: 1,960)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:491
- **n4 coverage**: T:2  F:1,960
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_5SubrsIN2OT7NumTypeILb1EjLj4EEEEEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_F` — cmplog:491  n4:1,960

### 782. `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF1FDSelectEJRKN2OT7NumTypeILb1EtLj2EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0_` @ 51:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 33, n4: 222)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:33
- **n4 coverage**: T:2  F:222
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF1FDSelectEJRKN2OT7NumTypeILb1EtLj2EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_12CFF1FDSelectEJRKN2OT7NumTypeILb1EtLj2EEEEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_F` — cmplog:33  n4:222

### 783. `_ZNK3CFF8Encoding11suppEncDataEv` @ 291:5
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 12)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:12  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF8Encoding11suppEncDataEv_291_5_T` — cmplog:1  n4:12
  - `harfbuzz__ZNK3CFF8Encoding11suppEncDataEv_291_5_F` — cmplog:0  n4:2

### 784. `_ZNK3CFF8Encoding11suppEncDataEv` @ 292:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 12)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:2  F:12
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF8Encoding11suppEncDataEv_292_5_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK3CFF8Encoding11suppEncDataEv_292_5_F` — cmplog:1  n4:12

### 785. `_ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE` @ 941:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 26,600, n4: 48,300)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:26,600
- **n4 coverage**: T:2  F:48,300
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE_941_7_T` — cmplog:0  n4:2
  - `harfbuzz__ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE_941_7_F` — cmplog:26,600  n4:48,300

### 786. `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj` @ 97:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 90)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:90
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_97_5_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_97_5_F` — cmplog:2  n4:90

### 787. `_ZNK2OT8ClassDef4costEv` @ 2209:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 339, n4: 2,080)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:339
- **n4 coverage**: T:2  F:2,080
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT8ClassDef4costEv_2209_5_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK2OT8ClassDef4costEv_2209_5_F` — cmplog:339  n4:2,080

### 788. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 583:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 313)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:2  F:313
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_583_2_T` — cmplog:0  n4:2
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_583_2_F` — cmplog:28  n4:313

### 789. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 595:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 313)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:2  F:313
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_595_2_T` — cmplog:0  n4:2
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_595_2_F` — cmplog:28  n4:313

### 790. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 281:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 12)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:12  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_281_11_T` — cmplog:5  n4:12
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_281_11_F` — cmplog:0  n4:2

### 791. `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t` @ 167:26
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 52, n4: 358)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:52
- **n4 coverage**: T:2  F:358
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_167_26_T` — cmplog:0  n4:2
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_167_26_F` — cmplog:52  n4:358

### 792. `hb-ot-shaper-arabic.cc:_ZL20reorder_marks_arabicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 711:23
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 145, n4: 297)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:145  F:0
- **n4 coverage**: T:297  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL20reorder_marks_arabicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_711_23_T` — cmplog:145  n4:297
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL20reorder_marks_arabicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_711_23_F` — cmplog:0  n4:2

### 793. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 86:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 211)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:2  F:211
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_86_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_86_7_F` — cmplog:5  n4:211

### 794. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 113:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 211)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:2  F:211
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_113_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_113_7_F` — cmplog:5  n4:211

### 795. `_Z20find_syllables_indicP11hb_buffer_t` @ 1221:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,060, n4: 189,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,060
- **n4 coverage**: T:2  F:189,000
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1221_2_T` — cmplog:0  n4:2
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1221_2_F` — cmplog:2,060  n4:189,000

### 796. `hb-ot-shaper-indic.cc:_ZL24initial_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 119, n4: 1,780)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:119  F:0
- **n4 coverage**: T:1,780  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL24initial_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:119  n4:1,780
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL24initial_reordering_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:2

### 797. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 679:20
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 80)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:2  F:80
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_679_20_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_679_20_F` — cmplog:2  n4:80

### 798. `hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj` @ 819:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 9, n4: 6,230)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:9  F:0
- **n4 coverage**: T:6,230  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_819_6_T` — cmplog:9  n4:6,230
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL37initial_reordering_consonant_syllablePK18hb_ot_shape_plan_tP9hb_face_tP11hb_buffer_tjj_819_6_F` — cmplog:0  n4:2

### 799. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1105:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91, n4: 4,010)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91
- **n4 coverage**: T:2  F:4,010
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1105_7_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1105_7_F` — cmplog:91  n4:4,010

### 800. `_Z20find_syllables_khmerP11hb_buffer_t` @ 365:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 45,900)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:2  F:45,900
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_365_2_T` — cmplog:0  n4:2
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_365_2_F` — cmplog:8,260  n4:45,900

### 801. `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 363:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 31)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:31  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_363_11_T` — cmplog:1  n4:31
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_363_11_F` — cmplog:0  n4:2

### 802. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 997:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:2  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_997_2_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_997_2_F` — cmplog:2,020  n4:73,800

### 803. `hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj` @ 437:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 1,210)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:1,210  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_437_7_T` — cmplog:1  n4:1,210
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL20reorder_syllable_useP11hb_buffer_tjj_437_7_F` — cmplog:0  n4:2

### 804. `hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t` @ 358:3
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 34, n4: 381)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:34  F:0
- **n4 coverage**: T:381  F:2
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t_358_3_T` — cmplog:34  n4:381
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL13is_halant_useRK15hb_glyph_info_t_358_3_F` — cmplog:0  n4:2

### 805. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 272:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 105, n4: 16,900)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:105
- **n4 coverage**: T:2  F:16,900
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_272_4_T` — cmplog:0  n4:2
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_272_4_F` — cmplog:105  n4:16,900

### 806. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 303:32
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 570, n4: 1,060)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:570
- **n4 coverage**: T:2  F:1,060
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_32_T` — cmplog:0  n4:2
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_32_F` — cmplog:570  n4:1,060

### 807. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 400:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 262, n4: 2,370)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:262
- **n4 coverage**: T:2  F:2,370
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_400_5_T` — cmplog:0  n4:2
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_400_5_F` — cmplog:262  n4:2,370

### 808. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 320:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:2  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_320_5_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_320_5_F` — cmplog:8,290  n4:24,000

### 809. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 341:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:2  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_341_5_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_341_5_F` — cmplog:8,290  n4:24,000

### 810. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 374:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:2  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_374_5_T` — cmplog:0  n4:2
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_374_5_F` — cmplog:8,290  n4:24,000

### 811. `_ZNK2OT9gvar_GVARINS_7NumTypeILb1EjLj3EEELj1196835154EE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 318)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:318  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EjLj3EEELj1196835154EE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:318
  - `harfbuzz__ZNK2OT9gvar_GVARINS_7NumTypeILb1EjLj3EEELj1196835154EE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:2

### 812. `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t` @ 84:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 66)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:2  F:66
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_84_7_T` — cmplog:0  n4:2
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_84_7_F` — cmplog:116  n4:66

### 813. `_ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t` @ 91:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 66)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:2  F:66
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_91_7_T` — cmplog:0  n4:2
  - `harfbuzz__ZN26hb_paint_bounded_context_t9pop_groupE25hb_paint_composite_mode_t_91_7_F` — cmplog:116  n4:66

### 814. `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t` @ 109:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 62)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:2  F:62
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_109_7_T` — cmplog:0  n4:2
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_109_7_F` — cmplog:116  n4:62

### 815. `_ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t` @ 116:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 116, n4: 62)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:116
- **n4 coverage**: T:2  F:62
- **Canonical identifiers**:
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_116_7_T` — cmplog:0  n4:2
  - `harfbuzz__ZN26hb_paint_extents_context_t9pop_groupE25hb_paint_composite_mode_t_116_7_F` — cmplog:116  n4:62

### 816. `_ZN21hb_sanitize_context_t13sanitize_blobIN3AAT4ankrEEEP9hb_blob_tS4_` @ 480:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 14, n4: 78)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14  F:0
- **n4 coverage**: T:78  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN3AAT4ankrEEEP9hb_blob_tS4__480_6_T` — cmplog:14  n4:78
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN3AAT4ankrEEEP9hb_blob_tS4__480_6_F` — cmplog:0  n4:2

### 817. `_ZNK21hb_sanitize_context_t17check_array_sizedIN3AAT6AnchorEEEbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 294)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:2  F:294
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN3AAT6AnchorEEEbPKT_jj_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN3AAT6AnchorEEEbPKT_jj_251_24_F` — cmplog:6  n4:294

### 818. `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_19OpenTypeOffsetTableENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 109)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:2  F:109
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_19OpenTypeOffsetTableENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT8OffsetToINS1_19OpenTypeOffsetTableENS1_7NumTypeILb1EjLj4EEEvLb1EEEEEbPKT_jj_251_24_F` — cmplog:4  n4:109

### 819. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4_` @ 480:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 35)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:35  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4__480_6_T` — cmplog:1  n4:35
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT16OpenTypeFontFileEEEP9hb_blob_tS4__480_6_F` — cmplog:0  n4:2

### 820. `_ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj` @ 539:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 472, n4: 748)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:472
- **n4 coverage**: T:2  F:748
- **Canonical identifiers**:
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_T` — cmplog:0  n4:2
  - `harfbuzz__ZN22hb_serialize_context_t8add_linkIN2OT8OffsetToINS1_6Layout9GSUB_impl19SubstLookupSubTableENS1_7NumTypeILb1EtLj2EEEvLb1EEEEEvRT_jNS_8whence_tEj_539_9_F` — cmplog:472  n4:748

### 821. `_ZNK11hb_vector_tI12hb_bit_set_tLb0EEixEi` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 43, n4: 73,100)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:43  F:0
- **n4 coverage**: T:73,100  F:2
- **Canonical identifiers**:
  - `harfbuzz__ZNK11hb_vector_tI12hb_bit_set_tLb0EEixEi_251_24_T` — cmplog:43  n4:73,100
  - `harfbuzz__ZNK11hb_vector_tI12hb_bit_set_tLb0EEixEi_251_24_F` — cmplog:0  n4:2

### 822. `_ZN11hb_vector_tIfLb0EE5allocEjb` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 87, n4: 789)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:87
- **n4 coverage**: T:2  F:789
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_251_24_T` — cmplog:0  n4:2
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_251_24_F` — cmplog:87  n4:789

### 823. `_ZN11hb_vector_tIfLb0EE5allocEjb` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 87, n4: 789)
- **Flip strength**: 2 (blocked side hit 2× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:87
- **n4 coverage**: T:2  F:789
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_251_47_T` — cmplog:0  n4:2
  - `harfbuzz__ZN11hb_vector_tIfLb0EE5allocEjb_251_47_F` — cmplog:87  n4:789

### 824. `_ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE14get_populationEv` @ 73:12
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 64, n4: 82)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:64
- **n4 coverage**: T:0  F:82
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE14get_populationEv_73_12_T` — cmplog:2  n4:0
  - `harfbuzz__ZNK2OT6Layout6Common17CoverageFormat2_4INS0_11MediumTypesEE14get_populationEv_73_12_F` — cmplog:64  n4:82

### 825. `hb-face.cc:_ZL15hb_bsearch_implIKN2OT23VariationSelectorRecordEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC_` @ 1206:14
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 28, n4: 68)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:28  F:2
- **n4 coverage**: T:68  F:0
- **Canonical identifiers**:
  - `harfbuzz_hb-face.cc:_ZL15hb_bsearch_implIKN2OT23VariationSelectorRecordEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_T` — cmplog:28  n4:68
  - `harfbuzz_hb-face.cc:_ZL15hb_bsearch_implIKN2OT23VariationSelectorRecordEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_F` — cmplog:2  n4:0

### 826. `_ZN17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE7bsearchIjEEPS2_RKT_S5_` @ 399:12
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 12,200, n4: 33,100)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:12,200
- **n4 coverage**: T:0  F:33,100
- **Canonical identifiers**:
  - `harfbuzz__ZN17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE7bsearchIjEEPS2_RKT_S5__399_12_T` — cmplog:2  n4:0
  - `harfbuzz__ZN17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE7bsearchIjEEPS2_RKT_S5__399_12_F` — cmplog:12,200  n4:33,100

### 827. `_ZNK17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE5bfindIjEEbRKT_Pj14hb_not_found_tj` @ 414:9
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 12,200, n4: 33,100)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:12,200
- **n4 coverage**: T:0  F:33,100
- **Canonical identifiers**:
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_T` — cmplog:2  n4:0
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT23VariationSelectorRecordEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_F` — cmplog:12,200  n4:33,100

### 828. `_ZNK2OT16OpenTypeFontFile8sanitizeEP21hb_sanitize_context_t` @ 520:5
- **Blocked side**: True (0 hits in `n4`)
- **Hit side**: False (cmplog: 6,130, n4: 16,500)
- **Flip strength**: 2 (blocked side hit 2× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:6,130
- **n4 coverage**: T:0  F:16,500
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT16OpenTypeFontFile8sanitizeEP21hb_sanitize_context_t_520_5_T` — cmplog:2  n4:0
  - `harfbuzz__ZNK2OT16OpenTypeFontFile8sanitizeEP21hb_sanitize_context_t_520_5_F` — cmplog:6,130  n4:16,500

### 829. `_ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 934, n4: 6,280)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:934
- **n4 coverage**: T:1  F:6,280
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl13AnchorFormat38sanitizeEP21hb_sanitize_context_t_251_24_F` — cmplog:934  n4:6,280

### 830. `_ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE` @ 128:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18, n4: 280)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:0
- **n4 coverage**: T:280  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_128_11_T` — cmplog:18  n4:280
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl20MarkMarkPosFormat1_2INS0_10SmallTypesEE5applyEPNS_21hb_ot_apply_context_tE_128_11_F` — cmplog:0  n4:1

### 831. `_ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t` @ 89:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 627, n4: 5,810)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:627
- **n4 coverage**: T:1  F:5,810
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_89_9_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK2OT6Layout9GPOS_impl11ValueFormat11apply_valueEPNS_21hb_ot_apply_context_tEPKNS1_9ValueBaseEPKNS_7NumTypeILb1EtLj2EEER19hb_glyph_position_t_89_9_F` — cmplog:627  n4:5,810

### 832. `_ZNK3AAT14LookupFormat10IN2OT7NumTypeILb1EtLj2EEEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 4)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:4  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT14LookupFormat10IN2OT7NumTypeILb1EtLj2EEEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:4
  - `harfbuzz__ZNK3AAT14LookupFormat10IN2OT7NumTypeILb1EtLj2EEEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 833. `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t` @ 731:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 64, n4: 298)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:64
- **n4 coverage**: T:1  F:298
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_731_5_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_731_5_F` — cmplog:64  n4:298

### 834. `_ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t` @ 735:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 64, n4: 298)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:64
- **n4 coverage**: T:1  F:298
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_735_5_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT6LookupIN2OT11HBGlyphID16EE8sanitizeEP21hb_sanitize_context_t_735_5_F` — cmplog:64  n4:298

### 835. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj` @ 251:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 176)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:176  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_47_T` — cmplog:7  n4:176
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_13LigatureEntryILb1EE9EntryDataEE8sanitizeEP21hb_sanitize_context_tPj_251_47_F` — cmplog:0  n4:1

### 836. `_ZNK3AAT13LookupFormat8IN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 84, n4: 215)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:84
- **n4 coverage**: T:1  F:215
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT13LookupFormat8IN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT13LookupFormat8IN2OT7NumTypeILb1EtLj2EEEE23collect_glyphs_filteredI12hb_bit_set_t13hb_bit_page_tEEvRT_RKT0__251_24_F` — cmplog:84  n4:215

### 837. `_ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE` @ 1278:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 19,400)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:19,400  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1278_9_T` — cmplog:1  n4:19,400
  - `harfbuzz__ZN3AAT16StateTableDriverINS_13ExtendedTypesEvNS_21RearrangementSubtableIS1_E5FlagsEE5driveINS3_16driver_context_tEEEvPT_PNS_22hb_aat_apply_context_tE_1278_9_F` — cmplog:0  n4:1

### 838. `_ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,200, n4: 137,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,200
- **n4 coverage**: T:1  F:137,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT__251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3AAT22hb_aat_apply_context_t13output_glyphsIN2OT11HBGlyphID16EEEbjPKT__251_24_F` — cmplog:18,200  n4:137,000

### 839. `_ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tS4_EEvRT_jRKT0_` @ 864:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 117, n4: 83)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:117
- **n4 coverage**: T:1  F:83
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tS4_EEvRT_jRKT0__864_42_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT10StateTableINS_13ExtendedTypesENS_19KerxSubTableFormat4INS_18KerxSubTableHeaderEE9EntryDataEE22collect_initial_glyphsI12hb_bit_set_tS4_EEvRT_jRKT0__864_42_F` — cmplog:117  n4:83

### 840. `_ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv` @ 749:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 6, n4: 193)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:6
- **n4 coverage**: T:1  F:193
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_749_5_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT6LookupIN2OT8OffsetToINS1_7ArrayOfINS_6AnchorENS1_7NumTypeILb1EjLj4EEEEENS5_ILb1EtLj2EEEvLb0EEEE8sanitizeEP21hb_sanitize_context_tPKv_749_5_F` — cmplog:6  n4:193

### 841. `_ZNK3AAT9KerxTableINS_4kerxEE23create_accelerator_dataEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 41, n4: 248)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:41
- **n4 coverage**: T:1  F:248
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE23create_accelerator_dataEj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3AAT9KerxTableINS_4kerxEE23create_accelerator_dataEj_251_24_F` — cmplog:41  n4:248

### 842. `_ZNK3AAT9KerxTableIN2OT7KernAATEE8sanitizeEP21hb_sanitize_context_t` @ 251:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 10, n4: 138)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:10  F:0
- **n4 coverage**: T:138  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE8sanitizeEP21hb_sanitize_context_t_251_47_T` — cmplog:10  n4:138
  - `harfbuzz__ZNK3AAT9KerxTableIN2OT7KernAATEE8sanitizeEP21hb_sanitize_context_t_251_47_F` — cmplog:0  n4:1

### 843. `_ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 80)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:80  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:80
  - `harfbuzz__ZNK3AAT19KerxSubTableFormat2IN2OT21KernAATSubTableHeaderEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 844. `_ZNK3AAT16LigatureSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 150)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:150  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT16LigatureSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:6  n4:150
  - `harfbuzz__ZNK3AAT16LigatureSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 845. `_ZNK3AAT17InsertionSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 75, n4: 423)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:75  F:0
- **n4 coverage**: T:423  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT17InsertionSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:75  n4:423
  - `harfbuzz__ZNK3AAT17InsertionSubtableINS_13ExtendedTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 846. `_ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj` @ 1260:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 52, n4: 586)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:52  F:0
- **n4 coverage**: T:586  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj_1260_11_T` — cmplog:52  n4:586
  - `harfbuzz__ZNK3AAT5ChainINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_tj_1260_11_F` — cmplog:0  n4:1

### 847. `_ZNK3AAT17InsertionSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 118)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:118  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3AAT17InsertionSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:118
  - `harfbuzz__ZNK3AAT17InsertionSubtableINS_13ObsoleteTypesEE8sanitizeEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 848. `hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC_` @ 1206:14
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 8, n4: 22)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:8  F:0
- **n4 coverage**: T:22  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_T` — cmplog:8  n4:22
  - `harfbuzz_hb-ot-font.cc:_ZL15hb_bsearch_implIKN2OT16VertOriginMetricEjJEEbPjRKT0_PT_mmPFiPKvSA_DpT1_ESC__1206_14_F` — cmplog:0  n4:1

### 849. `hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0_` @ 1134:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 91, n4: 825)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:91
- **n4 coverage**: T:1  F:825
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_F` — cmplog:91  n4:825

### 850. `hb-ot-shaper-hangul.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0_` @ 1134:42
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 726, n4: 2,520)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:726
- **n4 coverage**: T:1  F:2,520
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL12hb_in_rangesIjJjjEEbT_S0_S0_DpT0__1134_42_F` — cmplog:726  n4:2,520

### 851. `_ZNK17hb_sorted_array_tIKN2OT16VertOriginMetricEE5bfindIjEEbRKT_Pj14hb_not_found_tj` @ 414:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18, n4: 305)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18
- **n4 coverage**: T:1  F:305
- **Canonical identifiers**:
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT16VertOriginMetricEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK17hb_sorted_array_tIKN2OT16VertOriginMetricEE5bfindIjEEbRKT_Pj14hb_not_found_tj_414_9_F` — cmplog:18  n4:305

### 852. `_ZN12hb_bit_set_t9add_rangeEjj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 807, n4: 5,320)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:807
- **n4 coverage**: T:1  F:5,320
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_bit_set_t9add_rangeEjj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN12hb_bit_set_t9add_rangeEjj_251_24_F` — cmplog:807  n4:5,320

### 853. `_ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,000, n4: 82,900)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,000
- **n4 coverage**: T:1  F:82,900
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj_251_24_F` — cmplog:18,000  n4:82,900

### 854. `_ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 18,000, n4: 82,900)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:18,000
- **n4 coverage**: T:1  F:82,900
- **Canonical identifiers**:
  - `harfbuzz__ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj_251_47_T` — cmplog:0  n4:1
  - `harfbuzz__ZN12hb_bit_set_t9set_arrayIN2OT11HBGlyphID16EEEvbPKT_jj_251_47_F` — cmplog:18,000  n4:82,900

### 855. `_ZN11hb_buffer_t19merge_clusters_implEjj` @ 551:12
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 61)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1  F:61
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t19merge_clusters_implEjj_551_12_T` — cmplog:0  n4:1
  - `harfbuzz__ZN11hb_buffer_t19merge_clusters_implEjj_551_12_F` — cmplog:2  n4:61

### 856. `_ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE` @ 655:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 14, n4: 91)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14  F:0
- **n4 coverage**: T:91  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE_655_25_T` — cmplog:14  n4:91
  - `harfbuzz__ZN11hb_buffer_t21delete_glyphs_inplaceEPFbPK15hb_glyph_info_tE_655_25_F` — cmplog:0  n4:1

### 857. `hb_buffer_diff` @ 2193:7
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 63, n4: 124)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:63  F:0
- **n4 coverage**: T:124  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb_buffer_diff_2193_7_T` — cmplog:63  n4:124
  - `harfbuzz_hb_buffer_diff_2193_7_F` — cmplog:0  n4:1

### 858. `_ZN3CFF12dict_opset_t9parse_bcdERNS_14byte_str_ref_tE` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 33, n4: 92)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:33
- **n4 coverage**: T:1  F:92
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF12dict_opset_t9parse_bcdERNS_14byte_str_ref_tE_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF12dict_opset_t9parse_bcdERNS_14byte_str_ref_tE_251_24_F` — cmplog:33  n4:92

### 859. `hb_language_matches` @ 435:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 31)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:1  F:31
- **Canonical identifiers**:
  - `harfbuzz_hb_language_matches_435_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb_language_matches_435_7_F` — cmplog:3  n4:31

### 860. `hb_language_matches` @ 436:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 30)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:1  F:30
- **Canonical identifiers**:
  - `harfbuzz_hb_language_matches_436_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb_language_matches_436_7_F` — cmplog:3  n4:30

### 861. `hb_script_get_horizontal_direction` @ 596:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 29,700, n4: 79,800)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:29,700
- **n4 coverage**: T:1  F:79,800
- **Canonical identifiers**:
  - `harfbuzz_hb_script_get_horizontal_direction_596_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb_script_get_horizontal_direction_596_5_F` — cmplog:29,700  n4:79,800

### 862. `hb-number.cc:_ZL9strtod_rlPKcPS0_` @ 224:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 5)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:5
- **Canonical identifiers**:
  - `harfbuzz_hb-number.cc:_ZL9strtod_rlPKcPS0__224_9_T` — cmplog:0  n4:1
  - `harfbuzz_hb-number.cc:_ZL9strtod_rlPKcPS0__224_9_F` — cmplog:1  n4:5

### 863. `_ZNK2OT14ResourceRecord8sanitizeEP21hb_sanitize_context_tPKv` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:48  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT14ResourceRecord8sanitizeEP21hb_sanitize_context_tPKv_350_45_T` — cmplog:1  n4:48
  - `harfbuzz__ZNK2OT14ResourceRecord8sanitizeEP21hb_sanitize_context_tPKv_350_45_F` — cmplog:0  n4:1

### 864. `_ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GSUB_impl19SubstLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 53,000, n4: 78,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:53,000  F:0
- **n4 coverage**: T:78,000  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GSUB_impl19SubstLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:53,000  n4:78,000
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GSUB_impl19SubstLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 865. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 113)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:113  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:113
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 866. `_ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 845)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:1  F:845
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK2OT24VarSizedBinSearchArrayOfIN3AAT19LookupSegmentSingleINS_7NumTypeILb1EtLj2EEEEEE18last_is_terminatorEv_251_24_F` — cmplog:8  n4:845

### 867. `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEENS1_ILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 49)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:49  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEENS1_ILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:49
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEENS1_ILb1EjLj4EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 868. `_ZNK2OT7ArrayOfINS_21SVGDocumentIndexEntryENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 4, n4: 12)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:4  F:0
- **n4 coverage**: T:12  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_21SVGDocumentIndexEntryENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:4  n4:12
  - `harfbuzz__ZNK2OT7ArrayOfINS_21SVGDocumentIndexEntryENS_7NumTypeILb1EtLj2EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 869. `_ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_E16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 18)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:18  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:2  n4:18
  - `harfbuzz__ZNK2OT7ArrayOfINS_7NumTypeILb1EhLj1EEES2_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 870. `_ZNK2OT7ArrayOfIN3CFF12SuppEncodingENS_7NumTypeILb1EhLj1EEEE16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 1, n4: 10)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:1  F:0
- **n4 coverage**: T:10  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfIN3CFF12SuppEncodingENS_7NumTypeILb1EhLj1EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:1  n4:10
  - `harfbuzz__ZNK2OT7ArrayOfIN3CFF12SuppEncodingENS_7NumTypeILb1EhLj1EEEE16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:0  n4:1

### 871. `_ZNK2OT7ArrayOfINS_15MathValueRecordENS_7NumTypeILb1EtLj2EEEEixEi` @ 251:24
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,150  F:0
- **n4 coverage**: T:16,500  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_15MathValueRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_T` — cmplog:6,150  n4:16,500
  - `harfbuzz__ZNK2OT7ArrayOfINS_15MathValueRecordENS_7NumTypeILb1EtLj2EEEEixEi_251_24_F` — cmplog:0  n4:1

### 872. `_ZNK3CFF9FDSelect08sanitizeEP21hb_sanitize_context_tj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13, n4: 27)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13
- **n4 coverage**: T:1  F:27
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF9FDSelect08sanitizeEP21hb_sanitize_context_tj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3CFF9FDSelect08sanitizeEP21hb_sanitize_context_tj_251_24_F` — cmplog:13  n4:27

### 873. `_ZNK3CFF8FDSelect8sanitizeEP21hb_sanitize_context_tj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 33, n4: 221)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:33
- **n4 coverage**: T:1  F:221
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF8FDSelect8sanitizeEP21hb_sanitize_context_tj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3CFF8FDSelect8sanitizeEP21hb_sanitize_context_tj_251_24_F` — cmplog:33  n4:221

### 874. `_ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 17, n4: 254)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:17
- **n4 coverage**: T:1  F:254
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj_251_24_F` — cmplog:17  n4:254

### 875. `_ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj` @ 251:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 17, n4: 254)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:17  F:0
- **n4 coverage**: T:254  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj_251_47_T` — cmplog:17  n4:254
  - `harfbuzz__ZNK3CFF11FDSelect3_4IN2OT7NumTypeILb1EtLj2EEENS2_ILb1EhLj1EEEE8sanitizeEP21hb_sanitize_context_tj_251_47_F` — cmplog:0  n4:1

### 876. `hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_8EncodingEJEEERKT_PKviR21hb_sanitize_context_tDpOT0_` @ 51:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8, n4: 29)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8
- **n4 coverage**: T:1  F:29
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_8EncodingEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-font.cc:_ZN3CFFL20StructAtOffsetOrNullINS_8EncodingEJEEERKT_PKviR21hb_sanitize_context_tDpOT0__51_7_F` — cmplog:8  n4:29

### 877. `_ZNK3CFF7Charset8sanitizeEP21hb_sanitize_context_tPj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 382, n4: 1,110)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:382
- **n4 coverage**: T:1  F:1,110
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF7Charset8sanitizeEP21hb_sanitize_context_tPj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3CFF7Charset8sanitizeEP21hb_sanitize_context_tPj_251_24_F` — cmplog:382  n4:1,110

### 878. `_ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE` @ 794:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 13,500, n4: 37,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:13,500
- **n4 coverage**: T:1  F:37,000
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_794_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF21cff1_top_dict_opset_t10process_opEjRNS_26cff1_top_dict_interp_env_tERNS_22cff1_top_dict_values_tE_794_7_F` — cmplog:13,500  n4:37,000

### 879. `_ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE` @ 881:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,890, n4: 4,610)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,890
- **n4 coverage**: T:1  F:4,610
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_881_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF22cff1_font_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_23cff1_font_dict_values_tE_881_7_F` — cmplog:2,890  n4:4,610

### 880. `_ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE` @ 942:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 26,600, n4: 48,300)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:26,600
- **n4 coverage**: T:1  F:48,300
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE_942_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF25cff1_private_dict_opset_t10process_opEjRNS_12interp_env_tINS_8number_tEEERNS_31cff1_private_dict_values_base_tINS_10dict_val_tEEE_942_7_F` — cmplog:26,600  n4:48,300

### 881. `_ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 92)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1  F:92
- **Canonical identifiers**:
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK3CFF12CFF2FDSelect8sanitizeEP21hb_sanitize_context_tj_251_24_F` — cmplog:2  n4:92

### 882. `_ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE` @ 283:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16,600, n4: 98,100)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16,600
- **n4 coverage**: T:1  F:98,100
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE_283_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE_283_7_F` — cmplog:16,600  n4:98,100

### 883. `_ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE` @ 285:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 16,600, n4: 98,100)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:16,600
- **n4 coverage**: T:1  F:98,100
- **Canonical identifiers**:
  - `harfbuzz__ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE_285_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN3CFF25cff2_private_dict_opset_t10process_opEjRNS_27cff2_priv_dict_interp_env_tERNS_31cff2_private_dict_values_base_tINS_10dict_val_tEEE_285_7_F` — cmplog:16,600  n4:98,100

### 884. `_ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t` @ 443:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 260, n4: 1,090)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:260
- **n4 coverage**: T:1  F:1,090
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_443_11_T` — cmplog:0  n4:1
  - `harfbuzz__ZN2OT4cff219accelerator_templ_tIN3CFF25cff2_private_dict_opset_tENS2_31cff2_private_dict_values_base_tINS2_10dict_val_tEEEEC2EP9hb_face_t_443_11_F` — cmplog:260  n4:1,090

### 885. `_ZN2OT4cmap13accelerator_tC2EP9hb_face_t` @ 2052:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 9, n4: 76)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:9
- **n4 coverage**: T:1  F:76
- **Canonical identifiers**:
  - `harfbuzz__ZN2OT4cmap13accelerator_tC2EP9hb_face_t_2052_2_T` — cmplog:0  n4:1
  - `harfbuzz__ZN2OT4cmap13accelerator_tC2EP9hb_face_t_2052_2_F` — cmplog:9  n4:76

### 886. `hb-ot-font.cc:_ZL25hb_ot_get_glyph_v_originsP9hb_font_tPvjPKjjPijS4_jS1_` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 26, n4: 487)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:26
- **n4 coverage**: T:1  F:487
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-font.cc:_ZL25hb_ot_get_glyph_v_originsP9hb_font_tPvjPKjjPijS4_jS1__251_24_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-font.cc:_ZL25hb_ot_get_glyph_v_originsP9hb_font_tPvjPKjjPijS4_jS1__251_24_F` — cmplog:26  n4:487

### 887. `_ZNK2OT13VarRegionAxis8evaluateEi` @ 2481:22
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,480, n4: 5,640)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,480
- **n4 coverage**: T:1  F:5,640
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT13VarRegionAxis8evaluateEi_2481_22_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK2OT13VarRegionAxis8evaluateEi_2481_22_F` — cmplog:1,480  n4:5,640

### 888. `_ZNK2OT23MathTopAccentAttachment9get_valueEjP9hb_font_t` @ 287:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6,150, n4: 16,500)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6,150  F:0
- **n4 coverage**: T:16,500  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT23MathTopAccentAttachment9get_valueEjP9hb_font_t_287_9_T` — cmplog:6,150  n4:16,500
  - `harfbuzz__ZNK2OT23MathTopAccentAttachment9get_valueEjP9hb_font_t_287_9_F` — cmplog:0  n4:1

### 889. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 566:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 314)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:1  F:314
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_566_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_566_2_F` — cmplog:28  n4:314

### 890. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 567:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 314)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:1  F:314
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_567_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_567_2_F` — cmplog:28  n4:314

### 891. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 568:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 314)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:1  F:314
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_568_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_568_2_F` — cmplog:28  n4:314

### 892. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 569:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 314)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:1  F:314
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_569_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_569_2_F` — cmplog:28  n4:314

### 893. `_Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 606:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 28, n4: 314)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:28
- **n4 coverage**: T:1  F:314
- **Canonical identifiers**:
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_606_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z28_hb_ot_shape_fallback_spacesPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_606_2_F` — cmplog:28  n4:314

### 894. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 46:15
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_46_15_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_46_15_F` — cmplog:1  n4:48

### 895. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 50:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_50_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_50_2_F` — cmplog:1  n4:48

### 896. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 51:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_51_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_51_2_F` — cmplog:1  n4:48

### 897. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 60:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_60_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_60_2_F` — cmplog:1  n4:48

### 898. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 62:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_62_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_62_2_F` — cmplog:1  n4:48

### 899. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 63:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_63_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_63_2_F` — cmplog:1  n4:48

### 900. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 64:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_64_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_64_2_F` — cmplog:1  n4:48

### 901. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 66:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_66_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_66_2_F` — cmplog:1  n4:48

### 902. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 67:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_67_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_67_2_F` — cmplog:1  n4:48

### 903. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 71:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 48)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:48
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_71_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_71_2_F` — cmplog:1  n4:48

### 904. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 88:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_88_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_88_5_F` — cmplog:389  n4:1,650

### 905. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 89:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_89_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_89_5_F` — cmplog:389  n4:1,650

### 906. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 92:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_92_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_92_5_F` — cmplog:389  n4:1,650

### 907. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 93:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_93_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_93_5_F` — cmplog:389  n4:1,650

### 908. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 94:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_94_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_94_5_F` — cmplog:389  n4:1,650

### 909. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 95:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_95_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_95_5_F` — cmplog:389  n4:1,650

### 910. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 96:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_96_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_96_5_F` — cmplog:389  n4:1,650

### 911. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 136:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_136_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_136_5_F` — cmplog:389  n4:1,650

### 912. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 139:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_139_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_139_5_F` — cmplog:389  n4:1,650

### 913. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 154:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_154_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_154_5_F` — cmplog:389  n4:1,650

### 914. `hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj` @ 157:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 389, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:389
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_157_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL28recategorize_combining_classjj_157_5_F` — cmplog:389  n4:1,650

### 915. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 232:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_232_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_232_5_F` — cmplog:237  n4:990

### 916. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 243:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_243_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_243_5_F` — cmplog:237  n4:990

### 917. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 253:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_253_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_253_5_F` — cmplog:237  n4:990

### 918. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 258:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_258_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_258_5_F` — cmplog:237  n4:990

### 919. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 278:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_278_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_278_5_F` — cmplog:237  n4:990

### 920. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 289:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_289_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_289_5_F` — cmplog:237  n4:990

### 921. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 290:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_290_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_290_5_F` — cmplog:237  n4:990

### 922. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 299:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 237, n4: 990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:237
- **n4 coverage**: T:1  F:990
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_299_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_299_5_F` — cmplog:237  n4:990

### 923. `_ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t` @ 173:46
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 414, n4: 1,990)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:414
- **n4 coverage**: T:1  F:1,990
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_173_46_T` — cmplog:0  n4:1
  - `harfbuzz__ZN21hb_ot_shape_planner_t7compileER18hb_ot_shape_plan_tRK22hb_ot_shape_plan_key_t_173_46_F` — cmplog:414  n4:1,990

### 924. `hb-ot-shaper-arabic.cc:_ZL28arabic_fallback_plan_destroyP22arabic_fallback_plan_t` @ 358:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 472, n4: 746)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:472  F:0
- **n4 coverage**: T:746  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL28arabic_fallback_plan_destroyP22arabic_fallback_plan_t_358_11_T` — cmplog:472  n4:746
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL28arabic_fallback_plan_destroyP22arabic_fallback_plan_t_358_11_F` — cmplog:0  n4:1

### 925. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA18_14ligature_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 200:17
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 99, n4: 134)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:99  F:0
- **n4 coverage**: T:134  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA18_14ligature_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_17_T` — cmplog:99  n4:134
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA18_14ligature_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_17_F` — cmplog:0  n4:1

### 926. `hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j` @ 200:17
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 94, n4: 131)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:94  F:0
- **n4 coverage**: T:131  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_17_T` — cmplog:94  n4:131
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL42arabic_fallback_synthesize_lookup_ligatureIA1_19ligature_mark_set_tEPN2OT6Layout9GSUB_impl11SubstLookupEPK18hb_ot_shape_plan_tP9hb_font_tRKT_j_200_17_F` — cmplog:0  n4:1

### 927. `hb-ot-shaper-arabic.cc:_ZL26arabic_fallback_plan_shapeP22arabic_fallback_plan_tP9hb_font_tP11hb_buffer_t` @ 377:11
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 472, n4: 746)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:472  F:0
- **n4 coverage**: T:746  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL26arabic_fallback_plan_shapeP22arabic_fallback_plan_tP9hb_font_tP11hb_buffer_t_377_11_T` — cmplog:472  n4:746
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL26arabic_fallback_plan_shapeP22arabic_fallback_plan_tP9hb_font_tP11hb_buffer_t_377_11_F` — cmplog:0  n4:1

### 928. `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t` @ 26:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 140, n4: 584)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:140
- **n4 coverage**: T:1  F:584
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_26_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_26_5_F` — cmplog:140  n4:584

### 929. `hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t` @ 34:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 140, n4: 584)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:140
- **n4 coverage**: T:1  F:584
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_34_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18has_arabic_joining11hb_script_t_34_5_F` — cmplog:140  n4:584

### 930. `hb-ot-shaper-arabic.cc:_ZL12joining_typej` @ 205:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 25, n4: 151)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:25
- **n4 coverage**: T:1  F:151
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_205_11_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_205_11_F` — cmplog:25  n4:151

### 931. `hb-ot-shaper-arabic.cc:_ZL12joining_typej` @ 212:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 23)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1  F:23
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_212_11_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-arabic.cc:_ZL12joining_typej_212_11_F` — cmplog:2  n4:23

### 932. `hb-ot-shaper-hangul.cc:_ZL18data_create_hangulPK18hb_ot_shape_plan_t` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 45, n4: 158)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:45
- **n4 coverage**: T:1  F:158
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL18data_create_hangulPK18hb_ot_shape_plan_t_251_24_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL18data_create_hangulPK18hb_ot_shape_plan_t_251_24_F` — cmplog:45  n4:158

### 933. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 317:4
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 36)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:36  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_317_4_T` — cmplog:7  n4:36
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_317_4_F` — cmplog:0  n4:1

### 934. `hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 377:23
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 6, n4: 23)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:6  F:0
- **n4 coverage**: T:23  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_377_23_T` — cmplog:6  n4:23
  - `harfbuzz_hb-ot-shaper-hangul.cc:_ZL22preprocess_text_hangulPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_377_23_F` — cmplog:0  n4:1

### 935. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 92:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 212)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:1  F:212
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_92_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_92_7_F` — cmplog:5  n4:212

### 936. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 101:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 212)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:1  F:212
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_101_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_101_7_F` — cmplog:5  n4:212

### 937. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 131:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 74)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:74
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_131_4_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_131_4_F` — cmplog:1  n4:74

### 938. `hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj` @ 135:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 74)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:74
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_135_4_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-hebrew.cc:_ZL14compose_hebrewPK31hb_ot_shape_normalize_context_tjjPj_135_4_F` — cmplog:1  n4:74

### 939. `_Z20find_syllables_indicP11hb_buffer_t` @ 1151:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 119, n4: 1,790)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:119
- **n4 coverage**: T:1  F:1,790
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1151_7_T` — cmplog:0  n4:1
  - `harfbuzz__Z20find_syllables_indicP11hb_buffer_t_1151_7_F` — cmplog:119  n4:1,790

### 940. `_Z23hb_indic_get_categoriesj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 25, n4: 694)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:25
- **n4 coverage**: T:1  F:694
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__Z23hb_indic_get_categoriesj_251_24_F` — cmplog:25  n4:694

### 941. `_Z23hb_indic_get_categoriesj` @ 489:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 12, n4: 973)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:12
- **n4 coverage**: T:1  F:973
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_489_11_T` — cmplog:0  n4:1
  - `harfbuzz__Z23hb_indic_get_categoriesj_489_11_F` — cmplog:12  n4:973

### 942. `_Z23hb_indic_get_categoriesj` @ 501:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 13)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:1  F:13
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_501_11_T` — cmplog:0  n4:1
  - `harfbuzz__Z23hb_indic_get_categoriesj_501_11_F` — cmplog:3  n4:13

### 943. `_Z23hb_indic_get_categoriesj` @ 502:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 3, n4: 12)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:3
- **n4 coverage**: T:1  F:12
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_502_11_T` — cmplog:0  n4:1
  - `harfbuzz__Z23hb_indic_get_categoriesj_502_11_F` — cmplog:3  n4:12

### 944. `_Z23hb_indic_get_categoriesj` @ 511:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 4, n4: 20)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:4
- **n4 coverage**: T:1  F:20
- **Canonical identifiers**:
  - `harfbuzz__Z23hb_indic_get_categoriesj_511_11_T` — cmplog:0  n4:1
  - `harfbuzz__Z23hb_indic_get_categoriesj_511_11_F` — cmplog:4  n4:20

### 945. `hb-ot-shaper-indic.cc:_ZL21setup_syllables_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 119, n4: 1,790)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:119  F:0
- **n4 coverage**: T:1,790  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL21setup_syllables_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:119  n4:1,790
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL21setup_syllables_indicPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 946. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1160:11
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 1,150)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1  F:1,150
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1160_11_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1160_11_F` — cmplog:2  n4:1,150

### 947. `hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj` @ 1290:40
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 2, n4: 16,800)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:2  F:0
- **n4 coverage**: T:16,800  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1290_40_T` — cmplog:2  n4:16,800
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL31final_reordering_syllable_indicPK18hb_ot_shape_plan_tP11hb_buffer_tjj_1290_40_F` — cmplog:0  n4:1

### 948. `hb-ot-shaper-indic.cc:_ZL15decompose_indicPK31hb_ot_shape_normalize_context_tjPjS2_` @ 1522:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1,970, n4: 29,800)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1,970
- **n4 coverage**: T:1  F:29,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL15decompose_indicPK31hb_ot_shape_normalize_context_tjPjS2__1522_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL15decompose_indicPK31hb_ot_shape_normalize_context_tjPjS2__1522_5_F` — cmplog:1,970  n4:29,800

### 949. `hb-ot-shaper-indic.cc:_ZL13compose_indicPK31hb_ot_shape_normalize_context_tjjPj` @ 1553:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 85, n4: 3,150)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:85
- **n4 coverage**: T:1  F:3,150
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL13compose_indicPK31hb_ot_shape_normalize_context_tjjPj_1553_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-indic.cc:_ZL13compose_indicPK31hb_ot_shape_normalize_context_tjjPj_1553_7_F` — cmplog:85  n4:3,150

### 950. `_Z20find_syllables_khmerP11hb_buffer_t` @ 319:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 5, n4: 72)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:5
- **n4 coverage**: T:1  F:72
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_319_7_T` — cmplog:0  n4:1
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_319_7_F` — cmplog:5  n4:72

### 951. `_Z20find_syllables_khmerP11hb_buffer_t` @ 369:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,260, n4: 45,900)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,260
- **n4 coverage**: T:1  F:45,900
- **Canonical identifiers**:
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_369_2_T` — cmplog:0  n4:1
  - `harfbuzz__Z20find_syllables_khmerP11hb_buffer_t_369_2_F` — cmplog:8,260  n4:45,900

### 952. `hb-ot-shaper-khmer.cc:_ZL21setup_syllables_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 72)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:72  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL21setup_syllables_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:5  n4:72
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL21setup_syllables_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 953. `hb-ot-shaper-khmer.cc:_ZL13reorder_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 72)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:72  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL13reorder_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:5  n4:72
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL13reorder_khmerPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 954. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 344:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 80, n4: 1,160)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:80
- **n4 coverage**: T:1  F:1,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__344_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__344_5_F` — cmplog:80  n4:1,160

### 955. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 346:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 80, n4: 1,160)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:80
- **n4 coverage**: T:1  F:1,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__346_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__346_5_F` — cmplog:80  n4:1,160

### 956. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 347:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 80, n4: 1,160)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:80
- **n4 coverage**: T:1  F:1,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__347_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__347_5_F` — cmplog:80  n4:1,160

### 957. `hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2_` @ 348:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 80, n4: 1,160)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:80
- **n4 coverage**: T:1  F:1,160
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__348_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-khmer.cc:_ZL15decompose_khmerPK31hb_ot_shape_normalize_context_tjPjS2__348_5_F` — cmplog:80  n4:1,160

### 958. `_Z22find_syllables_myanmarP11hb_buffer_t` @ 574:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 22, n4: 168)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:22
- **n4 coverage**: T:1  F:168
- **Canonical identifiers**:
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_574_7_T` — cmplog:0  n4:1
  - `harfbuzz__Z22find_syllables_myanmarP11hb_buffer_t_574_7_F` — cmplog:22  n4:168

### 959. `hb-ot-shaper-myanmar.cc:_ZL23setup_syllables_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 22, n4: 168)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:22  F:0
- **n4 coverage**: T:168  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL23setup_syllables_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:22  n4:168
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL23setup_syllables_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 960. `hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 22, n4: 168)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:22  F:0
- **n4 coverage**: T:168  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:22  n4:168
  - `harfbuzz_hb-ot-shaper-myanmar.cc:_ZL15reorder_myanmarPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 961. `hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 370:47
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 14, n4: 137)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14  F:0
- **n4 coverage**: T:137  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_370_47_T` — cmplog:14  n4:137
  - `harfbuzz_hb-ot-shaper-thai.cc:_ZL20preprocess_text_thaiPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_370_47_F` — cmplog:0  n4:1

### 962. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 951:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 130, n4: 572)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:130
- **n4 coverage**: T:1  F:572
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_951_7_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_951_7_F` — cmplog:130  n4:572

### 963. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1005:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:1  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1005_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1005_2_F` — cmplog:2,020  n4:73,800

### 964. `hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t` @ 1053:2
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,020, n4: 73,800)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,020
- **n4 coverage**: T:1  F:73,800
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1053_2_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL18find_syllables_useP11hb_buffer_t_1053_2_F` — cmplog:2,020  n4:73,800

### 965. `hb-ot-shaper-use.cc:_ZL19setup_syllables_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 130, n4: 572)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:130  F:0
- **n4 coverage**: T:572  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL19setup_syllables_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:130  n4:572
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL19setup_syllables_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 966. `hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 130, n4: 572)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:130  F:0
- **n4 coverage**: T:572  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:130  n4:572
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL15record_pref_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 967. `hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t` @ 155:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 130, n4: 572)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:130  F:0
- **n4 coverage**: T:572  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_T` — cmplog:130  n4:572
  - `harfbuzz_hb-ot-shaper-use.cc:_ZL11reorder_usePK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_t_155_25_F` — cmplog:0  n4:1

### 968. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 118:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 75, n4: 943)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:75
- **n4 coverage**: T:1  F:943
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_118_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_118_4_F` — cmplog:75  n4:943

### 969. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 126:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 75, n4: 943)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:75
- **n4 coverage**: T:1  F:943
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_126_6_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_126_6_F` — cmplog:75  n4:943

### 970. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 136:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 374)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:1  F:374
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_136_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_136_4_F` — cmplog:30  n4:374

### 971. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 170:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 15, n4: 134)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:15  F:0
- **n4 coverage**: T:134  F:1
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_170_10_T` — cmplog:15  n4:134
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_170_10_F` — cmplog:0  n4:1

### 972. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 172:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 134)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:1  F:134
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_172_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_172_4_F` — cmplog:15  n4:134

### 973. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 199:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 45, n4: 2,840)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:45
- **n4 coverage**: T:1  F:2,840
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_199_18_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_199_18_F` — cmplog:45  n4:2,840

### 974. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 212:6
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 164)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:1  F:164
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_212_6_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_212_6_F` — cmplog:15  n4:164

### 975. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 228:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 540, n4: 1,730)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:540
- **n4 coverage**: T:1  F:1,730
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_228_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_228_4_F` — cmplog:540  n4:1,730

### 976. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 236:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 540, n4: 1,730)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:540
- **n4 coverage**: T:1  F:1,730
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_4_F` — cmplog:540  n4:1,730

### 977. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 236:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 540, n4: 1,730)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:540
- **n4 coverage**: T:1  F:1,730
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_18_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_236_18_F` — cmplog:540  n4:1,730

### 978. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 251:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 989)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:1  F:989
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_251_18_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_251_18_F` — cmplog:30  n4:989

### 979. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 254:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 30, n4: 989)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:30
- **n4 coverage**: T:1  F:989
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_254_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_254_4_F` — cmplog:30  n4:989

### 980. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 269:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 105, n4: 16,900)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:105
- **n4 coverage**: T:1  F:16,900
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_269_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_269_4_F` — cmplog:105  n4:16,900

### 981. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 275:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 105, n4: 16,900)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:105
- **n4 coverage**: T:1  F:16,900
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_275_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_275_4_F` — cmplog:105  n4:16,900

### 982. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 295:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 570, n4: 1,060)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:570
- **n4 coverage**: T:1  F:1,060
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_295_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_295_4_F` — cmplog:570  n4:1,060

### 983. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 303:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 570, n4: 1,060)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:570
- **n4 coverage**: T:1  F:1,060
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_4_F` — cmplog:570  n4:1,060

### 984. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 303:18
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 570, n4: 1,060)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:570
- **n4 coverage**: T:1  F:1,060
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_18_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_303_18_F` — cmplog:570  n4:1,060

### 985. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 333:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 329)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:1  F:329
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_333_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_333_4_F` — cmplog:15  n4:329

### 986. `_Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t` @ 460:4
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 15, n4: 179)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:15
- **n4 coverage**: T:1  F:179
- **Canonical identifiers**:
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_460_4_T` — cmplog:0  n4:1
  - `harfbuzz__Z37_hb_preprocess_text_vowel_constraintsPK18hb_ot_shape_plan_tP11hb_buffer_tP9hb_font_t_460_4_F` — cmplog:15  n4:179

### 987. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 307:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_307_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_307_5_F` — cmplog:8,290  n4:24,000

### 988. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 331:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_331_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_331_5_F` — cmplog:8,290  n4:24,000

### 989. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 335:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_335_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_335_5_F` — cmplog:8,290  n4:24,000

### 990. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 339:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_339_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_339_5_F` — cmplog:8,290  n4:24,000

### 991. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 340:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_340_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_340_5_F` — cmplog:8,290  n4:24,000

### 992. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 345:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_345_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_345_5_F` — cmplog:8,290  n4:24,000

### 993. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 355:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_355_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_355_5_F` — cmplog:8,290  n4:24,000

### 994. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 362:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_362_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_362_5_F` — cmplog:8,290  n4:24,000

### 995. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 368:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_368_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_368_5_F` — cmplog:8,290  n4:24,000

### 996. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 369:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_369_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_369_5_F` — cmplog:8,290  n4:24,000

### 997. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 370:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_370_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_370_5_F` — cmplog:8,290  n4:24,000

### 998. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 371:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_371_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_371_5_F` — cmplog:8,290  n4:24,000

### 999. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 377:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_377_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_377_5_F` — cmplog:8,290  n4:24,000

### 1000. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 380:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_380_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_380_5_F` — cmplog:8,290  n4:24,000

### 1001. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 384:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_384_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_384_5_F` — cmplog:8,290  n4:24,000

### 1002. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 387:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_387_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_387_5_F` — cmplog:8,290  n4:24,000

### 1003. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 388:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_388_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_388_5_F` — cmplog:8,290  n4:24,000

### 1004. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 394:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_394_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_394_5_F` — cmplog:8,290  n4:24,000

### 1005. `hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj` @ 395:5
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 8,290, n4: 24,000)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:8,290
- **n4 coverage**: T:1  F:24,000
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_395_5_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ot-shape.cc:_ZL23hb_ot_shaper_categorize11hb_script_t14hb_direction_tj_395_5_F` — cmplog:8,290  n4:24,000

### 1006. `_ZNK2OT11SegmentMaps9map_floatEfjj` @ 176:67
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 356, n4: 1,650)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:356
- **n4 coverage**: T:1  F:1,650
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT11SegmentMaps9map_floatEfjj_176_67_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK2OT11SegmentMaps9map_floatEfjj_176_67_F` — cmplog:356  n4:1,650

### 1007. `_ZNK2OT4VORG12get_y_originEj` @ 68:9
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 18, n4: 305)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:18  F:0
- **n4 coverage**: T:305  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT4VORG12get_y_originEj_68_9_T` — cmplog:18  n4:305
  - `harfbuzz__ZNK2OT4VORG12get_y_originEj_68_9_F` — cmplog:0  n4:1

### 1008. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4sbixEEEP9hb_blob_tS4_` @ 474:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 7, n4: 24)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:7  F:0
- **n4 coverage**: T:24  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4sbixEEEP9hb_blob_tS4__474_25_T` — cmplog:7  n4:24
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4sbixEEEP9hb_blob_tS4__474_25_F` — cmplog:0  n4:1

### 1009. `_ZNK21hb_sanitize_context_t17check_array_sizedIN2OT7DataMapEEEbPKT_jj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2, n4: 9)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2
- **n4 coverage**: T:1  F:9
- **Canonical identifiers**:
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT7DataMapEEEbPKT_jj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK21hb_sanitize_context_t17check_array_sizedIN2OT7DataMapEEEbPKT_jj_251_24_F` — cmplog:2  n4:9

### 1010. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4MATHEEEP9hb_blob_tS4_` @ 480:6
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 182, n4: 241)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:182  F:0
- **n4 coverage**: T:241  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4MATHEEEP9hb_blob_tS4__480_6_T` — cmplog:182  n4:241
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4MATHEEEP9hb_blob_tS4__480_6_F` — cmplog:0  n4:1

### 1011. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4avarEEEP9hb_blob_tS4_` @ 474:25
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 17, n4: 35)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:17  F:0
- **n4 coverage**: T:35  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4avarEEEP9hb_blob_tS4__474_25_T` — cmplog:17  n4:35
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4avarEEEP9hb_blob_tS4__474_25_F` — cmplog:0  n4:1

### 1012. `_ZNK22hb_serialize_context_t10copy_bytesEv` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 472, n4: 747)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:472
- **n4 coverage**: T:1  F:747
- **Canonical identifiers**:
  - `harfbuzz__ZNK22hb_serialize_context_t10copy_bytesEv_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZNK22hb_serialize_context_t10copy_bytesEv_251_24_F` — cmplog:472  n4:747

### 1013. `hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj` @ 91:45
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 1, n4: 32)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:1
- **n4 coverage**: T:1  F:32
- **Canonical identifiers**:
  - `harfbuzz_hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj_91_45_T` — cmplog:0  n4:1
  - `harfbuzz_hb-ucd.cc:_ZL22_hb_ucd_compose_hanguljjPj_91_45_F` — cmplog:1  n4:32

### 1014. `hb-unicode.cc:_ZL34_hb_emoji_is_Extended_Pictographicj` @ 71:10
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 5, n4: 299)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:5  F:0
- **n4 coverage**: T:299  F:1
- **Canonical identifiers**:
  - `harfbuzz_hb-unicode.cc:_ZL34_hb_emoji_is_Extended_Pictographicj_71_10_T` — cmplog:5  n4:299
  - `harfbuzz_hb-unicode.cc:_ZL34_hb_emoji_is_Extended_Pictographicj_71_10_F` — cmplog:0  n4:1

### 1015. `_ZN18hb_unicode_funcs_t24modified_combining_classEj` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 2,009, n4: 12,100)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:2,009
- **n4 coverage**: T:1  F:12,100
- **Canonical identifiers**:
  - `harfbuzz__ZN18hb_unicode_funcs_t24modified_combining_classEj_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN18hb_unicode_funcs_t24modified_combining_classEj_251_24_F` — cmplog:2,009  n4:12,100

### 1016. `_ZN18hb_unicode_funcs_t19space_fallback_typeEj` @ 239:7
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 471, n4: 1,250)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:471
- **n4 coverage**: T:1  F:1,250
- **Canonical identifiers**:
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_239_7_T` — cmplog:0  n4:1
  - `harfbuzz__ZN18hb_unicode_funcs_t19space_fallback_typeEj_239_7_F` — cmplog:471  n4:1,250

### 1017. `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE6resizeEibb` @ 487:9
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 260, n4: 1,090)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:260
- **n4 coverage**: T:1  F:1,090
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE6resizeEibb_487_9_T` — cmplog:0  n4:1
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE6resizeEibb_487_9_F` — cmplog:260  n4:1,090

### 1018. `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb` @ 251:24
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 251, n4: 903)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:251
- **n4 coverage**: T:1  F:903
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb_251_24_T` — cmplog:0  n4:1
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb_251_24_F` — cmplog:251  n4:903

### 1019. `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb` @ 251:47
- **Blocked side**: True (0 hits in `cmplog`)
- **Hit side**: False (cmplog: 251, n4: 903)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:0  F:251
- **n4 coverage**: T:1  F:903
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb_251_47_T` — cmplog:0  n4:1
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE5allocEjb_251_47_F` — cmplog:251  n4:903

### 1020. `_ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE14realloc_vectorIS3_TnPN12hb_enable_ifIXntsr3std28is_trivially_copy_assignableIT_EE5valueEvE4typeELPv0EEEPS3_j11hb_priorityILj0EE` @ 250:22
- **Blocked side**: False (0 hits in `cmplog`)
- **Hit side**: True (cmplog: 251, n4: 903)
- **Flip strength**: 1 (blocked side hit 1× by `n4`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:251  F:0
- **n4 coverage**: T:903  F:1
- **Canonical identifiers**:
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE14realloc_vectorIS3_TnPN12hb_enable_ifIXntsr3std28is_trivially_copy_assignableIT_EE5valueEvE4typeELPv0EEEPS3_j11hb_priorityILj0EE_250_22_T` — cmplog:251  n4:903
  - `harfbuzz__ZN11hb_vector_tIN3CFF31cff2_private_dict_values_base_tINS0_10dict_val_tEEELb0EE14realloc_vectorIS3_TnPN12hb_enable_ifIXntsr3std28is_trivially_copy_assignableIT_EE5valueEvE4typeELPv0EEEPS3_j11hb_priorityILj0EE_250_22_F` — cmplog:0  n4:1

### 1021. `_ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GPOS_impl17PosLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t` @ 350:45
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 14,000, n4: 23,100)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:14,000  F:1
- **n4 coverage**: T:23,100  F:0
- **Canonical identifiers**:
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GPOS_impl17PosLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_T` — cmplog:14,000  n4:23,100
  - `harfbuzz__ZNK2OT7ArrayOfINS_8OffsetToINS_6Layout9GPOS_impl17PosLookupSubTableENS_7NumTypeILb1EtLj2EEEvLb1EEES6_E16sanitize_shallowEP21hb_sanitize_context_t_350_45_F` — cmplog:1  n4:0

### 1022. `hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj` @ 233:11
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 3, n4: 1)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:3  F:1
- **n4 coverage**: T:1  F:0
- **Canonical identifiers**:
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_233_11_T` — cmplog:3  n4:1
  - `harfbuzz_hb-ot-shape-fallback.cc:_ZL13position_markPK18hb_ot_shape_plan_tP9hb_font_tP11hb_buffer_tR18hb_glyph_extents_tjj_233_11_F` — cmplog:1  n4:0

### 1023. `_ZN21hb_sanitize_context_t13sanitize_blobIN2OT4STATEEEP9hb_blob_tS4_` @ 251:24
- **Blocked side**: False (0 hits in `n4`)
- **Hit side**: True (cmplog: 20, n4: 26)
- **Flip strength**: 1 (blocked side hit 1× by `cmplog`)
- **Status**: ✅ CONFIRMED INPUT-DEPENDENT
- **cmplog coverage**: T:20  F:1
- **n4 coverage**: T:26  F:0
- **Canonical identifiers**:
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4STATEEEP9hb_blob_tS4__251_24_T` — cmplog:20  n4:26
  - `harfbuzz__ZN21hb_sanitize_context_t13sanitize_blobIN2OT4STATEEEP9hb_blob_tS4__251_24_F` — cmplog:1  n4:0
