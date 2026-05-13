"""Tests for utils module."""

import pytest
from utils import add, subtract, multiply, divide, reverse_string, is_palindrome


class TestMath:
    """Tests for math functions."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -2) == -3

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_subtract(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        assert subtract(3, 5) == -2

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_divide(self):
        assert divide(10, 2) == 5.0

    def test_divide_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestStrings:
    """Tests for string functions."""

    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty(self):
        assert reverse_string("") == ""

    def test_reverse_single_char(self):
        assert reverse_string("a") == "a"

    def test_is_palindrome_yes(self):
        assert is_palindrome("racecar") is True

    def test_is_palindrome_no(self):
        assert is_palindrome("hello") is False

    def test_is_palindrome_case_insensitive(self):
        assert is_palindrome("RaceCar") is True

    def test_is_palindrome_with_spaces(self):
        assert is_palindrome("tacocat") is True

    def test_is_palindrome_empty(self):
        assert is_palindrome("") is True
