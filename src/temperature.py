"""Temperature class with unit conversion and comparison."""

from functools import total_ordering
from typing import Self


@total_ordering
class Temperature:
    """Represents a temperature in Kelvin, Celsius, or Fahrenheit."""

    ACCEPTED_UNITS = frozenset({"K", "C", "F"})
    KELVIN_OFFSET = 273.15
    TOLERANCE = 1e-9

    def __init__(self, value: float = KELVIN_OFFSET, unit: str = "K") -> None:
        """
        Initialise the temperature.

        Args:
            value: The temperature value. Defaults to 273.15.
            unit: The unit of the value: "K", "C", or "F" (case-insensitive).
                Defaults to "K".

        Raises:
            ValueError: If the unit is not "K", "C", or "F", or if the
                temperature is below absolute zero.
        """
        self._value = value
        self._unit = self._process_unit(unit)

        if self.to_kelvin() < 0:
            raise ValueError("Temperature cannot be lower than absolute zero.")

    @property
    def value(self) -> float:
        """The temperature value (read-only)."""
        return self._value

    @property
    def unit(self) -> str:
        """The temperature unit (read-only)."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature value converted to Celsius."""
        if self._unit == "K":
            return self._value - self.KELVIN_OFFSET
        if self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value

    def to_kelvin(self) -> float:
        """Return the temperature value converted to Kelvin."""
        if self._unit == "K":
            return self._value
        return self.to_celsius() + self.KELVIN_OFFSET

    def to_fahrenheit(self) -> float:
        """Return the temperature value converted to Fahrenheit."""
        if self._unit == "F":
            return self._value
        return self.to_celsius() * 9 / 5 + 32

    def convert_to(self, target_unit: str) -> Self:
        """Convert the temperature to a chosen unit and return it as a new object."""
        target_unit = self._process_unit(target_unit)

        if target_unit == "C":
            value = self.to_celsius()
        elif target_unit == "K":
            value = self.to_kelvin()
        else:
            value = self.to_fahrenheit()

        return type(self)(value, target_unit)

    def __repr__(self) -> str:
        """Return the developer representation of the temperature."""
        return f"{type(self).__name__}({self._value!r}, {self._unit!r})"

    def __str__(self) -> str:
        """Return the temperature in a human-readable way."""
        return f"Temperature is {self._value} {self._unit}"

    def __eq__(self, other: object) -> bool:
        """Check for equality."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_celsius() - other.to_celsius()) < self.TOLERANCE

    def __lt__(self, other: object) -> bool:
        """Check for less than."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() < other.to_celsius() and not self == other

    @classmethod
    def _process_unit(cls, unit: str) -> str:
        """Return the unit in uppercase, or raise ValueError if it is not accepted."""
        processed_unit = unit.upper()

        if processed_unit not in cls.ACCEPTED_UNITS:
            raise ValueError(f"Unit must be K, C, or F, got {unit!r}.")

        return processed_unit
