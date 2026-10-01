"""Length conversions. Every unit is stored as its size in metres."""

from toybox.units._core import UnitTable

LENGTH = UnitTable(
    "length",
    "metre",
    {
        "millimetre": 0.001,
        "centimetre": 0.01,
        "metre": 1.0,
        "kilometre": 1000.0,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
        "nautical_mile": 1852.0,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a length value between two units, e.g. convert(1, "centimetre", "metre")."""
    return LENGTH.convert(value, from_unit, to_unit)
