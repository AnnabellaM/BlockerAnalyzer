# Fuzzing Root Cause Analysis — htslib
**Generated:** 2026-03-19
**Ranks analyzed:** 1–1
**Slices file:** `slices/htslib_slices.md`
**Mode:** Dynamic slice (non-zero hitcount nodes only; divergence point pre-identified)

---

BLOCKING BRANCH ANALYSIS
========================
Cluster: C01
Role: cluster-root
Members: (single-member cluster; no downstream or peer blockers in this batch)

Branches:
  targets/htslib/cram/cram_io.c:3747:13 (blocked side: False)

Location: `cram_free_container` in `cram/cram_io.c`
Branch Condition: `if (c->stats[id])` — loop over `id` in `[DS_RN, DS_TN)` (28 iterations per call)
Coverage Status:
  cmplog: True = 118,000 hits, False = 138,000 hits  (both sides reached)
  n4:     True = 101,000 hits, False = 0 hits         (False side never reached)

Program Slice (entry → blocking branch):

  [ENTRY]  int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
                                                        (hts_open_fuzzer.c:171)
  [CALL]   htsFile *hts_hopen(hFILE *hfile, const char *fn, const char *mode)
           — format detection; sets ht_file->format.category              (hts_open_fuzzer.c:186)
  [DATA]   int ftype = ht_file->format.category   [feeds=switch(ftype)]
           [cmplog: 3,860 | n4: 1,940]                                    (hts_open_fuzzer.c:193)
  [CTRL]   case sequence_data  →  must be True
           [cmplog: 3,630 | n4: 1,830]                                    (hts_open_fuzzer.c:200)
  [CALL]   void view_sam(const uint8_t *data, size_t size, char *mode, int close_abort)
           — invoked with mode "wc" (CRAM output)
           [cmplog: 3,630 | n4: 1,830]                                    (hts_open_fuzzer.c:203)
  [CALL]   htsFile *hts_hopen(hFILE *hfile, const char *fn, const char *mode)
           — reopens input as SAM/BAM/CRAM reader
           [cmplog: 10,800 | n4: 5,490]                                   (hts_open_fuzzer.c:60)
  [CALL]   samFile *sam_open(const char *fn, const char *mode)
           — opens /dev/null as CRAM writer (mode "wc")
           [cmplog: 10,800 | n4: 5,490]                                   (hts_open_fuzzer.c:67)
  [CALL]   sam_hdr_t *sam_hdr_read(htsFile *fp)
           [cmplog: 10,800 | n4: 5,490]                                   (hts_open_fuzzer.c:86)
  [CTRL]   hdr == NULL  →  must be False (non-NULL header required)
           [cmplog: 10,600 | n4: 5,490]                                   (hts_open_fuzzer.c:87)
  [CALL]   int sam_hdr_write(htsFile *fp, const sam_hdr_t *h)
           [cmplog: 10,600 | n4: 5,490]                                   (hts_open_fuzzer.c:99)
  [CTRL]   sam_hdr_write(out, hdr) != 0  →  must be False (success)
           [cmplog: 9,650 | n4: 5,490]                                    (hts_open_fuzzer.c:99)
  [CALL]   int sam_read1(htsFile *in, sam_hdr_t *h, bam1_t *b)
           — loop; executes at least once
           [cmplog: 26,200 | n4: 200,000]                                 (hts_open_fuzzer.c:106)
  [CTRL]   sam_read1(in, hdr, b) >= 0  →  must be True (loop body entered)
           [cmplog: 16,700 | n4: 195,000]                                 (hts_open_fuzzer.c:106)
  [CALL]   int sam_write1(htsFile *fp, const sam_hdr_t *h, const bam1_t *b)
           [cmplog: 16,700 | n4: 195,000]                                 (hts_open_fuzzer.c:107)
  [CALL]   int cram_put_bam_seq(cram_fd *fd, bam_seq_t *b)
           — triggered when fp->format.format == cram
           [cmplog: 5,370 | n4: 65,100]                                   (sam.c:4559)
  [CTRL]   !fd->ctr  →  must be True on first call (allocates new container)
           [cmplog: 1,700 | n4: 1,770]                                    (cram_encode.c:4005)
  [CALL]   cram_container *cram_new_container(int nrec, int nslice)
           — populates stats[DS_RN..DS_TN) via cram_stats_create()
           [cmplog: 1,700 | n4: 1,770]                                    (cram_encode.c:4006)
  [DATA]   c->stats[id] = cram_stats_create()   [feeds=c->stats[id]]
           — all 28 entries non-NULL after encoder construction
           [cmplog: 118,000 | n4: 101,000]                                (cram_io.c:3682)
  [CALL]   void cram_free_container(cram_container *c)
           ← DIVERGENCE POINT: cmplog 9,160 calls, n4 3,600 calls
           — cmplog calls this ~2.5× more than n4 because of additional
             decoder-path invocations (cram_read_container)
           [cmplog: 9,160 | n4: 3,600]                                    (cram_io.c:5626)
  [BRANCH] if (c->stats[id]) cram_stats_free(c->stats[id])   → BLOCKER (False unvisited in n4)
           [cmplog: T:118k F:138k | n4: T:101k F:0]                      (cram_io.c:3747:13)

  Type context:
    c:              cram_container *
    c->stats:       cram_stats *[DS_END]   — array of 28 initialized by cram_new_container;
                    zero-filled (calloc) and never populated by cram_read_container
    id:             enum cram_DS_ID        — loop variable; range [DS_RN=11, DS_TN=39), 28 iters
    fd->ctr:        cram_container *       — active write container on cram_fd; freed in cram_close
    ftype:          int (hts_fmt_option)   — format.category; must be sequence_data (= 1)
    cram_new_container: cram_container *cram_new_container(int nrec, int nslice)
    cram_read_container: cram_container *cram_read_container(cram_fd *fd)
    cram_free_container: void cram_free_container(cram_container *c)

