import random

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
    [],  # No color
    ["BLACK"],  # Only BLACK
    ["GREY"],  # Only GREY
    ["BLACK", "GREY"],  # Both colors
]


# Helper function to generate random text
def generate_random_string(length=10):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for i in range(length))
