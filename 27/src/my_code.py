
#Write class and imports here!
class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = 0

    def print_value(self, roi, years):
        value = self.price * self.quantity
        increase = self.compute_increase(roi, value, years)
        self.total_value += increase
        print(f"{self.name} {self.quantity} {self.price}")
        print(f"Stock value will be {increase:.2f}, and profit {increase - value:.2f}")

    @staticmethod
    def compute_increase(roi, value, years):
        return value * ((1+(roi/100))**years)
if __name__ == "__main__":
    #Write main program here
    stocks = []
    while True:
        name = input("Company name: ")
        price = float(input("Price: "))
        quantity = int(input("Amount: "))
        stocks.append(Stock(name, price, quantity))
        if input("More stocks (y/n)? ") == "n":
            break
    roi = float(input("Expected ROI-%: "))
    years = int(input("Years: "))
    total_value = 0
    for stock in stocks:
        stock.print_value(roi, years)
        total_value += stock.total_value
    print(f"Portfolio value will be {total_value:.2f}")
