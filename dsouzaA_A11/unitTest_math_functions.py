"""
test_math_functions.py
Release Tag: v1.0
"""

import unittest
from math_functions import power, divide

class TesterClass(unittest.TestCase):
 

    #Tests for power...
    def test_power_positive(self):
        print("Running Power tests...")
        self.assertEqual(power(2,3),8)

    def test_power_zero(self):
        self.assertEqual(power(5,0),1)

    def test_power_negative(self):
        self.assertAlmostEqual(power(4,-3), 0.015625)

    def test_power_negativebase(self):
        self.assertEqual(power(-4, 3), -64)
    
    def test_power_zerobase(self):
        self.assertEqual(power(0,3),0)

    def test_power_fractional(self):
        self.assertAlmostEqual(power(2, 1/2), 1.41421356237)

    def test_power_fractionbase(self):
        self.assertEqual(power(1/2, 2), 0.25)

    #tests for divide...
    def test_divide_decimalanswer(self):
        self.assertEqual(divide(10,4),2.5)

    def test_divide_regular(self):
        self.assertEqual(divide(10, 2), 5)  # 10 / 2 = 5

    def test_divide_zerodenom(self):
        with self.assertRaises(ValueError):
            divide(10,0)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0,2), 0)

    def test_divide_negative_numerator(self):
        self.assertEqual(divide(-10, 2), -5)  # -10 / 2 = -5

    def test_divide_negativedenom(self):
        self.assertEqual(divide(10,-2), -5)

    def test_divide_negative_nums(self):
        self.assertEqual(divide(-10, -2), 5)  # -10 / -2 = 5


if __name__ == "__main__":
    unittest.main()


