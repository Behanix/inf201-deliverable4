class Fraction:
    '''Represents a fraction with integer numerator and positive integer denominator.'''
    def __init__(self, numerator: int, denominator: int) -> None:
        '''Creates a Fraction. Raises ValueError if denominator is zero or negative.'''
        if denominator <= 0:
            raise ValueError("Denominator must be positive.")        
        self._numerator = numerator
        self._denominator = denominator

    def __calc__(self) -> float:
        return self._numerator / self._denominator

    def __eq__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return abs(self.calc() - other.calc()) < 1e-9

    def __ne__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return abs(self.calc() - other.calc()) > 1e-9

    @property 
    def numerator(self) -> int:
        '''Read-only access to numerator.'''
        return self._numerator

    @property 
    def denominator(self) -> int:
        '''Read-only access to denominator.'''
        return self._denominator