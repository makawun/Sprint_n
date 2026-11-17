from api import create_listing
from test_data import advertisement_data, build_listing_files
from helpers import build_auth_header


class TestCreateListing:
    def test_create_listing_returns_201(self, registered_user):
        response = create_listing(
            headers=build_auth_header(registered_user["token"]),
            files=build_listing_files(advertisement_data()),
        )

        assert response.status_code == 201
        assert "id" in response.json()

