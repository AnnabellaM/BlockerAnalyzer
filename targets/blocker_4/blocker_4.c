#include <stdint.h>
#include <stddef.h>
#include <string.h>

#define MIN_SIZE        8

static const uint8_t MAGIC_HEADER[2] = { 0xDE, 0xAD };
static const uint8_t MAGIC_TYPE[4]   = { 0xCA, 0xFE, 0xBA, 0xBE };
static const uint8_t MAGIC_FOOTER[2] = { 0xC0, 0xDE };

static int check_header(const uint8_t *data)
{
    return memcmp(data, MAGIC_HEADER, 2) == 0;
}

static int check_type(const uint8_t *data)
{
    return memcmp(data + 2, MAGIC_TYPE, 4) == 0;
}

static int check_footer(const uint8_t *data, size_t size)
{
    return memcmp(data + size - 2, MAGIC_FOOTER, 2) == 0;
}

static void process_packet(const uint8_t *data, size_t size)
{
    int a = check_header(data);
    int b = check_type(data);
    int c = check_footer(data, size);

    if (a && b && c) {
        __builtin_trap(); 
    }
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < MIN_SIZE)
        return 0;

    process_packet(data, size);

    return 0;
}