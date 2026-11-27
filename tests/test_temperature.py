import pytest
from temperature import Temperature


# 1.1. Initialization: default values
def test_default_unit() -> None:
    t = Temperature()
    assert t.value == 273.15
    assert t.unit == "K"
    assert Temperature(273.15, "K") == t
    assert Temperature(273.15, "C") != t


# 1.2. Initialization: case-insensitive units
def test_case_sensitivity() -> None:
    assert Temperature(273.15, "k") == Temperature(273.15, "K")
    assert Temperature(0.0, "c") == Temperature(0.0, "C")
    assert Temperature(32.0, "f") == Temperature(32.0, "F")
    assert Temperature(0.0, "C").convert_to("k") == Temperature(273.15, "K")
    assert Temperature(0.0, "k").unit == "K"


# 1.3. Read-only behavior
def test_read_only() -> None:
    t = Temperature(273.15, "K")
    with pytest.raises(AttributeError):
        t.value = 100.0
    with pytest.raises(AttributeError):
        t.unit = "C"

    t_converted = t.convert_to("F")
    assert t.unit == "K" and t.to_kelvin() == 273.15
    assert t_converted.to_celsius() == 0.0


# 2.1. Validation: invalid unit string
@pytest.mark.parametrize(
    "value, unit",
    [[273.15, "kay"], [100.0, "Celsius"], [32.0, "X"]]
)
def test_invalid_unit(value: float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(value, unit)

    with pytest.raises(ValueError):
        Temperature().convert_to(unit)


# 2.2. Validation: temperatures below absolute zero
@pytest.mark.parametrize(
    "value, unit",
    [[-1, "K"], [-274, "C"], [-460, "F"]]
)
def test_below_absolute_zero(value: float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(value, unit)


# 3 Conversion accuracy across reference points
def test_conversion_accuracy() -> None:
    # Absolute zero
    assert Temperature(-273.15, "C") == Temperature(0.0, "K") == Temperature(-459.67, "F")
    # Celsius–Fahrenheit crossover
    assert Temperature(-40.0, "C") == Temperature(233.15, "K") == Temperature(-40.0, "F")
    # Freezing point of water
    assert Temperature(0.0, "C") == Temperature(273.15, "K") == Temperature(32, "F")
    # Human body temperature
    assert Temperature(37, "C") == Temperature(310.15, "K") == Temperature(98.6, "F")
    # Boiling point of water
    assert Temperature(100, "C") == Temperature(373.15, "K") == Temperature(212, "F")


# 4. Round trip conversion
def test_round_trip() -> None:
    c_original = Temperature(0, "C")
    f = c_original.convert_to("F")
    k = f.convert_to("K")
    c_new = k.convert_to("C")

    assert c_original == c_new


# Cross unit comparison
def test_cross_unit() -> None:
    assert Temperature(0.0, "C") >= Temperature(273.15, "K")
    assert Temperature(0.1, "C") > Temperature(273.15, "K")
    assert Temperature(0.0, "F") < Temperature(273.15, "K")
    assert Temperature(-273.15, "C") <= Temperature(-459.67, "F")
    assert Temperature(300.15, "K") <= Temperature(90, "F")
    assert Temperature(0.0, "K") >= Temperature(-273.15, "C")


# Formatting
def test_formatting() -> None:
    t = Temperature()
    assert str(t) == "Temperature is 273.15 K"
    assert repr(t) == "Temperature(273.15, 'K')"
