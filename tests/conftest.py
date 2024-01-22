import pytest
from unittest.mock import Mock


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = "Bun 1"
    mock_bun.price = 50
    mock_bun.get_name.return_value = "Bun 1"
    mock_bun.get_price.return_value = 50

    return mock_bun


@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = 'sauce'
    mock_sauce.name = 'ketchup'
    mock_sauce.price = 10
    mock_sauce.get_type.return_value = 'sauce'
    mock_sauce.get_name.return_value = 'ketchup'
    mock_sauce.get_price.return_value = 10

    return mock_sauce


@pytest.fixture()
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = 'filling'
    mock_filling.name = 'cheese'
    mock_filling.price = 50.5
    mock_filling.get_type.return_value = 'filling'
    mock_filling.get_name.return_value = 'cheese'
    mock_filling.get_price.return_value = 50.5

    return mock_filling
