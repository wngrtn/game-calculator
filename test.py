from unittest import TestCase

from code import calculate


class TestEvaluate(TestCase):
    def test_simple_expression_int(self):
        self.assertEqual(3, calculate("3"))
        
    def test_handle_superfluous_space(self):
        self.assertEqual(3, calculate("  3    "))

    def test_simple_expression_float(self):
        self.assertEqual(3.0, calculate("3.0"))
        self.assertEqual(3.1, calculate("3.1"))

    def test_simple_sum(self):
        self.assertEqual(5, calculate("2.4 + 2.6"))

    def test_binary_operation(self):
        self.assertEqual(5, calculate("2.5 * 2"))
        self.assertEqual(-1, calculate("2 - 3"))
        self.assertEqual(-2, calculate("-4 / 2"))
        self.assertEqual(2, calculate("11 % 3"))

    def test_multiple_operations(self):
        self.assertEqual(10, calculate("3 + 3 + 4"))
        self.assertEqual(5, calculate("2 * 3 - 1"))
