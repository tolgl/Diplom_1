import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize('name,price',
                             [
                                 ['Test', 300],
                                 ['', 300]
                             ])
    def test_get_name(self, name, price):
        # создаем экземпляр (объект) класса Bun
        bun = Bun(name=name, price=price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('name,price',
                             [
                                 ['Test', 300],
                                 ['Test', 300.9]
                             ])
    def test_get_price(self, name, price):
        # создаем экземпляр (объект) класса Bun
        bun = Bun(name=name, price=price)

        assert bun.get_price() == price
