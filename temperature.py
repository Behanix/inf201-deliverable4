class Temperature():
    '''Converts temperatures into Kelvin, Celsius, or Fahrenheit.'''

    ACCEPTED_UNITS = ("K", "C", "F")
    def __init__(self, temp: float, unit: str) -> None:
        self._temp = temp
        self._unit = unit.upper()
        
        if self._unit not in self.ACCEPTED_UNITS:
                raise ValueError("Unit must be K, C or F.")

    

    def to_celcius(self, temp: float, unit: str) -> float:
        if self._unit == "K":
            return temp - 273.15
        if self._unit == "F":
            return (temp - 32) * 5 / 9
        return temp

    def to_kelvin(self) -> float:
         return self.to_celcius() + 273.15

    def to_fahrenheit(self) -> float:
         return self.to_celcius() * 9 / 5 + 32

    def convert_to(self, target_unit: str) -> Temperature:
         if target_unit.upper() not in self.ACCEPTED_UNITS:
              raise ValueError("Unit must be K, C, or F.")
         else:
              return Temperature

    def __repr__(self) -> str:
         return 

    def __str__(self) -> str:
         return f"Temperature is {self._temp} {self._unit}"

    def __eq__(self, other) -> bool:
         if not isinstance(other, Temperature):
              return NotImplemented
         a = self.to_celcius(self._temp, self._unit)
         b = self.to_celcius(other._temp, other._unit)
         return abs(a - b) < 1e-9

         
         
     

