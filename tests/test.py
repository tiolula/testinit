from unittest import TestCase
import src.calculator as calc

class CalculatorTests(TestCase):

    def test_example(self):
        a = 1
        b = 2
        expected_result = 3

        actual_result = calc.sum(a, b)

        self.assertEqual(actual_result, expected_result)

    def test_another_example(self):
        a = 3
        b = 5
        expected_result = 8

        actual_result = calc.sum(a, b)

        self.assertEqual(actual_result, expected_result)
