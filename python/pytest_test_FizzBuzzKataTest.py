import unittest


class fizzBuzzKataTest(unittest.TestCase):

    def isMultiple(self, value, mod):
        return (value % mod) == 0

    def fizzBuzzTest(self, n):
        if (self.isMultiple(n, 3)):
            if (self.isMultiple(n, 5)):
                return "FizzBuzz"
            return "Fizz"

        elif (self.isMultiple(n, 5)):
            return "Buzz"

        else:
            return str(n)

    def checkFizzBuzz(self, value, expectedVal):
        return expectedVal == self.fizzBuzzTest(value)

    def test_canCallFizzBuzzTest(self):
        self.assertTrue(self.fizzBuzzTest)

    def test_canGetOneWhenPassOne(self):
        self.assertTrue(self.checkFizzBuzz(1, "1"))

    def test_canGetTwoWhenPassTwo(self):
        self.assertTrue(self.checkFizzBuzz(2, "2"))

    def test_canGetFizzWhenPassThree(self):
        self.assertTrue(self.checkFizzBuzz(3, "Fizz"))

    def test_canGetBuzzWhenPassFive(self):
        self.assertTrue(self.checkFizzBuzz(5, "Buzz"))

    def test_canGetFizzWhenPassMultipleThree(self):
        self.assertTrue(self.checkFizzBuzz(6, "Fizz"))

    def test_canGetBuzzWhenPassMultipleFive(self):
        self.assertTrue(self.checkFizzBuzz(10, "Buzz"))

    def test_canGetFizzBuzzWhenPassMultipleThreeFive(self):
        self.assertTrue(self.checkFizzBuzz(15, "FizzBuzz"))


if __name__ == '__main__':
    unittest.main()