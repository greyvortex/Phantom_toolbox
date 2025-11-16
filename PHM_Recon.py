from PHM_ReconTools import *
import argparse
import os
import sys
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from colorama import Fore,Style
from datetime import datetime
import ctypes

# ------------ C lang integration ------------

lib_1 = ctypes.CDLL('./scanner.dll')
lib_1.main()

# ------------Current Date and Time------------
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

# ------------Argument Parser Setup------------
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")
parser.add_argument("target", help="domain name of the target")
parser.add_argument("-p" , "--port",type=str ,default="1-100" ,help="range of ports to be scanned (eg: -p 1-100)" )
parser.add_argument('-pS', action='store_true', help='Common port scan')
parser.add_argument('-pC', action='store_true', help='Custom port scan')
parser.add_argument('-pA', action='store_true', help='All ports scan')
parser.add_argument('-sT', action='store_true', help='TCP scan')
parser.add_argument('-sS', action='store_true', help='SYN scan')
parser.add_argument('-sA', action='store_true', help='ACK scan')
parser.add_argument('-sU', action='store_true', help='UDP scan')
parser.add_argument('-sF', action='store_true', help='FIN scan')
parser.add_argument('-sX', action='store_true', help='Xmas scan')
parser.add_argument('-sN', action='store_true', help='Null scan')
parser.add_argument('-sP', action='store_true', help='Ping host activity scan')
parser.add_argument('-wh', action='store_true', help='whois lookup')
parser.add_argument('-sub', action='store_true', help='Subdomain enumeration')
parser.add_argument('-dir', action='store_true', help='Directory scanner')
parser.add_argument("-c","--chat", type=str, help="Chat with Phantom AI (eg: -c 'What is my IP address?')")
args = parser.parse_args()

# ------------Extracting Arguments------------
target = args.target
port_range = args.port
start_port, end_port = map(int, port_range.split("-"))

#------------Main Function------------
def main():
    print(Fore.BLUE+ f"Phantom Recon v0.1.5 | By [Phantom Group]"+Style.RESET_ALL)
    print(Fore.BLUE+ f"Starting Recon at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
    if not (args.sT or args.sP or args.sA or args.sU or args.sF or args.sX or args.sN):
        if not (args.pS or args.pC or args.pA):
            args.sT = True
            args.pS = True

    if args.pS:
        PortScanner.common_ports(target,args)

    elif args.pA:
        PortScanner.all_ports(target,args)
        
    elif args.pC:
        PortScanner.custom_ports(target, start_port, end_port,args)

    if args.sub:
        subdomain.run_subdomain(target)
    
    if args.dir:
        directory.run_dir_scan(target)

    if args.wh:
        whois.whois_main(target)

    print(Fore.BLUE+ f"Recon completed at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
    sys.exit(0)

#------------Entry Point------------
if __name__ == "__main__":
    main()
   