class MixinProduct:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})")
        super().__init__(*args, **kwargs)
