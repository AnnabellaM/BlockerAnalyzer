/*
 * blocker_5.c — Enriched synthetic harness for n4 vs cmplog experiment (v4)
 *
 * Blocking branch: hb-ot-layout.hh:518:7
 *   _hb_glyph_info_ligated_internal(info) → info->lig_props() & IS_LIG_BASE
 *   False side: blocked in cmplog (0 hits), hit by n4 (2,550,000 hits)
 *
 * v4 over v3: each format check is wrapped in __attribute__((noinline)).
 * This forces LLVM to preserve distinct basic-block boundaries at each call
 * site, giving AFL 25-35 unique edge IDs vs 7 in v3 (where clang merged
 * sequential if-checks into a single basic block).  Core invariant unchanged.
 *
 * ── Input layout (19 bytes minimum) ─────────────────────────────────────────
 *
 *   [0-3]  font_magic           "OTTO"
 *   [4]    num_tables           must be >= 2
 *   [5]    gdef_tag_byte        must be 'G' (0x47)
 *   [6]    gsub_tag_byte        must be 'G' (0x47)
 *   [7]    gdef_version_major   must be 1
 *   [8]    gdef_version_minor   must be 2 (ClassDef present)
 *   [9]    gsub_version_major   must be 1
 *   [10]   lookup_type          must be 4 (ligature substitution)
 *   [11]   lookup_count         must be >= 1
 *   [12]   gdef_class           glyph props; bit 0x04 = LIGATURE
 *   [13]   prior_output_glyph
 *   [14]   prior_coverage_glyph
 *   [15]   main_coverage_glyph
 *   [16]   comp_count           must be >= 2
 *   [17]   component_glyph      must be != 0
 *   [18]   buf_codepoint
 *
 * ── False branch invariant ───────────────────────────────────────────────────
 *
 *   data[18] != data[14]   prior lookup does NOT fire → lig_props stays 0
 *   data[18] == data[15]   main coverage passes
 *   data[12] &  0x04       GDEF classifies glyph as LIGATURE
 *   data[17] != 0          match_input passes
 */

#include <stdint.h>
#include <stddef.h>
#include <string.h>
#ifdef ORACLE_MODE
#include <stdio.h>
#include <stdlib.h>
#endif

/* ── Constants ──────────────────────────────────────────────────────────── */

#define HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE  0x04u
#define IS_LIG_BASE                          0x10u

/* ── Types ──────────────────────────────────────────────────────────────── */

typedef union {
    uint32_t u32;
    uint16_t u16[2];
    uint8_t  u8[4];
} hb_var_int_t;

typedef struct {
    uint32_t     codepoint;
    uint32_t     mask;
    uint32_t     cluster;
    hb_var_int_t var1;
    hb_var_int_t var2;
} hb_glyph_info_t;

#define glyph_props(info)  ((info)->var1.u16[0])
#define lig_props(info)    ((info)->var1.u8[2])

/* ── Format check functions (noinline = distinct AFL call-site edges) ────── */

__attribute__((noinline))
static int check_magic(const uint8_t *data) {
    return memcmp(data, "OTTO", 4) == 0;
}

__attribute__((noinline))
static int check_num_tables(uint8_t b) {
    return b >= 2;
}

__attribute__((noinline))
static int check_gdef_tag(uint8_t b) {
    return b == 0x47u;   /* 'G' */
}

__attribute__((noinline))
static int check_gsub_tag(uint8_t b) {
    return b == 0x47u;   /* 'G' */
}

__attribute__((noinline))
static int check_gdef_version(uint8_t major, uint8_t minor) {
    return major == 1u && minor == 2u;
}

__attribute__((noinline))
static int check_gsub_version(uint8_t major) {
    return major == 1u;
}

__attribute__((noinline))
static int check_lookup_type(uint8_t t) {
    return t == 4u;   /* ligature substitution */
}

__attribute__((noinline))
static int check_lookup_count(uint8_t n) {
    return n >= 1u;
}

__attribute__((noinline))
static int check_comp_count(uint8_t n) {
    return n >= 2u;
}

/* ── GSUB/GDEF logic ────────────────────────────────────────────────────── */

