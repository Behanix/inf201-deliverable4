class Temperature():
    '''Converts temperatures into Kelvin, Celsius, or Fahrenheit.'''

    ACCEPTED_UNITS = ("K", "C", "F")
    def __init__(self, temp: float = 0.0, unit: str = "K") -> None:
        self._temp = temp
        self._unit = unit.upper()
        if self._unit not in self.ACCEPTED_UNITS:
             raise ValueError("Unit must be K, C or F.")
        if self.to_kelvin() < -1e-9:
             raise ValueError("Temperature must be above absolute zero.")    

    def to_celsius(self) -> float:
        '''Converts to celsius.'''
        if self._unit == "K":
            return self._temp - 273.15
        if self._unit == "F":
            return (self._temp - 32) * 5 / 9
        return self._temp

    def to_kelvin(self) -> float:
         '''Converts to kelvin.'''
         return self.to_celsius() + 273.15

    def to_fahrenheit(self) -> float:
         '''Converts to Fahrenheit.'''
         return self.to_celsius() * 9 / 5 + 32

    def convert_to(self, target_unit: str) -> Temperature:
         '''Converts Temperature object to another unit.'''
         target_unit = target_unit.upper()
         if target_unit not in self.ACCEPTED_UNITS:
              raise ValueError("Unit must be K, C, or F.")
         new_temp = self.to_celsius() if target_unit == "C" else \
                    self.to_fahrenheit() if target_unit == "F" else \
                    self.to_kelvin()
         return Temperature(new_temp, target_unit)

    def __repr__(self) -> str:
         '''Representation of class.'''
         return f"Temperature({self._temp:.1f}, {self._unit})"

    def __str__(self) -> str:
         '''Prints Temperature in a human readable way.'''
         return f"Temperature is {self._temp:.1f} {self._unit}"

    def __eq__(self, other) -> bool:
         '''Check for equality.'''
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celsius()
         b = other.to_celsius()
         return abs(a - b) < 1e-9

# Don't need because __eq__ already in place. 
#     def __ne__(self, other) -> bool:
#          '''Check for equality.'''
#          if not isinstance(other, Temperature):
#               return NotImplemented
#          a = self.to_celsius()
#          b = other.to_celsius()
#          return abs(a - b) > 1e-9

    def __lt__(self, other) -> bool:
         '''Check for less than.'''
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celsius()
         b = other.to_celsius()
         return a < b

    def __le__(self, other) -> bool:
         '''Check of less than or equal to.'''
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celsius()
         b = other.to_celsius()
         return abs(a - b) < 1e-9 or a < b

    def __gt__(self, other) -> bool:
         '''Check for greater than.'''
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celsius()
         b = other.to_celsius()
         return a > b

    def __ge__(self, other) -> bool:
         '''Check for greater than or equal to.'''
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celsius()
         b = other.to_celsius()
         return a >= b
         
@property
def temp(self) -> float:
    return self._temp

@property
def unit(self) -> str:
    return self._unit