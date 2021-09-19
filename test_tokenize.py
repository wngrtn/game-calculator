from unittest import TestCase
from code import _tokenize, TokenizeError


class TestTokenize(TestCase):
    def test_multiple_operations(self):
        self.assertEqual(
            ["3", "+", "3", "+", "4"], 
            _tokenize("3 + 3 + 4"),
        )

    def test_raises_on_multiple_dots(self):
        with self.assertRaises(TokenizeError):
            _tokenize("3.3.3")

    def test_does_not_raise_on_sign_after_operator(self):
        self.assertEqual(
            ["3", "*", "-3"],
            _tokenize("3 * -3"),
        )
        
        self.assertEqual(
            ["3", "+", "-3"],
            _tokenize("3 + -3"),
        )

    def test_does_raises_on_multiple_signs(self):
        with self.assertRaises(TokenizeError):
            _tokenize("+-3")

    def test_raises_on_letter(self):
        with self.assertRaises(TokenizeError):
            _tokenize("d")
        
        with self.assertRaises(TokenizeError):
            _tokenize("3d")

        with self.assertRaises(TokenizeError):
            _tokenize("3*d")
