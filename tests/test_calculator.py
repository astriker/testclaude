import pytest

from src.calculator import (
    add,
    divide,
    factorial,
    gcd,
    is_prime,
    lcm,
    multiply,
    power,
    subtract,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert gcd(0, 5) == 5


def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(3, 5) == 15
    assert lcm(0, 5) == 0


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
