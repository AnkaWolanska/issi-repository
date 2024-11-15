"""Test calculations"""
import pytest

from calculator import Calculator


def test_sum_two_numbers():
    """Test sum"""
    calc = Calculator (2, 3)
    assert calc.sum() == 5

def test_sub_two_numbers():
    """Test subtraction"""
    calc = Calculator(8, 3)
    assert calc.subtract() == 5

def test_mul_two_numbers():
    """Test multiplication"""
    calc = Calculator(2, 2.5)
    assert calc.multiply() == 5

def test_div_two_numbers():
    """Test division"""
    calc = Calculator(10, 2)
    assert calc.divide() == 5

def test_div_by_zero_two_numbers():
    """Test division by zero"""
    calc = Calculator(9, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()
