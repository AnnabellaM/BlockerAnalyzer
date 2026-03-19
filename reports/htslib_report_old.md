# Root Cause Analysis — htslib (Top 20 Blocking Branches)

**Analysis date:** 2026-03-18
**Analyst:** fuzzing-root-cause-analyzer
**Source:** `/home/miao/BlockerAnalyzer/targets/htslib/`
**Blockers source:** `/home/miao/BlockerAnalyzer/blockers/htslib_blockers.md` (ranks 1–20)
**Fuzzers:** AFL++ cmplog (primary), AFL++ n4 (confirming)
**Entry point:** `LLVMFuzzerTestOneInput` in `test/fuzz/hts_open_fuzzer.c`

---

## Cluster Decisions (Step 1.5)

The pre-computed clusters from `extract_blockers.py` were reviewed against source code.
Adjustments made:

| Decision | Ranks | Rationale |
|----------|-------|-----------|
| Merge ranks 3 + 4 → C01 (switch) | 3, 4 | Both are `case` arms in the same `switch (severity)` in `get_severity_tag` (hts.c:5167). Confirmed single switch. |
| Merge ranks 7 + 8 + 9 → C02 (switch) | 7, 8, 9 | All three are `case sam:` arms in three different format-dispatch switches. Same root cause: SAM format never produced by n4. Analyzed as one thematic cluster with per-function sub-notes. |
| Merge ranks 1 + 11 + 12 + 13 + 20 → C03 (chain) | 1, 11, 12, 13, 20 | All are NULL-guard `if (c->field)` checks inside `cram_free_container`. Shared cause: encoder-only fields are never populated by decoder path; n4 never reaches CRAM at all. |
| Merge ranks 10 + 14 + 16 → C04 (chain) | 10, 14, 16 | Three adjacent guards in `sam_hdr_destroy` on ref_count, target_name, and hrecs. All blocked for the same reason: n4 never produces SAM/BAM headers that populate these fields. |
| Merge ranks 6 + 17 → C05 (logical) | 6, 17 | Both are sequential guards in `sam_hdr_fill_hrecs` on bh->text/l_text and bh->target_name/n_targets. Blocked identically: n4 BAM inputs lack both text and target arrays. |
| Keep rank 2 → C06 (single) | 2 | `ks_resize` False path (buffer reuse). Standalone. |
| Keep rank 5 → C07 (single) | 5 | `pool_destroy` loop True. Standalone. |
| Keep rank 15 → C08 (single) | 15 | `add_stub_ref_sq_lines` loop True. Standalone. |
| Keep rank 18 → C09 (single) | 18 | `sam_hdr_count_lines` error-return guard. Standalone. |
| Keep rank 19 → C10 (single) | 19 | `hts_detect_format2` `@CO\t` magic. Standalone. |

---

## Skipped Blockers

No blockers in ranks 1–20 were eliminated by NEG rules. All 20 are reachable in principle
and blocked by analysable input-dependent constraints.

---

## Findings (ordered Critical → High)

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C03 (chain — NULL-guard checks in cram_free_container)
Branches:
  cram/cram_io.c:3720:9  False  (rank 20 — if (c->landmark))
  cram/cram_io.c:3723:9  False  (rank 13 — if (c->comp_hdr))
  cram/cram_io.c:3730:9  False  (rank 11 — if (c->slices))
  cram/cram_io.c:3747:13 False  (rank  1 — if (c->stats[id]))
  cram/cram_io.c:3751:9  False  (rank 12 — if (c->tags_used))
Location: cram_free_container() in cram/cram_io.c (lines 3710–3785)
Branch Condition: NULL-pointer guards — False arm means the field is NULL
  and the corresponding free/cleanup is skipped.
Coverage Status (blocked side is always False = "field is NULL"):
  Rank  1 (3747:13): cmplog T:118,000 F:138,000 | n4 T:101,000 F:0
  Rank 11 (3730:9 ): cmplog T:4,230   F:4,930   | n4 T:3,600   F:0
  Rank 12 (3751:9 ): cmplog T:4,230   F:4,930   | n4 T:3,600   F:0
  Rank 13 (3723:9 ): cmplog T:4,310   F:4,850   | n4 T:3,600   F:0
  Rank 20 (3720:9 ): cmplog T:6,510   F:2,650   | n4 T:3,600   F:0
  All five: True arm (field set, free it) reached by both fuzzers.
            False arm (field NULL, skip) reached only by cmplog, never by n4.
```

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → detects format == cram  (requires bytes 0–5 == "CRAM" + version)
  → view_sam(data, size, "wc", 0)     [CRAM write path]
      → hts_hopen(memfile, "data", "rb")
          → cram_dopen(hfile, "data", "r")
              → cram_read_file_def()   [consumes CRAM magic + header]
              → cram_read_SAM_hdr()
      → sam_hdr_read(in)
      → sam_write1(out, hdr, b)  loop
          → cram_encode_container(fd, ...)
              → cram_new_container()    [populates c->landmark, c->comp_hdr,
                                         c->slices, c->stats[], c->tags_used]
      → hts_close(out)
          → cram_close(fd)
              → cram_flush_container_mt(fd)
              → cram_free_container(c)   ← BLOCKING BRANCHES
                  False arm: field was never set → NULL
```

**Path Conditions Required:**
1. Input bytes 0–3 must equal `CRAM` (0x43 0x52 0x41 0x4D) — 4-byte magic prefix.
2. Byte 4 must be in [1,7] and byte 5 in [0,7] — CRAM version range check (hts.c:633).
3. Bytes 6–29: 4-byte big-endian SAM header length + header text (may be empty) — CRAM file definition.
4. The fuzzer must then produce a CRAM input that is minimal enough that some container
   fields are not populated (decoder path) while others are (produces the False arm).
