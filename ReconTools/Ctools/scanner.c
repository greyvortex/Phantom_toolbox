#include  <stdlib.h>
#include  <stdio.h>
#include  <string.h>
#include "scanner.h"

#ifdef _WIN32
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #pragma comment(lib, "ws2_32.lib")
    typedef SOCKET socket_t;
    #define CLOSE_SOCKET closesocket
    #define SOCKET_ERROR_CODE WSAGetLastError()
    #define INIT_NETWORKING() { WSADATA wsaData; WSAStartup(MAKEWORD(2,2), &wsaData); }
    #define CLEANUP_NETWORKING() WSACleanup()
#else
    #include <unistd.h>
    #include <arpa/inet.h>
    #include <netinet/in.h>
    #include <sys/socket.h>
    typedef int socket_t;
    #define CLOSE_SOCKET close
    #define SOCKET_ERROR_CODE errno
    #define INIT_NETWORKING()
    #define CLEANUP_NETWORKING()
#endif

int main(int argc , char *argv[]){
    if(argc != 2){
        printf("Usage: %s <IP_ADDRESS>\n", argv[0]);
        return 1;
    }

    const char *ip_address = argv[1];
    struct in_addr addr;

    INIT_NETWORKING();

    if(inet_pton(AF_INET, ip_address, &addr) != 1){
        printf("Invalid IP address format: %s\n", ip_address);
        CLEANUP_NETWORKING();
        return 1;
    }

    printf("Valid IP address: %s\n", ip_address);

    CLEANUP_NETWORKING();
    return 0;
}

int scan_port(const char *ip_address, int port){
    socket_t sock;
    struct sockaddr_in server_addr;
    int result;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock < 0){
        perror("Socket creation failed");
        return -1;
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip_address, &server_addr.sin_addr);

    result = connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr));
    CLOSE_SOCKET(sock);

    if(result == 0){
        return 1; // Port is open
    } else {
        return 0; // Port is closed
    }
}