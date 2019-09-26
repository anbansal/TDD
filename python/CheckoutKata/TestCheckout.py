import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


"""
def test_canAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)


def test_canAddItem(checkout):
    checkout.addItem("a")

"""


def test_canCalculateTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1
