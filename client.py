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

auth = client.recv(1024)

if auth != b"AUTH_OK":
    print("Authentication failed")
    client.close()
    exit()

print("Secure session established")

while True:
    msg = input("Message: ")
    mac = generate_mac(msg)
    payload = f"{msg}||{mac}"
    client.send(payload.encode())
