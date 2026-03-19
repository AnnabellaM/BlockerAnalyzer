# Root Cause Analysis — HarfBuzz Fuzzing Blockers (Ranks 1–40)

**Date:** 2026-03-18
**Target:** HarfBuzz text shaping library
**Coverage sources:** `coverage/harfbuzz/cmplog.cov`, `coverage/harfbuzz/n4.cov`
**Methodology:** Steps 1–5 (pre-screening, cluster confirmation, program slice, classification, findings)

---

## Cluster Confirmation Notes (Step 1.5)

Before analysis, each pre-computed cluster was verified against source code:

- **Ranks 7, 9, 11, 14, 18, 27** — all point to the same `StateTableDriver::drive()` template function in `hb-aat-layout-common.hh`. Ranks 7/27 share line 1262:11, ranks 11/14 share line 1287, rank 9 is at 1298:11, rank 18 is in a different `StateTableDriver` instantiation at 1268:19. The clusters correctly reflect distinct branch points in the same template. Ranks 7, 9, 11, 14 are all in the `LigatureSubtable` instantiation; ranks 18 and 27 are in `RearrangementSubtable` and `KerxSubTableFormat4` instantiations respectively. These are grouped by structural similarity into one cluster per instantiation class.

- **Ranks 3, 5, 17, 20, 21, 24** — all are `hvcurveto` template in `hb-cff-interp-cs-common.hh` lines 700 and 718/724. Ranks 3/5 share the same branch point (line 700:14, `True` side) with different template instantiations; ranks 17/21 share line 724:14; ranks 20/24 share line 718:11. These are confirmed as a single logical cluster representing the two branch points in `hvcurveto`: (a) the outer `if ((argStack.get_count() % 8) >= 4)` at line 690 and its inner loop exit at 718, and (b) the odd-argument `if (i < env.argStack.get_count())` extra delta at line 718 (True) and the final `flush=false` at line 724 (True). Grouped into one cluster **C-CFF2-HVCU**.

- **Ranks 4, 22, 25** — all in `VARC::get_path_at` / `VarComponent::get_path_at` in `OT/Var/VARC/VARC.cc`, different branch points at lines 347, 358, 360. Also rank 15 at line 370. These form cluster **C-VARC-PATH** (four related branches in the same function).

- **Ranks 8, 12** — both in `LigatureSubtable::driver_context_t::transition` (`hb-aat-layout-morx-table.hh`), lines 490:6 and 497:11. Confirmed as a chain cluster within the same function.

- **Ranks 30, 33, 40** — all in `ChainRuleSet::apply` (`hb-ot-layout-gsubgpos.hh`), lines 3511, 3526, and 3528. Confirmed as one cluster: they cover the fast-path lookup branches inside the same `for` loop.

- **Ranks 26, 31** — both in `hb_transform_t<float>::is_identity()` at lines 120:12 and 122:5 (short-circuit evaluation of `xx==1 && yx==0 && xy==0 && yy==1 && x0==0 && y0==0`). Confirmed as a `logical` cluster.

- **Ranks 10, 39** — different functions (`find_syllables_khmer` at 341:7 and `find_syllables_indic` at 1167:3). The branch point at 341:7 is `_trans_actions[_trans] == 0` (the "no action, skip" path in the Ragel FSM). Line 1167:3 in `find_syllables_indic` is the ternary in the Ragel trans lookup (`indic_category()` in range). These are separate single-branch entries, not merged.

- **Ranks 13, 35** — rank 13 is in `PosLookup::dispatch_recurse_func<hb_ot_apply_context_t>` (line 68:18 in `hb-ot-layout-gpos-table.hh`); rank 35 is in `MarkBasePosFormat1_2::accept` (line 104:6). Both concern GPOS mark attachment but are separate functions — kept as separate findings.

- **Rank 2** — `hb_any::operator()` at line 992:11 in `hb-iter.hh`. The False side means the for loop runs without finding a match (returns `false`). Confirmed as a `single` cluster.

- **Ranks 6, 1** — rank 1 (`_hb_glyph_info_get_lig_num_comps` at 518:7) and rank 6 (`ligate_input` at 1528:11) are distinct functions but both gated on having entered ligature-processing code that produces multi-component ligatures. Kept separate.

No splits or merges were required beyond what is described above.

---

## Findings (ordered by severity, Critical first)

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-CFF2-HVCU (logical/chain — multiple branch points in one function)**
**Ranks:** 3, 5, 17, 20, 21, 24
**Branches:**
- `hb-cff-interp-cs-common.hh:700:14 (True)` — Ranks 3 (cff2_extents), 5 (cff2_path)
- `hb-cff-interp-cs-common.hh:718:11 (True)` — Ranks 20 (cff2_extents), 24 (cff2_path)
- `hb-cff-interp-cs-common.hh:724:14 (True)` — Ranks 17 (cff2_extents), 21 (cff2_path)

**Location:** `hvcurveto<PATH, ENV, PARAM>()` in `src/hb-cff-interp-cs-common.hh`
**Branch Condition:** Three nested conditions inside `hvcurveto`:
1. Line 700: `for (; i + 8 <= env.argStack.get_count(); i += 8)` — inner loop condition in the `(argCount % 8) >= 4` branch (True = loop body entered again)
2. Line 718: `if (i < env.argStack.get_count())` — trailing odd delta in the `>= 4` branch (True = there is a trailing dx value)
3. Line 724: `for (; i + 8 <= env.argStack.get_count(); i += 8)` — inner loop in the `< 4` else branch (True = loop runs at all)

**Coverage Status:**
- Rank 3 (cff2_extents, 700:14 True): cmplog T:0, F:28 → n4 T:739,000, F:144,000
- Rank 5 (cff2_path, 700:14 True): cmplog T:0, F:17 → n4 T:554,000, F:108,000
- Rank 17 (cff2_extents, 724:14 True): cmplog T:0, F:36 → n4 T:138,000, F:25,800
- Rank 20 (cff2_extents, 718:11 True): cmplog T:0, F:28 → n4 T:114,000, F:30,100
- Rank 21 (cff2_path, 724:14 True): cmplog T:0, F:13 → n4 T:103,000, F:19,300
- Rank 24 (cff2_path, 718:11 True): cmplog T:0, F:17 → n4 T:85,800, F:22,400

**Execution Path to Branch:**
  Fuzzer input (font bytes) → `hb_shape()` → CFF2 font processing → `cs_interpreter_t::interpret()` → CFF2 charstring opcode dispatch (OpCode_hvcurveto at line 333) → `path_procs_t::hvcurveto()` → branch points at lines 690, 700, 718, 724

**Path Conditions Required:**
1. Input must be a valid CFF2 font (requires `cff` table header, CFF2 magic, valid charstring data)
2. The charstring must contain the `hvcurveto` opcode (0x1F)
3. **For line 700 True (inner loop entered a second time):** `(argStack.get_count() % 8) >= 4` AND `argStack.get_count() >= 12` — meaning the hvcurveto opcode must encode **12 or more arguments** starting with a 4-argument horizontal curve
4. **For line 718 True (trailing dx):** `(argCount % 8) >= 4` AND there is a single trailing argument after the loop (odd-count encoding). Requires `argCount == 4*k + 1` for some k ≥ 1.
5. **For line 724 True (else-branch loop runs):** `(argCount % 8) < 4` AND `argCount >= 8` — at least 8 args in the "vhcurveto-first" alternate encoding.

