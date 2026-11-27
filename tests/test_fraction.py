import pytest

from fractions import Fraction

# Initialization
def test_negative_denominator():
    with pytest.raises(ValueError):
      Fraction(1, -5)

def test_zero_denominator():
    with pytest.raises(ValueError):
      Fraction(1, 0)

def test_int_type():
    with pytest.raises(TypeError):
      Fraction(1.0, 3.0)

# Comparisons
def test_equal():
    assert Fraction(1, 2) == Fraction(5, 10)

def test_not_equal():
    assert Fraction(1, 4) != Fraction(1, 2)

def test_less_than():
    assert Fraction(1, 4) < Fraction(3, 4)

def test_less_equal():
    assert Fraction(1, 2) <= Fraction(5, 10)

def test_greater_than():
    assert Fraction(1, 2) > Fraction(1, 4)

def test_greater_equal():
    assert Fraction(1, 2) >= Fraction(1, 4)

# Arithmetic
def test_addition():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)

def test_subtraction():
    assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)

def test_multiplication():
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)

def test_division():
    assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)

def test_division_by_negative():
    assert Fraction(1, 2) / Fraction(-1, 3) == Fraction(-3, 2)

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 5)


# Other methods
def test_str():
    assert str(Fraction(1, 2)) == "(1/2)"

def test_repr():
    assert repr(Fraction(1, 3)) == "Fraction(1, 3)"