5. Alternatively: the CRAM encoder path (view_sam with "wc" mode) creates a fully
   populated container; the decoder path may produce NULL fields.

**Root Cause Category:** Input Format / Structure Constraints (CRAM magic bytes);
                         Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
The five False arms fire when `cram_free_container` is called on a container where the
corresponding field was never initialized. This happens in two scenarios:
(a) CRAM decoder path: `cram_read_container` uses `calloc`, leaving fields NULL until
    they are explicitly populated from the bitstream. If the container body is absent or
    truncated, fields like `c->comp_hdr`, `c->slices`, `c->tags_used`, and `c->landmark`
    remain NULL.
(b) The stats[] array (rank 1, line 3747) is populated only by `cram_new_container`
    (encoder path, cram_io.c:3682) via `cram_stats_create()`. The decoder path never
    creates stats objects; the loop `for (id = DS_RN; id < DS_TN; id++)` always finds
    c->stats[id] == NULL.

The n4 fuzzer never produces any of these scenarios because it never produces an input
whose first 6 bytes satisfy the CRAM magic check:
```c
// hts.c:633
if (len >= 6 && memcmp(s,"CRAM",4) == 0 && s[4]>=1 && s[4]<=7 && s[5]<=7)
```
This five-part conjunction requires the specific ASCII string "CRAM" followed by two
constrained byte values. Without a CRAM seed, the probability of a random mutation
satisfying all six byte positions simultaneously is approximately 1 in 2^46 per trial.
Because n4 never classifies any input as `cram` format, it never calls `cram_dopen`,
never creates or reads a CRAM container, and `cram_free_container` is never called at all
by n4. All five False branches are permanently unreachable by n4.

The cmplog fuzzer has CRAM inputs in its corpus (flip strength 138,000 on rank 1) and
exercises both the encoder path (True arm: field set → free it) and decoder path with
partial data (False arm: field NULL → skip).

**Fuzzer Barrier Severity:** Critical
(Mathematically infeasible without targeted help — requires 4 exact magic bytes plus
two constrained version bytes; pure mutation from non-CRAM seeds cannot reach this)

**Recommended Mitigations:**
1. Add a minimal valid CRAM file to the n4 seed corpus. Even a 1-record CRAM file
   (e.g., created with `samtools view -C input.bam > minimal.cram`) unblocks all
   five branches simultaneously.
2. Add `CRAM` (4 bytes) as a dictionary token (AFL++ `-x` option).
3. Add version byte patterns: `\x01\x00`, `\x02\x01`, `\x03\x00` as 2-byte dictionary
   tokens to help n4 construct the magic+version prefix by splicing.
4. A structured mutator with CRAM format awareness would complement seed-based coverage.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C02 (switch — `case sam:` arm blocked in three dispatch functions)
Branches:
  hts.c:1583:5  True  (rank 7 — case sam: in hts_hopen format switch)
  sam.c:4394:9  True  (rank 8 — case sam: in sam_read1 format switch)
  sam.c:2207:5  True  (rank 9 — case sam: in sam_hdr_read format switch)
Location: hts_hopen() (hts.c:1571), sam_read1() (sam.c:4267),
          sam_hdr_read() (sam.c:1928)
Branch Condition: switch (fp->format.format) { case sam: ... }
Coverage Status (blocked side is always True = SAM format selected):
  Rank 7 (hts.c:1583:5 T): cmplog T:6,840  F:20,500 | n4 T:0  F:13,000
  Rank 8 (sam.c:4394:9 T): cmplog T:5,940  F:20,200 | n4 T:0  F:200,000
  Rank 9 (sam.c:2207:5 T): cmplog T:5,130  F:5,760  | n4 T:0  F:5,490
  All three: False arm (non-SAM format dispatch) heavily hit by n4;
             True arm (SAM format) completely absent in n4.
```

**Execution Path to Branch (representative — hts_hopen, rank 7):**
```
LLVMFuzzerTestOneInput
  → hts_hopen(memfile, "data", "rb")
      → hts_detect_format2(hfile, fn, &fp->format)   [hts.c:1489]
          → reads first bytes of input (up to ~512 bytes)
          → checks SAM header tokens (hts.c:693–696):
              s[0] == '@' AND one of:
                memcmp(s, "@HD\t", 4) == 0
                memcmp(s, "@SQ\t", 4) == 0
                memcmp(s, "@RG\t", 4) == 0
                memcmp(s, "@PG\t", 4) == 0
                memcmp(s, "@CO\t", 4) == 0
          → sets fp->format.format = sam
      → switch (fp->format.format) {
          case sam:   ← BLOCKED IN n4
            fp->fp.hfile = hfile;
          }
