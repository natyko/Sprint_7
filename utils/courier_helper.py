import allure
import requests
import random
import string
import json
from urls import BASE_URL


class CourierHelper:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_courier():
        return {
            "login": CourierHelper.generate_random_string(),
            "password": CourierHelper.generate_random_string(),
            "firstName": CourierHelper.generate_random_string(),
        }

    @allure.step("Create a courier")
    def create_courier(self, courier_data):
        headers = {"Content-Type": "application/json"}
        return requests.post(
            f"{self.base_url}/courier", data=json.dumps(courier_data), headers=headers
        )

    @allure.step("Log in a courier")
    def login_courier(self, credentials):
        headers = {"Content-Type": "application/json"}
        return requests.post(
            f"{self.base_url}/courier/login",
            data=json.dumps(credentials),
            headers=headers,
        )

    @allure.step("Delete a courier")
    def delete_courier(self, courier_id):
        headers = {"Content-Type": "application/json"}
        return requests.delete(f"{self.base_url}/courier/{courier_id}", headers=headers)

    @allure.step("Register and return courier login/password/id")
    def register_new_courier_and_return_login_password_id(self):
        courier_data = self.generate_random_courier()
        create_response = self.create_courier(courier_data)
        assert create_response.status_code == 201
        login_response = self.login_courier(
            {"login": courier_data["login"], "password": courier_data["password"]}
        )
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        return {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "id": courier_id,
        }
