import pytest

from burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == "white bun"
        assert burger.bun.price == 50

    def test_add_ingredient_with_sauces(self, mock_sauce):
        burger = Burger()
        # добавляем 2 соуса
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'sauce'

    def test_add_ingredient_with_fillings(self, mock_filling):
        burger = Burger()
        # добавляем 3 начинки
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0].type == 'filling'
        assert burger.ingredients[2].type == 'filling'

    def test_add_ingredient_with_sauce_and_filling(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем соус и начинку
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'filling'

    def test_remove_ingredient_removing_first_ingredient_from_two(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем 2 ингредиента
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # удаляем ингредиент
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removing_last_ingredient_from_two(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем 2 ингредиента
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # удаляем ингредиент
        burger.remove_ingredient(-1)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removing_all_ingredients(self, mock_sauce):
        burger = Burger()
        # добавляем один ингредиент
        burger.add_ingredient(mock_sauce)
        # удаляем ингредиент
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_moving_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем два ингредиента
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # перемещаем ингредиенты
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0].type == 'filling'
        assert burger.ingredients[1].type == 'sauce'

    @pytest.mark.parametrize('index,new_index',
                             [
                                 [3, 0],
                                 [1, 2],
                                 [2, 2],
                                 [2, 3]
                             ])
    def test_move_ingredient_moving_with_invalid_index(self, mock_sauce, mock_filling, index, new_index):
        burger = Burger()
        # добавляем два ингредиента
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # перемещаем ингредиенты
        burger.move_ingredient(index, new_index)

        # проверяем отсутствие ошибки кода, что ингредиенты не удалились и не поменялись местами
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'filling'

    @pytest.mark.parametrize('index,new_index',
                             [
                                 [0, 0],
                                 [1, 1]
                             ])
    def test_move_ingredient_moving_with_same_index(self, mock_sauce, mock_filling, index, new_index):
        burger = Burger()
        # добавляем два ингредиента
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # перемещаем ингредиенты
        burger.move_ingredient(index, new_index)

        # проверяем что ингредиенты не поменялись местами
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'filling'
