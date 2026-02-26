import hmac
import hashlib

SECRET_KEY = b"shared_secret_key"

def generate_mac(message: str) -> str:
    mac = hmac.new(SECRET_KEY, message.encode(), hashlib.sha256)
    return mac.hexdigest()

def verify_mac(message: str, mac_value: str) -> bool:
    expected = generate_mac(message)
    return hmac.compare_digest(expected, mac_value)
