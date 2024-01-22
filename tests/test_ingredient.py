from ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type='sauce',
                                name='ketchup',
                                price=10.5)

        assert ingredient.get_price() == 10.5

    def test_get_name(self):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type='sauce',
                                name='ketchup',
                                price=10.5)

        assert ingredient.get_name() == 'ketchup'

    def test_get_type(self):
        # создаем экземпляр (объект) класса Ingredient
        ingredient = Ingredient(ingredient_type='sauce',
                                name='ketchup',
                                price=10.5)

        assert ingredient.get_type() == 'sauce'
