---
name: htslib project context
description: Key patterns, entry points, and blocker findings for the htslib fuzzing campaign
type: project
---

Fuzzer entry point is `LLVMFuzzerTestOneInput` in `test/fuzz/hts_open_fuzzer.c`.
Input is wrapped in an in-memory hFILE via `hopen("mem:", ...)`, opened with
`hts_hopen`, format-detected, then routed to `view_sam` (SAM/BAM/CRAM) or
`view_vcf` (VCF/BCF).

**Why:** This context is needed to trace execution paths for all blocking
branches — format detection is the first gate every input must pass.

**How to apply:** When analyzing htslib blockers, start at format detection in
`hts_hopen` and note whether the input category is `sequence_data` or
`variant_data`. Only those two categories exercise the SAM/CRAM/VCF code paths.

## Key validation patterns / barriers

- CRAM magic bytes: `CRAM` (0x43 0x52 0x41 0x4D). Must appear at byte 0 for
  format detection to classify input as CRAM.
- SAM header gate: `sam_hrecs_parse_single_line` (header.c:562) requires `@`
  prefix, two valid alpha type chars, valid type keyword (@HD/@SQ/@RG/@PG/@CO),
  and parseable key=value tags. Without this, `pool_alloc` is never called and
  `pool_destroy` iterates zero times.
- Log-level enum gap: `HTS_LOG_WARNING = 3` (not 2). Value 2 is unused.
  Default `hts_verbose = HTS_LOG_WARNING (3)`. All error-only inputs hit only
  `HTS_LOG_ERROR = 1` in `get_severity_tag`.
- `cram_read_container` uses `calloc` — so `c->stats[]` is all NULL.
  Only `cram_new_container` (encoder path) populates `stats[]` via
  `cram_stats_create()`. The decoder path always produces stats-null containers.

## Blocking branch findings (2026-03-17 campaign, top-5)

| Rank | Branch | File | Line | Root Cause |
|------|--------|------|------|------------|
| 1 | cram_free_container False (stats[id]) | cram/cram_io.c | 3747 | CRAM encoder path never reached; cram_new_container never called; requires real CRAM seed |
| 2 | ks_resize False (s->m >= size) | htslib/kstring.h:162 (in header.c) | 162 | Buffer reuse never occurs; requires 2+ valid SAM header lines in one input |
| 3 | get_severity_tag False (HTS_LOG_ERROR case fall-through) | hts.c | 5123 | WARNING-level log never triggered; requires partially-valid SAM with soft error |
| 4 | get_severity_tag True (HTS_LOG_WARNING case match) | hts.c | 5125 | Symmetric to Blocker 3; same fix |
| 5 | pool_destroy loop True (npools>0) | cram/pooled_alloc.c | 87 | pool_alloc never called; sam_hrecs_parse_single_line never succeeds; requires valid @-header |

## Coverage tool note

The llvm-cov annotator labels functions by the nearest preceding function label
in the output. Lines 5123/5125 are annotated as `get_severity_tag` in the
coverage file (the switch cases in that function), even though the compiled
source has the function starting at line 5165. The instrumented binary was
built from a slightly earlier source snapshot — the logic is identical.

## Effective mitigations (recommended, in order of impact)

1. Add SAM seed with duplicate SQ for WARNING trigger — unblocks Blockers 2, 3, 4, 5:
   `@HD\tVN:1.6\n@SQ\tSN:chr1\tLN:1000\n@SQ\tSN:chr1\tLN:2000\n`
2. Add real CRAM seed file (one record) — unblocks Blocker 1.
3. Dictionary: `CRAM`, `@HD`, `@SQ`, `@RG`, `@PG`, `@CO`, `VN:1.6`, `SN:`, `LN:`.
