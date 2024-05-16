class ProductModel:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }