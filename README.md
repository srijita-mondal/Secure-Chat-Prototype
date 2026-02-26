# Secure-Chat-Prototype

**Status:** Educational prototype demonstrating authenticated client–server messaging over TCP.

Basic client–server secure chat with TCP sockets and hash-based message authentication.

This project implements a basic client–server secure chat system using TCP sockets.  
It demonstrates session establishment, access control, and message authentication using hash-based MAC mechanisms.

## Features
- TCP client–server communication
- User authentication
- Secure session establishment
- Message integrity using HMAC-SHA256
- Basic access control

## Usage

Start server:

```bash
python3 server.py
```

## Demonstration

### Server Side — Session Establishment and Message Reception
The server authenticates the client, establishes a session identifier, and verifies message integrity using MAC before displaying received messages.

![Server Output](server.png)

### Client Side — Authenticated Message Transmission
The client authenticates with the server, establishes a secure session, and sends authenticated messages protected with HMAC-based integrity checks.

![Client Output](client.png)


