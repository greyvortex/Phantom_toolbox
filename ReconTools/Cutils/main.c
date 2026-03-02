#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "scanner.h"

typedef struct{
    char ip;
    int st_port;
    int end_port;
} target;

void port_scanner(const char *ip, int start_port, int end_port) {
    initialize_sockets();
    printf("Scanning %s from port %d to %d...\n", ip, start_port, end_port);
    cleanup_sockets();
}

int main(){
    target main;
    main.ip = "120.12.12.0";
    main.st_port = 22;
    main.end_port = 23;
    port_scanner(&main.ip, main.st_port , main.end_port);
}