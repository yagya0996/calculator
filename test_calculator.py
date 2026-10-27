import pytest
from calculator import add, subtract, multiply, divide, power, modulo, square_root, percent


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8


def test_modulo():
    assert modulo(10, 3) == 1


def test_square_root():
    assert square_root(9) == 3.0


def test_percent():
    assert percent(20, 50) == 10.0