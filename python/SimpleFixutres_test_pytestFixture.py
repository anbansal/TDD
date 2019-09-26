import pytest


@pytest.fixture()
def setup1():
    print("\nSetting Up 1")
    yield
    print("\nTearing Down")


@pytest.fixture()
def setup2(request):
    print("\nSetting Up 2")

    def teardown_a():
        print("\nTearing Down a")

    def teardown_b():
        print("\nTearing Down b")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_a)


def test1(setup1):
    print("Executing test1")
    assert True


# @pytest.mark.usefixtures("setup")
def test2(setup2):
    print("Executing test2")
    assert True
