import socket
import json
from crypto_utils import verify_mac

HOST = "0.0.0.0"
PORT = 5000

with open("users.json") as f:
    USERS = json.load(f)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server listening...")

conn, addr = server.accept()
print("Connected:", addr)

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

if USERS.get(username) != password:
    conn.send(b"AUTH_FAIL")
    conn.close()
else:
    conn.send(b"AUTH_OK")

while True:
    data = conn.recv(4096).decode()
    if not data:
        break

    msg, mac = data.split("||")
    if verify_mac(msg, mac):
        print(f"[{username}] {msg}")
    else:
        print("Integrity check failed")
