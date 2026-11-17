import requests

from urls import (
    CREATE_LISTING_URL,
    LISTINGS_URL,
    SIGNIN_URL,
    SIGNUP_URL,
    UPDATE_OFFER_URL,
)


def signup(payload: dict) -> requests.Response:
    return requests.post(SIGNUP_URL, json=payload)


def signin(payload: dict) -> requests.Response:
    return requests.post(SIGNIN_URL, json=payload)


def register_and_login(credentials: dict) -> dict:
    signup(credentials)
    signin_response = signin({
        "email": credentials["email"],
        "password": credentials["password"],
    })
    return {
        "email": credentials["email"],
        "password": credentials["password"],
        "token": signin_response.json()["token"]["access_token"],
    }


def create_listing(headers: dict, files: list) -> requests.Response:
    return requests.post(CREATE_LISTING_URL, headers=headers, files=files)


def update_listing(listing_id: int, headers: dict, data: dict) -> requests.Response:
    return requests.patch(f"{UPDATE_OFFER_URL}/{listing_id}", headers=headers, data=data)


def delete_listing(listing_id: int, headers: dict) -> requests.Response:
    return requests.delete(f"{LISTINGS_URL}/{listing_id}", headers=headers)

