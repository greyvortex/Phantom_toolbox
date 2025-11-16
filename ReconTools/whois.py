import socket
from colorama import Fore, Style


whois_servers = {
    ".com": "whois.verisign-grs.com",
    ".net": "whois.verisign-grs.com",
    ".org": "whois.pir.org",
    ".in": "whois.registry.in",
    ".co.in": "whois.registry.in",
    ".edu.in": "whois.registry.in",
    ".gov.in": "whois.registry.in",
    ".io": "whois.nic.io",
    ".me": "whois.nic.me"
}

def whois_main(target):
    print(Fore.LIGHTBLACK_EX + f"[+] Performing WHOIS lookup for: {target}")
    result = whois_lookup(target)
    print(Fore.LIGHTBLACK_EX + f"{result}")

def extract_tld(target):
    parts = target.lower().split('.')
    if len(parts) >= 3:
        sub_tld = "." + parts[-2] + "." + parts[-1]  # e.g., .edu.in
        if sub_tld in whois_servers:
            return sub_tld
    if len(parts) >= 2:
        tld = "." + parts[-1]  # e.g., .com
        if tld in whois_servers:
            return tld
    return None


def whois_lookup(target):
    tld = extract_tld(target)
    if not tld:
        return Fore.RED + f"[-] Unsupported or unknown TLD for domain '{target}'."+  Style.RESET_ALL
    server = whois_servers[tld]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, 43))
            s.sendall((target + "\r\n").encode())
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        return response.decode(errors="ignore")
    except Exception as e:
        return f"[!] Error connecting to WHOIS server: {e}"