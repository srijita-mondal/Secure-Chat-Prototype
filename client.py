import socket
from crypto_utils import generate_mac

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Username: ")
password = input("Password: ")

client.send(username.encode())
client.send(password.encode())

session_id = client.recv(1024).decode()

if session_id == "AUTH_FAIL":
    print("Authentication failed")
    exit()

print("Secure session established:", session_id)

while True:
    msg = input("Message: ")
    mac = generate_mac(session_id, msg)
    payload = f"{msg}||{mac}"
    client.send(payload.encode())
