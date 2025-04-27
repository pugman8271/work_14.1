from itertools import product

from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = Product.product_count

    def __str__(self):
        prod_sum = 0
        for product in self.__products:
            prod_sum += product.quantity
        return f"{self.name}, количество продуктов: {prod_sum} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Объект не является продуктом")
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self):
        try:
            price_sum = 0
            for product in self.__products:
                price_sum += product.price
            return  price_sum/len(self.__products)
        except ZeroDivisionError:
            return 0



    @property
    def products(self):
        return self.__products

    @products.getter
    def products(self):
        result = []
        for i in self.__products:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(result)
