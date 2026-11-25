class Temperature():
    '''Converts temperatures into Kelvin, Celsius, or Fahrenheit.'''

    ACCEPTED_UNITS = ("K", "C", "F")
    def __init__(self, temp: float, unit: str) -> None:
        self._temp = temp
        self._unit = unit.upper()
        
        if self._unit not in self.ACCEPTED_UNITS:
                raise ValueError("Unit must be K, C or F.")

    

    def to_celcius(self) -> float:
        if self._unit == "K":
            return self._temp - 273.15
        if self._unit == "F":
            return (self._temp - 32) * 5 / 9
        return self._temp

    def to_kelvin(self) -> float:
         return self.to_celcius() + 273.15

    def to_fahrenheit(self) -> float:
         return self.to_celcius() * 9 / 5 + 32

    def convert_to(self, target_unit: str) -> Temperature:
         target_unit = target_unit.upper()
         if target_unit not in self.ACCEPTED_UNITS:
              raise ValueError("Unit must be K, C, or F.")
         new_temp = self.to_celcius() if target_unit == "C" else \
                    self.to_fahrenheit() if target_unit == "F" else \
                    self.to_kelvin()
         return Temperature(new_temp, target_unit)

    def __repr__(self) -> str:
         return f"Temperature({self._temp:.1f}, {self._unit})"

    def __str__(self) -> str:
         return f"Temperature is {self._temp:.1f} {self._unit}"

    def __eq__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         return abs(a - b) < 1e-9

    def __ne__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         return abs(a - b) > 1e-9

    def __lt__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         return a < b

    def __le__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         if abs(a - b) < 1e-9:
              return True
         if a < b:
              return True

    def __gt__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         return a > b

    def __ge__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius()
         b = other.to_celcius()
         return a >= b
         
         
     