Path Conditions Required:
  1. `hts_hopen(memfile, "data", "rb")` succeeds — input passes initial format detection
  2. `ht_file->format.category == sequence_data` — input is SAM, BAM, or CRAM
  3. `view_sam(data, size, "wc", 0)` executes (mode "wc" = CRAM write arm)
  4. `sam_hdr_read(in)` returns non-NULL
  5. `sam_hdr_write(out, hdr)` returns 0 (success)
  6. `sam_read1` loop body executes at least once
  7. `fp->format.format == cram` in `sam_write1` (output file opened with mode "wc")
  8. `fd->ctr == NULL` on first `cram_put_bam_seq` call → `cram_new_container` allocates
     container; all 28 `stats[id]` entries are set to non-NULL via `cram_stats_create()`
  --- For the False branch (decoder path, cmplog only) ---
  9. Input must be a structurally valid CRAM file, triggering format detection as `cram`
  10. `cram_read_container` is called on the CRAM input — container allocated with `calloc`,
      leaving all `stats[]` entries NULL
  11. `cram_free_container` is called on this decoder container — loop hits NULL `stats[id]`,
      taking the False branch 28 times per decoder container freed

Root Cause Category: Input Format / Structure Constraints (CRAM Magic Value)

Root Cause Explanation:

  The False side of `if (c->stats[id])` at `cram_io.c:3747` is only reachable when
  `cram_free_container` is called with a container allocated by the CRAM decoder path
  (`cram_read_container`), not the encoder path (`cram_new_container`).

  The two allocation paths differ structurally:

  - `cram_new_container` (encoder, `cram_io.c:3644`): after allocating the container with
    `calloc`, it explicitly initializes every `stats[id]` slot for `id` in `[DS_RN, DS_TN)`
    by calling `cram_stats_create()` (line 3682). All 28 entries are non-NULL. When
    `cram_free_container` iterates this loop, `c->stats[id]` is always non-NULL → only the
    True branch fires.

  - `cram_read_container` (decoder, `cram_io.c:3793`): allocates the container with `calloc`
    (line 3883), copies the wire-format fields from a stack-local `c2` struct, and returns.
    It never calls `cram_stats_create()` — `stats[]` remains all-zero (NULL). When
    `cram_free_container` iterates this loop for a decoder container, `c->stats[id]` is
    always NULL → the False branch fires for all 28 iterations per container.

  The evidence from the dynamic slice supports this directly:
    - The `DATA` node at `cram_io.c:3682` (`c->stats[id] = cram_stats_create()`) has
      hitcounts [cmplog: 118,000 | n4: 101,000], showing that both fuzzers reach the encoder
      path's stats initialization.
    - The `CALL cram_free_container` divergence node has hitcounts [cmplog: 9,160 | n4: 3,600].
      cmplog calls the function ~2.5× more than n4. The extra ~5,560 cmplog invocations
      originate from the decoder path: `cram_read_container` is called by `cram_first_slice`
      and the `cram_dopen` read-header loop when the input is a structurally valid CRAM file.
      These decoder containers carry NULL `stats[]` and produce 28 False-branch hits each
      (138,000 False hits / ~5,000 decoder calls ≈ 27.6 ≈ 28 = DS_TN − DS_RN exactly).
    - n4 reaches `cram_free_container` 3,600 times, all via the encoder path (from
      `cram_close` freeing `fd->ctr` at line 5626). None of those containers are decoder
      containers, so the False branch is never hit.

  The root barrier is n4's corpus: it contains no CRAM-format input. CRAM detection
  requires a 6-byte conjunction at the start of the input (`hts.c:633`):
    - bytes 0–3: ASCII `CRAM` (0x43 0x52 0x41 0x4D)
    - byte 4:    version major in [1, 7]
    - byte 5:    version minor in [0, 7]
  Without this magic prefix the `hts_hopen` call at `hts_open_fuzzer.c:186` sets
  `format.category` to something other than `sequence_data`, the `switch` falls to
  `default`, and `view_sam` (including the CRAM read path) is never called. Consequently,
  `cram_read_container` is never invoked in n4, no decoder containers are ever created, and
  the False branch of `if (c->stats[id])` remains permanently at zero.

  Note that the False branch here is not dead code — it is the correct NULL-guard for
  decoder containers. There is no bug: the branch is intentionally designed to handle both
  constructor variants (encoder with non-NULL stats, decoder with NULL stats). It is purely
  unreachable for n4 because of the missing CRAM seed.

