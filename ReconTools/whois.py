"""
ReconTools/whois.py

WHOIS lookup module for Phantom Recon.
Stdlib-only (socket), no external WHOIS library required.
Follows referrals from IANA to the authoritative registry WHOIS server.

Wired up in Recon.py as:
    if args.wh:
        whois.whois_main(target)
"""

import socket
import re
from colorama import Fore, Style

IANA_WHOIS = "whois.iana.org"
DEFAULT_PORT = 43
SOCKET_TIMEOUT = 10
MAX_REFERRAL_HOPS = 3

# Non-standard / faster-path WHOIS servers for common TLDs
KNOWN_SERVERS = {
    "com": "whois.verisign-grs.com",
    "net": "whois.verisign-grs.com",
    "org": "whois.pir.org",
    "io": "whois.nic.io",
    "co": "whois.nic.co",
    "ai": "whois.nic.ai",
}

# Fields we try to pull out for the clean summary view
SUMMARY_FIELDS = {
    "Registrar": r"Registrar:\s*(.+)",
    "Creation Date": r"Creation Date:\s*(.+)",
    "Expiration Date": r"(?:Registry Expiry Date|Expiration Date):\s*(.+)",
    "Updated Date": r"Updated Date:\s*(.+)",
    "Name Server": r"Name Server:\s*(.+)",
    "Domain Status": r"Domain Status:\s*(.+)",
    "Registrant Org": r"Registrant Organization:\s*(.+)",
    "Registrant Country": r"Registrant Country:\s*(.+)",
}


def _query_whois_server(server, query, port=DEFAULT_PORT):
    with socket.create_connection((server, port), timeout=SOCKET_TIMEOUT) as sock:
        sock.sendall((query + "\r\n").encode("utf-8", errors="ignore"))
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
    return response.decode("utf-8", errors="ignore")


def _find_referral_server(whois_text):
    match = re.search(r"(?:refer|whois server|whois):\s*([\w.-]+\.\w+)", whois_text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def _get_tld(target):
    return target.rsplit(".", 1)[-1].lower()


def _perform_lookup(target, server=None):
    if server:
        return _query_whois_server(server, target)

    tld = _get_tld(target)
    current_server = KNOWN_SERVERS.get(tld, IANA_WHOIS)
    result = _query_whois_server(current_server, target)

    hops = 0
    while hops < MAX_REFERRAL_HOPS:
        referral = _find_referral_server(result)
        if not referral or referral.lower() == current_server.lower():
            break
        current_server = referral
        result = _query_whois_server(current_server, target)
        hops += 1

    return result


def _print_summary(raw_text):
    found_any = False
    for label, pattern in SUMMARY_FIELDS.items():
        matches = re.findall(pattern, raw_text, re.IGNORECASE)
        if not matches:
            continue
        found_any = True
        # Name Server can repeat; show all, dedup while keeping order
        seen = []
        for m in matches:
            val = m.strip()
            if val not in seen:
                seen.append(val)
        for val in seen:
            print(Fore.GREEN + f"  {label:<18}" + Style.RESET_ALL + f": {val}")
    if not found_any:
        print(Fore.YELLOW + "  No structured fields parsed — showing raw output below." + Style.RESET_ALL)


def whois_main(target, server=None, raw=False):
    """
    Entry point called from Recon.py via: whois.whois_main(target)

    target : domain name or IP address to look up
    server : optional specific WHOIS server to query directly (skips referrals)
    raw    : if True, print only the raw WHOIS response, skip the parsed summary
    """
    print(Fore.CYAN + f"[+] Running WHOIS lookup on {target}" + Style.RESET_ALL)

    try:
        raw_text = _perform_lookup(target, server)
    except socket.timeout:
        print(Fore.RED + f"[-] WHOIS query timed out for '{target}'." + Style.RESET_ALL)
        return None
    except socket.gaierror as e:
        print(Fore.RED + f"[-] Could not resolve WHOIS server ({e})." + Style.RESET_ALL)
        return None
    except OSError as e:
        print(Fore.RED + f"[-] Connection failed ({e})." + Style.RESET_ALL)
        return None

    if raw:
        print(raw_text)
        return raw_text

    print(Fore.CYAN + "-" * 50 + Style.RESET_ALL)
    _print_summary(raw_text)
    print(Fore.CYAN + "-" * 50 + Style.RESET_ALL)

    return raw_text