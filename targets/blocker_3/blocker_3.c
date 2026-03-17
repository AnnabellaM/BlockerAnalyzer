#include <stdint.h>
#include <stddef.h>
#include <string.h>

#define PACKET_SIZE     64

typedef struct {
    int unlocked;
} SessionState;

#ifdef UNLOCK_SECRET
static SessionState g_session = { 1 };
#else
static SessionState g_session = { 0 };
#endif

static int check_gate(SessionState *s)
{
    return s->unlocked;
}

static void process_packet(const uint8_t *data, size_t len)
{
    int gate = check_gate(&g_session);

    if (gate) {
        __builtin_trap();  
    }

    (void)data;
    (void)len;
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < 1)
        return 0;

    process_packet(data, size);

    return 0;
}
