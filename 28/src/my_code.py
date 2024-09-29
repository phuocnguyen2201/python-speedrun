

from datetime import datetime
#Write class and imports here!
class Product:
    def __init__(self, name, price, location, product_code):
        self.name = name
        self.price = price
        self.location = location
        self.product_code = product_code

    def ask_data(self):
        self.name = input("Name: ")
        self.price = float(input("Price: "))
        self.location = input("Location: ")
        self.product_code = input("Code: ")

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nLocation: {self.location}\nCode: {self.product_code}"
    
class Cloth(Product):
    def __init__(self, name, price, location, product_code, size, material):
        super().__init__(name, price, location, product_code)
        self.size = size
        self.material = material

    def ask_data(self):
        super().ask_data()
        self.size = input("Size: ")
        self.material = input("Material: ")

    def __str__(self):
        return super().__str__() + f"\nSize: {self.size}\nMaterial: {self.material}"

class Grocery(Product):
    def __init__(self, name, price, location, product_code, country_of_origin, best_before_date):
        super().__init__(name, price, location, product_code)
        self.country_of_origin = country_of_origin
        self.best_before_date = best_before_date

    def ask_data(self):
        super().ask_data()
        self.country_of_origin = input("Origin: ")
        self.best_before_date = input("Best before: ")

    def __str__(self):
        return super().__str__() + f"\nOrigin: {self.country_of_origin}\nBest before: {self.best_before_date}"

class Appliance(Product):
    def __init__(self, name, price, location, product_code, guarantee, weight):
        super().__init__(name, price, location, product_code)
        self.guarantee = guarantee
        self.weight = weight

    def ask_data(self):
        super().ask_data()
        self.guarantee = input("Guarantee: ")
        self.weight = input("Weight: ")

    def __str__(self):
        return super().__str__() + f"\nGuarantee: {self.guarantee}\nWeight: {self.weight}"

if __name__ == "__main__":
    #Main program here!
    products = []
    while True:
        product_type = input("Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: ")
        if product_type == "1":
            product = Grocery("", 0, "", "", "", "")
            product.ask_data()
            products.append(product)
        elif product_type == "2":
            product = Cloth("", 0, "", "", "", "")
            product.ask_data()
            products.append(product)
        elif product_type == "3":
            product = Appliance("", 0, "", "", "", "")
            product.ask_data()
            products.append(product)
        else:
            break
    for product in products:
        print(product)