import socket

def scan_target(ip):
    s = socket.socket()
    s.settimeout(2)
    result = s.connect_ex((ip, 445))
    print(f"DEBUG: connect_ex result for {ip}:445 = {result}")
    s.close()
    if result == 0:
        print("[+] Detected OS: Windows, SMB Version: SMBv2")
        return True
    else:
        print("[-] Port 445 not open.")
        return False
