---
name: htslib project context
description: Key patterns, entry points, and blocker findings for the htslib fuzzing campaign (updated 2026-03-18 — top-40 analysis)
type: project
---

Fuzzer entry point is `LLVMFuzzerTestOneInput` in `test/fuzz/hts_open_fuzzer.c`.
Input is wrapped in an in-memory hFILE via `hopen("mem:", ...)`, opened with
`hts_hopen`, format-detected, then routed to `view_sam` (SAM/BAM/CRAM) or
`view_vcf` (VCF/BCF). The harness also calls `sam_hdr_count_lines(hdr, "SQ")`
after `sam_hdr_read`, which forces `sam_hdr_fill_hrecs` to run lazily.

**Why:** This context is needed to trace execution paths for all blocking
branches — format detection is the first gate every input must pass.

**How to apply:** When analyzing htslib blockers, start at format detection in
`hts_hopen` and note whether the input category is `sequence_data` or
`variant_data`. Only those two categories exercise the SAM/CRAM/VCF code paths.

## Key validation patterns / barriers

- CRAM magic bytes: `CRAM` (0x43 0x52 0x41 0x4D) at bytes 0–3, then byte 4
  in [1,7] and byte 5 in [0,7]. Six-byte conjunction. ~2^-46 probability random.
- SAM header gate: `hts_detect_format2` (hts.c:693) requires s[0]=='@' AND
  one of `@HD\t`, `@SQ\t`, `@RG\t`, `@PG\t`, `@CO\t` at bytes 0–3.
  `@CO\t` is the last alternative (most obscure; separate dictionary token needed).
- BAM magic: `BAM\1` (4 bytes). Required to exercise bam_hdr_read path.
- Log-level enum gap: `HTS_LOG_WARNING = 3` (not 2). Value 2 is unused.
  Default `hts_verbose = HTS_LOG_WARNING (3)`. All error-only inputs hit only
  `HTS_LOG_ERROR = 1` in `get_severity_tag`. WARNING fires on duplicate @SQ LN.
- `cram_read_container` uses `calloc` — so `c->stats[]` is all NULL.
  Only `cram_new_container` (encoder path) populates `stats[]` via
  `cram_stats_create()`. The decoder path always produces stats-null containers.
- The False branch of `if (c->stats[id])` at `cram_io.c:3747` fires for decoder
  containers (NULL stats from calloc) and never for encoder containers (all non-NULL).
  The encoder partial-failure path does NOT reach line 3747: `cram_new_container`'s
  `err:` block (line 3693) frees `c` directly, never calling `cram_free_container`.
  Therefore, to exercise the False side, the fuzzer needs a CRAM-format input that
  exercises `cram_read_container` — not just any CRAM encoder activity.
- `SEQS_PER_SLICE = 10000` (cram_structs.h:87), `SLICE_PER_CNT = 1` (cram_structs.h:89).
  Container flush via `cram_next_container` requires 10,000 records per slice by default.
  Harness-level override: `cram_set_option(fd, CRAM_OPT_SEQS_PER_SLICE, 2)` reduces to 2.
- `sam_hdr_fill_hrecs` is the lazy-parse entrypoint for BAM headers. Its two
  guards (bh->target_name and bh->text) only fire for BAM inputs with non-empty
  reference lists and embedded SAM text respectively.
- `pool_destroy` loop (npools > 0) requires at least one successful call to
  `sam_hrecs_parse_single_line` → `pool_alloc` → `new_pool` (SAM path only).

## Line number offset note

The instrumented binary was built from a slightly earlier source snapshot (~42 lines
earlier). Coverage-file line numbers are offset from current source by about 42.
Example: get_severity_tag appears at 5123/5125 in coverage but 5165/5167 in source.
Logic is identical; use grep to locate functions by name rather than by line number.

## Blocking branch findings (top-20 analysis, 2026-03-18)

All top-20 blockers share one underlying theme: the n4 fuzzer has no CRAM, BAM,
or SAM seeds, so it never passes any of the three format-magic gates. This produces
a cascade of unreachable branches in every format-specific downstream function.

| Cluster | Ranks | Functions | Root Cause |
|---------|-------|-----------|------------|
| C03 | 1,11,12,13,20 | cram_free_container | CRAM magic gate; CRAM encoder fields never set |
| C02 | 7,8,9 | hts_hopen/sam_read1/sam_hdr_read | SAM @XX\t magic absent in n4 |
| C01 | 3,4 | get_severity_tag | WARNING-level log requires semi-valid SAM (dup @SQ LN) |
| C04 | 10,14,16 | sam_hdr_destroy | SAM/BAM format gates; ref_count/target_name/hrecs fields |
| C05 | 6,17 | sam_hdr_fill_hrecs | BAM magic + non-empty header text and reference list |
| C06 | 2 | ks_resize | SAM format gate (buffer reuse on 2nd header line) |
| C07 | 5 | pool_destroy | SAM format gate (pool never filled) |
| C08 | 15 | add_stub_ref_sq_lines | BAM/SAM with nref > 0 |
| C09 | 18 | sam_hdr_count_lines | BAM + malformed embedded @SQ (dup name triggers error) |
| C10 | 19 | hts_detect_format2 | @CO\t magic token specifically absent |

## Effective mitigations (ranked by # of blockers unblocked)

