import pytest


@pytest.fixture(scope="session", autouse=True)
def setupSession1():
    print("\nSetting up Session 1")


@pytest.fixture(scope="module", autouse=True)
def setupModule1():
    print("\nSetting up Module 1")


@pytest.fixture(scope="function", params=[1, 2, 3])
def setupFunction1(request):
    retVal = request.param
    print("\nSetting up Function 1! retVal = {}".format(retVal))
    return retVal


def test1(setupFunction1):
    print("\nExecuting test 1")
    print("\nSet Up = {}".format(setupFunction1))
    assert True


def test2():
    print("\nExecuting test 2")
