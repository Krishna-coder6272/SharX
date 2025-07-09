# 👿 SharX - Advanced SMB Brute Force Tool


---

## Description
SharX is an advanced SMB brute force tool designed to scan targets for open SMB ports and perform brute force attacks using username-password combinations. It supports multithreading for faster scanning and includes a basic exploit module for enumerating SMB shares.

---

## 💥 Features
- SMB port scanning before brute force
- Multithreaded brute force attacks
- CSV logging of valid credentials
- Basic SMB share enumeration exploit
- Easy command-line interface
- Create your own username:password lists using passgen in modules 

---





## 💯 Installation
Make sure you have Python 3 installed along with the required dependencies.

Install dependencies with:

- pip install requirements.txt


---


## 💪 Usage
python3 sharx.py <target_ip> -w <path_to_wordlist> -t <threads>

## Example:
python3 sharx.py 10.10.116.59 -w wordlists/common.txt -t 5

---


## 😇 AUTHOR
Krishna Sahu

---


## ❌ Disclaimer
Use this tool only on systems you own or have explicit permission to test. Unauthorized use is illegal.

---


