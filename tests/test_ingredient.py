import pytest

from ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('price', [10, 10.99])
    def test_get_price(self, price):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type='sauce',
                                name='ketchup',
                                price=price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', ['hot sauce', 'cutlet'])
    def test_get_name(self, name):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type='sauce',
                                name=name,
                                price=10.5)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', ['sauce', 'filling'])
    def test_get_type(self, ingredient_type):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type=ingredient_type,
                                name='ketchup',
                                price=10.5)

        assert ingredient.get_type() == ingredient_type
