import unittest
import Calculator

class MyTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.addition(1, 1), 2)

    def subtraction(self):
        self.assertEqual(Calculator.subtraction(3, 1), 2)

    def multiplication(self):
        self.assertEqual(Calculator.multiplication(15, 2), 30)

    def division(self):
        self.assertEqual(Calculator.division(30, 6), 5)

    def test_results_property(self):
        self.assertEqual(Calculator.addition(2, 1), 3)

if __name__ == '__main__':
    unittest.main()
