"""Mass conversions. Every unit is stored as its size in kilograms."""

from toybox.units._core import UnitTable

MASS = UnitTable(
    "mass",
    "kilogram",
    {
        "milligram": 1e-06,
        "gram": 0.001,
        "kilogram": 1.0,
        "tonne": 1000.0,
        "ounce": 0.028349523125,
        "pound": 0.45359237,
        "stone": 6.35029318,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a mass value between two units, e.g. convert(1, "gram", "kilogram")."""
    return MASS.convert(value, from_unit, to_unit)