__attribute__((noinline))
static void set_lig_props_for_ligature(hb_glyph_info_t *info,
                                        unsigned lig_id,
                                        unsigned lig_num_comps)
{
    info->var1.u8[2] = (uint8_t)((lig_id << 5) | IS_LIG_BASE | (lig_num_comps & 0x0Fu));
}

__attribute__((noinline))
static int ligated_internal(const hb_glyph_info_t *info)
{
    return (lig_props(info) & IS_LIG_BASE) != 0;
}

/* THE BLOCKING BRANCH LIVES HERE. */
__attribute__((noinline))
static unsigned get_lig_num_comps(const hb_glyph_info_t *info)
{
    if (glyph_props(info) & HB_OT_LAYOUT_GLYPH_PROPS_LIGATURE) {
        if (ligated_internal(info)) {          /* BRANCH blocked=False */
            return lig_props(info) & 0x0Fu;
        } else {
#ifdef ORACLE_MODE
            puts("FALSE_BRANCH");
            fflush(stdout);
#endif
            return 1u;
        }
    }
    return 0u;
}

__attribute__((noinline))
static int match_input(uint8_t component_glyph)
{
    return component_glyph != 0;
}

__attribute__((noinline))
static void ligate_input(hb_glyph_info_t *cur, unsigned comp_count, unsigned lig_id)
{
    unsigned last = get_lig_num_comps(cur);   /* BLOCKING BRANCH inside */
    (void)last;
    set_lig_props_for_ligature(cur, lig_id, comp_count);
}

/* ══════════════════════════════════════════════════════════════════════════
 * LLVMFuzzerTestOneInput
 * ══════════════════════════════════════════════════════════════════════════ */
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < 19)
        return 0;

    /* Format checks — each through noinline fn → distinct AFL call-site edge */
    if (!check_magic(data))                          return 0;
    if (!check_num_tables(data[4]))                  return 0;
    if (!check_gdef_tag(data[5]))                    return 0;
    if (!check_gsub_tag(data[6]))                    return 0;
    if (!check_gdef_version(data[7], data[8]))       return 0;
    if (!check_gsub_version(data[9]))                return 0;
    if (!check_lookup_type(data[10]))                return 0;
    if (!check_lookup_count(data[11]))               return 0;

    uint8_t gdef_class           = data[12];
    uint8_t prior_output_glyph   = data[13];
    uint8_t prior_coverage_glyph = data[14];
    uint8_t main_coverage_glyph  = data[15];
    uint8_t comp_count           = data[16];
    uint8_t component_glyph      = data[17];
    uint8_t buf_codepoint        = data[18];

    if (!check_comp_count(comp_count))               return 0;

    /* Initialise buffer glyph — lig_props starts at 0, not a raw input byte */
    hb_glyph_info_t cur = {0};
    cur.codepoint   = buf_codepoint;
    cur.var1.u16[0] = (uint16_t)gdef_class;
    cur.var1.u8[2]  = 0;

    /* Prior GSUB pass — cmplog redqueen target: buf_codepoint vs prior_coverage */
    uint8_t active_codepoint;
    if (buf_codepoint == prior_coverage_glyph) {
        ligate_input(&cur, comp_count, /*lig_id=*/1u);   /* sets IS_LIG_BASE */
        active_codepoint = prior_output_glyph;
    } else {
        active_codepoint = buf_codepoint;
    }

    /* Main GSUB coverage check — cmplog redqueen target: active vs main_coverage */
    if (active_codepoint != main_coverage_glyph)     return 0;

    if (!match_input(component_glyph))               return 0;

    /* Main ligate_input — BLOCKING BRANCH inside get_lig_num_comps */
    ligate_input(&cur, comp_count, /*lig_id=*/2u);

    return 0;
}

/* ── Oracle ─────────────────────────────────────────────────────────────── */
#ifdef ORACLE_MODE
int main(int argc, char **argv)
{
    if (argc < 2) { fprintf(stderr, "usage: oracle <input_file>\n"); return 1; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror(argv[1]); return 1; }
    uint8_t buf[4096];
    size_t n = fread(buf, 1, sizeof(buf), f);
    fclose(f);
    LLVMFuzzerTestOneInput(buf, n);
    return 0;
}
#endif
