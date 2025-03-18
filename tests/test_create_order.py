import pytest
import allure
import copy
from utils.order_helper import OrderHelper
from data.data import valid_order


@allure.epic("Order API Tests")
@allure.feature("Create Order")
class TestCreateOrder:

    @allure.story("Create Order with Different Color Options")
    @allure.title("Create order with color option: {color_option}")
    @allure.description("Test creating orders with different color options")
    @pytest.mark.parametrize(
        "color_option", [([]), (["BLACK"]), (["GREY"]), (["BLACK", "GREY"])]
    )
    def test_create_order_with_different_colors(self, base_url, color_option):
        order_helper = OrderHelper(base_url)
        order_data = copy.deepcopy(valid_order)
        order_data["color"] = color_option

        response = order_helper.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.story("Create Order with Required Fields")
    @allure.title("Create order with only required fields")
    @allure.description("Test creating an order with only the required fields")
    def test_create_order_with_required_fields_only(self, base_url):
        order_helper = OrderHelper(base_url)
        order_data = {
            "firstName": "Test",
            "lastName": "Customer",
            "address": "Test Address",
            "metroStation": 1,
            "phone": "+7 999 123 45 67",
            "rentTime": 1,
            "deliveryDate": "2023-12-30",
        }

        response = order_helper.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.story("Track Number in Response")
    @allure.title("Verify track number is returned in response")
    @allure.description("Test that the order creation response contains a track number")
    def test_order_creation_returns_track_number(self, base_url):
        order_helper = OrderHelper(base_url)
        order_data = copy.deepcopy(valid_order)

        response = order_helper.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
