#!/usr/bin/env bash
# run.sh — blocker_5 fuzzer comparison experiment (v3)
# Runs cmplog then no-cmplog for 5 minutes each on the same initial seed,
# then counts how many evolved seeds in each queue still hit the False branch.
set -euo pipefail

DURATION=300   # seconds per fuzzer (5 minutes)
OUTPUT=/output
SEEDS=/experiment/seeds
BUILD=/experiment/build

mkdir -p "$OUTPUT/cmplog" "$OUTPUT/n4" "$SEEDS" "$BUILD"

# ── AFL++ environment ─────────────────────────────────────────────────────────
export AFL_SKIP_CPUFREQ=1
export AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
export AFL_NO_UI=1
export AFL_QUIET=1

echo core > /proc/sys/kernel/core_pattern 2>/dev/null || true

# ── Step 1: Compile ───────────────────────────────────────────────────────────
echo "[1/5] Compiling..."

LIBDRIVER=/AFLplusplus/libAFLDriver.a

# cmplog main binary: standard edge coverage (fuzz target for cmplog campaign)
unset AFL_LLVM_NGRAM_SIZE
unset AFL_LLVM_CMPLOG
afl-clang-fast \
    /experiment/blocker_5.c "$LIBDRIVER" -o "$BUILD/target_cmplog"

# cmplog instrumented binary: comparison logging; passed via -c to afl-fuzz
# NGRAM must remain unset
AFL_LLVM_CMPLOG=1 afl-clang-fast \
    /experiment/blocker_5.c "$LIBDRIVER" -o "$BUILD/target_cmplog_cmplog"

# n4 target: standard edge coverage, no cmplog — only difference is no -c flag
unset AFL_LLVM_NGRAM_SIZE
unset AFL_LLVM_CMPLOG
afl-clang-fast \
    /experiment/blocker_5.c "$LIBDRIVER" -o "$BUILD/target_n4"

# Oracle: plain gcc, ORACLE_MODE — prints "FALSE_BRANCH" when blocked side hit
gcc -DORACLE_MODE /experiment/blocker_5.c -o "$BUILD/oracle"

echo "    cmplog target:        $BUILD/target_cmplog"
echo "    cmplog (-c) target:   $BUILD/target_cmplog_cmplog"
echo "    n4 target:            $BUILD/target_n4"
echo "    oracle:               $BUILD/oracle"

# ── Step 2: Seed ─────────────────────────────────────────────────────────────
echo "[2/5] Creating and verifying seed..."

# Seed layout (19 bytes):
#   [0-3]  "OTTO"  — font magic
#   [4]    0x02    — num_tables: 2
#   [5]    0x47    — gdef_tag_byte: 'G'
#   [6]    0x47    — gsub_tag_byte: 'G'
#   [7]    0x01    — gdef_version_major: 1
#   [8]    0x02    — gdef_version_minor: 2 (ClassDef)
#   [9]    0x01    — gsub_version_major: 1
#   [10]   0x04    — lookup_type: 4 (ligature)
#   [11]   0x01    — lookup_count: 1
#   [12]   0x04    — gdef_class: LIGATURE bit set
#   [13]   0xAA    — prior_output_glyph
#   [14]   0xFF    — prior_coverage_glyph: != buf_codepoint → prior does NOT fire
#   [15]   0x42    — main_coverage_glyph: == buf_codepoint
#   [16]   0x02    — comp_count: 2
#   [17]   0x01    — component_glyph: non-zero
#   [18]   0x42    — buf_codepoint: == main_coverage [15], != prior_coverage [14]
#                    → prior lookup skipped → lig_props stays 0 → False branch
python3 -c "
import sys
sys.stdout.buffer.write(
    b'OTTO'    # font_magic
    b'\x02'    # num_tables: 2
    b'\x47'    # gdef_tag_byte: 'G'
    b'\x47'    # gsub_tag_byte: 'G'
    b'\x01'    # gdef_version_major: 1
    b'\x02'    # gdef_version_minor: 2
    b'\x01'    # gsub_version_major: 1
    b'\x04'    # lookup_type: 4 (ligature)
    b'\x01'    # lookup_count: 1
    b'\x04'    # gdef_class: LIGATURE
    b'\xAA'    # prior_output_glyph
    b'\xFF'    # prior_coverage_glyph: != buf_codepoint → prior doesn't fire
    b'\x42'    # main_coverage_glyph: == buf_codepoint
    b'\x02'    # comp_count: 2
    b'\x01'    # component_glyph: non-zero
    b'\x42'    # buf_codepoint: matches main_coverage, != prior_coverage → False branch
)
" > "$SEEDS/valid.bin"

