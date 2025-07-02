import csv
import os

csv_file = 'output/results.csv'
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

# Create file with header if not exists
if not os.path.isfile(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Target IP', 'Username', 'Password', 'Status'])

def log_result(ip, username, password, status):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip, username, password, status])
