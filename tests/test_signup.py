from api import signup
from test_data import invalid_email_credentials, user_credentials


class TestSignup:
    def test_signup_with_unique_email_returns_201(self):
        response = signup(user_credentials())

        assert response.status_code == 201

    def test_signup_with_existing_email_returns_400(self, registered_user):
        response = signup({
            "email": registered_user["email"],
            "password": registered_user["password"],
            "submitPassword": registered_user["password"],
        })

        assert response.status_code == 400

    def test_signup_with_invalid_email_returns_400(self):
        response = signup(invalid_email_credentials())

        assert response.status_code == 400

