# Root Cause Report — htslib Fuzzing Blockers

**Target:** htslib (`test/fuzz/hts_open_fuzzer.c`)
**Fuzzers analyzed:** AFL++ cmplog, AFL++ n4
**Coverage format:** llvm-cov annotated source (per `coverage/htslib/`)
**Date:** 2026-03-17
**Analyst:** fuzzing-root-cause-analyzer

---

## Fuzzer Entry Point

`LLVMFuzzerTestOneInput` in `test/fuzz/hts_open_fuzzer.c`:

1. Wraps the input bytes in an in-memory `hFILE` via `hopen("mem:", ...)`.
2. Opens it with `hts_hopen`, which runs format detection (`hts_detect_format2`).
3. Dispatches based on `format.category`:
   - `sequence_data` → `view_sam()` three times (SAM output, BAM output, CRAM output).
   - `variant_data` → `view_vcf()` twice.
   - Anything else → no-op return.

For `sequence_data`, format detection requires the input to begin with the CRAM magic bytes `CRAM` (0x43 0x52 0x41 0x4D), a `@` SAM header line, or a BAM BGZF magic. For SAM, `view_sam` then calls `sam_hdr_read` → `sam_hrecs_parse_line` to parse `@`-prefixed header lines.

---

## Blocker Analyses

---

### BLOCKER 1

```
BLOCKING BRANCH ANALYSIS
========================
Location: cram/cram_io.c:3747 (cram_free_container)
Branch Condition: if (c->stats[id])   [for id = DS_RN..DS_TN in a for-loop]
Blocked Side: False (condition is always True in cmplog; always False in n4)
Coverage Status: n4: True=101,000 / False=0  |  cmplog: True=118,000 / False=138,000
Flip Strength: 138,000
```

**Execution Path to Branch:**

```
LLVMFuzzerTestOneInput
  → view_sam(..., "wc", 0)          [CRAM output mode]
    → hts_hopen(memfile, "data", "rb")   [format detection]
    → sam_hdr_read(in)
    → sam_read1 loop → sam_write1
      → cram_encode.c: cram_put_bam_seq
        → cram_new_container(seqs_per_slice, slices_per_container)
            [allocates c->stats[DS_RN..DS_TN] via cram_stats_create()]
        → cram_encode_container(fd, c)
        → cram_free_container(c)
            → for (id = DS_RN; id < DS_TN; id++)
                if (c->stats[id])         ← BRANCH AT LINE 3747
```

Also reached in the CRAM *decoder* path:

```
LLVMFuzzerTestOneInput
  → view_sam(..., "rb")
    → cram_decode.c: cram_get_seq
      → cram_read_container(fd)     [calloc-based: stats[] all NULL]
      → cram_free_container(c)
          → for (id = DS_RN; id < DS_TN; id++)
              if (c->stats[id])     ← always False when from cram_read_container
```

**Path Conditions Required:**

1. Input must begin with CRAM magic bytes `CRAM` (0x43 0x52 0x41 0x4D) for `format.category` to be `sequence_data` and CRAM format to be selected.
2. The CRAM file must contain a structurally valid SAM container header so that `cram_read_container` succeeds far enough to return a non-NULL container.
3. For the **True branch** (n4 is blocked on False): a container must have been created via `cram_new_container` (the encoder path), which explicitly calls `cram_stats_create()` for all `DS_RN..DS_TN` slots (cram_io.c:3681-3682). This happens only in the CRAM *write* path (`view_sam(..., "wc", 0)`).
4. For the **False branch** (n4 never hits it): a CRAM container must be read via `cram_read_container` (cram_io.c:3883), which uses `calloc` — leaving `stats[]` all-NULL. The False side fires when freeing a decoded container that was never populated by the encoder.

**Root Cause Category:** Input Format/Structure Constraint + Path Explosion / Depth Barrier

**Root Cause Explanation:**

`cram_free_container` is called from two distinct origins:

- **Encoder path** (`cram_new_container` → `cram_encode_container` → `cram_free_container`): The `stats[]` array is fully populated because `cram_new_container` explicitly allocates each slot. The True branch always fires here. This is what cmplog exercises when it successfully produces CRAM output.

- **Decoder path** (`cram_read_container` → `cram_free_container`): The container is `calloc`-initialized at cram_io.c:3883; `stats[]` is never populated during decoding. The False branch always fires here.

