#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "portscanner.h"

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <IP_ADDRESS> <PORT> <TIMEOUT_MS>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char *ip = argv[1];
    int port = atoi(argv[2]);
    int timeout_ms = atoi(argv[3]);

    if (port <= 0 || port > 65535) {
        fprintf(stderr, "Invalid port number. Must be between 1 and 65535.\n");
        return EXIT_FAILURE;
    }

    if (timeout_ms < 0) {
        fprintf(stderr, "Timeout must be a non-negative integer.\n");
        return EXIT_FAILURE;
    }

    int result = scan_port(ip, port, timeout_ms);
    if (result < 0) {
        fprintf(stderr, "Error scanning port %d on %s\n", port, ip);
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;


}