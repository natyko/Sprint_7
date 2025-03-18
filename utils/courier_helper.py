import requests
import random
import string
import json


class CourierHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    # Method to generate a random courier data
    def generate_random_courier(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = "".join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        return {"login": login, "password": password, "firstName": first_name}

    # Method to create a courier
    def create_courier(self, courier_data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{self.base_url}/courier", data=json.dumps(courier_data), headers=headers
        )
        return response

    # Method to log in a courier
    def login_courier(self, credentials):
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{self.base_url}/courier/login",
            data=json.dumps(credentials),
            headers=headers,
        )
        return response

    # Method to delete a courier
    def delete_courier(self, courier_id):
        headers = {"Content-Type": "application/json"}
        response = requests.delete(
            f"{self.base_url}/courier/{courier_id}", headers=headers
        )
        return response

    # Method to register a new courier and return login, password, and id
    def register_new_courier_and_return_login_password_id(self):
        courier_data = self.generate_random_courier()
        create_response = self.create_courier(courier_data)
        if create_response.status_code == 201:
            login_response = self.login_courier(
                {"login": courier_data["login"], "password": courier_data["password"]}
            )

            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                return {
                    "login": courier_data["login"],
                    "password": courier_data["password"],
                    "id": courier_id,
                }

        return None
