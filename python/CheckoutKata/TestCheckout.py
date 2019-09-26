from Checkout import Checkout


def test_canAddItemPrice():
    co = Checkout()
    co.addItemPrice("a",1)