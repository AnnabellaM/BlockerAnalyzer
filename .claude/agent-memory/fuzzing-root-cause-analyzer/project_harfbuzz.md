---
name: harfbuzz project context
description: Entry point, GSUB ligature processing gate, IS_LIG_BASE blocking branch finding and mitigations from 2026-03-19 campaign.
type: project
---

harfbuzz rank-1 blocker (2026-03-19): `_hb_glyph_info_get_lig_num_comps` at `hb-ot-layout.hh:518:7`, False side blocked in cmplog fuzzer (0 hits) but reachable in n4 fuzzer (2,550,000 hits).

**Why:** Root cause is Input Format / Structure Constraints. The False side requires a font where a glyph is GDEF-classified as LIGATURE (bit 0x04 in glyph_props) but has never been processed by `ligate_input()` — so its `lig_props` byte lacks the `IS_LIG_BASE` flag (0x10). `IS_LIG_BASE` is set exclusively by `_hb_glyph_info_set_lig_props_for_ligature()` at `hb-ot-layout-gsubgpos.hh:1565` (inside `ligate_input`). The cmplog fuzzer lacks seeds with the required correlated GDEF+GSUB table structure; n4 already has them.

**How to apply:** When analyzing other harfbuzz blockers, note that the n4 fuzzer corpus is structurally richer for font binary format than cmplog. Seed cross-pollination from n4 to cmplog is the primary recommended fix for font-structure-dependent blockers. The `lig_props` byte (`var1.u8[2]` in `hb_glyph_info_t`) is a key internal flag field — several other branches in the shaping pipeline are also gated on its sub-bits.

Key entry chain: `LLVMFuzzerTestOneInput` → `hb_shape` → `hb_shape_full` → `hb_ot_map_t::substitute` → `apply<GSUBProxy>` → `apply_string` → `apply_forward` → `LigatureSubstFormat1_2::apply` → `LigatureSet::apply` → `Ligature::apply` → `ligate_input` → `_hb_glyph_info_get_lig_num_comps` → blocking branch.

Slices file: `slices/harfbuzz_slices.md` (rank 1 only, dynamic slice with per-fuzzer hitcounts).
Report: `reports/harfbuzz_report.md`.
