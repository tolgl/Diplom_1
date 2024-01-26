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

    def test_get_price_with_bun_sauce_filling(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем булки и ингредиенты
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == 160.5

    def test_get_price_without_ingredients(self, mock_bun):
        burger = Burger()
        # добавляем только булки
        burger.set_buns(mock_bun)

        assert burger.get_price() == 100

    def test_get_price_without_buns(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем только ингредиенты
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == 60.5

    def test_get_price_without_one_ingredient(self, mock_bun, mock_filling):
        burger = Burger()
        # добавляем булки и один ингредиент
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == 150.5

    def test_get_price_without_buns_and_ingredients(self):
        burger = Burger()

        # проверяем что цена без булок и ингредиентов 0
        assert burger.get_price() == 0

    def test_get_receipt_with_buns_sauce_filling(self, mock_bun, mock_sauce, mock_filling):
        # создаем бургер с полным списком продуктов
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # получаем рецепт
        receipt = burger.get_receipt()
        # проверяем что в рецепте указаны названия всех ингредиентов
        assert 'white bun' in receipt
        assert 'chili sauce' in receipt
        assert 'cutlet' in receipt
        assert '160.5' in receipt

    def test_get_receipt_without_one_ingredient(self, mock_bun, mock_sauce):
        # создаем бургер без одного ингредиента
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        # получаем рецепт
        receipt = burger.get_receipt()
        # проверяем что в рецепте указаны названия всех ингредиентов
        assert 'white bun' in receipt
        assert 'chili sauce' in receipt
        assert 'cutlet' not in receipt
        assert '110' in receipt

    def test_get_receipt_without_buns(self, mock_sauce, mock_filling):
        # создаем бургер без одного ингредиента
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # получаем рецепт
        receipt = burger.get_receipt()
        # проверяем что в рецепте указаны названия всех ингредиентов
        assert 'white bun' not in receipt
        assert 'chili sauce' in receipt
        assert 'cutlet' not in receipt
        assert '60.5' in receipt

    def test_get_receipt_without_buns_and_ingredients(self):
        # создаем пустой бургер
        burger = Burger()
        # получаем рецепт
        receipt = burger.get_receipt()
        # проверяем что в рецепте указаны названия всех ингредиентов
        assert len(receipt) == 0
        