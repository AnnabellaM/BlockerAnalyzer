# Program Slices — harfbuzz
**Generated:** 2026-03-19
**Source:** `blockers/harfbuzz_blockers.md`
**Ranks processed:** 1–1  (1 passed NEG screening, 0 skipped)

---

## Slice 1

**Key:** `hb-ot-layout.cc:_hb_glyph_info_get_lig_num_comps|518:7`
**Function:** `_hb_glyph_info_get_lig_num_comps(hb_glyph_info_t const*)`
**Blocked side:** False
**Flip strength:** 2,550,000
**Source line:** `_hb_glyph_info_ligated_internal (info))`

### Program Slice

```
ENTRY  hb-shape-fuzzer.cc:13              int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)                        [cmplog: 6150 | n4: 16500]
CALL   hb-shape.cc:197                    void hb_shape(hb_font_t *font, hb_buffer_t *buffer, const hb_feature_t *features, unsigned int num_features)  [cmplog: 12300 | n4: 33000]
CALL   hb-shape.cc:127                    hb_bool_t hb_shape_full(hb_font_t *font, hb_buffer_t *buffer, const hb_feature_t *features, unsigned int num_features, const char * const *shaper_list)  [cmplog: 18000 | n4: 48300]
CALL   hb-ot-layout.cc:2084              void hb_ot_map_t::substitute(const hb_ot_shape_plan_t *plan, hb_font_t *font, hb_buffer_t *buffer) const  [cmplog: 17000 | n4: 44300]
CALL   hb-ot-layout.cc:2022              void hb_ot_map_t::apply<GSUBProxy>(const GSUBProxy &proxy, const hb_ot_shape_plan_t *plan, hb_font_t *font, hb_buffer_t *buffer) const  [cmplog: 17000 | n4: 44300]
CTRL   hb-ot-layout.cc:2051              accel->digest.may_intersect(c.digest)                                                [must=True] [cmplog: 2020 | n4: ~7000+]
CALL   hb-ot-layout.cc:2061              void apply_string<GSUBProxy>(hb_ot_apply_context_t *c, const GSUBProxy::Lookup &lookup, const hb_ot_layout_lookup_accelerator_t &accel)  [cmplog: 2020 | n4: ~17100 aggregate]
CALL   hb-ot-layout.cc:1968              bool apply_string<GSUBProxy>(hb_ot_apply_context_t *c, const OT::Layout::GSUB_impl::SubstLookup &lookup, const hb_ot_layout_lookup_accelerator_t &accel)  [cmplog: 2490 | n4: 17100]
CALL   hb-ot-layout.cc:2001              bool apply_forward(hb_ot_apply_context_t *c, const hb_ot_layout_lookup_accelerator_t &accel)                  [cmplog: 2310 | n4: ~16000]
CALL   hb-ot-layout.cc:1919              bool apply_forward(hb_ot_apply_context_t *c, const hb_ot_layout_lookup_accelerator_t &accel)                  [cmplog: 3250 | n4: 21600]
CTRL   hb-ot-layout.cc:1927              accel.digest.may_have(cur.codepoint)                                                [must=True] [cmplog: 290000 | n4: ~large]
CTRL   hb-ot-layout.cc:1930              accel.apply(c, use_hot_subtable_cache)                                              [must=True] [cmplog: 28000 | n4: ~large]
CALL   src/OT/Layout/GSUB/LigatureSubst.hh:103   bool OT::Layout::GSUB_impl::LigatureSubstFormat1_2<OT::Layout::SmallTypes>::apply(hb_ot_apply_context_t *c, void *external_cache) const  [cmplog: 10000 | n4: 755000]
CTRL   src/OT/Layout/GSUB/LigatureSubst.hh:115   index == NOT_COVERED                                                        [must=False] [cmplog: 8110 | n4: 593000]
CALL   src/OT/Layout/GSUB/LigatureSet.hh:85      bool OT::Layout::GSUB_impl::LigatureSet<OT::Layout::SmallTypes>::apply(hb_ot_apply_context_t *c, const hb_set_digest_t *seconds) const  [cmplog: 8110 | n4: 593000]
CALL   src/OT/Layout/GSUB/Ligature.hh:71         bool OT::Layout::GSUB_impl::Ligature<OT::Layout::SmallTypes>::apply(hb_ot_apply_context_t *c) const  [cmplog: 13600 | n4: 1530000]
CTRL   src/OT/Layout/GSUB/Ligature.hh:111        !match_input(c, count, &component[1], match_glyph, nullptr, &match_end, match_positions, &total_component_count)  [must=False] [cmplog: 5280 | n4: ~1350000]
CALL   hb-ot-layout-gsubgpos.hh:1502            bool ligate_input(hb_ot_apply_context_t *c, unsigned int count, unsigned int match_end, hb_codepoint_t lig_glyph, unsigned int total_component_count)  [cmplog: 5280 | n4: 91900]
DATA   hb-ot-layout-gsubgpos.hh:1560            unsigned int last_num_components = _hb_glyph_info_get_lig_num_comps(&buffer->cur())  [feeds=info] [cmplog: 5280 | n4: 91900]
CALL   hb-ot-layout.hh:502                       unsigned int _hb_glyph_info_get_lig_num_comps(const hb_glyph_info_t *info)  [cmplog: 260000 | n4: 3670000]
DATA   hb-ot-layout.hh:504                       (info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE)                  [feeds=branch_517] [cmplog: 9040 True | n4: 2580000 True]
CTRL   hb-ot-layout.hh:517                       (info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE)                  [must=True] [cmplog: 9040 | n4: 2580000]
BRANCH hb-ot-layout.hh:518:7                     _hb_glyph_info_ligated_internal(info)  →  info->lig_props() & IS_LIG_BASE   [blocked=False] [cmplog: 0 | n4: 2550000]
```

