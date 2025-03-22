# Test data for courier creation
valid_courier = {
    "login": "test_courier_login",
    "password": "test_password",
    "firstName": "TestCourier",
}

# Test data for order creation
valid_order = {
    "firstName": "Test",
    "lastName": "Customer",
    "address": "Test street, 123",
    "metroStation": 4,
    "phone": "+7 999 888 77 66",
    "rentTime": 5,
    "deliveryDate": "2023-12-30",
    "comment": "Test comment",
}

# Color options for parameterized tests
color_options = [
    [],
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
]

# Additional test data for courier creation (missing fields scenarios)
courier_without_login = {
    # Missing the "login" field
    "password": "testpassword",
    "firstName": "TestName",
}
courier_without_password = {
    # Missing the "password" field
    "login": "testlogin",
    "firstName": "TestName",
}
courier_without_first_name = {
    # Missing the "firstName" field
    "login": "unique_login",
    "password": "unique_password",
}

# Additional test data for courier login scenarios
missing_login_payload = {"password": "testpassword"}
missing_password_payload = {"login": "testlogin"}
invalid_credentials = {
    "login": "invalid",
    "password": "wrong",
}
wrong_password = "wrongpass"

# Test data for order creation with only required fields
order_required_fields_only = {
    "firstName": "Test",
    "lastName": "Customer",
    "address": "Test Address",
    "metroStation": 1,
    "phone": "+7 999 123 45 67",
    "rentTime": 1,
    "deliveryDate": "2023-12-30",
}

# Constant for nonexistent courier ID
nonexistent_courier_id = 999999999
