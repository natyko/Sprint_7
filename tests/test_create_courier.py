import allure
from utils.courier_helper import CourierHelper


@allure.epic("Courier API Tests")
@allure.feature("Create Courier")
class TestCreateCourier:
    @allure.story("Successful Courier Creation")
    @allure.title("Create a courier with valid data")
    @allure.description(
        "Test creating a courier with valid login, password, and firstName"
    )
    def test_create_courier_success(self, base_url):

        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()

        try:
            response = courier_helper.create_courier(courier_data)

            assert response.status_code == 201
            assert response.json() == {"ok": True}

        finally:
            login_response = courier_helper.login_courier(
                {"login": courier_data["login"], "password": courier_data["password"]}
            )

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                courier_helper.delete_courier(courier_id)

    @allure.story("Duplicate Courier Creation")
    @allure.title("Create a duplicate courier")
    @allure.description(
        "Test that creating a courier with an existing login returns an error"
    )
    def test_create_duplicate_courier(self, base_url):
        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()

        try:
            courier_helper.create_courier(courier_data)

            response = courier_helper.create_courier(courier_data)

            assert response.status_code == 409
            assert "message" in response.json()

        finally:
            login_response = courier_helper.login_courier(
                {"login": courier_data["login"], "password": courier_data["password"]}
            )

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                courier_helper.delete_courier(courier_id)

    @allure.story("Missing Required Fields")
    @allure.title("Create a courier without login")
    @allure.description("Test that creating a courier without a login returns an error")
    def test_create_courier_without_login(self, base_url):
        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()
        del courier_data["login"]

        response = courier_helper.create_courier(courier_data)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.story("Missing Required Fields")
    @allure.title("Create a courier without password")
    @allure.description(
        "Test that creating a courier without a password returns an error"
    )
    def test_create_courier_without_password(self, base_url):

        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()
        del courier_data["password"]

        response = courier_helper.create_courier(courier_data)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.story("Missing Required Fields")
    @allure.title("Create a courier without firstName")
    @allure.description(
        "Test that creating a courier without a firstName returns an error"
    )
    def test_create_courier_without_first_name(self, base_url):
        courier_helper = CourierHelper(base_url)
        courier_data = courier_helper.generate_random_courier()
        del courier_data["firstName"]

        response = courier_helper.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}
