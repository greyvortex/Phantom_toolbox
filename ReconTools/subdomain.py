import requests
from colorama import Fore, Style
#from concurrent.futures import ThreadPoolExecutor, as_completed

def check_subdomain(domain, subdomain_list):
    for sub in subdomain_list:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(Fore.LIGHTWHITE_EX + f"[+] Found: {url}")
        except requests.ConnectionError:
            pass

def run_subdomain(domain): 
    print(Fore.LIGHTBLACK_EX + f"[*] Starting Subdomain Enumeration for {domain}...")
    try:
        with open("ReconTools\wordlists\subdomain.txt", "r") as file:
            subdomains = [line.strip() for line in file]
        check_subdomain(domain, subdomains)
        print(Fore.LIGHTBLACK_EX +"|Subdomain Scan Completed| \n" + Style.RESET_ALL)
        print("=="*50, "\n")

    except FileNotFoundError:
        print(Fore.RED + "[!] Error: Subdomain wordlist not found." + Style.RESET_ALL)