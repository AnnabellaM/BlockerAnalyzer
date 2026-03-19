---
name: harfbuzz target structure
description: Fuzzer entry point, source layout, and coverage conventions for the harfbuzz target
type: project
---

**Fuzzer entry point:** `LLVMFuzzerTestOneInput` is defined in `targets/harfbuzz/test/fuzzing/hb-shape-fuzzer.cc`. The compiled binary also includes `test/api/test-ot-face.c` via `#include`. The fuzzer calls `hb_shape(input.font, buffer, nullptr, 0)` twice — once with a fixed ASCII string and once with font-data-derived UTF-32.

**Why:** Multiple fuzzer files exist; the one used for coverage is hb-shape-fuzzer.cc (confirmed by coverage file showing function body matching this file).

**How to apply:** When tracing from ENTRY for any harfbuzz blocker, start at `hb-shape-fuzzer.cc:13` (LLVMFuzzerTestOneInput) then follow `hb_shape` → `hb_shape_full` → OT pipeline.

**Key call chain (GSUB path):**
- `hb_shape` (hb-shape.cc:189) → `hb_shape_full` (hb-shape.cc:127)
- `hb_shape_full` → `hb_ot_map_t::substitute` (hb-ot-layout.cc:2084)
- `hb_ot_map_t::substitute` → `hb_ot_map_t::apply<GSUBProxy>` (hb-ot-layout.cc:2022)
- `apply<GSUBProxy>` → `apply_string<GSUBProxy>` (hb-ot-layout.cc:1968) — one call per lookup that passes digest filter
- `apply_string` → `apply_forward` (hb-ot-layout.cc:1919) or `apply_backward`
- `apply_forward` → `accel.apply` → lookup-type-specific `apply` (e.g. `LigatureSubstFormat1_2::apply`)

**Source layout:**
- OT table implementations: `src/OT/Layout/GSUB/`, `src/OT/Layout/GPOS/`, `src/OT/Var/`
- Inline utility functions (lig_props, glyph_props, etc.): `src/hb-ot-layout.hh`
- Apply context and match/ligate helpers: `src/hb-ot-layout-gsubgpos.hh`
- Main GSUB/GPOS apply orchestration: `src/hb-ot-layout.cc`

**Coverage conventions:**
- Function sections in cmplog/n4.cov are prefixed by mangled name without file prefix for template instantiations, but with `hb-ot-layout.cc:` prefix for static functions defined in that .cc (which actually come from included .hh files).
- `_hb_glyph_info_get_lig_num_comps` appears under prefix `hb-ot-layout.cc:` in coverage even though defined in `hb-ot-layout.hh` — because hb-ot-layout.cc is the translation unit.
- Line numbers in coverage match the .hh file line numbers (as inlined into the .cc TU).
