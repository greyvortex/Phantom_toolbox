#ifndef PORTSCANNER_H
#define PORTSCANNER_H

void initialize_sockets();
void cleanup_sockets();
int create_socket();
void close_socket(int sock);
int set_socket_timeout(int sock, int timeout_ms);
int connect_socket(int sock, const char *ip, int port);

#endif