```

**Path Conditions Required:**
1. Input must begin with exactly one of: `@HD\t`, `@SQ\t`, `@RG\t`, `@PG\t`, or `@CO\t`
   (4-byte SAM header prefix with literal tab character as the 4th byte).
2. OR: input must parse as a tab-delimited SAM record with ≥11 columns (body-only SAM).
3. Once SAM format is detected, all three dispatch switches downstream see
   `fp->format.format == sam` and take the `case sam:` arm.

**Root Cause Category:** Input Format / Structure Constraints; Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
SAM format detection (hts.c:693) requires a 4-byte magic prefix of the form `@XX\t`
where `XX` is one of five specific two-letter tag codes. The n4 fuzzer has never produced
any input satisfying this pattern, so `fp->format.format` is never `sam`. All three
`case sam:` dispatch arms across `hts_hopen`, `sam_hdr_read`, and `sam_read1` are
unreachable by n4.

The asymmetry in False-arm counts (n4 hits 13,000–200,000 False occurrences) shows n4
reaches all three functions regularly with non-SAM inputs (BAM, unrecognized). The zero
True-arm count is not a depth problem — n4 reaches the switch — but a format-detection
gate problem upstream.

The cmplog fuzzer's compare-logging instrumentation records the byte comparisons in
`memcmp(s, "@HD\t", 4)` etc. and feeds them as mutation hints, allowing it to construct
SAM header prefixes and exercise the `case sam:` arm (flip strength 5,000–7,000).

**Fuzzer Barrier Severity:** High
(4-byte magic value with literal `@`, two specific alpha chars, and `\t`;
without a dictionary token, n4 has a ~1-in-2^32 chance per mutation trial)

**Recommended Mitigations:**
1. Add a minimal SAM seed to the n4 corpus:
   ```
   @HD\tVN:1.6\tSO:unsorted\n
   ```
   This 24-byte seed satisfies format detection and exercises the `case sam:` arm in all
   three functions simultaneously.
2. Add SAM header tokens to the AFL++ dictionary:
   `@HD\t`, `@SQ\t`, `@RG\t`, `@PG\t`, `@CO\t`, `VN:1.6\t`, `SN:`, `LN:`.
3. A SAM seed with actual alignment records (11 tab-separated fields after the header)
   additionally exercises `sam_read1`'s `case sam:` arm during the read loop.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C01 (switch — HTS_LOG_ERROR vs HTS_LOG_WARNING case arms)
Branches:
  hts.c:5123:5 (source: ~5168:5) False  (rank 3 — past HTS_LOG_ERROR case)
  hts.c:5125:5 (source: ~5170:5) True   (rank 4 — HTS_LOG_WARNING case match)
Location: get_severity_tag() in hts.c (lines 5165–5183 in source)
Branch Condition: switch (severity) with case HTS_LOG_ERROR / HTS_LOG_WARNING
Coverage Status:
  Rank 3 (5123:5 F): cmplog T:7,640   F:22,600 | n4 T:279   F:0
  Rank 4 (5125:5 T): cmplog T:22,600  F:7,640  | n4 T:0     F:279
  Interpretation: in n4, when get_severity_tag fires, severity is always
  HTS_LOG_ERROR (value 1 in enum); the WARNING arm (value 3) is never reached.
  In cmplog, WARNING fires 22,600 times vs ERROR 7,640 times.
```

**Code context (hts.c:5165–5183):**
```c
static char get_severity_tag(enum htsLogLevel severity)
{
    switch (severity) {
    case HTS_LOG_ERROR:        // value 1 — rank 3: False arm (fall-through past it)
        return 'E';
    case HTS_LOG_WARNING:      // value 3 — rank 4: True arm (match)
        return 'W';
    case HTS_LOG_INFO:         // value 4
        return 'I';
    case HTS_LOG_DEBUG:        // value 5
        return 'D';
    case HTS_LOG_TRACE:        // value 6
        return 'T';
    default:
        break;
    }
    return '*';
}
```
Note: value 2 is absent from the enum (gap between ERROR=1 and WARNING=3).

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → view_sam(...)
      → sam_hdr_read(in) / sam_hdr_parse / header processing
          → triggers hts_log(HTS_LOG_WARNING, context, fmt, ...)
              [only if a soft-validation anomaly is encountered]
              → hts_verbose check: WARNING (3) <= default hts_verbose (3) → pass
              → get_severity_tag(HTS_LOG_WARNING)  ← BLOCKED IN n4
                  case HTS_LOG_WARNING: return 'W';
```

**Path Conditions Required:**
1. `hts_log` must be called with `severity == HTS_LOG_WARNING` (enum value 3).
2. The call fires only for specific soft-validation conditions in header parsing, such as:
   - Duplicate `@SQ` line with conflicting `LN:` value (header.c:162 triggers a warning).
   - `@SQ` line missing a required tag.
   - Alignment record with a field value out of expected range but not fatal.
3. The input must be partially valid: valid enough for format detection and initial parsing
   to succeed (ERROR would fire only on hard parse failures), but containing one structural
   anomaly that triggers a WARNING-level diagnostic.

**Root Cause Category:** Deep Nested Condition Dependencies; Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**
`get_severity_tag` is called inside `hts_log` only when a log event fires at or below the
current verbosity threshold. n4's inputs produce only ERROR-level log events (hard parse
failures during SAM/header processing) or no log events at all. They never produce the
"semi-valid with one anomaly" inputs needed to trigger WARNING-level events.

The specific trigger most accessible to fuzzing is a duplicate `@SQ` entry with differing
`LN:` values (header.c:162: `if (tmp != -1 && tmp != len)`). This fires:
```c
hts_log_error("Header includes @SQ line ...");  // inside sam_hdr_fill_hrecs -> no, WARNING
```
Actually the warning is at: a second `@SQ SN:xxx LN:yyy` where the LN differs from the
first occurrence — `invLN = 1` is set and a warning is emitted at header.c after the
tag loop. The cmplog fuzzer has learned to produce such inputs (flip strength 22,600).

Additionally, the enum gap (no value 2) means a fuzzer numerically sweeping enum values
would jump from ERROR=1 to WARNING=3, skipping value 2 entirely. Without knowing the
exact enum value 3, a mutator relying on arithmetic mutations would miss WARNING.

**Fuzzer Barrier Severity:** High
(Requires a partially-valid SAM/BAM input with a specific structural anomaly;
the enum gap compounds the difficulty for numeric mutation strategies)

**Recommended Mitigations:**
1. Add a SAM seed specifically crafted to trigger a WARNING: duplicate `@SQ` with
   conflicting lengths:
   ```
   @HD\tVN:1.6\n@SQ\tSN:chr1\tLN:1000\n@SQ\tSN:chr1\tLN:2000\n
   ```
   This unblocks ranks 3 and 4 simultaneously.
2. Add `\x03` (the integer value of HTS_LOG_WARNING) as a dictionary byte if any code
   path passes the severity as a raw integer.
3. The C02 SAM seeds are a prerequisite (n4 must reach SAM parsing before WARNING can fire).

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C04 (chain — field-guard checks in sam_hdr_destroy)
Branches:
  sam.c:122:9  True   (rank 10 — if (bh->ref_count > 0))
  sam.c:127:9  True   (rank 16 — if (bh->target_name))
  sam.c:134:9  False  (rank 14 — if (bh->hrecs))
Location: sam_hdr_destroy() in sam.c (lines 117–140)
Branch Condition: guards on ref_count, target_name, and hrecs fields
Coverage Status:
  Rank 10 (122:9 T): cmplog T:5,050  F:15,300 | n4 T:0  F:7,330
  Rank 16 (127:9 T): cmplog T:3,590  F:11,700 | n4 T:0  F:7,330
  Rank 14 (134:9 F): cmplog T:11,100 F:4,220  | n4 T:7,330 F:0
  Rank 10 + 16 True: n4 never reaches destroy with a populated header.
  Rank 14 False: n4 always has hrecs set (SAM path); BAM path (hrecs=NULL)
                 is blocked.
```

