from api import update_listing
from test_data import advertisement_data
from helpers import build_auth_header


class TestUpdateListing:
    def test_update_own_listing_price_returns_200(self, registered_user, created_listing):
        data = advertisement_data()
        data["price"] = "1001"

        response = update_listing(
            listing_id=created_listing,
            headers=build_auth_header(registered_user["token"]),
            data=data,
        )

        assert response.status_code == 200

    def test_update_listing_of_another_user_returns_401(
        self, created_listing, second_registered_user
    ):
        data = advertisement_data()
        data["price"] = "1001"

        response = update_listing(
            listing_id=created_listing,
            headers=build_auth_header(second_registered_user["token"]),
            data=data,
        )

        assert response.status_code == 401

