import unittest
from calculator import multiply, divide


class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == "__main__":
    unittest.main()