# Sprint 7 - API Testing for Yandex Scooter

This project tests the API for the Yandex Scooter educational service. The API documentation is available at: qa-scooter.praktikum-services.ru/docs/

## Project Structure

- `data/` - Stores test data
- `tests/` - Contains test files for different API endpoints
- `utils/` - CHelper functions for interacting with the API
- `conftest.py` - Pytest fixtures for test setup and teardown
- `requirements.txt` - Dependencies required for the project


## API Endpoints Tested

1. Create courier
2. Login courier
3. Create order
4. Get order list
5. Delete courier


## How to Run Tests

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests:
   ```
   python -m pytest
   ```

3. Generate Allure report:
   ```
   python -m pytest --alluredir=./target/allure-results
   ```

4. View Allure report:
   ```
   allure serve ./target/allure-results
   ```