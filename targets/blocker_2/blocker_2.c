#include <stdint.h>
#include <stddef.h>
#include <string.h>

#define PACKET_SIZE     64
#define PROTO_BASIC     0x01
#define PROTO_EXTENDED  0x02
#define PROTO_LEGACY    0x03
#define PROTO_SECURE    0x04
#define PROTO_UNKNOWN   0x00

typedef struct {
    uint8_t data[PACKET_SIZE];
    size_t  data_len;
} FilePacket;

static int secret_unlocked = 0;

static void process_secret(FilePacket *fp)
{
    secret_unlocked = 1;
    (void)fp;
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < 2)
        return 0;

    FilePacket fp;
    memset(&fp, 0, sizeof(fp));

    fp.data_len = (size - 1) < sizeof(fp.data)
                  ? (size - 1) : sizeof(fp.data);
    memcpy(fp.data, data + 1, fp.data_len);

    if (secret_unlocked) {
        __builtin_trap();
    }

    return 0;
}