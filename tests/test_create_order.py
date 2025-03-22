import pytest
import allure
import copy
from utils.order_helper import OrderHelper
from data.data import valid_order, color_options, order_required_fields_only


@allure.epic("Order API Tests")
@allure.feature("Create Order")
class TestCreateOrder:

    @allure.title("Create Order with Different Color Options")
    @allure.description("Verify order created with color option: {color_option}")
    @pytest.mark.parametrize("color_option", color_options)
    def test_create_order_with_different_colors(self, base_url, color_option):
        order_helper = OrderHelper(base_url)
        order_data = copy.deepcopy(valid_order)
        order_data["color"] = color_option

        response = order_helper.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Create Order with Required Fields")
    @allure.description("Verify order creation with only required fields")
    def test_create_order_with_required_fields_only(self, base_url):
        order_helper = OrderHelper(base_url)
        response = order_helper.create_order(order_required_fields_only)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Track Number in Response")
    @allure.description("Verify track number is returned in response")
    def test_order_creation_returns_track_number(self, base_url):
        order_helper = OrderHelper(base_url)
        order_data = copy.deepcopy(valid_order)
        response = order_helper.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
