from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_samsung],
    )
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_method(product_samsung):

    assert (
        str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_add_method(product_samsung, product_iphone):
    result = product_samsung + product_iphone
    expected = (180000.0 * 5) + (80000 * 3)
    assert result == expected


def test_category_str():
    category_test = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [],
    )
    product_test = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Черный цвет", 180000.0, 10
    )
    category_test.add_product(product_test)
    expected_output = "Смартфоны, количество продуктов: 10 шт."
    assert str(category_test) == expected_output


def test_smartphone_init(smartphone_iphone):
    assert smartphone_iphone.name == "Iphone 15"
    assert smartphone_iphone.description == "512GB, Gray space"
    assert smartphone_iphone.price == 210000
    assert smartphone_iphone.quantity == 8
    assert smartphone_iphone.efficiency == 98.2
    assert smartphone_iphone.model == "15"
    assert smartphone_iphone.memory == 512
    assert smartphone_iphone.color == "Gray space"


def test_lawn_grass_init(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == '7 дней'
    assert lawn_grass.color == "Зеленый"


def test_smartphone_add(smartphone_iphone):
    another_phone = Smartphone("Samsung Galaxy S23 Ultra",
                               "256GB, Серый цвет, 200MP камера",
                               180000.0, 5, 95.5,
                               "S23 Ultra", 256, "Серый")
    total_price = smartphone_iphone + another_phone
    assert (total_price == (smartphone_iphone.price * smartphone_iphone.quantity)
            + (another_phone.price * another_phone.quantity))


def test_lawn_grass_add(lawn_grass):
    another_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    total_price = lawn_grass + another_grass
    assert total_price == (lawn_grass.price * lawn_grass.quantity) + (another_grass.price * another_grass.quantity)


def test_mixin_test(prod_mixin_test):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert repr(product1) == prod_mixin_test
