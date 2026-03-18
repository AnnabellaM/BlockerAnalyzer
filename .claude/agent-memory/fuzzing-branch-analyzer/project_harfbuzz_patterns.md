---
name: harfbuzz blocker patterns
description: Key blocking branch patterns, top locations, and fuzzer complementarity for harfbuzz (2026-03-18, 1023 confirmed blockers)
type: project
---

Analysis of harfbuzz fuzzing coverage revealed 1,023 confirmed input-dependent blocking branches.

**Why:** harfbuzz is a large C++ text shaping library with complex OpenType layout logic; branch asymmetries reflect input-format diversity (scripts, glyph types, table variants).

**How to apply:** Use these patterns to guide root-cause and coverage-analyst work for harfbuzz.

## Scale
- cmplog: 11,322 branch pairs, 4,076 asymmetric
- n4: 12,476 branch pairs, 3,647 asymmetric
- Confirmed input-dependent: 1,023
- Unconfirmed candidates: 6,700

## Fuzzer complementarity
- n4 confirms ALL 1,023 confirmed blockers (n4 hits the blocked side in every confirmed case)
- cmplog is the "primary" fuzzer that misses branches n4 hits; n4 consistently provides broader coverage of OpenType layout paths

## Top blocking locations (by flip strength)
1. hb-ot-layout.cc `_hb_glyph_info_get_lig_num...` line 518:7 — False blocked, flip 2,550,000
2. hb-ot-font.cc `$_33clI...` line 992:11 — False blocked, flip 1,600,000
3. CFF `path_procs_t<cff2_path_procs_extents...>` line 700:14 — True blocked, flip 739,000
4. OT::VARC `get_path_at` line 347:7 — False blocked, flip 627,000
5. CFF `path_procs_t<cff2_path_procs_path_t...>` line 700:14 — True blocked, flip 554,000
6. hb-ot-layout.cc `OT::L::ligate_input` line 1528:11 — False blocked, flip 520,000
7-9. AAT StateTableDriver lines 1262:11, 1298:11, 1287:60 — multiple clustered blockers

## Recurring patterns
- AAT StateTableDriver (`_ZN3AAT16StateTableDriver...`): multiple clustered blockers at lines 1262, 1267, 1268, 1287, 1298 — likely a switch/chain cluster in state machine dispatch
- CFF cs_opset_t (`cff1_cs_opse` and `cff2_cs_opse`): many True-blocked branches at lines 277, 278, 292, 309, 317, 321, 325, 329, 333 — likely switch arms for CFF charstring opcodes
- OT::VARC `get_path_at`: multiple clustered blockers at lines 344, 347, 358, 360, 370 — logical/chain cluster in variation compositing
- OT::ChainRuleSet `SmallTypes`: dense cluster at lines 3452, 3511, 3515, 3519, 3523, 3526, 3528 — switch/chain for chained context substitution
- CFF path_procs_t (cff1 and cff2 variants): blockers at lines 499, 700, 718, 724 — path construction branches
- Script-specific syllable finders: find_syllables_indic, find_syllables_khmer, find_syllables_myanmar, find_syllables_use all show clustered True-blocked branches — script state machine arms not triggered by cmplog's corpus

## Key observation
cmplog's corpus appears weaker on:
1. Complex OpenType GPOS/GSUB chained context lookups
2. CFF2 variable font charstring rendering paths
3. AAT (Apple Advanced Typography) state machine transitions
4. Script-specific shaping for Indic, Khmer, Myanmar scripts
