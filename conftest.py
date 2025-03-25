import collections.abc
import pytest
from urls import BASE_URL
from utils.courier_helper import CourierHelper
from data.data import courier_without_first_name

collections.Mapping = collections.abc.Mapping


@pytest.fixture
def base_url():
    """Base URL fixture providing the API base URL from urls.py"""
    return BASE_URL


@pytest.fixture
def headers():
    """Default headers for HTTP requests"""
    return {"Content-Type": "application/json"}


@pytest.fixture
def courier_helper(base_url):
    """Provides a CourierHelper instance for interacting with the Courier API"""
    helper = CourierHelper(base_url)
    yield helper


@pytest.fixture
def courier_data(courier_helper):
    """
    Fixture to supply a unique courier data payload, generates a random courier.
    """
    data = courier_helper.generate_random_courier()
    yield data
    # Cleanup: attempt to log in and delete the courier if it was created successfully
    if "login" in data and "password" in data:
        login_resp = courier_helper.login_courier(
            {"login": data["login"], "password": data["password"]}
        )
        if login_resp.status_code == 200:
            courier_id = login_resp.json().get("id")
            if courier_id:
                courier_helper.delete_courier(courier_id)


@pytest.fixture
def registered_courier(courier_helper):
    """
    Fixture to register a new courier before a test and delete it after the test.
    """
    credentials = courier_helper.register_new_courier_and_return_login_password_id()
    assert credentials is not None, "Failed to register a new courier for the test"
    yield credentials
    courier_helper.delete_courier(credentials["id"])


@pytest.fixture
def courier_without_first_name_data(courier_helper):
    """
    Fixture to supply a courier payload missing the firstName field.
    """
    data = courier_without_first_name.copy()
    yield data
    login_resp = courier_helper.login_courier(
        {"login": data.get("login"), "password": data.get("password")}
    )
    if login_resp.status_code == 200:
        courier_id = login_resp.json().get("id")
        if courier_id:
            courier_helper.delete_courier(courier_id)
