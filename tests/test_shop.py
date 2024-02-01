"""
Протестируйте классы из модуля homework/pages.py
"""
import pytest

from models.pages import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100) == True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(100) == True

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert product in cart.products

    def test_remove_product(self, product, cart):
        cart.add_product(product)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_not_in_cart(self, product, cart):
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_clear(self, product, cart):
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product, cart):
        cart.add_product(product)
        assert cart.get_total_price() == 100

    def test_buy(self, product, cart):
        cart.add_product(product)
        cart.buy()
        assert cart.products == {}

    def test_buy_more_than_available(self, product, cart):
        cart.add_product(Product("milk", 50, "This is milk", 1), 2)
        with pytest.raises(ValueError):
            cart.buy()
