# n4 vs cmplog: Why the Same Corpus Produces Opposite Results on Different Barrier Types

**Date:** 2026-03-19
**Targets analyzed:** htslib rank 1, harfbuzz rank 1

---

## Observation

Both n4 and cmplog start from the same initial seed corpus, yet consistently diverge on two specific blockers:

| Target | Blocker | cmplog | n4 | Winner |
|--------|---------|--------|----|--------|
| htslib | `cram_free_container` False side — `c->stats[id] == NULL` | 138k False hits | 0 False hits | cmplog |
| harfbuzz | `_hb_glyph_info_get_lig_num_comps` False side — `IS_LIG_BASE == 0` | 0 False hits | 2.55M False hits | n4 |

---

## Root Cause: The Two Barrier Types Map to Opposite Fuzzer Strengths

### htslib — Magic value barrier, cmplog wins

The barrier is a 6-byte conjunction at the input boundary: bytes 0–5 must be `CRAM\x03\x01` for the input to be detected as a CRAM file by `hts_detect_format2`. Without CRAM-format input, the decoder path (`cram_read_container`) is never reached, and `c->stats[id]` is always non-NULL (set by the encoder path `cram_new_container`).

cmplog intercepts the `memcmp(buf, "CRAM", 4)` call, records the expected value, and splices it into the input (input-to-state correspondence / redqueen technique). This directly synthesizes valid CRAM headers. n4 has no comparison logging and cannot satisfy this ~2⁻⁴⁶ probabilistic barrier.

The divergence point in the dynamic slice is **upstream** (at `cram_free_container` call site — cmplog: 9,160 calls, n4: 3,600): the barrier is accessibility, not predicate satisfaction.

### harfbuzz — Structural/semantic barrier, n4 wins

The barrier is a single bit: `info->lig_props() & IS_LIG_BASE`. This bit is written exclusively by `_hb_glyph_info_set_lig_props_for_ligature()`, called only from `ligate_input()`. Reaching the False side requires a font where a glyph is classified as LIGATURE in GDEF's `GlyphClassDef` table, but has not been processed by a prior `ligate_input` call in the current shaping run — a cross-table structural relationship between GDEF and GSUB.

The divergence point in the dynamic slice is **at the branch itself** (both fuzzers: ~9k True hits for cmplog, ~2.58M True hits for n4): both fuzzers fully reach the predicate; only n4 satisfies it.

---

## Why cmplog's Redqueen Pass Destroys the harfbuzz Property

cmplog doesn't replace havoc mutations — it adds a redqueen pass on top. The redqueen pass replays an input with comparison instrumentation, identifies offsets where input bytes match one side of a comparison, and replaces them with the other side to satisfy the predicate.

For OpenType fonts, the bytes that appear in comparisons during GSUB/GDEF processing are glyph IDs, class values, coverage table offsets, and lookup indices — exactly the bytes that define the GDEF+GSUB relationship required for the harfbuzz False branch.

When cmplog's redqueen pass runs on a seed that has the right GDEF+GSUB structure, it finds comparisons against those bytes and replaces them with comparison-satisfying values. This is locally correct for those comparisons but globally wrong for the cross-table invariant — a glyph class value changed to satisfy one comparison may destroy the LIGATURE classification in GDEF that another code path depends on.

```
n4:      random mutation → coverage filter → structural property preserved by accident
cmplog:  random mutation → coverage filter  (same)
       + redqueen pass  → comparison filter → structural property systematically degraded
```

n4 has no oracle about what bytes to target. Its mutations are blind — some destroy the GDEF+GSUB relationship, some don't. The coverage feedback loop rewards the survivors, gradually accumulating seeds with the structural property intact. cmplog's redqueen pass introduces a directed mutation pressure toward bytes that are compared during font processing — degrading the cross-table invariant while solving local predicates.

The coverage feedback loop cannot compensate: the redqueen pass corrupts the structural property before the coverage check can "see" a seed that hits the False branch. cmplog never accumulates queue entries for that code path.

---

## General Principle

