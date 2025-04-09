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


    def add_product(self, product):
        if isinstance(product, Product):
            pass
        else:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @products.getter
    def products(self):
        result = []
        for i in self.__products:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.")
        return "\n".join(result)

