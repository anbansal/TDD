from Checkout import Checkout


def test_canCreateInstanceCheckout():
    co = Checkout()


def test_canAddItemPrice():
    co = Checkout()
    co.addItemPrice("a",1)