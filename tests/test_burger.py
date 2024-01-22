from burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == "Bun 1"
        assert burger.bun.price == 50

    def test_add_ingredient_with_sauces(self, mock_sauce):
        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        # добавляем 2 соуса
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'sauce'

    def test_add_ingredient_with_fillings(self, mock_filling):
        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        # добавляем 3 начинки
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0].type == 'filling'
        assert burger.ingredients[2].type == 'filling'

    def test_add_ingredient_with_sauce_and_filling(self, mock_sauce, mock_filling):
        # создаем экземпляр (объект) класса Burger
        burger = Burger()
        # добавляем соус и начинку
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == 'sauce'
        assert burger.ingredients[1].type == 'filling'