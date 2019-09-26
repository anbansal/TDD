import pytest


@pytest.fixture(scope="session")
def setupSession2():
    print("\nSetting up Session 2")


@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetting up Module 2")


@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetting up Function 2")


@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetting up Class 2")


class TestClass:
    def test1(self):
        print("\nTest 1 of Class")

    def test2(self):
        print("\nTest 2 of Class")