**Code at sam_hdr_destroy (sam.c:117–140):**
```c
void sam_hdr_destroy(sam_hdr_t *bh) {
    int32_t i;
    if (bh == NULL) return;

    if (bh->ref_count > 0) {      // line 123 — rank 10 True BLOCKED in n4
        --bh->ref_count;           // decrement and return without freeing
        return;
    }
    if (bh->target_name) {         // line 128 — rank 16 True BLOCKED in n4
        for (i = 0; i < bh->n_targets; ++i)
            free(bh->target_name[i]);
        free(bh->target_name);
        free(bh->target_len);
    }
    free(bh->text);
    if (bh->hrecs)                  // line 135 — rank 14 False BLOCKED in n4
        sam_hrecs_free(bh->hrecs);
    if (bh->sdict)
        kh_destroy(s2i, (khash_t(s2i) *) bh->sdict);
    free(bh);
}
```

**Execution Paths:**

*Rank 10 True (ref_count > 0):*
```
LLVMFuzzerTestOneInput
  → view_sam(data, size, "w", 1)    [SAM format input]
      → sam_hdr_read(in)
          [SAM path: sam_hdr_create → sam_hdr_build_from_sam_file]
          → fp->bam_header->ref_count = 1    [sam.c:1915]
      → sam_hdr_destroy(hdr)        ← bh->ref_count == 1 → True arm
```

*Rank 16 True (target_name not NULL):*
```
  → sam_hdr_read(in) on a SAM/BAM input with @SQ lines
      → bh->target_name allocated  [via target array construction]
  → sam_hdr_destroy(hdr)           ← target_name set → True arm
```

*Rank 14 False (hrecs is NULL):*
```
  → sam_hdr_read(in) on a BAM input
      → bam_hdr_read() → produces header with hrecs == NULL
  → sam_hdr_destroy(hdr)           ← bh->hrecs == NULL → False arm (skip free)
```

**Path Conditions Required:**
- Rank 10: SAM format input (so ref_count is set to 1 by `sam_hdr_read`).
- Rank 16: SAM input with `@SQ` lines OR BAM input with reference entries.
- Rank 14: BAM input (so `bam_hdr_read` creates header without hrecs).

**Root Cause Category:** Input Format / Structure Constraints (SAM/BAM format gates)

**Root Cause Explanation:**
All three branches require format-specific behavior:
- Ranks 10 and 16 require SAM format: n4 never produces SAM inputs (blocked by C02's
  `@XX\t` gate), so `ref_count` and `target_name` are never set to their non-zero states.
- Rank 14 requires BAM format: n4 never produces BAM inputs (magic `BAM\1` gate), so
  `bam_hdr_read` is never called, and the only path to `sam_hdr_destroy` in n4 comes via
  the SAM/CRAM path which always populates `bh->hrecs` before destroy.

In practice, `sam_hdr_destroy` is called 7,330 times by n4 (False arm of rank 14), but
always with `bh->hrecs != NULL` (n4's SAM parse populates hrecs immediately via
`sam_hdr_create`) and always with `ref_count == 0` and `target_name == NULL`.

**Fuzzer Barrier Severity:** High

**Recommended Mitigations:**
1. SAM seeds (C02 mitigation) unblock ranks 10 and 16 directly.
2. A BAM seed with `BAM\1` magic unblocks rank 14 (hrecs=NULL from bam_hdr_read).
3. Add `BAM\1` to the AFL++ dictionary for the BAM magic prefix.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C05 (logical — sam_hdr_fill_hrecs input-field guards)
Branches:
  header.c:1134:9  True  (rank 17 —
    if (bh->target_name && bh->target_len && bh->n_targets > 0))
  header.c:1142:21 True  (rank  6 —
    if (bh->text && bh->l_text > 0))
