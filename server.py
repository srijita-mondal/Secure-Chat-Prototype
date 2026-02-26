import socket
import json
from crypto_utils import verify_mac, new_session_id

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

username = conn.recv(1024).decode().strip()
password = conn.recv(1024).decode().strip()

if USERS.get(username) != password:
    conn.send(b"AUTH_FAIL")
    conn.close()
    exit()

session_id = new_session_id()
conn.send(session_id.encode())

print("Session established:", session_id)

while True:
    data = conn.recv(4096).decode()
    if not data:
        break

    try:
        msg, mac = data.split("||")
        if verify_mac(session_id, msg, mac):
            print(f"[{username}] {msg}")
        else:
            print("Integrity check failed")
    except:
        print("Malformed packet")
