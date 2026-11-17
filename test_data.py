import io
import random

from helpers import generate_test_image_bytes, generate_unique_email, normalize_price

DEFAULT_PASSWORD = "12345678"


def user_credentials() -> dict:
    return {
        "email": generate_unique_email(),
        "password": DEFAULT_PASSWORD,
        "submitPassword": DEFAULT_PASSWORD,
    }


def invalid_email_credentials() -> dict:
    return {
        "email": "kavun_37",
        "password": DEFAULT_PASSWORD,
        "submitPassword": DEFAULT_PASSWORD,
    }


def advertisement_data() -> dict:
    return {
        "name": f"Cadillac {random.randint(100, 999)}",
        "category": "Авто",
        "condition": "Новый",
        "city": "Москва",
        "description": "Успейте купить! Только сейчас!",
        "price": f"{random.randint(1_000_000, 40_000_000)}",
    }


def build_listing_files(data: dict, image_count: int = 3) -> list:
    files = [
        ("name", (None, data["name"])),
        ("category", (None, data["category"])),
        ("condition", (None, data["condition"])),
        ("city", (None, data["city"])),
        ("description", (None, data["description"])),
        ("price", (None, normalize_price(data["price"]))),
    ]
    for index in range(image_count):
        files.append(
            ("images", (f"test{index}.png", io.BytesIO(generate_test_image_bytes()), "image/png"))
        )
    return files

