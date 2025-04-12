class Product:
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