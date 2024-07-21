class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product {self.name} - {self.price}"
    

class Category:
    products = []

    def __init__(self, name, products) -> None:
        self.name = name
        self.products = products

    def add(self, product):
        self.products.append(product)

    def show(self):
        for product in self.products:
            print(product)

kayak = Product("kayak", 1000)
bike = Product("bike", 500)
surfboard = Product("surfboard", 300)

sports = Category("Sports", [kayak, bike])

print(sports.show())

sports.add(surfboard)

print(sports.show())