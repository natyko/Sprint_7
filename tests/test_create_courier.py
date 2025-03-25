import allure
from data.data import (
    courier_without_password,
    courier_without_login,
    courier_without_first_name,
)


@allure.epic("Courier API Tests")
@allure.feature("Create Courier")
class TestCreateCourier:

    @allure.title("Successful Courier Creation")
    @allure.description("Verify courier creation with valid data")
    def test_create_courier_success(self, courier_helper, courier_data):
        courier_data = courier_helper.generate_random_courier()
        response = courier_helper.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json()["ok"] is True

        login_response = courier_helper.login_courier(
            {"login": courier_data["login"], "password": courier_data["password"]}
        )
        courier_id = login_response.json().get("id")
        courier_helper.delete_courier(courier_id)

    @allure.title("Duplicate Courier Creation")
    @allure.description("Verify duplicate courier creation returns a 409 error")
    def test_create_duplicate_courier(self, courier_helper, courier_data):
        courier_data = courier_helper.generate_random_courier()
        first_response = courier_helper.create_courier(courier_data)
        assert first_response.status_code == 201
        second_response = courier_helper.create_courier(courier_data)
        assert second_response.status_code == 409
        assert (
            second_response.json()["message"]
            == "Этот логин уже используется. Попробуйте другой."
        )

        login_response = courier_helper.login_courier(
            {"login": courier_data["login"], "password": courier_data["password"]}
        )
        courier_id = login_response.json().get("id")
        courier_helper.delete_courier(courier_id)

    @allure.title("Missing Required Fields")
    @allure.description("Verify courier creation without login")
    def test_create_courier_without_login(self, courier_helper):
        response = courier_helper.create_courier(courier_without_login)
        assert response.status_code == 400
        assert (
            response.json()["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Missing Required Fields")
    @allure.description("Verify courier creation without password")
    def test_create_courier_without_password(self, courier_helper):
        response = courier_helper.create_courier(courier_without_password)
        assert response.status_code == 400
        assert (
            response.json()["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Missing Required Fields")
    @allure.description("Verify courier creation without firstName")
    def test_create_courier_without_first_name(self, courier_helper):
        response = courier_helper.create_courier(courier_without_first_name)
        assert response.status_code == 409
        assert (
            response.json()["message"]
            == "Этот логин уже используется. Попробуйте другой."
        )
