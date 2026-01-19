#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "scanner.h"

int main(int argc , char *argv[]){
    if(argc != 2){
        printf("No extra arguments needed.\n");
    }
    scan_port(argv[1], 80);

    return 0;
}