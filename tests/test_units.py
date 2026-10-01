import pytest

from toybox.units import UnknownUnitError, convert, quantities


def test_lengths():
    assert convert("length", 1, "mile", "kilometre") == pytest.approx(1.609344)
    assert convert("length", 12, "inch", "foot") == pytest.approx(1)


def test_data_binary_vs_decimal():
    assert convert("data", 1, "gibibyte", "gigabyte") == pytest.approx(1.073741824)


def test_temperature():
    assert convert("temperature", 100, "celsius", "fahrenheit") == pytest.approx(212)
    with pytest.raises(ValueError):
        convert("temperature", -500, "celsius", "kelvin")


def test_unknown_unit_and_quantity():
    with pytest.raises(UnknownUnitError):
        convert("mass", 1, "furlong", "gram")
    with pytest.raises(KeyError):
        convert("luminosity", 1, "a", "b")
    assert "volume" in quantities()
