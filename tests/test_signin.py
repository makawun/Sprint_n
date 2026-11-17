from api import signin


class TestSignin:
    def test_signin_with_valid_credentials_returns_201(self, registered_user):
        response = signin({
            "email": registered_user["email"],
            "password": registered_user["password"],
        })

        assert response.status_code == 201

    def test_signin_response_contains_access_token(self, registered_user):
        response = signin({
            "email": registered_user["email"],
            "password": registered_user["password"],
        })

        assert "access_token" in response.json()["token"]