class MixinProduct:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self):
        print(repr(self))

    def __repr__(self) -> str:
        return (f"\n"
                f"**********\n"
                f"Создан объект: {self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})\n"
                f"**********\n")
