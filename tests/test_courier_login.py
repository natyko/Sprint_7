import allure
import requests

from utils.courier_helper import CourierHelper


@allure.epic("Courier API Tests")
@allure.feature("Courier Login")
class TestCourierLogin:
    @allure.story("Successful Login")
    @allure.title("Login with valid credentials")
    @allure.description("Test logging in with valid courier credentials")
    def test_courier_login_success(self, base_url):

        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()

        try:

            create_response = courier_helper.create_courier(courier_data)
            assert create_response.status_code == 201

            login_data = {
                "login": courier_data["login"],
                "password": courier_data["password"],
            }
            login_response = courier_helper.login_courier(login_data)

            assert login_response.status_code == 200
            assert "id" in login_response.json()

        finally:
            login_response = courier_helper.login_courier(
                {"login": courier_data["login"], "password": courier_data["password"]}
            )

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                courier_helper.delete_courier(courier_id)

    @allure.story("Missing Required Fields")
    @allure.title("Login without login field")
    @allure.description(
        "Test that logging in without providing a login returns an error"
    )
    def test_courier_login_without_login(self, base_url):

        courier_helper = CourierHelper(base_url)
        login_data = {"password": "testpassword"}

        response = courier_helper.login_courier(login_data)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.story("Missing Required Fields")
    @allure.title("Login without password field")
    @allure.description(
        "Test that logging in without providing a password returns an error"
    )
    def test_courier_login_without_password(self, base_url):

        courier_helper = CourierHelper(base_url)
        login_data = {"login": "testlogin"}

        response = courier_helper.login_courier(login_data)

        assert response.status_code == 504

        try:
            response_data = response.json()
            assert "message" in response_data
        except requests.exceptions.JSONDecodeError:

            assert response.text

    @allure.story("Invalid Credentials")
    @allure.title("Login with incorrect credentials")
    @allure.description(
        "Test that logging in with incorrect credentials returns an error"
    )
    def test_courier_login_with_incorrect_credentials(self, base_url):
        # Arrange
        courier_helper = CourierHelper(base_url)
        login_data = {
            "login": "nonexistentlogin12345",
            "password": "wrongpassword12345",
        }

        response = courier_helper.login_courier(login_data)

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.story("Invalid Credentials")
    @allure.title("Login with correct login but wrong password")
    @allure.description(
        "Test that logging in with a correct login but wrong password returns an error"
    )
    def test_courier_login_with_wrong_password(self, base_url):

        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()

        try:
            create_response = courier_helper.create_courier(courier_data)
            assert create_response.status_code == 201

            login_data = {
                "login": courier_data["login"],
                "password": "wrongpassword12345",
            }
            login_response = courier_helper.login_courier(login_data)

            assert login_response.status_code == 404
            assert "message" in login_response.json()

        finally:
            correct_login_response = courier_helper.login_courier(
                {"login": courier_data["login"], "password": courier_data["password"]}
            )

            if correct_login_response.status_code == 200:
                courier_id = correct_login_response.json()["id"]
                courier_helper.delete_courier(courier_id)
