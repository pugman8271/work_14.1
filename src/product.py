from src.baseproduct import BaseProduct
from src.poduct_mixin import MixinProduct


class Product(BaseProduct, MixinProduct):
    name: str
    description: str
    price: int
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, prod_dict):
        name = prod_dict["name"]
        description = prod_dict["description"]
        __price = prod_dict["price"]
        quantity = prod_dict["quantity"]
        return cls(name, description, __price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value <= self.__price:
                self.__price = value