Location: sam_hdr_fill_hrecs() in header.c (lines 1289–1321)
Branch Condition: guards on the presence of pre-existing target arrays and raw text
Coverage Status:
  Rank  6 (1142:21 T): cmplog T:7,260  F:3,420  | n4 T:0  F:1,830
  Rank 17 (1134:9  T): cmplog T:3,540  F:11,600 | n4 T:0  F:7,330
  n4 reaches the function (False arm hit) but neither True branch fires.
```

**Code at sam_hdr_fill_hrecs (header.c:1289–1321):**
```c
int sam_hdr_fill_hrecs(sam_hdr_t *bh) {
    sam_hrecs_t *hrecs = sam_hrecs_new();
    if (!hrecs) return -1;

    if (bh->target_name && bh->target_len && bh->n_targets > 0) { // line 1295 (rank 17)
        if (sam_hrecs_refs_from_targets_array(hrecs, bh) != 0) {
            sam_hrecs_free(hrecs);
            return -1;
        }
    }

    if (bh->text && bh->l_text > 0) {  // line 1303 (rank 6)
        if (sam_hrecs_parse_lines(hrecs, bh->text, bh->l_text) != 0) {
            sam_hrecs_free(hrecs);
            return -1;
        }
    }

    if (add_stub_ref_sq_lines(hrecs) < 0) { ...  }
    bh->hrecs = hrecs;
    ...
}
```

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → view_sam(...)
      → sam_hdr_read(in) on a BAM input  → hdr with hrecs==NULL
      → sam_hdr_count_lines(hdr, "SQ")   [harness line 97]
          → if (!bh->hrecs) sam_hdr_fill_hrecs(bh)  ← BLOCKING GUARDS HERE
              bh->target_name: NULL (n4 BAM inputs have no valid reference list)
              bh->text:        NULL (n4 BAM inputs have no embedded header text)
```

**Path Conditions Required:**
- Rank 17 True: BAM input where the binary header has `n_targets >= 1` (a 4-byte LE
  reference count field in the BAM header), causing `bam_hdr_read` to populate
  `bh->target_name` and `bh->target_len`.
- Rank 6 True: BAM input where the embedded SAM text section has `l_text > 0` (the
  4-byte LE text length field in the BAM header contains a non-zero value and is followed
  by that many bytes of SAM header text).
- n4 never produces BAM inputs (magic `BAM\1` gate), so neither condition is ever met.

**Root Cause Category:** Input Format / Structure Constraints (BAM magic + structured header)

**Root Cause Explanation:**
`sam_hdr_fill_hrecs` is called lazily when a header object was created without its
`hrecs` structure (the BAM path). For n4's execution flow: n4 reaches
`sam_hdr_fill_hrecs` via `sam_hdr_count_lines` (harness line 97), but only from SAM
format inputs where `bh->hrecs` was already set by `sam_hdr_create` — meaning the
`if (!bh->hrecs)` guard in `sam_hdr_count_lines` is False and `sam_hdr_fill_hrecs` is
skipped entirely. When n4 does somehow reach `sam_hdr_fill_hrecs` (via a BAM-like input
that fails early), `bh->target_name` and `bh->text` are NULL because the BAM header
parse never completed.

The cmplog fuzzer has BAM seeds with non-empty reference lists and embedded header text,
so it fires both True arms regularly (flip strength 7,260 and 3,540).

**Fuzzer Barrier Severity:** High

**Recommended Mitigations:**
1. A BAM seed with `BAM\1` magic + `n_targets >= 1` + non-empty `l_text` section
   unblocks both ranks simultaneously.
2. Add `BAM\1` to the dictionary; once BAM paths are entered, mutation will
   populate the reference-count and text-length fields.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C06 (single — ks_resize False: buffer already sufficient)
Branches:
  header.c (inlined ks_resize):162:6  False  (rank 2 — if (s->m < size))
Location: ks_resize() inlined into header.c compilation unit
Branch Condition: False means s->m >= size — existing kstring capacity is sufficient,
                  realloc is skipped.
Coverage Status:
  Rank 2 (162:6 F): cmplog T:15,900  F:27,800 | n4 T:5,490  F:0
  True arm (need to grow buffer) hit by both; False arm (buffer reuse) only cmplog.
```

**Code context (kstring.h, inlined at compile time into header.c):**
```c
static inline int ks_resize(kstring_t *s, size_t size) {
    if (s->m < size) {      // False: s->m >= size, buffer already big enough
        char *tmp;
        kroundup_sz(size);
        if (size > SIZE_MAX - 1 || !(tmp = (char*)realloc(s->s, size + 1)))
            return -1;
        s->m = size;
        s->s = tmp;
    }
    return 0;
}
```

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → view_sam(...)
      → sam_hdr_read(in) on SAM input
          → sam_hdr_build_from_sam_file(hdr, fp)
              → loop: hts_getline (read @-header lines)
              → for each header line: ks_resize(&str, needed_size)
                  1st call: s->m == 0 → s->m < size → True (alloc)
                  2nd call: s->m >= needed_size → False ← BLOCKED IN n4
                  (buffer reuse on second/subsequent SAM header lines)
```

**Path Conditions Required:**
1. SAM format input (so `sam_hdr_build_from_sam_file` is called).
2. At least two `@`-header lines, so the second line fits within the capacity allocated
   for the first (triggering the buffer-reuse False arm).
3. n4 never produces SAM inputs (C02 gate).

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency (prerequisite: SAM format gate)

**Root Cause Explanation:**
The False arm of `ks_resize` fires when a kstring's existing allocation is large enough
to hold the new data — common during SAM header processing when multiple lines of similar
length are read sequentially. After the first `@`-header line is processed and the buffer
is grown to accommodate it, subsequent lines of equal or shorter length reuse the buffer
without reallocating.

