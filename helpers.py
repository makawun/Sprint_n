import random
import string
import uuid


def generate_random_string(length: int = 8) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choices(alphabet, k=length))


def generate_unique_email(prefix: str = "spb") -> str:
    return f"{prefix}{random.randint(100, 999)}_{uuid.uuid4().hex[:8]}@gmail.com"


def normalize_price(price_text: str) -> str:
    return price_text.strip().replace(" ", "")


def build_auth_header(token: str) -> dict:
    return {"authorization": f"Bearer {token}"}


def generate_test_image_bytes() -> bytes:
    return (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
        b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01"
        b"\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
    )