import allure
from data.data import (
    invalid_credentials,
    wrong_password,
)


@allure.epic("Courier API Tests")
@allure.feature("Courier Login")
class TestCourierLogin:
    @allure.title("Successful Login")
    @allure.description(
        "Verify that a courier can log in successfully with valid credentials"
    )
    def test_successful_login(self, courier_helper, registered_courier):
        """Verify that a courier can log in successfully with valid credentials."""
        creds = registered_courier
        response = courier_helper.login_courier(
            {"login": creds["login"], "password": creds["password"]}
        )
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Missing Password Field")
    @allure.description("Attempt to log in without providing a password.")
    def test_login_without_password(self, courier_helper, courier_data):
        courier_data = courier_helper.generate_random_courier()
        courier_helper.create_courier(courier_data)

        response = courier_helper.login_courier({"login": courier_data["login"]})
        assert response.status_code == 504

    @allure.title("Invalid Credentials")
    @allure.description(
        "Attempt to log in with credentials that don't exist in the system."
    )
    def test_login_with_invalid_credentials(self, courier_helper):
        """Attempt to log in with invalid credentials. Expect a 404 error."""
        response = courier_helper.login_courier(invalid_credentials)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Wrong Password")
    @allure.description("Attempt to log in with a valid login but incorrect password.")
    def test_login_with_wrong_password(self, courier_helper, registered_courier):
        """Attempt to log in with a valid login but wrong password. Expect a 404 error."""
        creds = registered_courier
        response = courier_helper.login_courier(
            {"login": creds["login"], "password": wrong_password}
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
