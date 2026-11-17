import pytest

from api import (
    create_listing,
    delete_listing,
    register_and_login,
)
from test_data import advertisement_data, build_listing_files, user_credentials
from helpers import build_auth_header


@pytest.fixture
def registered_user() -> dict:
    return register_and_login(user_credentials())


@pytest.fixture
def second_registered_user() -> dict:
    return register_and_login(user_credentials())


@pytest.fixture
def created_listing(registered_user: dict) -> int:
    headers = build_auth_header(registered_user["token"])
    response = create_listing(
        headers=headers,
        files=build_listing_files(advertisement_data()),
    )
    listing_id = response.json()["id"]
    yield listing_id
    delete_listing(listing_id=listing_id, headers=headers)

