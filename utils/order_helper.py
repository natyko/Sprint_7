import requests
import json


class OrderHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    # Method to create an order
    def create_order(self, order_data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{self.base_url}/orders", data=json.dumps(order_data), headers=headers
        )
        return response

    # Method to get list of orders
    def get_orders(self):
        response = requests.get(f"{self.base_url}/orders")
        return response

    # Method to get a specific order by track number
    def get_order_by_track(self, track):
        response = requests.get(f"{self.base_url}/orders/track?t={track}")
        return response

    # Method to accept an order
    def accept_order(self, order_id, courier_id):
        headers = {"Content-Type": "application/json"}
        response = requests.put(
            f"{self.base_url}/orders/accept/{order_id}?courierId={courier_id}",
            headers=headers,
        )
        return response

    # Method to create an order and return its track number
    def create_order_and_return_track(self, order_data):
        response = self.create_order(order_data)
        if response.status_code == 201:
            return response.json().get("track")
        return None
