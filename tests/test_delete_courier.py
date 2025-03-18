import allure
import requests

from utils.courier_helper import CourierHelper


@allure.epic("Courier Management")
@allure.feature("Courier Deletion")
class TestCourierDeletion:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    @allure.title("Test successful courier deletion")
    @allure.description("Check that a courier can be successfully deleted")
    def test_courier_deletion_success(self, base_url):
        courier_helper = CourierHelper(base_url)

        courier_data = courier_helper.generate_random_courier()

        create_response = courier_helper.create_courier(courier_data)
        assert create_response.status_code == 201

        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
        login_response = courier_helper.login_courier(login_data)
        assert login_response.status_code == 200

        courier_id = login_response.json()["id"]

        response = requests.delete(f"{base_url}/courier/{courier_id}")

        assert response.status_code == 200
        assert response.json() == {"ok": True}

        login_response = courier_helper.login_courier(login_data)
        assert login_response.status_code == 404

    @allure.title("Test deletion of nonexistent courier ID")
    @allure.description(
        "Verify that attempting to delete a nonexistent courier ID returns the expected error"
    )
    def test_courier_deletion_nonexistent_id(self, base_url):

        non_existent_id = 999999999

        response = requests.delete(f"{base_url}/courier/{non_existent_id}")

        assert response.status_code == 404
        assert "message" in response.json()
        assert response.json()["message"]