n4 never reaches this code because it never produces SAM inputs. The C02 mitigation
(SAM seeds) is fully sufficient to unblock this branch as well.

**Fuzzer Barrier Severity:** High (gated behind SAM format; self-resolves with SAM seeds)

**Recommended Mitigations:**
1. The C02 SAM seed mitigation is sufficient. A multi-line SAM header (2+ `@SQ` lines)
   maximizes buffer-reuse opportunities.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C07 (single — pool_destroy loop True: pool has allocated entries)
Branches:
  cram/pooled_alloc.c:87:17  True  (rank 5 — for (i = 0; i < p->npools; i++))
Location: pool_destroy() in cram/pooled_alloc.c (lines 84–92)
Branch Condition: loop condition `i < p->npools`, True means pool was used (npools > 0)
Coverage Status:
  Rank 5 (87:17 T): cmplog T:12,400  F:30,400 | n4 T:0  F:14,600
  False arm (empty pool, no body) hit by both; True arm (iterate and free) only cmplog.
```

**Code at pool_destroy:**
```c
void pool_destroy(pool_alloc_t *p) {
    size_t i;
    for (i = 0; i < p->npools; i++) {   // ← True arm BLOCKED in n4
        free(p->pools[i].pool);
    }
    free(p->pools);
    free(p);
}
```

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → view_sam(...)
      → sam_hdr_read(in) on SAM input
          → sam_hdr_create(fp)
              → sam_hdr_build_from_sam_file(hdr, fp)
                  → sam_hrecs_parse_single_line(hrecs, line, len)
                      → pool_alloc(hrecs->str_pool, ...)
                          → new_pool(p)   [if current pool exhausted]
                              → p->npools++   [becomes >= 1]
      → sam_hdr_destroy(hdr)
          → sam_hrecs_free(hrecs)
              → pool_destroy(hrecs->str_pool)   ← BLOCKING BRANCH
                  i < p->npools (True if npools > 0)
```

**Path Conditions Required:**
1. SAM format input (so `sam_hrecs_parse_single_line` is called).
2. At least one valid `@`-prefixed header line that is successfully parsed, causing
   `pool_alloc` to be called, which calls `new_pool` and increments `p->npools` to 1.

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency (prerequisite: SAM format gate)

**Root Cause Explanation:**
`pool_alloc` is the SAM header string pool allocator used to store string fragments from
parsed `@`-header lines. The pool's `npools` counter starts at 0 and is incremented by
`new_pool` whenever a new memory block is requested. `pool_alloc` is only called from
`sam_hrecs_parse_single_line`, which is only called when a SAM header line beginning with
`@` is encountered.

n4 never produces SAM inputs → `sam_hrecs_parse_single_line` never runs → `pool_alloc`
never called → `p->npools` remains 0 → `pool_destroy` loop condition `i < p->npools`
is always False immediately.

The cmplog fuzzer hits the True arm 12,400 times, confirming it regularly processes SAM
inputs with at least one valid header line.

**Fuzzer Barrier Severity:** High (fully unblocked by C02 SAM seed mitigation)

**Recommended Mitigations:**
1. The C02 SAM seed is sufficient. Any SAM input with a single `@HD\t` or `@SQ\t` line
   parsed successfully will increment `npools` to 1 and unblock this branch.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C08 (single — add_stub_ref_sq_lines loop True: nref > 0)
Branches:
  header.c:1109:19 (source ~1270:5) True  (rank 15 —
    for (tid = 0; tid < hrecs->nref; tid++))
Location: add_stub_ref_sq_lines() in header.c (lines 1266–1287)
Branch Condition: loop condition True means hrecs->nref > 0
Coverage Status:
  Rank 15 (1109:19 T): cmplog T:4,030  F:11,100 | n4 T:0  F:7,330
  False arm (nref == 0) heavily hit; True arm (iterate references) only cmplog.
```

**Code at add_stub_ref_sq_lines:**
```c
static int add_stub_ref_sq_lines(sam_hrecs_t *hrecs) {
    int tid;
    char len[32];
    for (tid = 0; tid < hrecs->nref; tid++) {  // ← True BLOCKED in n4
        if (hrecs->ref[tid].ty == NULL) {
            // add synthetic @SQ line for a reference without an @SQ record
            ...
        }
    }
    return 0;
}
```

**Execution Path to Branch:**
```
LLVMFuzzerTestOneInput
  → view_sam(...)
      → sam_hdr_count_lines(hdr, "SQ")
          → sam_hdr_fill_hrecs(bh)
              → sam_hrecs_refs_from_targets_array(hrecs, bh)
                  → hrecs->nref = bh->n_targets   [e.g. 1]
              → add_stub_ref_sq_lines(hrecs)  ← BLOCKING BRANCH
                  tid < hrecs->nref (True if nref > 0)