if "$BUILD/oracle" "$SEEDS/valid.bin" | grep -q "FALSE_BRANCH"; then
    echo "    Seed verified: hits False branch."
else
    echo "    ERROR: seed does not hit False branch — aborting."
    exit 1
fi

# ── Step 3: cmplog campaign ───────────────────────────────────────────────────
echo "[3/5] Running cmplog (standard edge coverage + redqueen) for ${DURATION}s..."
afl-fuzz \
    -i "$SEEDS" \
    -o "$OUTPUT/cmplog" \
    -c "$BUILD/target_cmplog_cmplog" \
    -V "$DURATION" \
    -- "$BUILD/target_cmplog" @@ || true

CMPLOG_QUEUE="$OUTPUT/cmplog/default/queue"
CMPLOG_TOTAL=$(find "$CMPLOG_QUEUE" -name 'id:*' | wc -l)
echo "    Done. Queue: $CMPLOG_TOTAL seeds."

# ── Step 4: n4 campaign ───────────────────────────────────────────────────────
echo "[4/5] Running n4 (standard edge coverage, no cmplog) for ${DURATION}s..."
afl-fuzz \
    -i "$SEEDS" \
    -o "$OUTPUT/n4" \
    -V "$DURATION" \
    -- "$BUILD/target_n4" @@ || true

N4_QUEUE="$OUTPUT/n4/default/queue"
N4_TOTAL=$(find "$N4_QUEUE" -name 'id:*' | wc -l)
echo "    Done. Queue: $N4_TOTAL seeds."

# ── Step 5: Count False branch hits ──────────────────────────────────────────
echo "[5/5] Checking False branch hits in each queue..."

count_false_hits() {
    local queue_dir="$1"
    local hits=0
    while IFS= read -r -d '' seed; do
        if "$BUILD/oracle" "$seed" 2>/dev/null | grep -q "FALSE_BRANCH"; then
            hits=$((hits + 1))
        fi
    done < <(find "$queue_dir" -name 'id:*' -print0)
    echo "$hits"
}

CMPLOG_FALSE=$(count_false_hits "$CMPLOG_QUEUE")
N4_FALSE=$(count_false_hits "$N4_QUEUE")

# ── Summary ───────────────────────────────────────────────────────────────────
CMP_PCT=$(python3 -c "print(f'{$CMPLOG_FALSE/$CMPLOG_TOTAL*100:.1f}' if $CMPLOG_TOTAL > 0 else '0.0')")
N4_PCT=$(python3 -c "print(f'{$N4_FALSE/$N4_TOTAL*100:.1f}' if $N4_TOTAL > 0 else '0.0')")

SUMMARY="$OUTPUT/summary.txt"
tee "$SUMMARY" <<EOF

════════════════════════════════════════════════════
  Experiment: blocker_5 v3 — cross-table invariant
  Hypothesis: cmplog's redqueen degrades GDEF+GSUB
              structural property; no-cmplog preserves it
  Both fuzzers: standard edge coverage
  Only difference: cmplog has -c with AFL_LLVM_CMPLOG=1 binary
  Duration per fuzzer: ${DURATION}s
════════════════════════════════════════════════════

  cmplog (standard edge + redqueen):
    Queue size:         $CMPLOG_TOTAL seeds
    False branch hits:  $CMPLOG_FALSE / $CMPLOG_TOTAL  ($CMP_PCT%)

  n4 (standard edge, no cmplog):
    Queue size:         $N4_TOTAL seeds
    False branch hits:  $N4_FALSE / $N4_TOTAL  ($N4_PCT%)

  Queues saved to:
    $CMPLOG_QUEUE
    $N4_QUEUE

  Interpretation:
    If cmp_pct << n4_pct  → hypothesis supported
    If cmp_pct ≈ n4_pct   → corpus gap, not mutation degradation
    If both ≈ 100%         → target too simple (coverage not saturated)
    If both ≈ 0%           → property is generically fragile

════════════════════════════════════════════════════
EOF
