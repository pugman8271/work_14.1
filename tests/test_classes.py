from itertools import product

from src.category import Category
from src.product import Product

def test_init_category(category_smart):
    assert category_smart.name == "Смартфоны"


def test_init_product(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"


def test_init_category_counter(category_smart):
    assert category_smart.category_count == 1


def test_init_product_counter(product_samsung):
    assert product_samsung.product_count == 1


def test_price(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5

def test_change_price_zero(product_samsung):
    product_samsung.price = 0
    assert product_samsung.price == 180000.0


def test_new_product(product_samsung_new):
    new_product = Product.new_product(product_samsung_new)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_getter(product_samsung):
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                        [product_samsung])
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_method(product_samsung):

    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_method(product_samsung, product_iphone):
    result = product_samsung + product_iphone
    expected = (180000.0 * 5) + (80000 * 3)
    assert result == expected


def test_category_str():
    category_test = Category('Смартфоны', "Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни", [])
    product_test = Product('Samsung Galaxy S23 Ultra', '256GB, Черный цвет', 180000.0, 10)
    category_test.add_product(product_test)
    expected_output = "Смартфоны, количество продуктов: 10 шт."
    assert str(category_test) == expected_output


