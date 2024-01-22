import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', ['', 'test', '!@#$%^&*', None])
    def test_get_name(self, name):

        # создаем экземпляр (объект) класса Bun
        bun = Bun(name=name, price=10)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [10, 10.99, 0.0, None])
    def test_get_price(self, price):
        # создаем экземпляр (объект) класса Bun
        bun = Bun(name='test', price=price)

        assert bun.get_price() == price
