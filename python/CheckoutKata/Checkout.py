class Checkout:
    class Discount:
        def __init__(self, NbrItems, Price):
            self.nbrItems = NbrItems
            self.price = Price

    def __init__(self):
        self.items = {}
        self.discount = {}
        self.prices = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.prices[item] * cnt
        return total

    def addDiscountRule(self, item, noOfItems, newPrice):
        discount = self.Discount(noOfItems, newPrice)
        self.discount[item] = discount
