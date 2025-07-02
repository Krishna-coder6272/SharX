import sys
import os
from colorama import Fore, Style, init
init()

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from modules import scanner, brute, logger, exploit
import argparse

def main():
    print(Fore.CYAN + r"""
 ____  _              __  __
/ ___|| |__   __ _ _ _\ \\/ /
\___ \| '_ \ / _` | '__\  / 
 ___) | | | | (_| | |  /  \ 
|____/|_| |_|\__,_|_| /_/\_\

SharX - Advanced SMB Brute Force Tool
""" + Style.RESET_ALL)
    print(Fore.YELLOW + "[*] Author: Krishna Sahu" + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description="SharX - Advanced SMB Brute Force Tool")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Threads count")
    args = parser.parse_args()

    print("[+] Scanning target...")
    if not scanner.scan_target(args.target):
        print(Fore.RED + "[-] Brute force aborted. SMB port is closed." + Style.RESET_ALL)
        return

    print("[+] Running brute force attack...")
    creds = brute.run_brute_force(args.target, args.wordlist, args.threads)

    if creds:
        username, password = creds
        print(Fore.GREEN + f"[+] Valid credentials found: {username}:{password}" + Style.RESET_ALL)
        exploit.enumerate_shares(args.target, username, password)
    else:
        print(Fore.RED + "[-] No valid credentials found." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
