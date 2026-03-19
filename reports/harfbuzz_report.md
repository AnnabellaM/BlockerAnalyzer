# Root Cause Analysis Report — harfbuzz
**Generated:** 2026-03-19
**Ranks analyzed:** 1–1
**Slices source:** `slices/harfbuzz_slices.md`

---

## Findings

BLOCKING BRANCH ANALYSIS
========================
Cluster: C01
Role: cluster-root
  Members: (single-member cluster — no downstream or peer members identified)

Branches: hb-ot-layout.hh:518:7 (blocked side: False)
Location: `_hb_glyph_info_get_lig_num_comps` in `src/hb-ot-layout.hh`
Branch Condition: `_hb_glyph_info_ligated_internal(info)` — i.e., `info->lig_props() & IS_LIG_BASE`
Coverage Status:
  cmplog fuzzer: True side = 9,040 hits;  False side = 0 hits  (BLOCKED)
  n4 fuzzer:     True side = 2,580,000 hits;  False side = 2,550,000 hits  (reachable)

Program Slice (entry → blocking branch):
  [ENTRY]  int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)                                  (hb-shape-fuzzer.cc:13)
  [CALL]   void hb_shape(hb_font_t *font, hb_buffer_t *buffer, const hb_feature_t *features,
               unsigned int num_features)                                                                 (hb-shape.cc:197)
  [CALL]   hb_bool_t hb_shape_full(hb_font_t *font, hb_buffer_t *buffer,
               const hb_feature_t *features, unsigned int num_features,
               const char * const *shaper_list)                                                          (hb-shape.cc:127)
  [CALL]   void hb_ot_map_t::substitute(const hb_ot_shape_plan_t *plan,
               hb_font_t *font, hb_buffer_t *buffer) const                                              (hb-ot-layout.cc:2084)
  [CALL]   void hb_ot_map_t::apply<GSUBProxy>(const GSUBProxy &proxy,
               const hb_ot_shape_plan_t *plan, hb_font_t *font, hb_buffer_t *buffer) const              (hb-ot-layout.cc:2022)
  [CTRL]   accel->digest.may_intersect(c.digest)  → must be TRUE                                        (hb-ot-layout.cc:2051)
  [CALL]   void apply_string<GSUBProxy>(hb_ot_apply_context_t *c,
               const GSUBProxy::Lookup &lookup,
               const hb_ot_layout_lookup_accelerator_t &accel)                                          (hb-ot-layout.cc:2061)
  [CALL]   bool apply_string<GSUBProxy>(hb_ot_apply_context_t *c,
               const OT::Layout::GSUB_impl::SubstLookup &lookup,
               const hb_ot_layout_lookup_accelerator_t &accel)                                          (hb-ot-layout.cc:1968)
  [CALL]   bool apply_forward(hb_ot_apply_context_t *c,
               const hb_ot_layout_lookup_accelerator_t &accel)                                          (hb-ot-layout.cc:2001)
  [CALL]   bool apply_forward(hb_ot_apply_context_t *c,
               const hb_ot_layout_lookup_accelerator_t &accel)                                          (hb-ot-layout.cc:1919)
  [CTRL]   accel.digest.may_have(cur.codepoint)  → must be TRUE                                        (hb-ot-layout.cc:1927)
  [CTRL]   accel.apply(c, use_hot_subtable_cache)  → must be TRUE                                      (hb-ot-layout.cc:1930)
  [CALL]   bool OT::Layout::GSUB_impl::LigatureSubstFormat1_2<OT::Layout::SmallTypes>::apply(
               hb_ot_apply_context_t *c, void *external_cache) const                                    (OT/Layout/GSUB/LigatureSubst.hh:103)
  [CTRL]   index == NOT_COVERED  → must be FALSE                                                        (OT/Layout/GSUB/LigatureSubst.hh:115)
  [CALL]   bool OT::Layout::GSUB_impl::LigatureSet<OT::Layout::SmallTypes>::apply(
               hb_ot_apply_context_t *c, const hb_set_digest_t *seconds) const                         (OT/Layout/GSUB/LigatureSet.hh:85)
  [CALL]   bool OT::Layout::GSUB_impl::Ligature<OT::Layout::SmallTypes>::apply(
               hb_ot_apply_context_t *c) const                                                          (OT/Layout/GSUB/Ligature.hh:71)
  [CTRL]   !match_input(c, count, &component[1], match_glyph, nullptr, &match_end,
               match_positions, &total_component_count)  → must be FALSE                               (OT/Layout/GSUB/Ligature.hh:111)
  [CALL]   bool ligate_input(hb_ot_apply_context_t *c, unsigned int count,
               unsigned int match_end, hb_codepoint_t lig_glyph,
               unsigned int total_component_count)                                                      (hb-ot-layout-gsubgpos.hh:1502)
  [DATA]   unsigned int last_num_components = _hb_glyph_info_get_lig_num_comps(&buffer->cur())
               [feeds=info]                                                                              (hb-ot-layout-gsubgpos.hh:1560)
  [CALL]   unsigned int _hb_glyph_info_get_lig_num_comps(const hb_glyph_info_t *info)                  (hb-ot-layout.hh:502)
  [DATA]   (info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE)
               [feeds=branch_517]                                                                        (hb-ot-layout.hh:504)
  [CTRL]   (info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE)  → must be TRUE                  (hb-ot-layout.hh:517)
  [BRANCH] _hb_glyph_info_ligated_internal(info)
               i.e. info->lig_props() & IS_LIG_BASE  → BLOCKER (False side unvisited)                  (hb-ot-layout.hh:518:7)

  Type context (sufficient for C reconstruction):
    info:                       const hb_glyph_info_t *
    info->glyph_props():        uint16_t  (alias: var1.u16[0])
    info->lig_props():          uint8_t   (alias: var1.u8[2])
    HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE: unsigned int  (value 0x04u)
    IS_LIG_BASE:                #define   (value 0x10)
    hb_glyph_info_t:            struct { hb_codepoint_t codepoint; hb_mask_t mask;
                                         uint32_t cluster; hb_var_int_t var1; hb_var_int_t var2; }
    _hb_glyph_info_ligated_internal: static inline bool (const hb_glyph_info_t *info)
                                     { return info->lig_props() & IS_LIG_BASE; }
    _hb_glyph_info_set_lig_props_for_ligature:
                                static inline void (hb_glyph_info_t *info,
                                                    unsigned int lig_id,
                                                    unsigned int lig_num_comps)
                                { info->lig_props() = (lig_id << 5) | IS_LIG_BASE | (lig_num_comps & 0x0F); }