### Key Variables

| Variable | Type |
|----------|------|
| `info` | `const hb_glyph_info_t *` |
| `info->glyph_props()` | `uint16_t` (alias for `var1.u16[0]`) |
| `info->lig_props()` | `uint8_t` (alias for `var1.u8[2]`) |
| `HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE` | `unsigned int` (value `0x04u`) |
| `IS_LIG_BASE` | `#define` (value `0x10`) |
| `last_num_components` | `unsigned int` |
| `hb_glyph_info_t` | `struct { hb_codepoint_t codepoint; hb_mask_t mask; uint32_t cluster; hb_var_int_t var1; hb_var_int_t var2; }` |
| `hb_ot_apply_context_t` | `struct OT::hb_ot_apply_context_t` |
| `hb_buffer_t` | `struct hb_buffer_t` |
| `hb_ot_layout_lookup_accelerator_t` | `struct OT::hb_ot_layout_lookup_accelerator_t` |

### Path Conditions

1. `buffer->len > 0` and `c->lookup_mask != 0` (apply_string entry guard at hb-ot-layout.cc:1972)
2. `!lookup.is_reverse()` — forward substitution path taken (hb-ot-layout.cc:1994)
3. `accel.digest.may_have(cur.codepoint)` — glyph codepoint is in the lookup's bloom filter (hb-ot-layout.cc:1927)
4. `cur.mask & c->lookup_mask` — glyph is in the lookup's mask (hb-ot-layout.cc:1928)
5. `c->check_glyph_property(&cur, c->lookup_props)` — glyph passes property filter (hb-ot-layout.cc:1929)
6. The subtable applied is `LigatureSubstFormat1_2<SmallTypes>` — lookup type 4 (ligature substitution)
7. `index != NOT_COVERED` — current glyph codepoint is in the ligature coverage table (OT/Layout/GSUB/LigatureSubst.hh:115)
8. `match_input(...)` succeeds — all subsequent ligature components are present in the buffer (OT/Layout/GSUB/Ligature.hh:111)
9. `info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE` is non-zero — the current buffer glyph (buffer->cur()) at the time of `_hb_glyph_info_get_lig_num_comps` is classified as a ligature in GDEF (hb-ot-layout.hh:517)
10. `info->lig_props() & IS_LIG_BASE` is zero — the glyph is GDEF-classified as a ligature but has NOT been through a prior `ligate_input` call that set `IS_LIG_BASE` via `_hb_glyph_info_set_lig_props_for_ligature` (hb-ot-layout.hh:518, **blocked False side**)

**Divergence point:** `BRANCH hb-ot-layout.hh:518:7` `_hb_glyph_info_ligated_internal(info)` False side [cmplog: 0 | n4: 2550000]