```

**Path Conditions Required:**
- `bh->n_targets >= 1`: requires a BAM input with a reference count field ≥ 1 in the
  binary header, OR a SAM input with `@SQ` lines that were processed before this call.
- n4 never produces BAM inputs and never produces SAM inputs (dual gate).

**Root Cause Category:** Input Format / Structure Constraints (BAM/SAM format gate)

**Root Cause Explanation:**
`hrecs->nref` is populated from `bh->n_targets` by `sam_hrecs_refs_from_targets_array`
(called when `bh->n_targets > 0`). For n4: `bh->n_targets` is always 0 because:
(a) BAM inputs (which store the reference list in binary) are never produced by n4.
(b) SAM inputs (which populate `n_targets` via `@SQ` parsing) are never produced by n4.
Thus `hrecs->nref` stays 0 and `add_stub_ref_sq_lines` finds no work to do.

**Fuzzer Barrier Severity:** High

**Recommended Mitigations:**
1. Any BAM seed with `n_targets >= 1` in the binary header unblocks this branch.
2. Any SAM seed with at least one `@SQ\tSN:...\tLN:...\n` line also unblocks it.
3. Both are already covered by the C02 and C04 seed recommendations.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C09 (single — sam_hdr_count_lines error guard)
Branches:
  header.c:2150:9 (coverage: 1789:13) True  (rank 18 —
    if (sam_hdr_fill_hrecs(bh) != 0))
Location: sam_hdr_count_lines() in header.c (lines 2142–2170)
Branch Condition: sam_hdr_fill_hrecs returns -1 (error)
Coverage Status:
  Rank 18 (1789:13 T): cmplog T:3,020  F:7,650 | n4 T:0  F:5,490
  False arm (success) hit by both; True arm (error) only cmplog.
```

**Code at sam_hdr_count_lines (header.c:2142–2152):**
```c
int sam_hdr_count_lines(sam_hdr_t *bh, const char *type) {
    ...
    if (!bh->hrecs) {
        if (sam_hdr_fill_hrecs(bh) != 0)   // ← True arm BLOCKED in n4
            return -1;
    }
    ...
}
```

**Path Conditions Required:**
1. `bh->hrecs` must be NULL at the time of the call (BAM path — bam_hdr_read leaves
   `bh->hrecs = NULL`).
2. `sam_hdr_fill_hrecs` must then fail (return -1), which requires:
   - `bh->text` is non-NULL and `l_text > 0` (so `sam_hrecs_parse_lines` is called), AND
   - The embedded SAM text has a parsing error, e.g., a duplicate `@SQ SN:` entry:
     `header.c:1229: hts_log_error("Duplicate entry \"%s\" ...")` returns -1.

**Root Cause Category:** Deep Nested Condition Dependencies (BAM format + malformed header)

**Root Cause Explanation:**
For this error path to fire, the fuzzer must produce a BAM input that:
(a) Passes the `BAM\1` magic check (4-byte prefix).
(b) Has `l_text > 0` (non-empty embedded SAM header section).
(c) Contains a duplicate `@SQ SN:` tag pair in the embedded text, causing
    `sam_hrecs_parse_lines` to return -1 inside `sam_hdr_fill_hrecs`.

The n4 fuzzer never achieves (a) — it never produces BAM inputs. When n4 does reach
`sam_hdr_count_lines`, `bh->hrecs` is always already set (n4's inputs come from SAM path
where hrecs is populated immediately), so the `if (!bh->hrecs)` guard is False and
`sam_hdr_fill_hrecs` is never called from this site.

**Fuzzer Barrier Severity:** High (two-layer requirement: BAM magic + malformed text)

**Recommended Mitigations:**
1. A BAM seed with a duplicate reference name in the embedded SAM text section directly
   triggers this error path:
   `BAM\1` + [l_text bytes] + `@SQ\tSN:chr1\tLN:1000\n@SQ\tSN:chr1\tLN:2000\n`.
2. The general BAM seed recommendation (C04/C05 mitigations) is a prerequisite; once
   BAM inputs are explored, mutation will occasionally produce duplicate `@SQ` entries.

---

### BLOCKING BRANCH ANALYSIS
```
========================
Cluster: C10 (single — hts_detect_format2 @CO\t magic match)
Branches:
  hts.c:696:15  True  (rank 19 — memcmp(s, "@CO\t", 4) == 0)
Location: hts_detect_format2() in hts.c (lines 693–706)
Branch Condition: last alternative in a 5-way || expression matching SAM header tags
Coverage Status:
  Rank 19 (696:15 T): cmplog T:3,000  F:418 | n4 T:0  F:409
  False arm (no @CO match — but overall SAM clause matched via earlier alternative)
  hit by n4; True arm (@CO match specifically) never hit by n4.
```

**Code context (hts.c:693–706):**
```c
else if (len >= 4 && s[0] == '@' &&
         (memcmp(s, "@HD\t", 4) == 0 || memcmp(s, "@SQ\t", 4) == 0 ||
          memcmp(s, "@RG\t", 4) == 0 || memcmp(s, "@PG\t", 4) == 0 ||
          memcmp(s, "@CO\t", 4) == 0)) {    // ← rank 19 True BLOCKED
    fmt->category = sequence_data;
    fmt->format = sam;
    ...
}
```
Note: In llvm-cov branch reporting, each `||` sub-expression generates its own branch
entry. Rank 19's True arm means the `memcmp(s, "@CO\t", 4) == 0` comparison returned
true (the first four alternatives were all false, but the fifth matched).

**Path Conditions Required:**
1. Input bytes 0–3 must be `@CO\t` specifically (not `@HD`, `@SQ`, `@RG`, or `@PG`).
2. The `@CO\t` token is a SAM comment header; it is rarely used in practice and absent
   from most fuzzing seed corpora and dictionaries.
3. n4 never produces any `@XX\t` prefix (C02 gate), making this doubly blocked.

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency; Magic Value constraints

**Root Cause Explanation:**
The `@CO\t` check is the last of five alternatives in a short-circuit `||` expression.
Reaching the True arm of this specific sub-expression requires that all four preceding
alternatives were False AND the fifth (`@CO\t`) matched. This means the input must start
with `@CO\t` — not just any SAM header prefix.

Even the cmplog fuzzer, which has learned `@HD\t` and `@SQ\t` (the most common SAM
headers), produces `@CO\t` only when it specifically has a seed or dictionary token
containing that string. The n4 fuzzer has neither. The `@CO` comment tag is valid SAM
spec but uncommon in real-world files and absent from typical fuzzer dictionaries.