Path Conditions Required:
  1. `buffer->len > 0` and `c->lookup_mask != 0` — apply_string entry guard (hb-ot-layout.cc:1972)
  2. `!lookup.is_reverse()` — forward substitution path taken (hb-ot-layout.cc:1994)
  3. `accel.digest.may_have(cur.codepoint)` — glyph codepoint passes the lookup's bloom filter (hb-ot-layout.cc:1927)
  4. `cur.mask & c->lookup_mask` — glyph is in the lookup's mask (hb-ot-layout.cc:1928)
  5. `c->check_glyph_property(&cur, c->lookup_props)` — glyph passes property filter (hb-ot-layout.cc:1929)
  6. Applied subtable is `LigatureSubstFormat1_2<SmallTypes>` — GSUB lookup type 4 (ligature substitution)
  7. `index != NOT_COVERED` — current glyph is in the ligature coverage table (OT/Layout/GSUB/LigatureSubst.hh:115)
  8. `match_input(...)` succeeds — all subsequent ligature component glyphs are present in the buffer (OT/Layout/GSUB/Ligature.hh:111)
  9. `info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE` is non-zero — the glyph at `buffer->cur()` at the moment `ligate_input` calls `_hb_glyph_info_get_lig_num_comps` is GDEF-classified as a ligature (hb-ot-layout.hh:517)
  10. `info->lig_props() & IS_LIG_BASE` is ZERO — glyph is GDEF-classified as a ligature but does NOT carry the `IS_LIG_BASE` flag, meaning it was NOT previously produced by a `ligate_input` call during this shaping run (hb-ot-layout.hh:518, **the blocked False side**)