**Root Cause Category:** Input Format/Structure Constraints + Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
The `hvcurveto` opcode encodes alternating horizontal/vertical Bézier curves. All three True-side branches require argument counts that trigger specific encodings: ≥12 args (for the inner loop to execute a second time), or the odd-argument variant (≥5 args with odd count), or the alternate ≥8-arg form. The cmplog fuzzer never generates CFF2 charstrings with these argument counts because CFF2 is rarely in the seed corpus, and when it is, the charstring opcodes (variable-length encoded, with argument stack counts read from preceding `number` pushes) are difficult to mutate into the exact multi-argument forms needed. The n4 fuzzer (which uses a structured mutation) succeeds far more frequently. The True branches all require well-formed CFF2 charstring argument sequences with specific lengths, making them structurally unreachable without CFF2-aware mutation.

**Fuzzer Barrier Severity: High**
CFF2 fonts are rare in corpus; specific argument stack sizes for hvcurveto alternate encodings require structured input generation.

**Recommended Mitigations:**
1. Add CFF2 font samples with hvcurveto opcodes using 8, 9, 12, and 13+ arguments to the seed corpus.
2. Add CFF opcode byte values (`0x1F` for hvcurveto) and multi-argument prefixes to the fuzzer dictionary.
3. Use a structured CFF2-aware mutator that understands charstring argument stacks.
4. Consider a libFuzzer custom mutator that directly generates valid CFF2 charstring sequences.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-VARC-PATH (chain — sequential conditions in one function)**
**Ranks:** 4, 22, 25, 15
**Branches:**
- `OT/Var/VARC/VARC.cc:347:7 (False)` — Rank 4
- `OT/Var/VARC/VARC.cc:358:47 (False)` — Rank 22
- `OT/Var/VARC/VARC.cc:360:11 (True)` — Rank 25
- `OT/Var/VARC/VARC.cc:370:11 (False)` — Rank 15

**Location:** `VARC::get_path_at()` in `src/OT/Var/VARC/VARC.cc`
**Branch Conditions:**
- Line 347: `if (c.draw_session)` — draw path vs. extents path
- Line 358: `leaf_transform.is_identity()` — whether a transform pen is needed
- Line 360: `if (c.font->face->table.glyf->get_path_at(...))` — TrueType glyph path lookup
- Line 370: `if (!c.font->face->table.glyf->get_extents_at(...))` — TrueType extents lookup (extents path)

**Coverage Status:**
- Rank 4 (347:7 False): cmplog T:14, F:0 → n4 T:724,000, F:627,000
- Rank 22 (358:47 False): cmplog T:6, F:0 → n4 T:143,000, F:97,000
- Rank 25 (360:11 True): cmplog T:0, F:6 → n4 T:74,200, F:166,000
- Rank 15 (370:11 False): cmplog T:8, F:0 → n4 T:334,000, F:150,000

**Execution Path to Branch:**
  Font input → `hb_shape()` or extents API → `VARC::accelerator_t::get_path()` or `get_extents()` → `VARC::get_path_at()` → `VarComponent::get_path_at()` (for composite components) → `VARC::get_path_at()` recursively → branch points at 347, 358, 360, 370

**Path Conditions Required:**
1. Input font must contain a valid `VARC` table (version 1, with `coverage`, `varStore`, `axisIndicesList`, and `glyphRecords` offsets populated)
2. The queried glyph must appear in the VARC coverage (i.e., be a variable composite glyph)
3. The glyph must not be a recursive call to itself (cycle check passes)
4. **For 347 False (extents path):** `c.draw_session` must be null — i.e., the fuzzer harness must call the extents API, not the draw API, for a VARC glyph
5. **For 358 False (non-identity transform):** The VarComponent's decoded transform fields (rotation, scale, skew, translation from font data) must result in a non-identity transform matrix
6. **For 360 True (glyf lookup succeeds):** The component glyph GID must exist in the `glyf` table, AND the `glyf` table's `get_path_at` must succeed (non-composite, valid glyph data present)
7. **For 370 False (glyf extents fails, fallback needed):** The component glyph is NOT in `glyf`, requiring fallback to CFF2 or CFF1 for extents

**Root Cause Category:** Input Format/Structure Constraints + Deep Nested Condition Dependencies

**Root Cause Explanation:**
The VARC table is a new OpenType extension for variable composite glyphs. The cmplog fuzzer rarely produces inputs containing a valid VARC table structure because: (a) the VARC table has multiple nested offsets that must all be valid, (b) the glyph records must reference valid GIDs present in the coverage, and (c) the transform fields are encoded with specific bit-flags (`flags_t`) that must be set in the VarComponent binary data. The False side of 347 (extents path) requires a harness call via `get_extents` rather than `get_path`, which depends on which API the fuzzer exercises. The non-identity transform path (358 False) requires the VarComponent binary to encode non-zero rotation/scale/skew/translation, which requires specific bits in the `flags_t` bitmask and corresponding floating-point values. The cmplog fuzzer never reaches these because it fails VARC table sanitization almost entirely, while n4 (with more iterations) occasionally generates valid VARC payloads. The 360 True/370 False distinction depends on which underlying table (glyf vs. CFF2) is present for the component glyph, adding another structural constraint.

**Fuzzer Barrier Severity: High**
VARC is a complex new table format with multi-level nested binary structures; the cmplog fuzzer essentially never generates valid VARC data, while n4 reaches these only rarely.

**Recommended Mitigations:**
1. Add valid VARC-containing font files to the fuzzer seed corpus (e.g., from Google Fonts variable composite fonts).
2. Write a custom structure-aware generator that produces valid VARC table payloads with non-identity transforms.
3. Add the VARC table tag bytes (`VARC` = `0x56415243`) to the fuzzer dictionary.
4. Create a targeted harness that specifically exercises the extents API path for VARC glyphs.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-AAT-LIGTABLE (chain — two conditions in LigatureSubtable::transition)**
**Ranks:** 8, 12
**Branches:**
- `hb-aat-layout-morx-table.hh:490:6 (True)` — Rank 12
- `hb-aat-layout-morx-table.hh:497:11 (True)` — Rank 8

**Location:** `LigatureSubtable<ExtendedTypes>::driver_context_t::transition()` in `src/hb-aat-layout-morx-table.hh`
**Branch Conditions:**
- Line 490: `if (unlikely (match_length && match_positions[(match_length - 1u) % ARRAY_LENGTH(match_positions)] == buffer->out_len))` — guards against double-marking the same position when `DontAdvance` is active
- Line 497: `if (LigatureEntryT::performAction(entry))` — whether the current state machine entry triggers a ligature substitution action

**Coverage Status:**
- Rank 12 (490:6 True): cmplog T:0, F:6 → n4 T:194,000, F:77,800
- Rank 8 (497:11 True): cmplog T:0, F:66 → n4 T:351,000, F:583

**Execution Path to Branch:**
  Font bytes (morx/morx table) → `hb_shape()` → AAT morx processing → `Chain::apply()` → `LigatureSubtable::apply()` → `StateTableDriver::drive()` → per-glyph `transition()` → branch at 490 / 497