**Fuzzer Barrier Severity:** High

**Recommended Mitigations:**
1. Add `@CO\t` explicitly to the AFL++ dictionary.
2. Add a SAM seed that begins with `@CO\t`, e.g.:
   ```
   @CO\tThis is a comment line\n
   ```
3. The C02 SAM seeds mitigations should include a `@CO` line (the recommended seed
   above already contains one).

---

## Summary Table

| Rank | Function | Line:Col | Side | Cluster | Root Cause | Severity |
|------|----------|----------|------|---------|------------|----------|
| 1 | `cram_free_container` | 3747:13 | False | C03 | CRAM magic bytes never in n4 corpus | Critical |
| 11 | `cram_free_container` | 3730:9 | False | C03 | CRAM magic bytes never in n4 corpus | Critical |
| 12 | `cram_free_container` | 3751:9 | False | C03 | CRAM magic bytes never in n4 corpus | Critical |
| 13 | `cram_free_container` | 3723:9 | False | C03 | CRAM magic bytes never in n4 corpus | Critical |
| 20 | `cram_free_container` | 3720:9 | False | C03 | CRAM magic bytes never in n4 corpus | Critical |
| 2 | `header.c:ks_resize` | 162:6 | False | C06 | SAM format gate (buffer reuse) | High |
| 3 | `get_severity_tag` | 5123:5 | False | C01 | Semi-valid SAM needed for WARNING | High |
| 4 | `get_severity_tag` | 5125:5 | True | C01 | Semi-valid SAM needed for WARNING | High |
| 5 | `pool_destroy` | 87:17 | True | C07 | SAM format gate (pool unused) | High |
| 6 | `sam_hdr_fill_hrecs` | 1142:21 | True | C05 | BAM magic + non-empty header text | High |
| 7 | `hts_hopen` | 1583:5 | True | C02 | SAM `@XX\t` magic absent in n4 | High |
| 8 | `sam_read1` | 4394:9 | True | C02 | SAM `@XX\t` magic absent in n4 | High |
| 9 | `sam_hdr_read` | 2207:5 | True | C02 | SAM `@XX\t` magic absent in n4 | High |
| 10 | `sam_hdr_destroy` | 122:9 | True | C04 | SAM format gate (ref_count) | High |
| 14 | `sam_hdr_destroy` | 134:9 | False | C04 | BAM path needed (hrecs=NULL) | High |
| 15 | `add_stub_ref_sq_lines` | 1109:19 | True | C08 | BAM/SAM with nref > 0 | High |
| 16 | `sam_hdr_destroy` | 127:9 | True | C04 | SAM format gate (target_name) | High |
| 17 | `sam_hdr_fill_hrecs` | 1134:9 | True | C05 | BAM magic + n_targets > 0 | High |
| 18 | `sam_hdr_count_lines` | 1789:13 | True | C09 | BAM + malformed embedded header | High |
| 19 | `hts_detect_format2` | 696:15 | True | C10 | `@CO\t` magic token absent | High |

---

## Top Recommendations

### P1 — Add a SAM seed to the n4 corpus (unblocks ranks 2, 3, 4, 5, 7, 8, 9, 10, 16, 19)

The single most impactful action. A seed that starts with `@CO\t` (to cover rank 19)
and includes a duplicate `@SQ` with conflicting LN (to cover ranks 3, 4):

```
@CO\tFuzzer seed comment
@HD\tVN:1.6\tSO:unsorted
@SQ\tSN:chr1\tLN:248956422
@SQ\tSN:chr1\tLN:500000
@RG\tID:rg1\tSM:sample1
@PG\tID:prog1\tPN:tool\tVN:1.0
read1\t0\tchr1\t100\t60\t10M\t*\t0\t0\tACGTACGTAC\tIIIIIIIIII
```

This 10-cluster unblock is the highest-ROI change possible for this campaign.

### P2 — Add a CRAM seed to the n4 corpus (unblocks ranks 1, 11, 12, 13, 20)

Generate with: `samtools view -C -o minimal.cram minimal.bam`
Add `minimal.cram` to the n4 seed directory. This is the only way to exercise
the CRAM encoder/decoder paths and unblock the five C03 cluster branches.

### P3 — Add a BAM seed to the n4 corpus (unblocks ranks 6, 14, 15, 17, 18)

A BAM file with: (a) at least one reference sequence (`n_targets >= 1`), (b) non-empty
embedded header text (`l_text > 0`). For rank 18, also include a duplicate `@SQ SN:`
in the embedded text to trigger the fill-hrecs error path.

### P4 — Extend the AFL++ dictionary

```
# SAM header tokens
@HD\t
@SQ\t
@RG\t
@PG\t
@CO\t
VN:1.6\t
SN:chr1\t
LN:1000\n

# Format magic bytes
CRAM
BAM\x01
\x1f\x8b\x08\x00
```

### P5 — Consider a structured / grammar-aware mutator

All 20 top blocking branches reduce to a single theme: the n4 fuzzer cannot produce
inputs that satisfy the binary magic-byte checks guarding CRAM (`CRAM` + version bytes),
BAM (`BAM\1`), or SAM (`@XX\t` prefix). A structured mutator that understands these
format frames — or a harness wrapper that splices format-correct headers around the
fuzzer's payload — would address all 20 blockers simultaneously and provide much deeper
penetration into the SAM/BAM/CRAM processing code.

---

*Report written to `/home/miao/BlockerAnalyzer/reports/htslib_report.md`*
*Analysis date: 2026-03-18*