Root Cause Category: Input Format / Structure Constraints

Root Cause Explanation:
  The blocking condition is `_hb_glyph_info_ligated_internal(info)` returning False at line 518 of
  `hb-ot-layout.hh`. This function tests a single bit: `info->lig_props() & IS_LIG_BASE` (0x10).

  The `IS_LIG_BASE` flag is written exclusively by
  `_hb_glyph_info_set_lig_props_for_ligature()` at line 463:
    `info->lig_props() = (lig_id << 5) | IS_LIG_BASE | (lig_num_comps & 0x0F);`
  This setter is called only from `ligate_input()` (hb-ot-layout-gsubgpos.hh:1565), and only when
  `is_ligature` is true (line 1563), i.e., when the current glyph sequence is classified as a proper
  base ligature (not a mark ligature and not a base+mark sequence).

  The sequence of conditions required to reach line 518 with IS_LIG_BASE == 0 is:
    (a) The font's GDEF table classifies the incoming glyph's codepoint as class LIGATURE
        (sets bit 0x04 in glyph_props), so condition 9 (CTRL at line 517) is True.
    (b) BUT: the `IS_LIG_BASE` bit in `lig_props` is clear, meaning one of two scenarios:
        - **Scenario A (pre-existing ligature glyph in the font):** The input codepoint is a
          glyph ID that the font's GDEF table already marks as a ligature in its
          GlyphClassDef subtable — a pre-classified ligature — without HarfBuzz having formed
          it via GSUB type-4 substitution during this shaping call. Since `_hb_buffer_get_glyphs()`
          maps Unicode codepoints to glyph IDs via cmap, a font can contain a glyph that is
          GDEF-classified as a ligature but is directly accessible via the cmap without requiring
          any GSUB substitution. When `ligate_input` is called for the first time on such a glyph
          (it appears at `buffer->cur()` as a GDEF ligature), `lig_props` still contains 0 because
          `_hb_glyph_info_set_lig_props_for_ligature` has not yet been called for it.
        - **Scenario B (nested ligature substitution):** A prior GSUB pass created a ligature
          (setting IS_LIG_BASE), then a subsequent GSUB pass performs another ligature substitution
          where the first component is that ligature. In this case `ligate_input` is called with
          `buffer->cur()` being the pre-existing ligature. The call to `_hb_glyph_info_get_lig_num_comps`
          at line 1560 (to count `last_num_components`) occurs BEFORE the glyph at `buffer->cur()`
          is replaced — so its `lig_props` still has IS_LIG_BASE set, reaching the True side, not
          the False side.

  The False side is therefore reached in Scenario A: when `buffer->cur()` is a glyph whose codepoint
  is GDEF-ligature-classified but whose `lig_props` byte is 0 (never set by `ligate_input` in this
  shaping run). The fuzzer (cmplog) never exercises this because all fonts in its corpus that trigger
  GSUB ligature substitution produce buffer states where, by the time `ligate_input` is called for a
  second time on a buffer glyph, the first component is always one that was already processed by a
  prior `ligate_input` (IS_LIG_BASE set). To hit the False side, the corpus needs a font where:
    1. GDEF marks a glyph as class LIGATURE in GlyphClassDef, AND
    2. That glyph appears directly in the input buffer as `buffer->cur()` when a ligature
       substitution fires (i.e., it is one of the component glyphs fed into `ligate_input`,
       specifically the first component at buffer->cur()), AND
    3. Its `lig_props` byte has NOT been written by a prior `ligate_input` call in this shaping run.

  This is a font-structure constraint: it requires crafting a specific combination of GDEF
  GlyphClassDef entries and GSUB LigatureSubst lookup tables in the binary font input. A random
  fuzzer cannot discover this by mutating bytes because:
    - The font format is a complex binary structure (SFNT/OpenType tables) with length-prefixed,
      offset-indexed subtables; random bit flips produce structurally invalid fonts rejected early.
    - The cmplog fuzzer's comparisons log primitive comparisons (integers, small byte sequences)
      but cannot synthesize the correlated constraint across two separate OpenType tables (GDEF
      GlyphClassDef and GSUB LigatureSubst) that jointly control this branch.
    - The n4 fuzzer reaches this path abundantly (2,550,000 hits on the False side), indicating
      it has seeds with appropriately structured fonts — the cmplog fuzzer lacks these seeds.

