import hmac
import hashlib
import secrets

SECRET_KEY = b"shared_secret_key"

def generate_mac(session_id: str, message: str) -> str:
    data = f"{session_id}:{message}".encode()
    mac = hmac.new(SECRET_KEY, data, hashlib.sha256)
    return mac.hexdigest()

def verify_mac(session_id: str, message: str, mac_value: str) -> bool:
    expected = generate_mac(session_id, message)
    return hmac.compare_digest(expected, mac_value)

def new_session_id():
    return secrets.token_hex(8)
