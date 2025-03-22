import requests
import json
import allure
from urls import BASE_URL


class OrderHelper:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    @allure.step("Create an order")
    def create_order(self, order_data):
        headers = {"Content-Type": "application/json"}
        return requests.post(
            f"{self.base_url}/orders", data=json.dumps(order_data), headers=headers
        )

    @allure.step("Get all orders")
    def get_orders(self):
        return requests.get(f"{self.base_url}/orders")

    @allure.step("Get order by track")
    def get_order_by_track(self, track):
        return requests.get(f"{self.base_url}/orders/track?t={track}")

    @allure.step("Accept order")
    def accept_order(self, order_id, courier_id):
        headers = {"Content-Type": "application/json"}
        return requests.put(
            f"{self.base_url}/orders/accept/{order_id}?courierId={courier_id}",
            headers=headers,
        )

    @allure.step("Create and return track number")
    def create_order_and_return_track(self, order_data):
        response = self.create_order(order_data)
        if response.status_code == 201:
            return response.json().get("track")
        return None
