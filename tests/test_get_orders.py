import allure
from utils.order_helper import OrderHelper
from data.data import valid_order


@allure.epic("Order API Tests")
@allure.feature("Get Orders")
class TestGetOrders:

    @allure.story("Get Orders List")
    @allure.title("Get list of all orders")
    @allure.description("Test retrieving the list of all orders")
    def test_get_orders_returns_list(self, base_url):
        order_helper = OrderHelper(base_url)

        response = order_helper.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    @allure.story("Get Orders After Creating")
    @allure.title("Create order and verify it appears in orders list")
    @allure.description(
        "Test creating an order and then verifying it appears in the orders list"
    )
    def test_create_order_and_get_orders(self, base_url):
        order_helper = OrderHelper(base_url)

        create_response = order_helper.create_order(valid_order)
        assert create_response.status_code == 201

        response = order_helper.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert len(response.json()["orders"]) > 0