Fuzzer Barrier Severity: High
  The condition is structurally straightforward (NULL pointer guard), but reaching it requires
  a 6-byte magic-number conjunction that n4 is extremely unlikely to produce by mutation alone.
  The probability of random 6-byte alignment is approximately 2^-46. Once a real CRAM seed is
  added, the False branch becomes immediately and frequently reachable (as cmplog demonstrates
  with 138,000 hits). No code changes are needed.

Recommended Mitigations:
  1. Add a minimal CRAM seed file to n4's corpus. Generate one with:
       samtools view -C -T /dev/null -o minimal.cram minimal.bam
     Any syntactically valid CRAM file works. Copy it into the n4 queue directory
     (`fuzz/htslib_out/default/queue/`). This single action unblocks the False branch
     immediately (cmplog demonstrates 138,000 hits per run with its CRAM seeds).

  2. Add the CRAM magic token `CRAM` (4 bytes) to the AFL++ dictionary
     (`-x cram.dict`) so that mutation can splice it at offset 0. Combine with version
     bytes e.g. `\x03\x01` (CRAM v3.1) as a second dictionary entry `CRAM\x03\x01`.
     This helps even when no seed is present, though it is slower than a seed file.

  3. (Same-seed, broader impact) A single real CRAM file as seed also unblocks all other
     CRAM-gated blockers in this target (ranks 11, 12, 13, 20 in the previously analyzed
     top-20, and ranks 16, 17, 22, 24, 25 in ranks 21–40). A CRAM seed is the highest
     return-per-action mitigation across the entire n4 campaign.

---

## Summary Table

| Cluster | Location | Blocked Side | Root Cause Category | Severity | Key Fix |
|---------|----------|--------------|---------------------|----------|---------|
| C01 | `cram_free_container` @ `cram_io.c:3747` | False (`c->stats[id]` is NULL) | Input Format / Structure Constraints (CRAM Magic Value) | High | Add CRAM seed to n4 corpus |

---

## Top Recommendations

1. **Add a CRAM seed to n4's corpus** — unblocks C01 immediately and all other CRAM-gated
   blockers in the campaign (estimated 10+ additional branches across ranks 1–40). Highest
   return-per-action mitigation available. Command:
     `samtools view -C -T /dev/null -o seed.cram input.bam`

2. **Add CRAM magic dictionary token** — `CRAM\x03\x01` as a 6-byte AFL++ dictionary entry.
   Provides a fallback path if CRAM seeds are unavailable or for corpus diversification.

---

*(No blockers were skipped by NEG pre-screening for ranks 1–1.)*
