import requests
from colorama import Fore, Style


def run_dir_scan(domain):
    print(Fore.LIGHTBLACK_EX + f"[*] Starting Directory Enumeration for {domain}...")
    try:
        with open("PHM_ReconTools/wordlists/directory.txt", "r") as file:
            dir_list = [line.strip() for line in file]
        found_dir = check_dir(domain, dir_list)
        print(Fore.LIGHTBLACK_EX + "\n|Directory Scan Completed| \n" + Style.RESET_ALL)
        print("\n")
        #for directory in found_dir:
            #print(Fore.LIGHTWHITE_EX + f"{directory}")
    except FileNotFoundError:
        pass


def check_dir(domain, dir_list):
    active_dirs = []
    for dir in dir_list:
        url = f"http://{domain}/{dir}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(Fore.LIGHTWHITE_EX + f"[+] Found: {url}" + Style.RESET_ALL)
                active_dirs.append(url)
        except requests.ConnectionError:
            print(Fore.RED + f"[!] Connection error for {url}" + Style.RESET_ALL)
        except requests.Timeout:
            print(Fore.RED + f"[!] Timeout error for {url}" + Style.RESET_ALL)
    return active_dirs