| Barrier type | Description | Where divergence appears in slice | Favored fuzzer |
|---|---|---|---|
| Magic value / format header | Specific byte sequence at input boundary; expressed as a direct comparison | Upstream — count gap at an early CALL/CTRL node | cmplog (comparison logging cracks it) |
| Structural / semantic invariant | Cross-table or multi-step property; not expressed as a single comparison | At the branch — both fuzzers reach the predicate | n4 (blind mutations + coverage feedback; redqueen can't help and may hurt) |

**The position of the divergence point in the dynamic slice is a proxy for barrier type**, and therefore a predictor of which fuzzer design advantage applies.

For complex structured binary formats (OpenType, ELF, CRAM), cmplog's comparison guidance is a local oracle: it knows what value a specific comparison expects but doesn't know that changing that value breaks a relationship several table-lookups away. In those cases, "uninformed" random mutation + coverage feedback can outperform "informed" comparison-guided mutation.

---
cmplog does both random mutations AND comparison-guided mutations

  cmplog isn't a replacement for havoc — it runs regular AFL++ havoc mutations plus an additional "redqueen" pass. In the
  redqueen pass, cmplog replays an input with comparison instrumentation enabled, finds every comparison where one operand
  matches bytes in the input, and tries replacing those bytes with the other operand. Then it checks if coverage increased.

  So cmplog should also benefit from the same coverage feedback loop as n4, on top of having comparison guidance. The
  question is: why doesn't it?

  The redqueen pass specifically targets the bytes that matter for cross-table consistency

  This is the key. In an OpenType font, the bytes that show up in comparisons during GSUB/GDEF processing are glyph IDs,
  class values, coverage table offsets, and lookup indices — exactly the bytes that define the GDEF+GSUB relationship the
  harfbuzz False branch depends on. When cmplog's redqueen pass fires on a font that has the right GDEF+GSUB structure, it
  looks at what the program is comparing and says: "at offset X, the program compared value 0x03 against 0x07, let me replace
   it with 0x07." That byte replacement satisfies one local comparison — but it may change a glyph class value or an offset
  that corrupts the cross-table consistency required for the False branch.

  n4 mutates those same bytes randomly, with no preference. Some mutations destroy the property, some don't — coverage
  feedback keeps the ones that don't. cmplog mutates those bytes directionally, toward satisfying whatever comparison the
  program happened to make — and that direction is locally correct for that comparison but globally wrong for the cross-table
   invariant.

  The asymmetry: what cmplog's guidance optimizes for

  n4:      random mutation → coverage filter → structural property preserved by accident
  cmplog:  random mutation → coverage filter  ← same thing
         + redqueen pass  → comparison filter → structural property systematically degraded

  The redqueen pass adds a second selection pressure that pushes mutations toward satisfying local comparisons. For htslib,
  that pressure aligns with the barrier (the barrier IS a comparison). For harfbuzz, that pressure works against the barrier
  — the barrier is a cross-table invariant that isn't directly expressed as a comparison cmplog can log.

  Why the coverage feedback loop doesn't save cmplog

  You might expect: even with the destructive redqueen mutations, the coverage feedback should select for inputs that reach
  the False branch and discard the ones that don't. But this requires that at least some inputs survive the redqueen pass
  with the structural property intact. The problem is that the redqueen pass runs on every interesting seed, including the
  ones that have the right GDEF+GSUB structure. The pass targets bytes that are compared during shaping — which include the
  glyph class and coverage table bytes — and replaces them with values that satisfy those comparisons. By the time the seed
  is saved back to the queue, the structural property has been overwritten. The coverage feedback loop never gets to "see" a
  surviving variant of that seed with the False branch hit, because the redqueen pass corrupts it before the coverage check.

  In short

  cmplog's comparison guidance is a local oracle: it knows what value a specific comparison expects, but it doesn't know that
   changing that value breaks a relationship three table-lookups away. n4 has no oracle — it mutates blindly — and that
  blindness is an advantage when the barrier requires maintaining a global structural invariant that isn't locally visible as
   a comparison.
