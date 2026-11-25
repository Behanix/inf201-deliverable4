from temperature import Temperature
import pytest

# Initialization

# Default values
def test_default_unit():
    t = Temperature()
    assert t._temp == 0.0
    assert t._unit == "K"
    assert Temperature(0.0, "K") == t
    assert Temperature(0.0, "C") != t

test_default_unit()

# Case-insensitive units

def test_case_sensitivity():
    assert Temperature(273.15, "k") == Temperature(273.15, "K")
    assert Temperature(0.0, "c") == Temperature(0.0, "C")
    assert Temperature(32.0, "f") == Temperature(32.0, "F")
    assert Temperature(0.0, "C").convert_to("k") == Temperature(273.15, "K")
    assert Temperature(0.0, "k")._unit == "K"

test_case_sensitivity()

def test_read_only():
    t = Temperature(273.15, "K")
    with pytest.raises(AttributeError):
        t._temp = 100.0
    with pytest.raises(AttributeError):
        t._unit = "C"

    t_converted = t.convert_to("F")
    assert t._unit == "K" and t.to_kelvin() == 273.15
    assert t_converted.to_celsius == 0.0

test_read_only()



# test_read_only()

# Validation


# Conversions