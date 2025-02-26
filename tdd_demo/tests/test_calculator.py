"""Tests the Calculator class"""

import pytest

from src.calculator import Calculator

def test_add_numbers_returns_sum():
	"Tests the addition feature of the calculator."
	
	my_calculator = Calculator
	result = my_calculator.add(x=2, y=3)
	assert result == 5
