"""Tests the Calculator class"""

import pytest

from src.calculator import Calculator

my_calculator = Calculator

def test_add_numbers_returns_sum():
	result = my_calculator.add(x=2, y=3)
	assert result == 5