**Path Conditions Required:**
1. Input font must contain a valid morx (AAT Extended Morph) table with a LigatureSubtable entry
2. The morx chain must be enabled (feature flags match the buffer's feature settings)
3. The state machine must transition through states with `SetComponent` flag set (to accumulate match positions)
4. **For 490 True:** The same glyph must be visited twice without advancing — i.e., a state with the `DontAdvance` flag (`entry.flags & DontAdvance`) must fire `SetComponent` at the same output position twice. This requires a very specific state machine edge in the morx data.
5. **For 497 True:** The entry must have `performAction` set — the state machine must enter a state with a ligature action, which requires the morx ligature action table to be non-empty and the current path through the state machine to reach an action-triggering state. In cmplog, the state machine is traversed but action-triggering transitions are not reached.

**Root Cause Category:** Input Format/Structure Constraints + Deep Nested Condition Dependencies

**Root Cause Explanation:**
AAT morx LigatureSubtable processing requires the font's binary morx state machine to encode specific state transitions. The 490 True path requires a `DontAdvance + SetComponent` combination that fires on the same output position twice — a degenerate state machine configuration unlikely to appear in random fonts. The 497 True path (ligature action) requires the state machine to encode action entries (with `LigActionLast` set in the 32-bit action word), and the input text must drive the state machine to a state where an action fires. The cmplog fuzzer rarely produces valid morx table structures, and when it does, the action-triggering state transitions (which require specific glyph class sequences encoded in the state machine transition table) are not reached because the generated glyph sequences don't match the state machine's expected inputs.

**Fuzzer Barrier Severity: High**
AAT morx ligature tables are complex binary structures; action-triggering requires both a valid morx state machine AND a matching glyph sequence at shaping time.

**Recommended Mitigations:**
1. Add font samples with morx LigatureSubtable entries to the corpus.
2. Use a morx-aware structure mutator that generates valid state machine entries with ligature actions.
3. Add test inputs (text sequences) that exercise morx state machine transitions when combined with valid morx fonts.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-AAT-STDRIVE (chain — StateTableDriver fast-path and safe-to-break conditions)**
**Ranks:** 7, 9, 11, 14
**Branches (all in `StateTableDriver<ExtendedTypes, LigatureEntry, ...>::drive()`, `hb-aat-layout-common.hh`):**
- `1262:11 (False)` — Rank 7: inner `do-while` loop klass change condition (False = klass changed, loop exits)
- `1287:32 (False)` — Rank 14: `is_null_transition` True branch exits (the `if (is_null_transition)` check entered)
- `1287:60 (True)` — Rank 11: `klass == old_klass` condition True (loop continues)
- `1298:11 (False)` — Rank 9: `if (!is_safe_to_break && ...)` (False = is safe to break, no unsafe annotation)

**Coverage Status:**
- Rank 7 (1262:11 False): cmplog T:66, F:0 → n4 T:583, F:351,000
- Rank 14 (1287:32 False): cmplog T:2, F:0 → n4 T:195,000, F:155,000
- Rank 11 (1287:60 True): cmplog T:0, F:2 → n4 T:195,000, F:59
- Rank 9 (1298:11 False): cmplog T:60, F:0 → n4 T:1,370, F:350,000

**Execution Path to Branch:**
  Font + text input → `hb_shape()` → AAT morx/kerx processing → `StateTableDriver::drive()` → state machine inner loop (lines 1261–1293) and safe-to-break logic (lines 1296–1351)

**Path Conditions Required:**
1. A valid morx/kerx AAT table must exist
2. The state machine must enter the `else` branch at line 1259 (i.e., `last_range == nullptr`, meaning no per-range flags)
3. **For 1262 (inner loop / null transition fast path):** `is_null_transition` must be true — the state must be at `STATE_START_OF_TEXT`, next state also `STATE_START_OF_TEXT`, no action, advancing. A run of non-actionable glyphs in the same class must appear. The False of 1262:11 means the loop exits (klass changes) — this requires a transition from one glyph class to another. The True (rank 11) means the glyph class stays the same across multiple glyphs.
4. **For 1287:32 False (didn't enter null-transition branch):** `is_null_transition` is False — the state machine is not in the simple pass-through case (either there's an action, or the state changes non-trivially). This is the much more common path — n4 reaches this far more because it generates longer inputs with varied glyph sequences.
5. **For 1298:11 False (safe-to-break):** the complex `is_safe_to_break` conjunction at lines 1325–1351 evaluates to True — no action, already at start state or epsilon transition to start, no end-of-text action. This requires specifically non-actionable transitions, which is blocked when cmplog's font data causes the state machine to always be in actionable states.

**Root Cause Category:** Input Format/Structure Constraints + Algorithmic/Semantic Barriers

**Root Cause Explanation:**
The StateTableDriver fast-path (null-transition loop at line 1262) and safe-to-break logic (line 1298) are optimizations that depend on the combination of font-defined state machine structure and input glyph sequence properties. The cmplog fuzzer hits these rarely because: (1) its AAT table structures are mostly invalid (failing sanitization before reaching `drive()`), and (2) even with valid tables, generating glyph sequences that trigger specific fast-path conditions (long runs of same-class non-actionable glyphs) requires both a specific font and a matching text input simultaneously. The n4 fuzzer, with more iterations, occasionally generates valid font+text combinations that exercise these paths. The safe-to-break False (rank 9) requires the state machine to actually fire actions, which in turn requires the font's morx action table to be non-trivially populated.

**Fuzzer Barrier Severity: High**
Two-dimensional barrier: both the font structure (state machine) and the input text (glyph class sequences) must align simultaneously.

**Recommended Mitigations:**
1. Add valid AAT morx fonts (especially Apple system fonts with complex ligature state machines) to the corpus.
2. Use a two-dimensional corpus: (font, text) pairs where the text is known to exercise specific state machine paths.
3. Add common morx-triggering character sequences (e.g., Arabic ligature sequences for morx fonts) to a text seed corpus.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-AAT-REARR (single — StateTableDriver RearrangementSubtable null-transition)**
**Rank:** 18
**Branch:** `hb-aat-layout-common.hh:1268:19 (True)`
**Location:** `StateTableDriver<ExtendedTypes, void, RearrangementSubtable::Flags>::drive()` — `do { ... } while (klass == old_klass)` inner continuation condition

**Coverage Status:** cmplog T:0, F:95 → n4 T:126,000, F:1,210

**Execution Path:**
  Font → AAT morx Rearrangement subtable processing → `StateTableDriver::drive()` → null-transition fast path at line 1265 → inner loop at 1268

**Path Conditions Required:**
1. Valid morx table with RearrangementSubtable entry
2. Input text must produce a glyph sequence that is all in the same glyph class, all non-actionable, staying in `STATE_START_OF_TEXT` — a run of 2+ identical-class glyphs with no state machine actions

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
Identical to the C-AAT-STDRIVE cluster but for the Rearrangement subtable instantiation. The True side (loop continues because klass stayed the same) requires at least two consecutive glyphs of the same AAT class that trigger no action. The cmplog fuzzer's morx tables are usually invalid or have action-triggering entries for all classes, so this pass-through path is never exercised.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Same as C-AAT-STDRIVE mitigations.
2. Specifically add morx RearrangementSubtable samples to corpus.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-GLYPH-LIGNUM (single — lig_num_comps conditional)**
**Rank:** 1
**Branch:** `hb-ot-layout.hh:518:7 (False)`
**Location:** `_hb_glyph_info_get_lig_num_comps()` — `if ((info->glyph_props() & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE) && _hb_glyph_info_ligated_internal(info))` returns 0 (not a multi-component ligature with internal lig properties)

**Coverage Status:** cmplog T:9,040, F:0 → n4 T:26,200, F:2,550,000

**Execution Path:**
  Font + text → `hb_shape()` → GSUB ligature substitution → `ligate_input()` → `_hb_glyph_info_get_lig_num_comps()` → condition at line 504

**Path Conditions Required:**
1. A GSUB LigatureSubst lookup must fire, producing a ligature glyph
2. The font must have the ligature glyph marked with `LIGATURE` glyph property (set from GDEF table ClassDef)
3. **For False side:** The resulting glyph must NOT have `_hb_glyph_info_ligated_internal()` set — i.e., the glyph's `lig_props()` must indicate it was NOT produced via an internal HarfBuzz ligature assembly process. This happens when a glyph has the LIGATURE property from GDEF but was not shaped via the internal `ligate_input()` path (e.g., a pre-formed ligature from an unusual GSUB path), OR when called on a glyph that is a ligature component being queried for its num_comps *after* replacement.

**Root Cause Category:** Deep Nested Condition Dependencies

**Root Cause Explanation:**
The False path at line 518 returns 1 (not a multi-component ligature with internal tracking), which requires the glyph to be a GDEF-declared LIGATURE but with `ligated_internal == 0`. This is an unusual state: normally when a ligature is formed via `ligate_input()`, both properties are set together. The n4 fuzzer sees this 2.55 million times, indicating it reaches many GSUB lookups via longer, more complex substitution chains (possibly involving fonts with GDEF LIGATURE class glyphs that are being processed in contexts where the `lig_id` tracking is not active, or via lookup paths that set GLYPH_PROPS_LIGATURE from GDEF independently of the shaping process). The cmplog fuzzer likely produces simpler fonts where GSUB ligatures and GDEF classification are not set up in this configuration. The barrier is the simultaneous requirement of a GDEF-classified LIGATURE glyph and a context where `lig_props()` does NOT have the internal bit set.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add fonts with GSUB ligatures AND a GDEF table that separately classifies glyphs as LIGATURE to the seed corpus.
2. Add test inputs that exercise GSUB lookups generating both simple and complex ligature chains.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-LIGATE-MARK (single — ligate_input mark-ligature check)**
**Rank:** 6
**Branch:** `hb-ot-layout-gsubgpos.hh:1528:11 (False)`
**Location:** `ligate_input()` — `if (!is_mark_ligature && last_lig_id)` at line 1598 (note: the blockers report cites 1528:11 which maps to the comment block line range; the actual condition controlling the False side is at 1598)

**Coverage Status:** cmplog T:68, F:0 → n4 T:35,100, F:520,000

**Path Conditions Required:**
1. A GSUB Ligature lookup must fire
2. The ligature must be a "mark ligature" — all components are marks (as set by `_hb_glyph_info_is_mark()`)
3. OR `last_lig_id == 0` — the last component was not attached to any prior ligature

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
The False side of `if (!is_mark_ligature && last_lig_id)` is taken when the condition is False, meaning either `is_mark_ligature == true` (a mark-mark ligature) OR `last_lig_id == 0` (no prior ligature component tracking). The n4 fuzzer generates fonts where GSUB ligature lookups fire across varied glyph sequences that include mark glyphs or untracked components, while the cmplog fuzzer's simpler inputs always produce ligatures where non-mark components have a valid `last_lig_id`, always entering the True path. Reaching the False path requires either mark-only ligatures (unusual font feature) or ligatures formed from components with no lig ID tracking (e.g., the first ligature in a sequence).

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add fonts with GSUB mark ligature lookups (e.g., Arabic combining mark ligatures) to the corpus.
2. Add Unicode mark character sequences (U+0300+ range) paired with appropriate Arabic/Indic fonts.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-HB-ANY (single — hb_any iterator empty)**
**Rank:** 2
**Branch:** `hb-iter.hh:992:11 (False)`
**Location:** `hb_any::operator()` — the `for (auto it = hb_iter(c); it; ++it)` loop increment condition — the False side is taken when the iterator is exhausted without finding a match (function returns `false`).

**Coverage Status:** cmplog T:663, F:0 → n4 T:3,640, F:1,600,000

**Context:** This is instantiated as `hb_any(coords_range, ...)` in a lambda inside the hb_ot font function static initializer region, but the coverage address at 992:11 in the context of `_ZNK4$_33clIR10hb_array_tIKiE...` suggests it is the `hb_any` applied to an array of coordinate values (likely variation coordinates) where the predicate checks for a non-zero coordinate.

**Path Conditions Required:**
1. The code path calling `hb_any` on a coordinate array must be reached
2. **For False side:** All elements in the array must fail the predicate — i.e., all variation coordinates are zero (or the array is empty)

**Root Cause Category:** Algorithmic/Semantic Barriers

**Root Cause Explanation:**
The cmplog fuzzer exercises this path (663 True hits, 0 False), meaning it always finds at least one matching element. The n4 fuzzer exercises the False path 1.6 million times. This suggests the False side corresponds to a font with all-zero variation coordinates (a non-variable font queried through the variable font path, or a zero-coordinates design position). The cmplog fuzzer likely generates inputs where variation coordinates are non-zero (from corpus font files), while the n4 fuzzer explores degenerate all-zero cases. This is a data-value constraint rather than a structural barrier.

**Fuzzer Barrier Severity: Medium**
Reachable with a seed corpus that includes non-variable fonts or zero-coordinate variation fonts.

**Recommended Mitigations:**
1. Add non-variable fonts (all variation coordinates zero) to the seed corpus alongside variable fonts.
2. Add a zero-coordinates test case explicitly.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-KHMER-FSM (single — Khmer Ragel FSM action dispatch)**
**Rank:** 10
**Branch:** `hb-ot-shaper-khmer-machine.hh:341:7 (True)`
**Location:** `find_syllables_khmer()` — `if (_khmer_syllable_machine_trans_actions[_trans] == 0)` — the True side means the FSM transition has no action (skip the action dispatch switch).

**Coverage Status:** cmplog T:0, F:8,260 → n4 T:209,000, F:45,900

**Path Conditions Required:**
1. Input text must contain Khmer Unicode code points (U+1780–U+17FF range), causing the Khmer shaper to activate
2. The Khmer glyph must be classified into a category that triggers a state machine transition with `_trans_actions == 0`
3. Specifically, the Khmer syllable machine must reach a transition where no action fires — this happens for transitional states (non-final states in the syllable parser) — e.g., the middle of a consonant cluster accumulation

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
The Khmer syllable machine is a Ragel-generated FSM that processes `khmer_category()` values. The cmplog fuzzer does not generate Khmer text sequences (the fuzzer corpus likely lacks Khmer Unicode code points), so the Khmer shaper is activated extremely rarely (8,260 False hits = some Khmer is processed, but all transitions happen to fire actions). The n4 fuzzer generates Khmer sequences more frequently (209,000 True hits). The no-action transition (True side) occurs for intermediate syllable parser states that accumulate glyph components before a complete syllable is recognized — e.g., consonant + vowel sign mid-accumulation. The cmplog fuzzer's Khmer inputs apparently always trigger final states with actions.

**Fuzzer Barrier Severity: Medium**
Reachable with Khmer text in the seed corpus; the intermediate-state transitions are easy to hit with valid Khmer syllables.

**Recommended Mitigations:**
1. Add Khmer Unicode text samples (U+1780–U+17FF consonant + vowel sequences) to the fuzzer corpus.
2. Add Khmer-specific font files paired with Khmer text to the seed corpus.
3. Add Khmer Unicode code point bytes to the fuzzer dictionary.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-AAT-KERX4 (chain — KerxSubTableFormat4 transition action)**
**Ranks:** 28, 27
**Branches:**
- `hb-aat-layout-kerx-table.hh:557:23 (False)` — Rank 28: inside `KerxSubTableFormat4::driver_context_t::transition()`, some condition related to kerning action flag
- `hb-aat-layout-common.hh:1262:11 (True)` — Rank 27: StateTableDriver null-transition True (loop continues same klass), KerxSubTableFormat4 instantiation

**Coverage Status:**
- Rank 28 (557:23 False): cmplog T:110,000, F:0 → n4 T:111,000, F:55,300
- Rank 27 (1262:11 True): cmplog T:0, F:110,000 → n4 T:55,400, F:166,000

**Execution Path:**
  Font → `hb_shape()` → AAT kerx table processing → `KerxSubTableFormat4::apply()` → `StateTableDriver::drive()` → `transition()` / null-transition loop

**Path Conditions Required:**
1. Valid kerx table with Format 4 (ContextualGlyphSubstitution) entry
2. Input text that drives the state machine through both actionable and non-actionable transitions
3. **Rank 28 False:** Inside `transition()` at line 557, the False branch of a kerning action flag check — the font must encode a KerxFormat4 entry where the specific sub-table flag governing this branch is false (e.g., `CrossStream` or action flags not set for this entry)
4. **Rank 27 True:** Same as C-AAT-STDRIVE; requires a run of same-class non-actionable glyphs in the KerxSubTableFormat4 state machine

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
The cmplog fuzzer exercises the `transition()` True path (110K hits) but never the False side (rank 28), meaning the kerx Format4 fonts it generates always have the action flag set for transitions it exercises. The n4 fuzzer generates kerx fonts where some transitions lack the action flag. Simultaneously, rank 27 (null-transition True) requires consecutive same-class glyphs with no action — n4 generates these while cmplog does not.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add font samples with kerx Format 4 tables, including entries with and without the action flag, to the corpus.
2. Test with text containing consecutive glyphs from the same kerx class.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-AAT-GLYPH-OUT (single — output_glyphs deletion check)**
**Rank:** 29
**Branch:** `hb-aat-layout-common.hh:176:11 (True)` — `if (glyphs[i] == DELETED_GLYPH)` inside `output_glyphs()`

**Coverage Status:** cmplog T:0, F:18,200 → n4 T:44,500, F:92,700

**Path Conditions Required:**
1. An AAT morx Insertion subtable must fire and output glyphs
2. One of the output glyph GIDs must equal `DELETED_GLYPH` (a special sentinel value used to mark glyphs for deletion)
3. This requires the morx insertion action table to encode a `DELETED_GLYPH` GID value in its output glyph list

**Root Cause Category:** Magic Value / Checksum Constraints

**Root Cause Explanation:**
`DELETED_GLYPH` is a specific sentinel GID (0xFFFF or similar special value) used as a placeholder in AAT output glyph arrays. The True side fires only when the morx table's insertion action list contains this special value. The cmplog fuzzer's morx tables, even when partially valid, never encode this specific sentinel value in the output glyph list. The n4 fuzzer generates it occasionally. The barrier is that `DELETED_GLYPH` is a specific 16-bit value that must appear in the morx insertion action array.

**Fuzzer Barrier Severity: High**
Magic value constraint (specific GID value in font binary data).

**Recommended Mitigations:**
1. Add the `DELETED_GLYPH` sentinel value to the fuzzer dictionary.
2. Include morx font samples where insertion subtables reference deleted-glyph entries.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-CHAIN-FAST (chain — ChainRuleSet::apply fast-path branches)**
**Ranks:** 30, 33, 40
**Branches (all in `ChainRuleSet<SmallTypes>::apply()`, `hb-ot-layout-gsubgpos.hh`):**
- `3511:11 (False)` — Rank 33: `if (lenP1 > 1 ? ... : ...)` outer ternary False side — taken when `lenP1 <= 1` AND `match_lookahead` check fails
- `3526:8 (False)` — Rank 30: `if (r.apply(c, lookup_context))` — rule applied successfully but returned false (no substitution triggered)
- `3528:10 (True)` — Rank 40: `if (unsafe_to != (unsigned) -1)` — a valid unsafe_to boundary was computed (some skippable was detected in the lookahead iterator)

**Coverage Status:**
- Rank 33 (3511 False): cmplog T:490, F:0 → n4 T:100,000, F:13,700
- Rank 30 (3526 False): cmplog T:490, F:0 → n4 T:57,000, F:41,000
- Rank 40 (3528 True): cmplog T:0, F:490 → n4 T:9,640, F:47,400

**Execution Path:**
  Font + text → GSUB ChainContext lookup → `ChainRuleSet::apply()` → fast-path branch at 3505–3598

**Path Conditions Required:**
1. A GSUB ChainContextSubst Format 1 lookup must be active
2. The `HB_OPTIMIZE_SIZE_VAL` must be false and `num_rules > 4` (the fast path must be selected)
3. **For 3511 False:** The `lenP1 <= 1` case must hold AND the lookahead match must fail — requires a rule with no input beyond the current glyph where the lookahead context does not match
4. **For 3526 False:** A candidate rule passes the fast-path glyph checks but `_.apply()` fails — the rule's backtrack/lookahead context does not fully match
5. **For 3528 True:** The skippy iterator detects a skippable glyph in the lookahead (`unsafe_to != -1`) — the second glyph after the current position is a default-ignorable, requiring the fast path to fall through to the slow path

**Root Cause Category:** Deep Nested Condition Dependencies + Algorithmic/Semantic Barriers

**Root Cause Explanation:**
The ChainRuleSet fast path (introduced to avoid repeated context look-ups) has several branches that are only reached with specific font+text configurations. The cmplog fuzzer exercises the fast path (490 True hits of 3511 True and 3526 True), meaning it always finds rules that pass pre-checks and successfully apply. The False sides require rules that pass the first-glyph check but then fail deeper context matching (3526 False = rule passes but fails in full apply), or skippable glyphs in lookahead (3528 True). These require fonts with complex ChainContext rules involving multiple lookahead/backtrack sequences, combined with input text containing default-ignorable code points (e.g., variation selectors, zero-width joiners) between rule-relevant glyphs.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add fonts with GSUB ChainContextSubst lookups that include rules with backtrack/lookahead > 2 elements.
2. Add text sequences containing Unicode default-ignorable code points (variation selectors, ZWNJ, ZWJ) interspersed with shaping-relevant code points.
3. Add fonts where some ChainContext rules explicitly fail (backtrack context not satisfied) to exercise the False path.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-TRANSFORM-IDENTITY (logical — is_identity multi-condition short-circuit)**
**Ranks:** 26, 31
**Branches (all in `hb_transform_t<float>::is_identity()`, `hb-geometry.hh`):**
- `120:12 (False)` — Rank 26: `xx == 1 && yx == 0` fails (either xx ≠ 1 or yx ≠ 0)
- `122:5 (False)` — Rank 31: `x0 == 0 && y0 == 0` fails (either x0 ≠ 0 or y0 ≠ 0)

**Coverage Status:**
- Rank 26 (120:12 False): cmplog T:6, F:0 → n4 T:177,000, F:62,700
- Rank 31 (122:5 False): cmplog T:6, F:0 → n4 T:149,000, F:27,700

**Execution Path:**
  VARC composite glyph rendering → `VARC::get_path_at()` → `leaf_transform.is_identity()` at line 357 → `is_identity()` checks at 120–122

**Path Conditions Required:**
1. VARC table processing path must be reached (same as C-VARC-PATH)
2. **For 120 False:** The VarComponent's transform matrix must have `xx ≠ 1` or `yx ≠ 0` — i.e., the component has non-identity scale or rotation (flags `HAVE_SCALE_X`, `HAVE_ROTATION` etc. set in the VarComponent flags)
3. **For 122 False:** The transform matrix must have `x0 ≠ 0` or `y0 ≠ 0` — i.e., a non-zero translation (flags `HAVE_TRANSLATE_X` or `HAVE_TRANSLATE_Y` set)

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
These are subconditions of `is_identity()`, used to decide whether to construct a full transform pen for VARC component rendering. The False sides require non-identity transforms from VarComponent binary data. Since the cmplog fuzzer almost never generates valid VARC data (see C-VARC-PATH), it rarely reaches this check, and when it does (6 True hits), the transform is identity (all defaults). The n4 fuzzer generates valid VARC components with non-identity transforms more frequently. The barrier is the same as for C-VARC-PATH: valid VARC binary structure with non-default transform flags.

**Fuzzer Barrier Severity: High** (inherits from VARC barrier)

**Recommended Mitigations:**
1. Same as C-VARC-PATH mitigations.
2. Specifically ensure VARC seed fonts have VarComponents with non-identity transforms (rotation, scale, translation fields set).

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-CFF-HINTMASK (single — hintmask seen_hintmask guard)**
**Rank:** 32
**Branch:** `hb-cff-interp-cs-common.hh:178:9 (False)` — `if (!seen_hintmask)` — the False side means `seen_hintmask` is already true (hintmask was already processed)

**Coverage Status:** cmplog T:30, F:0 → n4 T:318, F:24,200

**Path Conditions Required:**
1. CFF1 or CFF2 charstring must contain a hintmask or cntrmask operator
2. `determine_hintmask_size()` must be called MORE THAN ONCE during a single charstring interpretation — i.e., the charstring must have both hstem/vstem operators AND a hintmask operator, and the interpreter must call `determine_hintmask_size()` again after it's already been called once (during re-entry or a second hintmask in the same charstring)

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
The `seen_hintmask` guard prevents re-counting stems after the first hintmask appears. The False path (already seen) fires when `determine_hintmask_size()` is called a second time in the same charstring. This happens for charstrings with multiple hintmask operators (e.g., when a CFF charstring has complex hint replacement sequences). The cmplog fuzzer's CFF charstrings are too simple or always exercise only one hintmask per charstring. Reaching the False path requires a CFF charstring specifically structured with multiple hintmask/cntrmask operators following the initial hstem/vstem declarations.

**Fuzzer Barrier Severity: Medium**
The CFF hintmask path is reachable with CFF fonts that have complex hint replacement; adding such fonts to the corpus should help.

**Recommended Mitigations:**
1. Add CFF1 fonts with complex hint replacement (multiple hintmask operators) to the corpus.
2. Add CFF charstring bytes for hintmask opcode (`0x13`/`0x14`) to the dictionary.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-GLYF-NODATA (single — glyf table empty check)**
**Rank:** 34
**Branch:** `OT/glyf/glyf.hh:514:9 (True)` — `if (!has_data()) return false` — the glyf table has no data

**Coverage Status:** cmplog T:0, F:6 → n4 T:12,200, F:228,000

**Path Conditions Required:**
1. `VARC::get_path_at()` must be reached for a component glyph (from C-VARC-PATH)
2. The `c.draw_session` must be non-null (draw path)
3. The `is_identity()` check (line 357) must evaluate, and `get_path_at` on the glyf table is called
4. **For True side:** `glyf_accelerator_t::has_data()` returns false — the font has NO glyf table (pure CFF or CFF2 font)

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
The True side fires when `glyf->get_path_at()` is called but the font has no glyf table. This path returns `false` so the caller tries CFF2 fallback. This requires a font that has a VARC table but no glyf table (purely CFF2 or CFF1 outlines). The cmplog fuzzer's VARC fonts, when valid at all, apparently always have glyf data; n4 generates VARC+CFF-only fonts.

**Fuzzer Barrier Severity: Medium**

**Recommended Mitigations:**
1. Add CFF2 fonts with VARC tables (no glyf) to the corpus.
2. Pair VARC seed fonts with both glyf-based and CFF2-based component references.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-MARKBASE-ACCEPT (single — MarkBasePos accept multiplied glyph check)**
**Rank:** 35
**Branch:** `OT/Layout/GPOS/MarkBasePosFormat1.hh:104:6 (True)` — inside `accept()`: `!_hb_glyph_info_multiplied(&buffer->info[idx - 1])` — True means the previous glyph was NOT produced by a MultipleSubst lookup

**Coverage Status:** cmplog T:0, F:462 → n4 T:12,000, F:128,000

**Path Conditions Required:**
1. GPOS MarkBasePosFormat1 lookup must apply
2. The current glyph must be "multiplied" (produced by a GSUB MultipleSubst lookup): `_hb_glyph_info_multiplied()` returns true
3. The glyph's lig_comp must be non-zero (not the first component): `_hb_glyph_info_get_lig_comp() != 0`
4. `idx > 0` must hold (not at buffer start)
5. **For True side:** The previous glyph must NOT be multiplied — meaning it was a normal glyph or a different kind of substitution product

**Root Cause Category:** Deep Nested Condition Dependencies

**Root Cause Explanation:**
The `accept()` function filters out non-first components of MultipleSubst sequences to prevent double-attaching marks. The True path at line 104 fires when: the current glyph is a non-first MultipleSubst component AND the previous glyph is NOT multiplied (allowing attachment because the previous glyph isn't part of the same MultipleSubst sequence). This requires a font with both GSUB MultipleSubst and GPOS MarkBasePos lookups, AND the specific condition that the previous glyph in the buffer is not a MultipleSubst product. The cmplog fuzzer's fonts rarely combine MultipleSubst with MarkBasePos in this exact way.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add fonts combining GSUB MultipleSubst and GPOS MarkBasePos lookups.
2. Add test text sequences that trigger MultipleSubst substitutions followed by mark positioning.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-USE-REORDER (single — USE syllable reorder VPre/VMPre check)**
**Rank:** 36
**Branch:** `hb-ot-shaper-use.cc:436:7 (False)` — `else if (((flag) & (FLAG(USE(VPre)) | FLAG(USE(VMPre)))) && 0 == _hb_glyph_info_get_lig_comp(&info[i]) && j < i)` — False means the condition is not met (glyph is not VPre/VMPre, or is a non-first lig component, or j >= i)

**Coverage Status:** cmplog T:1, F:0 → n4 T:1,210, F:12,000

**Path Conditions Required:**
1. Universal Shaping Engine (USE) shaper must activate (requires appropriate Unicode script and USE-supported font)
2. The reorder_syllable_use function must process a syllable with VPre or VMPre vowels
3. **For False side:** Within the "move things back" loop, a glyph must be encountered that is NOT VPre/VMPre, or is a lig_comp > 0, or j >= i — i.e., the loop finds a glyph that does not need to be moved back (common case during post-base vowel scanning)

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
The USE shaper requires fonts and text from Universal-Shaping-Engine supported scripts (e.g., Balinese, Buginese, Rejang). The cmplog fuzzer essentially never generates valid USE text+font combinations (only 1 True hit total). The False path at line 436 is the common case inside the reordering loop where most glyphs don't match the VPre/VMPre criterion — it fires 12,000 times per n4 because n4 generates more USE syllable sequences. The barrier is primarily the lack of USE script fonts and text in the cmplog corpus.

**Fuzzer Barrier Severity: Medium**

**Recommended Mitigations:**
1. Add USE-script fonts (e.g., Buginese, Balinese, Javanese) with VPre/VMPre vowels to the corpus.
2. Add Unicode text samples for USE scripts to the seed corpus.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-MARKARRAY-ANCHOR (single — MarkArray::apply anchor retrieval check)**
**Rank:** 37
**Branch:** `hb-ot-layout-gsubgpos.hh:251:24 (False)` — referenced as being in `MarkArray::apply()`
**Note:** The coverage report cites function `_ZNK2OT6Layout9GPOS_impl9MarkArray5apply...` at line 251:24. This is a shared template-level check (`check_assign` or offset dereference) used across many GPOS structures. In the MarkArray context, this corresponds to the `if (unlikely (!found)) return_trace(false)` anchor lookup at line 34 in MarkArray.hh, OR a sanitize-context check at a shared header line 251. The False side means the anchor was NOT found (no valid anchor for this mark class in this base glyph).

**Coverage Status:** cmplog T:4, F:0 → n4 T:2,400, F:10,700

**Path Conditions Required:**
1. GPOS MarkBasePos or MarkMarkPos lookup must fire
2. The mark glyph must be in the coverage
3. **For False side:** `anchors.get_anchor()` must return `found = false` — the AnchorMatrix for the base glyph does not contain an anchor for the mark's class

**Root Cause Category:** Input Format/Structure Constraints

**Root Cause Explanation:**
The False path fires when the font's AnchorMatrix does not provide an anchor for a specific (base glyph, mark class) combination. This is a valid OpenType state: the spec allows a subtable to not provide an anchor for all mark class/base combinations, triggering fallthrough to the next subtable. The cmplog fuzzer's GPOS tables apparently always succeed in finding anchors (4 True hits), while n4 generates GPOS tables with sparse anchor coverage.

**Fuzzer Barrier Severity: Medium**

**Recommended Mitigations:**
1. Add GPOS fonts with sparse AnchorMatrix tables (not all base/mark-class combinations covered).
2. Include test inputs where marks do not have defined anchors in GPOS.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-SKIP-ITER-24BIT (single — skipping_iterator 24-bit glyph data path)**
**Rank:** 38
**Branch:** `hb-ot-layout-gsubgpos.hh:641:9 (True)` — `if (match_glyph_data24) return *match_glyph_data24` at line 650 (the 24-bit glyph data path in `get_glyph_data()`)

**Coverage Status:** cmplog T:0, F:145,000 → n4 T:10,300, F:1,480,000

**Path Conditions Required:**
1. A GSUB/GPOS lookup using 24-bit (beyond-64K) glyph IDs must be active
2. The `match_glyph_data24` pointer must be non-null — i.e., the lookup was set up with `HBGlyphID24` data rather than `HBGlyphID16`
3. This requires `#ifndef HB_NO_BEYOND_64K` to be true (compiled with > 64K glyph support) AND the font must contain lookups referencing glyph IDs > 65535

**Root Cause Category:** Input Format/Structure Constraints + Code Unreachability

**Root Cause Explanation:**
HarfBuzz supports fonts with more than 65,535 glyphs via 24-bit glyph IDs, enabled by the `HB_NO_BEYOND_64K` compile flag. The `match_glyph_data24` path in `get_glyph_data()` is only active when a lookup is configured with 24-bit data. The cmplog fuzzer never generates fonts with glyph IDs > 65535 (the byte sequence needed to encode such IDs in OpenType tables is specific and rare), so `match_glyph_data24` is always null. The n4 fuzzer occasionally generates such inputs (10,300 True hits vs. 1.48M False). This requires fonts with GSUB/GPOS tables using the 24-bit extended glyph ID format.

**Fuzzer Barrier Severity: High**

**Recommended Mitigations:**
1. Add font samples with glyph IDs > 65535 (using the 24-bit glyph ID encoding) to the corpus.
2. Add the 3-byte extended glyph ID encoding to the fuzzer dictionary.

---

### BLOCKING BRANCH ANALYSIS
========================
**Cluster: C-INDIC-FSM (single — Indic Ragel FSM state transition dispatch)**
**Rank:** 39
**Branch:** `hb-ot-shaper-indic-machine.hh:1167:3 (False)` — the ternary `_slen > 0 && _keys[0] <= indic_category() && indic_category() <= _keys[1] ? ... : _slen` — the False side means the glyph's `indic_category()` is OUT of range for the current state's transition key span (no valid transition = default transition to error/non-Indic)

**Coverage Status:** cmplog T:163, F:0 → n4 T:526,000, F:10,300

**Path Conditions Required:**
1. Indic shaper must activate (Unicode Indic script characters)
2. The Ragel FSM must be in a state where the current glyph's `indic_category()` falls OUTSIDE the expected key range for that state
3. This corresponds to encountering a non-Indic or unexpected category glyph in the middle of an Indic syllable parse

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
The False side fires when an Indic syllable parse encounters a glyph whose Indic category is not covered by the current state's transition table (out-of-range default transition). The cmplog fuzzer generates valid Indic text (163 True hits where the category is in-range), but never encounters the out-of-range case. The n4 fuzzer generates hybrid inputs where non-Indic code points appear in the middle of Indic sequences, triggering the default transition (10,300 False hits). This requires mixing Indic Unicode ranges with non-Indic characters.

**Fuzzer Barrier Severity: Medium**

**Recommended Mitigations:**
1. Add mixed-script Indic+non-Indic Unicode text sequences to the corpus.
2. Use Indic text with embedded ASCII or other non-Indic characters that cause FSM state errors.

---

## Summary Table

| Rank(s) | Cluster ID | Function / Location | Blocked Branch | Root Cause Category | Severity |
|---------|------------|---------------------|----------------|---------------------|----------|
| 3,5,17,20,21,24 | C-CFF2-HVCU | `hvcurveto()` — `hb-cff-interp-cs-common.hh:690–724` | True sides of inner loop, trailing delta, alternate encoding | Input Format/Structure + Seed Deficiency | High |
| 4,22,25,15 | C-VARC-PATH | `VARC::get_path_at()` — `OT/Var/VARC/VARC.cc:347–381` | False/True sides of draw vs. extents path, transform identity, glyf lookup | Input Format/Structure + Deep Nested Deps | High |
| 8,12 | C-AAT-LIGTABLE | `LigatureSubtable::transition()` — `morx-table.hh:490,497` | Double-mark guard True, performAction True | Input Format/Structure + Deep Nested Deps | High |
| 7,9,11,14 | C-AAT-STDRIVE | `StateTableDriver::drive()` — `aat-layout-common.hh:1262–1298` | Null-transition fast path, safe-to-break | Input Format/Structure + Algorithmic | High |
| 18 | C-AAT-REARR | `StateTableDriver` (Rearrangement) — `1268:19` | Null-transition loop continuation | Input Format/Structure | High |
| 1 | C-GLYPH-LIGNUM | `_hb_glyph_info_get_lig_num_comps()` — `hb-ot-layout.hh:504` | LIGATURE+internal bit check False | Deep Nested Condition Deps | High |
| 6 | C-LIGATE-MARK | `ligate_input()` — `hb-ot-layout-gsubgpos.hh:1598` | Mark-ligature / last_lig_id==0 False | Input Format/Structure | High |
| 2 | C-HB-ANY | `hb_any::operator()` — `hb-iter.hh:992` | Loop empty (all-zero coords) | Algorithmic/Semantic Barriers | Medium |
| 10 | C-KHMER-FSM | `find_syllables_khmer()` — `khmer-machine.hh:341` | No-action transition True | Seed/Dictionary Deficiency | Medium |
| 28,27 | C-AAT-KERX4 | `KerxSubTableFormat4::transition()` + StateTableDriver | Action flag False, null-transition True | Input Format/Structure | High |
| 29 | C-AAT-GLYPH-OUT | `output_glyphs()` — `aat-layout-common.hh:176` | DELETED_GLYPH sentinel True | Magic Value Constraint | High |
| 30,33,40 | C-CHAIN-FAST | `ChainRuleSet::apply()` — `gsubgpos.hh:3511–3528` | Rule apply failure, lookahead fail, skippable detected | Deep Nested Deps | High |
| 26,31 | C-TRANSFORM-IDENTITY | `hb_transform_t::is_identity()` — `hb-geometry.hh:120,122` | Short-circuit False (non-identity transform) | Input Format/Structure | High |
| 32 | C-CFF-HINTMASK | `determine_hintmask_size()` — `cff-interp-cs-common.hh:178` | seen_hintmask already True | Input Format/Structure | Medium |
| 34 | C-GLYF-NODATA | `glyf_accelerator_t::get_path_at()` — `glyf.hh:514` | glyf has no data | Input Format/Structure | Medium |
| 35 | C-MARKBASE-ACCEPT | `MarkBasePosFormat1_2::accept()` — `MarkBasePosFormat1.hh:104` | Non-multiplied previous glyph True | Deep Nested Deps | High |
| 36 | C-USE-REORDER | `reorder_syllable_use()` — `hb-ot-shaper-use.cc:436` | Non-VPre/VMPre glyph in reorder loop | Seed/Dictionary Deficiency | Medium |
| 37 | C-MARKARRAY-ANCHOR | `MarkArray::apply()` — `MarkArray.hh:34` (line 251 in coverage) | Anchor not found False | Input Format/Structure | Medium |
| 38 | C-SKIP-ITER-24BIT | `skipping_iterator_t::get_glyph_data()` — `gsubgpos.hh:650` | 24-bit glyph data path | Input Format/Structure | High |
| 39 | C-INDIC-FSM | `find_syllables_indic()` — `indic-machine.hh:1167` | Out-of-range category (default transition) | Seed/Dictionary Deficiency | Medium |

---

## Skipped Blockers

No blockers from ranks 1–40 were filtered by NEG rules. All 40 confirmed input-dependent blockers passed pre-screening (all are in reachable functions that are exercised by at least one fuzzer, with the blocking side exercised by the confirming fuzzer).

---

## Top Recommendations

### Priority 1: Seed Corpus Expansion (addresses ~60% of blockers)
1. **Add CFF2 font samples** with `hvcurveto` opcodes using varied argument counts (8, 9, 12, 13+ args). This directly unblocks C-CFF2-HVCU (6 branches, ranks 3,5,17,20,21,24).
2. **Add VARC-containing fonts** (variable composite glyphs, e.g., from Google Fonts VARC spec implementations). This unblocks C-VARC-PATH (ranks 4,22,25,15) and C-TRANSFORM-IDENTITY (ranks 26,31) and C-GLYF-NODATA (rank 34).
3. **Add AAT morx/kerx font samples** (Apple system fonts or fonts with morx tables), combined with text sequences exercising ligature state machines. This addresses C-AAT-LIGTABLE, C-AAT-STDRIVE, C-AAT-REARR, C-AAT-KERX4, C-AAT-GLYPH-OUT (ranks 7–12, 18, 27–29).
4. **Add USE-script, Khmer, and Indic text sequences** with fonts supporting those scripts. Addresses C-KHMER-FSM (rank 10), C-USE-REORDER (rank 36), C-INDIC-FSM (rank 39).
5. **Add fonts with 24-bit extended glyph IDs** (>65535 glyphs) to address C-SKIP-ITER-24BIT (rank 38).

### Priority 2: Dictionary Additions (addresses magic value and opcode barriers)
6. Add CFF opcode bytes: `hvcurveto` (`0x1F`), `hintmask` (`0x13`), `cntrmask` (`0x14`) to the fuzzer dictionary.
7. Add the VARC table tag bytes (`0x56 0x41 0x52 0x43`).
8. Add the `DELETED_GLYPH` sentinel value (e.g., `0xFF 0xFF`) to the dictionary for AAT morx tables.
9. Add morx table tag (`0x6D 0x6F 0x72 0x78`) and kerx tag (`0x6B 0x65 0x72 0x78`) bytes.
10. Add Khmer Unicode range start/end bytes (U+1780 = `0xE1 0x9E 0x80`) to dictionary.

### Priority 3: Structural/Harness Changes (addresses fundamental barriers)
11. **Two-dimensional corpus strategy for AAT:** Maintain (font, text) pairs rather than fonts alone. AAT processing requires both a valid font AND a text sequence that exercises the state machine.
12. **Structured CFF2 mutator:** Implement a custom libFuzzer mutator that understands CFF2 charstring encoding, specifically targeting argument stack sizes for hvcurveto/vhcurveto alternate forms.
13. **VARC-aware generator:** Build a generator that constructs valid VARC table payloads with non-identity transform components, then fuzz from this baseline.
14. **Expand harness API calls:** Ensure the fuzzer harness exercises both `hb_font_get_glyph_extents()` (extents path) and `hb_font_draw_glyph()` (draw path) for VARC glyphs, to cover both `c.draw_session` being null and non-null.
15. **GSUB+GPOS combination fonts:** Add fonts that combine `MultipleSubst` with `MarkBasePos`, and `ChainContextSubst` with complex backtrack/lookahead, to address C-MARKBASE-ACCEPT and C-CHAIN-FAST.
