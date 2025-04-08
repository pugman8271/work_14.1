def test_init_category(category_smart):
    assert category_smart.name == "Смартфоны"


def test_init_product(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"


def test_init_category_counter(category_smart):
    assert category_smart.category_count == 1


def test_init_product_counter(product_samsung):
    assert product_samsung.product_count == 1


