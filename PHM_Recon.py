from PHM_ReconTools import *
from PHM_UtilityTools import *
import argparse
import os
import sys
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from colorama import Fore,Style
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

#arguments
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")
#parser.add_argument("-td" , "--target" ,type=str ,required=True , help="domain name of the target" )
parser.add_argument("target", help="domain name of the target")
parser.add_argument("-p" , "--port",type=str ,default="1-100" ,help="range of ports to be scanned (eg: -p 1-100)" )
parser.add_argument('-pS', action='store_true', help='Common port scan')
parser.add_argument('-pC', action='store_true', help='Custom port scan')
parser.add_argument('-pA', action='store_true', help='All ports scan')
#parser.add_argument('--range', type=str, default='common', help='Specify the scan range')
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
#parser.add_argument('--help', action='help', help='Show this help message and exit')

args = parser.parse_args()


target = args.target
port_range = args.port
start_port, end_port = map(int, port_range.split("-"))

if __name__ == "__main__":
    print(Fore.BLUE+ f"Phantom Recon v0.1.5 | By [Phantom Group]"+Style.RESET_ALL)
    print(Fore.BLUE+ f"Starting Recon at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
    updatemanager.get_latest_commit_hash()
    updatemanager.comparator(updatemanager.get_latest_commit_hash())

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

    PHM_UtilityTools.log_manager(target, " | ".join([arg for arg in vars(args) if getattr(args, arg) and arg not in ['target', 'port']]), PortScanner.open_ports, start_time=current_time, additional_info=f"Port Range: {port_range}")
    print(Fore.BLUE+ f"Recon completed at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
    sys.exit(0)