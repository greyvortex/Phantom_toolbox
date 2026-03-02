#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")



int main() {
    const char *ip = "192.168.1.1"; // Example IP address
    int port = 80; // Example port number
    int timeout_ms = 10; // Timeout in milliseconds
    int sock;
    struct sockaddr_in target;

    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Socket creation failed");
        return -1;
    }
    printf("Step 1");
    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr(ip);

    // Set timeout
    DWORD timeout = timeout_ms;
    setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (const char*)&timeout, sizeof(timeout));
    setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (const char*)&timeout, sizeof(timeout));
    printf("Step 2");

    int result = connect(sock, (struct sockaddr*)&target, sizeof(target));
    printf("Step 3");
    if (result == 0) {
        printf("Port %d is OPEN\n", port);
    } else {

        int err = WSAGetLastError();
        if (err == WSAETIMEDOUT) printf("Port %d is FILTERED\n", port);
        else printf("Port %d is CLOSED\n", port);

    }

    printf("Step 4");
    closesocket(sock);
    WSACleanup();


    return 0;
}