1. **SAM seed** (unblocks ranks 2,3,4,5,7,8,9,10,16,19 — 10 branches):
   ```
   @CO\tFuzzer seed comment
   @HD\tVN:1.6\tSO:unsorted
   @SQ\tSN:chr1\tLN:248956422
   @SQ\tSN:chr1\tLN:500000
   @RG\tID:rg1\tSM:sample1
   @PG\tID:prog1\tPN:tool\tVN:1.0
   read1\t0\tchr1\t100\t60\t10M\t*\t0\t0\tACGTACGTAC\tIIIIIIIIII
   ```
   Starts with @CO (rank 19), has duplicate @SQ LN (ranks 3,4), multi-line (rank 2),
   has @-lines (rank 5), SAM format (ranks 7,8,9,10,16).

2. **CRAM seed** (unblocks ranks 1,11,12,13,20 — 5 branches):
   Any real CRAM file. Generate: `samtools view -C -o minimal.cram minimal.bam`

3. **BAM seed** (unblocks ranks 6,14,15,17,18 — 5 branches):
   BAM file with n_targets>=1, l_text>0, and duplicate @SQ in embedded text.

4. **Dictionary tokens**: `CRAM`, `BAM\x01`, `@HD\t`, `@SQ\t`, `@RG\t`, `@PG\t`,
   `@CO\t`, `VN:1.6\t`, `SN:`, `LN:`.

## Blocking branch findings (ranks 21–40 analysis, 2026-03-18)

Ranks 21–40 continue the same underlying theme: n4 format-magic gates dominate.
New secondary blockers appear in cmplog: aux field structure and CRAM encoder paths.

| Cluster | Ranks | Functions | Root Cause |
|---------|-------|-----------|------------|
| C11 | 24,33 | hts_detect_format2 | SAM @HD/@SQ/@RG/@PG sub-conditions absent in n4 (logical ||) |
| C12 | 29,30 | bam_hdr_write | BAM format gate + l_text>0 and n_targets>0 |
| C13 | 23,27 | refs_free (cram_io.c) | CRAM magic gate; h_meta populated / ref_id=NULL for no-@SQ CRAM |
| C14 | 21 | sam_hrecs_free | SAM format gate; hrecs->ref only non-NULL when @SQ lines present |
| C15 | 22 | sam_hrecs_rebuild_text | SAM format gate; False = hrecs hash populated |
| C16 | 25 | cram_dopen | CRAM magic gate (reader init path) |
| C17 | 26 | hts_detect_format2 | CRAM 6-byte magic conjunction (same as C03 detection side) |
| C18 | 28 | sam_hdr_update_target_arrays | SAM format gate + nref>0 |
| C19 | 31 | kstring.c:ks_resize | Buffer reuse timing (False = no realloc needed) |
| C20 | 32 | cram_free_block | CRAM format + NULL block pointer (partial/empty slice) |
| C21 | 34 | sam_format1_append | SAM format gate + aux tags in alignment records |
| C22 | 35 | hts_hopen | CRAM magic gate (cram_dopen null-check error path) |
| C23 | 36 | bam_aux_get | SAM format gate + aux tags in alignment records |
| C24 | 37 | cram_free_container | CRAM magic gate + CRAM encoder tags_used (encoder-only field) |
| C25 | 38 | refs_from_header | CRAM magic gate + sam_hdr_fill_hrecs failure (malformed CRAM header) |
| C26 | 39,40 | sam_hdr_write / view_sam | CRAM output mode ("wc") + cram_set_header2 failure |

## New patterns observed in ranks 21–40

- **Aux field barrier**: `sam_format1_append` (C21) and `bam_aux_get` (C23) both require
  alignment records with non-empty aux sections. Aux tags are a structured optional format
  (`XX:T:value`) that naive mutation rarely generates. Blocks ~17% of SAM records even in cmplog.
- **CRAM encoder vs decoder distinction**: `tags_used` and `stats[]` fields are only populated
  in the encoder path (`cram_new_container`). Decoder containers always have NULL/empty versions
  of these fields. CRAM inputs from real files (decoder path) cannot trigger these branches.
- **kstring reuse**: The False branch of `ks_resize` fires only when a kstring is reused
  without being freed — persistent-mode fuzzing strongly increases this.
- **CRAM output mode**: Harness uses mode "wc" in some call variants. `sam_hdr_write`'s
  CRAM arm only fires for `out` opened as CRAM. Verify the harness rotates through all output modes.

## Extended effective mitigations (ranks 21–40 additions)

5. **SAM seed with aux tags** (unblocks C11, C14, C15, C18, C21, C23 — 7+ branches):
   ```
   @SQ\tSN:chr1\tLN:248956422
   @RG\tID:rg1\tSM:sample1
   @PG\tID:bwa\tPN:bwa\tVN:0.7.17
   read1\t0\tchr1\t1\t60\t10M\t*\t0\t0\tACGTACGTAC\tIIIIIIIIII\tNM:i:0\tRG:Z:rg1
   ```

6. **CRAM seed with aux tags** (unblocks C16, C17, C22, C24, C25 — 6+ branches):
   Real CRAM produced by BWA MEM (includes NM, MD, RG aux tags in alignment records).

7. **No-@SQ CRAM seed** (unblocks C13 rank 27 False — 1 branch):
   CRAM with only unmapped reads, no @SQ header lines → ref_id stays NULL.

8. **Extended dictionary tokens**: `NM:i:`, `RG:Z:`, `MD:Z:`, `AS:i:`, `CRAM\x03\x01`.