Fuzzer Barrier Severity: High
  The False side is mathematically reachable (n4 demonstrates this with 2.55M hits), so the barrier
  is not Critical. However, the cmplog fuzzer has 0 hits despite 9,040 True-side hits, indicating
  it consistently misses this structural font pattern. The barrier is High because satisfying
  conditions 1–10 simultaneously requires a structurally valid OpenType font with correlated
  GDEF+GSUB table contents — something that cannot be discovered by mutation of structurally invalid
  input or by cmplog's comparison-guided mutation alone.

Recommended Mitigations:
  1. **Seed corpus cross-pollination:** Import the n4 fuzzer's queue seeds that exercise the False
     side into the cmplog fuzzer's corpus. The n4 fuzzer already has 2.55M hits on this branch;
     its seeds are the direct solution for the cmplog barrier.
  2. **Structure-aware font mutation (libprotobuf-mutator / grammar fuzzer):** Use a format-aware
     mutator that understands OpenType table layout. This ensures GDEF GlyphClassDef and GSUB
     LigatureSubst tables remain internally consistent while exploring glyph class assignments that
     set LIGATURE in GDEF without a prior GSUB substitution having fired for that glyph.
  3. **Targeted corpus addition:** Craft or find a minimal OpenType font that contains at least one
     glyph directly accessible via cmap (no GSUB substitution needed) that is classified as LIGATURE
     in GDEF's GlyphClassDef table, with a GSUB type-4 lookup that treats that glyph ID as a
     component. Add this font as a seed to the cmplog fuzzer's input corpus.
  4. **Dictionary augmentation:** Add the OpenType magic bytes (`\x00\x01\x00\x00` for TrueType,
     `OTTO` for CFF) and key SFNT table tags (`GDEF`, `GSUB`, `cmap`, `liga`) to the fuzzer
     dictionary. These tokens help the mutator assemble structurally recognizable font fragments
     that survive early parsing gates.

---

## Summary Table

| Cluster ID | Location | Blocked Side | Root Cause Category | Severity | Key Fix |
|------------|----------|--------------|---------------------|----------|---------|
| C01 | `_hb_glyph_info_get_lig_num_comps` in `hb-ot-layout.hh:518` | False | Input Format / Structure Constraints | High | Import n4 queue seeds into cmplog corpus; use structure-aware font mutator |

---

## Top Recommendations

1. **Cross-pollinate seeds from n4 to cmplog** (highest impact, zero implementation cost): The n4
   fuzzer already reaches the False branch 2.55M times. Import its seed queue directly into the
   cmplog fuzzer's corpus to immediately unblock this branch for the cmplog campaign.

2. **Add a structure-aware OpenType mutator** (medium effort, long-term coverage gain): A grammar-
   or protobuf-based mutator that understands SFNT table structure will systematically explore the
   GDEF × GSUB interaction space that controls this and other font-structure-dependent branches.

3. **Add a minimal crafted font seed** (low effort, targeted fix): One carefully constructed binary
   font where a cmap-accessible glyph is GDEF-classified as LIGATURE but no prior GSUB substitution
   fires for it — directly satisfying conditions 9 and 10 simultaneously.

4. **Extend the fuzzer dictionary with OpenType table tags and magic bytes** (low effort,
   broad benefit): Helps the mutator produce valid enough font skeletons to survive early
   parsing rejection and reach deeper GSUB/GDEF processing logic.
