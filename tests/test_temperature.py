from temperature import Temperature
import pytest

# Initialization

# Default values
def test_default_unit():
    t = Temperature()
    assert t.temp == 273.15
    assert t.unit == "K"
    assert Temperature(273.15, "K") == t
    assert Temperature(273.15, "C") != t


# Case-insensitive units

def test_case_sensitivity():
    assert Temperature(273.15, "k") == Temperature(273.15, "K")
    assert Temperature(0.0, "c") == Temperature(0.0, "C")
    assert Temperature(32.0, "f") == Temperature(32.0, "F")
    assert Temperature(0.0, "C").convert_to("k") == Temperature(273.15, "K")
    assert Temperature(0.0, "k").unit == "K"


def test_read_only():
    t = Temperature(273.15, "K")
    with pytest.raises(AttributeError):
        t.temp = 100.0
    with pytest.raises(AttributeError):
        t.unit = "C"

    t_converted = t.convert_to("F")
    assert t.unit == "K" and t.to_kelvin() == 273.15
    assert t_converted.to_celsius() == 0.0

# Validation

def test_invalid_unit():
    for bad_input in [(273.15, "kay"), (100.0, "Celsius"), (32.0, "X")]:
        with pytest.raises(ValueError):
            Temperature(bad_input[0], bad_input[1])


def test_below_absolute_zero():
    for below in [(-1, "K"), (-274, "C"), (-460, "F")]:
        with pytest.raises(ValueError):
            Temperature(below[0], below[1])

def test_invalid_conversion():
    with pytest.raises(ValueError):
        Temperature().convert_to("Q")


# Conversions

# Absolute zero
def test_absolute_zero():
    c = Temperature(-273.15, "C")
    k = Temperature(0.0, "K")
    f = Temperature(-459.67, "F")

    assert c == k == f

# Celsius-Fahrenheit crossover
def test_c_to_f():
    c = Temperature(-40.0, "C")
    k = Temperature(233.15, "K")
    f = Temperature(-40.0, "F")

    assert c == k == f

# Freezing point of water
def test_freezing_point():
    c = Temperature(0.0, "C")
    k = Temperature(273.15, "K")
    f = Temperature(32, "F")

    assert c == k == f

# Human body temperature
def test_human_temp():
    c = Temperature(37, "C")
    k = Temperature(310.15, "K")
    f = Temperature(98.6, "F")

    assert c == k == f

# Boiling point of water
def test_boiling_point():
    c = Temperature(100, "C")
    k = Temperature(373.15, "K")
    f = Temperature(212, "F")

    assert c == k == f

# Round trip conversion
def test_round_trip():
    c = Temperature(0, "C")
    f = c.convert_to("F")
    k = f.convert_to("K")
    C = k.convert_to("C")

    assert c == C

# Cross unit comparison
def test_cross_unit():
    assert Temperature(0.0, "C") >= Temperature(273.15, "K")
    assert Temperature(0.1, "C") > Temperature(273.15, "K")
    assert Temperature(0.0, "F") < Temperature(273.15, "K")
    assert Temperature(-273.15, "C") <= Temperature(-459.67, "F")
    assert Temperature(300.15, "K") <= Temperature(90, "F")
    assert Temperature(0.0, "K") >= Temperature(-273.15, "C")

# Formatting
def test_formatting():
    t = Temperature()
    assert str(t) == "Temperature is 273.15 K"
    assert repr(t) == "Temperature(273.15, 'K')"
