from functools import total_ordering
from typing import Self

@total_ordering
class Fraction:
    '''Represents a fraction with integer numerator and positive integer denominator.'''

    TOLERANCE = 1e-9
    
    def __init__(self, numerator: int, denominator: int) -> None:
        '''Creates a Fraction.
        Args:
            numerator: The numerator, any integer.
            denominator: The denominator, a strictly positive integer.

        Raises:
            TypeError: If numerator or denominator is not an integer.
            ValueError: If denominator is zero or negative.
        '''
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
    
        if denominator <= 0:
            raise ValueError("Denominator must be positive.")

        self._numerator = numerator
        self._denominator = denominator


    def calc(self) -> float:
        """Return the value of the fraction as a float."""
        return self.numerator / self.denominator

   # Comparision methods    
    def __eq__(self, other) -> bool:
        """Return True if both fractions have the same value."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return abs(self.calc() - other.calc()) < self.TOLERANCE

    def __lt__(self, other) -> bool:
        """Return True if this fraction is smaller than other."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.calc() < other.calc()

    # Arithmetic operators methods
    def __add__(self, other) -> Self:
        """Return the sum of two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_den = (self.denominator * other.denominator)
        return type(self)(new_num, new_den)

    def __sub__(self, other) -> Self:
        """Return the difference of two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_den = (self.denominator * other.denominator)
        return type(self)(new_num, new_den)

    def __mul__(self, other) -> Self:
        """Return the product of two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (self.numerator * other.numerator)
        new_den = (self.denominator * other.denominator)
        return type(self)(new_num, new_den)

    def __truediv__(self, other) -> Self:
        """Return the quotient of two fractions.
        
        Raises:
            ZeroDivisionError: If other is equal to zero.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction equal to zero.")
        
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        
        if new_den < 0:
            new_num = -new_num
            new_den = -new_den
        return type(self)(new_num, new_den)

    # Other methods
    def __repr__(self):
        """Return the official string representation of the object."""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        """Return a human-readable string representation."""
        return f"({self.numerator}/{self.denominator})"

    @property 
    def numerator(self) -> int:
        '''Read-only access to numerator.'''
        return self._numerator

    @property 
    def denominator(self) -> int:
        '''Read-only access to denominator.'''
        return self._denominator

