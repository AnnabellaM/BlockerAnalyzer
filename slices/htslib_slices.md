# Program Slices — htslib
**Generated:** 2026-03-19
**Source:** `blockers/htslib_blockers.md`
**Mode:** Dynamic slice (nodes filtered to non-zero hit count in at least one fuzzer)
**Ranks processed:** 1–1  (1 passed NEG screening, 0 skipped)

---

## Slice 1

**Key:** `cram_free_container|3747:13`
**Function:** `cram_free_container`
**Blocked side:** False
**Flip strength:** 138,000
**Source line:** `if (c->stats[id]) cram_stats_free(c->stats[id]);`

### Program Slice

```
ENTRY  targets/htslib/test/fuzz/hts_open_fuzzer.c:171   int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)                               [cmplog: 5,120 | n4: 2,010]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:186   htsFile *hts_hopen(hFILE *hfile, const char *fn, const char *mode)                         [cmplog: 5,120 | n4: 2,010]
DATA   targets/htslib/test/fuzz/hts_open_fuzzer.c:193   int ftype = ht_file->format.category                                    [feeds=switch(ftype)] [cmplog: 3,860 | n4: 1,940]
CTRL   targets/htslib/test/fuzz/hts_open_fuzzer.c:200   case sequence_data                                                           [must=True]       [cmplog: 3,630 | n4: 1,830]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:203   void view_sam(const uint8_t *data, size_t size, char *mode, int close_abort)                  [cmplog: 3,630 | n4: 1,830]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:60    htsFile *hts_hopen(hFILE *hfile, const char *fn, const char *mode)                         [cmplog: 10,800 | n4: 5,490]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:67    samFile *sam_open(const char *fn, const char *mode)                                        [cmplog: 10,800 | n4: 5,490]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:86    sam_hdr_t *sam_hdr_read(htsFile *fp)                                                       [cmplog: 10,800 | n4: 5,490]
CTRL   targets/htslib/test/fuzz/hts_open_fuzzer.c:87    hdr == NULL → return                                                         [must=False]      [cmplog: 10,600 | n4: 5,490]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:99    int sam_hdr_write(htsFile *fp, const sam_hdr_t *h)                                         [cmplog: 10,600 | n4: 5,490]
CTRL   targets/htslib/test/fuzz/hts_open_fuzzer.c:99    sam_hdr_write(out, hdr) != 0 → goto err                                     [must=False]      [cmplog: 9,650 | n4: 5,490]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:106   int sam_read1(htsFile *in, sam_hdr_t *h, bam1_t *b)                                        [cmplog: 26,200 | n4: 200,000]
CTRL   targets/htslib/test/fuzz/hts_open_fuzzer.c:106   sam_read1(in, hdr, b) >= 0 — loop body executes                            [must=True]       [cmplog: 16,700 | n4: 195,000]
CALL   targets/htslib/test/fuzz/hts_open_fuzzer.c:107   int sam_write1(htsFile *fp, const sam_hdr_t *h, const bam1_t *b)                           [cmplog: 16,700 | n4: 195,000]
CALL   targets/htslib/sam.c:4559                         int cram_put_bam_seq(cram_fd *fd, bam_seq_t *b)                                             [cmplog: 5,370 | n4: 65,100]
CTRL   targets/htslib/cram/cram_encode.c:4005            !fd->ctr — True on first call, allocates new container                      [must=True]       [cmplog: 1,700 | n4: 1,770]
CALL   targets/htslib/cram/cram_encode.c:4006            cram_container *cram_new_container(int nrec, int nslice)                                    [cmplog: 1,700 | n4: 1,770]
DATA   targets/htslib/cram/cram_io.c:3682                c->stats[id] = cram_stats_create()                                         [feeds=c->stats[id]] [cmplog: 118,000 | n4: 101,000]
CALL   targets/htslib/cram/cram_io.c:5626                void cram_free_container(cram_container *c)                                                 [cmplog: 9,160 | n4: 3,600]  ← divergence
BRANCH targets/htslib/cram/cram_io.c:3747:13             if (c->stats[id]) cram_stats_free(c->stats[id])                            [blocked=False]   [cmplog: T:118k F:138k | n4: T:101k F:0]
```

**Divergence point:** `CALL cram_free_container` at `cram/cram_io.c:5626` — cmplog: 9,160 calls, n4: 3,600 calls. cmplog calls `cram_free_container` ~2.5× more than n4. The extra ~5,000 cmplog calls originate from the **decoder path** (`cram_read_container` → `cram_first_slice` / `cram_dopen` read-header loop), which zero-initializes `stats[]` via `calloc` — leaving all 28 entries NULL. The False branch fires 28 times per decoder container (138,000 / ~5,000 ≈ 28, matching `DS_TN − DS_RN`). n4 never triggers CRAM format detection for the input read, so `cram_read_container` is never called and every `cram_free_container` call comes only from the encoder path with fully-initialized stats.

### Key Variables

| Variable | Type | Role |
|----------|------|------|
| `c` | `cram_container *` | Container being freed; stats[] state depends on which constructor was used |
| `c->stats[id]` | `cram_stats *[DS_END]` | Per-data-series statistics; non-NULL when created by `cram_new_container`, NULL when created by `cram_read_container` (zero from calloc) |
| `id` | `enum cram_DS_ID` | Loop variable over `DS_RN..DS_TN` (28 data series IDs) |
| `fd->ctr` | `cram_container *` | Active write container on `cram_fd`; freed in `cram_close` |
| `ftype` | `int (hts_fmt_option)` | Format category of input; must be `sequence_data` to reach CRAM write path |

### Path Conditions

1. `hts_hopen(memfile, "data", "rb")` returns non-NULL (input passes format detection)
2. `ht_file->format.category == sequence_data` (input is SAM/BAM/CRAM)
3. `view_sam(data, size, "wc", 0)` is entered — CRAM write path
4. `sam_hdr_read(in)` returns non-NULL (header parsed successfully)
5. `sam_hdr_write(out, hdr)` returns 0 (success)
6. `sam_read1` loop body executes at least once
7. `fp->format.format == cram` in `sam_write1` (output opened with mode `"wc"`)
8. `fd->ctr == NULL` on first `cram_put_bam_seq` call → `cram_new_container` allocates container with all `stats[id]` non-NULL
9. **For False branch (cmplog only):** input must trigger CRAM format detection → `cram_read_container` called → container with NULL `stats[]` → `cram_free_container` hits False side 28× per container
