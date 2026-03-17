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
static int target_reached  = 0;

static void process_secret(FilePacket *fp)
{
    secret_unlocked = 1;
    (void)fp;
}

static uint8_t compute_checksum(const uint8_t *data, size_t len)
{
    uint32_t sum = 0;
    for (size_t i = 0; i < len; i++)
        sum += data[i];
    return (uint8_t)(sum & 0xFF);
}

static void FUNC(FilePacket *fp)
{
    uint8_t computed = compute_checksum(fp->data, fp->data_len);

    if (computed == PROTO_BASIC) {
    } else if (computed == PROTO_EXTENDED) {
    } else if (computed == PROTO_LEGACY) {
    } else if (computed == PROTO_SECURE) {
        process_secret(fp);
    }
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    if (size < 2)
        return 0;

    if (data[0] == 0xFF) {
        secret_unlocked = 1;
        return 0;
    }

    FilePacket fp;
    memset(&fp, 0, sizeof(fp));

    fp.data_len = (size - 1) < sizeof(fp.data)
                  ? (size - 1) : sizeof(fp.data);
    memcpy(fp.data, data + 1, fp.data_len);

    FUNC(&fp);

    if (secret_unlocked) {
        target_reached = 1;
    }

    return 0;
}