The n4 fuzzer never reaches the encoder path because it cannot construct a CRAM input that passes all of CRAM format detection, magic byte validation (bytes 0–3 must be `C`, `R`, `A`, `M`), and SAM header parsing. Without a valid CRAM input, `format.category != sequence_data`, the `view_sam(..., "wc", ...)` call is skipped entirely, and `cram_new_container` is never invoked. Consequently `cram_free_container` only ever sees decoder-path containers (stats all NULL), so the False branch for `if (c->stats[id])` has zero hits in n4.

The n4 fuzzer also reaches `cram_free_container` from early-exit error paths in `cram_read_container` itself (e.g., line 3890, 3896, 3901), all of which produce containers with `stats[]` null — reinforcing the all-True count.

**Fuzzer Barrier Severity: Critical**

The CRAM magic bytes `CRAM` are a 4-byte exact match at offset 0. Without them, format detection returns a non-CRAM category and the entire CRAM encoder path is bypassed. The n4 fuzzer (which lacks cmplog's comparison-logging feedback) cannot guess this 4-byte sequence under random mutation from typical seed inputs.

**Recommended Mitigations:**

1. Add a minimal valid CRAM seed file (even a single-record CRAM) to the fuzzer corpus. This immediately routes the input through `sequence_data` and activates both the decoder and encoder paths.
2. Add the token `CRAM` (bytes `0x43 0x52 0x41 0x4D`) to the AFL++ fuzzer dictionary so that mutation can produce inputs with the correct magic prefix.
3. Consider a structure-aware CRAM mutator or a CRAM-specific harness that bypasses format detection and calls `cram_new_container` / `cram_encode_container` directly.

---

### BLOCKER 2

```
BLOCKING BRANCH ANALYSIS
========================
Location: htslib/kstring.h:162 (ks_resize inline, instantiated in header.c)
Branch Condition: if (s->m < size)   — False side: buffer already large enough
Blocked Side: False (n4 never hits the branch-not-taken path)
Coverage Status: n4: True=5,490 / False=0  |  cmplog: True=15,900 / False=27,800
Flip Strength: 27,800
```

The `ks_resize` inline function (kstring.h:159-172):

```c
static inline int ks_resize(kstring_t *s, size_t size)
{
    if (s->m < size) {           // line 162 — False side blocked in n4
        char *tmp;
        size = (size > (SIZE_MAX>>2)) ? size : size + (size >> 1);
        tmp = (char*)realloc(s->s, size);
        if (!tmp) return -1;
        s->s = tmp;
        s->m = size;
    }
    return 0;
}
```

The False branch (`s->m >= size`) fires when the kstring buffer is already large enough — i.e., a second or subsequent call to `ks_resize` reuses a previously allocated buffer.

**Execution Path to Branch:**

```
LLVMFuzzerTestOneInput
  → view_sam(data, size, "w", 1)      [SAM output]
    → hts_hopen → format detection
    → sam_hdr_read(in)
      → sam_hrecs_parse_line (header.c)
        → loop over '@'-prefixed header lines
          → kputsn(fp->line.s, fp->line.l, &str)   [header.c:1405]
            → ks_resize(&str, str.l + fp->line.l)  [first call → True: allocates]
          → [second header line]
          → kputsn(fp->line.s, fp->line.l, &str)
            → ks_resize(&str, str.l + fp->line.l)  [second call → False: reuses buffer]
```

**Path Conditions Required:**

1. Input must be recognized as `sequence_data` (SAM/BAM/CRAM magic or `@` header).
2. `sam_hdr_read` must successfully parse at least one `@`-prefixed header line so that `str` is allocated.
3. **At least a second valid `@` header line must follow** such that the cumulative `kputsn` length on the second line does not exceed `str.m` — i.e., `str.l + line2.l <= str.m`. Because `ks_resize` grows the buffer by 1.5× on the first call, a second line of roughly equal or smaller length to the first will fit in the already-allocated buffer, hitting the False branch.

**Root Cause Category:** Fuzzer Seed/Dictionary Deficiency + Deep Nested Condition Dependencies

**Root Cause Explanation:**

The n4 fuzzer's corpus does not contain inputs with multiple valid SAM header lines. A single `@HD` or `@SQ` line causes one `ks_resize` call (True branch — buffer allocated). For the False branch to fire, a second header line must be present that fits within the already-allocated buffer capacity.

The n4 fuzzer is further blocked upstream by the SAM format gate: the input must begin with `@` (or BAM magic), and each header line must pass `valid_sam_header_type` (`@HD`, `@SQ`, `@RG`, `@PG`, `@CO`). Without a seed containing at least two such lines, the buffer is freshly created for each run and `s->m` never exceeds the first line's allocation. Since the buffer is initialized fresh per `view_sam` call (`str` is a local `kstring_t` on the stack, initialized to `{0,0,NULL}`), every single-line run hits only the True branch.

The cmplog fuzzer overcomes this via comparison logging — it identifies the `@`-type tokens and learns to produce multi-line headers, resulting in 27,800 False-branch hits.

**Fuzzer Barrier Severity: High**

The False branch is reachable with any two valid SAM header lines, but requires the fuzzer to consistently produce structured multi-line `@`-prefixed content. Without seeds or dictionary tokens, the n4 fuzzer explores this territory very slowly.

**Recommended Mitigations:**

1. Add a seed with two or more SAM header lines, e.g.:
   ```
   @HD\tVN:1.6\n@SQ\tSN:chr1\tLN:248956422\n
   ```
   This guarantees the False branch fires on the second `kputsn` call.
2. Add dictionary tokens: `@HD`, `@SQ`, `@RG`, `@PG`, `@CO`, `VN:`, `SN:`, `LN:`.
3. For thoroughness, add a seed with a longer first line followed by a shorter second line to ensure `str.l + line2.l <= str.m` on the second call.

---

### BLOCKER 3

```
BLOCKING BRANCH ANALYSIS
========================
Location: hts.c:5123 (get_severity_tag)
Branch Condition: switch (severity) — case HTS_LOG_ERROR (value=1): False side
                  i.e., the switch falls through to a non-ERROR case
Blocked Side: False (n4 always enters the HTS_LOG_ERROR case; never falls through)
Coverage Status: n4: True=279 / False=0  |  cmplog: True=7,640 / False=22,600
Flip Strength: 22,600
```

Note: The coverage tool labels these lines as `get_severity_tag`. In the source
tree at this analysis date, the function body appears at hts.c:5165, but the
instrumented binary was compiled from a slightly earlier version where it was at
line 5121. The logic is identical.

```c
static char get_severity_tag(enum htsLogLevel severity)
{
    switch (severity) {
    case HTS_LOG_ERROR:       // line 5123 — branch True=279, False=0 in n4
        return 'E';
    case HTS_LOG_WARNING:     // line 5125 — branch True=0, False=279 in n4
        return 'W';
    case HTS_LOG_INFO:
        return 'I';
    ...
    }
    return '*';
}
```

The "False" side of `case HTS_LOG_ERROR` means the switch did not match
`HTS_LOG_ERROR` — i.e., `severity` was something other than `HTS_LOG_ERROR`
(value 1). This branch is the collective "fall-through" to subsequent cases.

**Execution Path to Branch:**

```
LLVMFuzzerTestOneInput
  → view_sam / view_vcf / format detection
    → any hts_log_warning(...) call   [e.g., hts_log(HTS_LOG_WARNING, ...)]
      → hts_log(severity=HTS_LOG_WARNING, ...)
        → (severity=3 <= hts_verbose=3: condition true)
        → get_severity_tag(HTS_LOG_WARNING)   [severity=3, not HTS_LOG_ERROR=1]
          → switch falls through case HTS_LOG_ERROR → hits case HTS_LOG_WARNING
```

**Path Conditions Required:**

1. `hts_log` must be called with `severity <= hts_verbose` (default: `HTS_LOG_WARNING = 3`).
2. The `severity` argument must not be `HTS_LOG_ERROR` (value 1). It must be `HTS_LOG_WARNING` (value 3), `HTS_LOG_INFO` (4), `HTS_LOG_DEBUG` (5), or `HTS_LOG_TRACE` (6).
3. Therefore, a `hts_log_warning(...)` call site must be triggered. There are approximately 149 `hts_log_warning` call sites across the htslib source. These fire for conditions like duplicate `@SQ` reference names, non-fatal header inconsistencies, or format quirks that do not cause parsing failure.

**Root Cause Category:** Algorithmic/Semantic Barrier (enum gap) + Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**

`HTS_LOG_WARNING` has enum value 3 (not 2 — there is a deliberate gap in the enum):

```c
enum htsLogLevel {
    HTS_LOG_OFF,       // 0
    HTS_LOG_ERROR,     // 1
    HTS_LOG_WARNING = 3,  // explicit skip of value 2
    HTS_LOG_INFO,      // 4
    ...
};
```

Value 2 is deliberately unused. All 279 calls to `hts_log` that n4 triggers arrive via `hts_log_error` (severity=1). This means every parse failure, memory error, or invalid input condition produces an ERROR-level log call, hitting only the `HTS_LOG_ERROR` case in `get_severity_tag`.

A WARNING-level log requires the input to be *partially valid*: the parser must successfully enter the header processing logic and then encounter a non-fatal anomaly (e.g., a duplicate `@SQ` SN, an unknown optional tag, a missing optional field). The n4 fuzzer's inputs are either too malformed (immediately rejected, producing ERROR logs) or too random (not reaching warning-emitting code paths at all).

This blocker is a direct consequence of the n4 fuzzer lacking seeds that produce partially-valid SAM headers which pass initial validation but contain soft errors that trigger warnings.

**Fuzzer Barrier Severity: High**

The WARNING path requires inputs that are structurally valid enough to pass primary parsing gates yet contain specific secondary anomalies. This is a narrow semantic corridor that random mutation from malformed seeds almost never reaches.

**Recommended Mitigations:**

1. Add a seed with a duplicate `@SQ SN:` name, which triggers `hts_log_warning` from the `add_sq_seq_names` path in `header.c`. Example:
   ```
   @HD\tVN:1.6\n@SQ\tSN:chr1\tLN:1000\n@SQ\tSN:chr1\tLN:2000\n
   ```
   This forces two SQ entries with the same name but different LN values, which triggers a WARNING about conflicting SQ lines.
2. Alternatively, include a seed that triggers the `hts_log_warning` in `hts_detect_format2` for ambiguous format signatures.
3. Consider enabling a custom log handler during fuzzing that counts WARNING calls, allowing coverage feedback to treat a WARNING invocation as a distinct coverage event.

---

### BLOCKER 4

```
BLOCKING BRANCH ANALYSIS
========================
Location: hts.c:5125 (get_severity_tag)
Branch Condition: switch (severity) — case HTS_LOG_WARNING (value=3): True side
                  i.e., severity == HTS_LOG_WARNING
Blocked Side: True (n4 never enters the HTS_LOG_WARNING case)
Coverage Status: n4: True=0 / False=279  |  cmplog: True=22,600 / False=7,640
Flip Strength: 22,600
```

This is the symmetric counterpart to Blocker 3 in the same switch statement. The
True side of `case HTS_LOG_WARNING` fires when `severity == HTS_LOG_WARNING` (value 3).
The False side (which n4 always hits) means the switch fell through this case without
matching — i.e., `severity` was `HTS_LOG_ERROR` (the only value that reaches
`get_severity_tag` in n4).

**Execution Path to Branch:**

Identical to Blocker 3. The same call to `get_severity_tag(HTS_LOG_WARNING)` that
produces the False side of Blocker 3 also produces the True side of Blocker 4.
Both blockers are resolved by the same fix.

**Path Conditions Required:**

Same as Blocker 3:
1. A `hts_log_warning(...)` (or `hts_log(HTS_LOG_WARNING, ...)`) call must be triggered.
2. The `hts_log` gate `severity <= hts_verbose` must pass (it always does for WARNING since `hts_verbose` defaults to `HTS_LOG_WARNING=3`).
3. The input must be partially valid enough to reach a warning-emitting code path.

**Root Cause Category:** Algorithmic/Semantic Barrier (same enum gap) + Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**

This is the exact complement of Blocker 3 within the same switch body. In the
n4 campaign, all 279 `get_severity_tag` invocations carry `severity=HTS_LOG_ERROR`
(value 1), which matches `case HTS_LOG_ERROR` immediately and returns `'E'` without
ever evaluating `case HTS_LOG_WARNING`. The True branch of `case HTS_LOG_WARNING`
therefore has zero hits.

The root cause is identical: the n4 fuzzer cannot produce inputs that trigger
warning-level conditions. See Blocker 3 for the full explanation.

**Fuzzer Barrier Severity: High**

Same severity as Blocker 3. Blockers 3 and 4 are resolved together by any input
that causes a single `hts_log_warning` call.

**Recommended Mitigations:**

Identical to Blocker 3. Both blockers are unblocked simultaneously by any seed
that triggers a WARNING-level log event.

---

### BLOCKER 5

```
BLOCKING BRANCH ANALYSIS
========================
Location: cram/pooled_alloc.c:87 (pool_destroy)
Branch Condition: for (i = 0; i < p->npools; i++)  — True side: loop body entered
Blocked Side: True (n4 never enters the loop body)
Coverage Status: n4: True=0 / False=14,600  |  cmplog: True=12,400 / False=30,400
Flip Strength: 12,400
```

```c
void pool_destroy(pool_alloc_t *p) {
    size_t i;

    for (i = 0; i < p->npools; i++) {    // line 87 — True blocked in n4
        free(p->pools[i].pool);
    }
    free(p->pools);
    free(p);
}
```

The True branch fires when `p->npools > 0`, meaning at least one memory pool block
was allocated via `pool_alloc` → `new_pool`. The False branch (loop condition false
on first check) fires when `p->npools == 0` — the pool was created but never had
`pool_alloc` called on it.

**Execution Path to Branch:**

```
LLVMFuzzerTestOneInput
  → view_sam(data, size, "w", 1)
    → hts_hopen → format detection (sequence_data)
    → sam_hdr_read(in)
      → sam_hrecs_parse_line(hrecs, ...)      [header.c:1368 loop]
        → sam_hrecs_parse_single_line(...)    [header.c:1394]
          → pool_alloc(hrecs->type_pool)       [header.c:562]
            → new_pool(p) → p->npools++        [pooled_alloc.c:110]
      → sam_hrecs_free(hrecs)                  [on cleanup path]
        → pool_destroy(hrecs->type_pool)       [header.c:2483]
          → for (i=0; i < p->npools; i++)      ← True branch fires
```

For the True branch to fire, `pool_alloc` must be called at least once, which
requires `sam_hrecs_parse_single_line` to succeed on at least one header line.

**Path Conditions Required:**

1. Input must be recognized as `sequence_data` (SAM `@` prefix or BAM/CRAM magic).
2. `sam_hdr_read` must enter the header parsing loop (first byte of input is `@`).
3. At least one header line must pass all of the following in `sam_hrecs_parse_line` (header.c):
   - Line length >= 3 characters.
   - `fp->line.s[1]` and `fp->line.s[2]` are both `isalpha_c`.
   - `valid_sam_header_type` returns true (`@HD`, `@SQ`, `@RG`, `@PG`, or `@CO`).
4. `sam_hrecs_parse_single_line` must succeed without returning NULL — meaning tag parsing (colon-delimited key-value pairs) succeeds and `pool_alloc(hrecs->type_pool)` is called at line 562.

**Root Cause Category:** Deep Nested Condition Dependencies + Fuzzer Seed/Dictionary Deficiency

**Root Cause Explanation:**

`pool_destroy` is called 14,600 times in the n4 campaign, but `p->npools` is always 0.
The coverage data (n4.cov, lines 2480-2486) shows that the `pool_destroy` calls in the
successful header-parsing teardown path (`sam_hrecs_free`, header.c:2480-2486) run
7,330 times — but `npools` is 0 in every case.

This happens because `pool_alloc` is only called from `sam_hrecs_parse_single_line`
(header.c:562, 609, 814, 865, 935). For `pool_alloc` to be called, the line must:
(a) start with `@`, (b) have two valid alpha characters as the type code, (c) match
one of the five known SAM header types, and (d) have the line successfully tokenized
into key=value fields. The n4 fuzzer's inputs that reach the SAM parsing path fail
the `valid_sam_header_type` check (line 1388) because the two type characters are
random, or the line is too short, or the format detection misidentifies the input.

The coverage of `sam_hrecs_parse_single_line` for n4 is 0 (the function itself has
zero hits in n4), confirming that no header line ever passes all of the gates in
the `sam_hdr_read` loop before `pool_alloc` is reached. Without `pool_alloc` being
called even once, `new_pool` never increments `npools`, and `pool_destroy` always
sees an empty pool.

**Fuzzer Barrier Severity: High**

The barrier is a conjunction: valid SAM `@`-type prefix, valid two-character type
keyword, and at least one parseable key=value tag pair. Any of these three checks
failing silently rejects the header line before `pool_alloc` is called. The n4 fuzzer
has no dictionary or seed that reliably produces this combination.

**Recommended Mitigations:**

1. Add a minimal valid SAM header seed:
   ```
   @HD\tVN:1.6\n
   ```
   This is the simplest input that passes all three gates and causes `pool_alloc` to
   be called for the `@HD` type entry, incrementing `npools` to 1.
2. For stronger coverage, add:
   ```
   @HD\tVN:1.6\n@SQ\tSN:chr1\tLN:1000\n
   ```
   This causes two `pool_alloc` calls (one type + one tag entry each), giving
   `npools >= 1` and reliably hitting the True branch of the loop in `pool_destroy`.
3. Add dictionary tokens: `@HD`, `@SQ`, `@RG`, `@PG`, `@CO`, `VN:`, `SN:`, `LN:`.
4. The same seed also unblocks Blocker 2 (ks_resize False) and Blockers 3/4
   (get_severity_tag WARNING), making a single well-chosen seed highly effective.

---

## Summary Table

| Rank | Location | Blocked Side | Root Cause Category | Severity | Single Fix |
|------|----------|-------------|---------------------|----------|------------|
| 1 | `cram_io.c:3747` (`cram_free_container`) | False | Input Format/Structure: CRAM magic bytes required for encoder path | **Critical** | Add CRAM seed file |
| 2 | `kstring.h:162` (`ks_resize`, in header.c) | False | Seed Deficiency: requires 2+ valid SAM header lines | **High** | Add multi-line SAM seed |
| 3 | `hts.c:5123` (`get_severity_tag`) | False | Semantic Barrier: WARNING-level log never triggered | **High** | Add seed with soft-error header |
| 4 | `hts.c:5125` (`get_severity_tag`) | True | Semantic Barrier: same as Blocker 3, symmetric case | **High** | Same as Blocker 3 |
| 5 | `pooled_alloc.c:87` (`pool_destroy`) | True | Nested Conditions: `pool_alloc` never called, `npools` stays 0 | **High** | Add minimal `@HD` seed |

---

## Top Recommendations

Listed in order of expected coverage impact (most blockers unblocked per action):

### Recommendation 1: Add a multi-line SAM header seed with a soft error

```
@HD\tVN:1.6\n@SQ\tSN:chr1\tLN:1000\n@SQ\tSN:chr1\tLN:2000\n
```

**Unblocks:** Blockers 2, 3, 4, and 5 simultaneously.

- Blocker 5 (`pool_destroy` True): `pool_alloc` is called for the `@HD` and both
  `@SQ` entries, so `npools >= 1`.
- Blocker 2 (`ks_resize` False): three header lines cause multiple `kputsn` calls
  on the same `str` buffer; the second and third calls find `str.m` already large
  enough.
- Blockers 3 and 4 (`get_severity_tag` WARNING): the duplicate `@SQ SN:chr1` with
  conflicting `LN` values triggers a `hts_log_warning` from the SAM header
  validation logic (`add_sq_seq_names` in `header.c`), sending severity 3
  (`HTS_LOG_WARNING`) through `get_severity_tag`.

### Recommendation 2: Add a real CRAM seed file

Place any minimal valid CRAM file (one reference, one read) in the fuzzer corpus.

**Unblocks:** Blocker 1 (`cram_free_container` False).

A CRAM seed causes `format.category == sequence_data` with CRAM format, routing
the input through `view_sam(..., "wc", ...)`, which invokes `cram_new_container`.
`cram_new_container` populates `stats[]` via `cram_stats_create()`, making the
False branch of `if (c->stats[id])` reachable for the first time.

### Recommendation 3: Add AFL++ fuzzer dictionary tokens

Tokens to add: `CRAM`, `@HD`, `@SQ`, `@RG`, `@PG`, `@CO`, `VN:1.6`, `SN:`, `LN:`.

This allows random mutations to land on valid SAM/CRAM constructs more often,
accelerating discovery of the conditions required for all five blockers.

### Recommendation 4: Long-term — structured SAM/CRAM mutator

For sustained coverage improvement beyond the top-5 blockers, integrate a
format-aware mutator (e.g., using `libprotobuf-mutator` with a SAM/CRAM grammar
or a custom AFL++ custom mutator). Structured mutation prevents the fuzzer from
spending budget on inputs that fail format detection gates entirely.
