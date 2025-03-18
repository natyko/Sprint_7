import collections.abc

collections.Mapping = collections.abc.Mapping

import pytest


@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru/api/v1"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}
