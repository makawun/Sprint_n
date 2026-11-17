from api import delete_listing
from helpers import build_auth_header


class TestDeleteListing:
    def test_delete_own_listing_returns_200(self, registered_user, created_listing):
        response = delete_listing(
            listing_id=created_listing,
            headers=build_auth_header(registered_user["token"]),
        )

        assert response.status_code == 200
        assert response.json().get("message") == "Объявление удалено успешно"