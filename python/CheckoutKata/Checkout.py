class Checkout:
    def __init__(self):
        self.items = {}
        self.total = 0

    def addItemPrice(self, item, price):
        self.items[item] = price

    def addItem(self, item):
        self.total += self.items[item]

    def calculateTotal(self):
        return self.total

    def addDiscountRule(self, item, noOfItems, newPrice):
        return
