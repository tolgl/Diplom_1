from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.name = "Bun 1"
        mock_bun.price = 50
        mock_bun.get_name.return_value = "Bun 1"
        mock_bun.get_price.return_value = 50

        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == "Bun 1"
        assert burger.bun.price == 50

    def test_add_ingredient_with_sauces(self):
        mock_sauce = Mock()
        mock_sauce.type = 'sauce'
        mock_sauce.name = 'ketchup'
        mock_sauce.price = 10
        mock_sauce.get_type.return_value = 'sauce'
        mock_sauce.get_name.return_value = 'ketchup'
        mock_sauce.get_price.return_value = 10

        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'sauce'

    def test_add_ingredient_with_fillings(self):
        mock_filling = Mock()
        mock_filling.type = 'filling'
        mock_filling.name = 'cheese'
        mock_filling.price = 50.5
        mock_filling.get_type.return_value = 'filling'
        mock_filling.get_name.return_value = 'cheese'
        mock_filling.get_price.return_value = 50.5

        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0].type == 'filling'
        assert burger.ingredients[2].type == 'filling'
