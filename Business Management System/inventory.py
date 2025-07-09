class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity)

    def low_stock_items(self, threshold=5):
        return (p for p in self.products.values() if p.quantity < threshold)