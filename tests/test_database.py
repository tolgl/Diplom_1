import pytest

from database import Database


class TestDatabase:

    @pytest.mark.parametrize('index,name',
                             [
                                 [0, 'black bun'],
                                 [1, 'white bun'],
                                 [2, 'red bun']
                             ])
    def test_available_buns_get_name(self, index, name):
        # создаем экземпляр (объект) класса Database
        database = Database()
        buns = database.available_buns()

        assert buns[index].get_name() == name

    @pytest.mark.parametrize('index,price',
                             [
                                 [0, 100],
                                 [1, 200],
                                 [2, 300]
                             ])
    def test_available_buns_get_price(self, index, price):
        # создаем экземпляр (объект) класса Database
        database = Database()
        buns = database.available_buns()

        assert buns[index].get_name() == price

    @pytest.mark.parametrize('index,ingredient_type',
                             [
                                 [0, 'SAUCE'],
                                 [1, 'SAUCE'],
                                 [2, 'SAUCE'],
                                 [3, 'FILLING'],
                                 [4, 'FILLING'],
                                 [5, 'FILLING']
                             ])
    def test_available_ingredients_get_type(self, index, ingredient_type):
        # создаем экземпляр (объект) класса Database
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[index].get_type() == ingredient_type

    @pytest.mark.parametrize('index,name',
                             [
                                 [0, 'hot sauce'],
                                 [1, 'sour cream'],
                                 [2, 'chili sauce'],
                                 [3, 'cutlet'],
                                 [4, 'dinosaur'],
                                 [5, 'sausage']
                             ])
    def test_available_ingredients_get_name(self, index, name):
        # создаем экземпляр (объект) класса Database
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[index].get_name() == name

    @pytest.mark.parametrize('index,price',
                             [
                                 [0, 100],
                                 [1, 200],
                                 [2, 300],
                                 [3, 100],
                                 [4, 200],
                                 [5, 300]
                             ])
    def test_available_ingredients_get_price(self, index, price):
        # создаем экземпляр (объект) класса Database
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[index].get_price() == price
