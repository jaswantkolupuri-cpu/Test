"""Area conversions. Every unit is stored as its size in square_metres."""

from toybox.units._core import UnitTable

AREA = UnitTable(
    "area",
    "square_metre",
    {
        "square_metre": 1.0,
        "hectare": 10000.0,
        "square_kilometre": 1000000.0,
        "square_foot": 0.09290304,
        "acre": 4046.8564224,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a area value between two units, e.g. convert(1, "hectare", "square_metre")."""
    return AREA.convert(value, from_unit, to_unit)
