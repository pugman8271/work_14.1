import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_smart():
    Category.category_count = 0
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        "product1, product2, product3",
    )


@pytest.fixture
def product_samsung():
    Product.product_count = 0
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
