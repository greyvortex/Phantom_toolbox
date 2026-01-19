#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "portscanner.h"

#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")

#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#endif

int scan_port(const char *ip, int port, int timeout_ms) {
    int sock;
    struct sockaddr_in target;

#ifdef _WIN32
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);
#endif

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Socket creation failed");
        return -1;
    }

    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr(ip);

    // Set timeout
#ifdef _WIN32
    DWORD timeout = timeout_ms;
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (const char*)&timeout, sizeof(timeout));
    setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (const char*)&timeout, sizeof(timeout));
#else
    struct timeval tv;
    tv.tv_sec = timeout_ms / 1000;
    tv.tv_usec = (timeout_ms % 1000) * 1000;
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (const char*)&tv, sizeof(tv));
    setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (const char*)&tv, sizeof(tv));
#endif

    int result = connect(sock, (struct sockaddr*)&target, sizeof(target));
    if (result == 0) {
        printf("Port %d is OPEN\n", port);
    } else {
#ifdef _WIN32
        int err = WSAGetLastError();
        if (err == WSAETIMEDOUT) printf("Port %d is FILTERED\n", port);
        else printf("Port %d is CLOSED\n", port);
#else
        if (errno == ETIMEDOUT) printf("Port %d is FILTERED\n", port);
        else printf("Port %d is CLOSED\n", port);
#endif
    }

#ifdef _WIN32
    closesocket(sock);
    WSACleanup();
#else
    close(sock);
#endif

    return 0;
}

int main() {
    const char *target_ip = "192.168.1.1";
    for (int port = 20; port <= 1024; port++) {
        scan_port(target_ip, port, 500);
    }
    return 0;
}