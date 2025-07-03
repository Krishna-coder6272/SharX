import random
import string


# Genrate your own lists Randomly
# 👇 How many combos you want (set to 300 for example)
combo_count = 300

# Sample base usernames and passwords
base_usernames = ["admin", "user", "root", "test", "guest", "krishna", "dev", "local"]
base_passwords = ["1234", "admin", "password", "root", "toor", "test123", "welcome", "qwerty"]

# Extra password patterns to mix


def generate_password():
    base = random.choice(base_passwords)
    suffix = ''.join(random.choices(string.digits, k=2))
    special = random.choice(["", "!", "@", "#"])
    return base + suffix + special

# Create combo list
combos = set()
while len(combos) < combo_count:
    u = random.choice(base_usernames)
    p = generate_password()
    combos.add(f"{u}:{p}")

# Write to file
with open("small.txt", "w") as f:
    for combo in combos:
        f.write(combo + "\n")

print(f"[+] Combo list saved to small.txt with {len(combos)} combos.")
