"""Volume conversions. Every unit is stored as its size in litres."""

from toybox.units._core import UnitTable

VOLUME = UnitTable(
    "volume",
    "litre",
    {
        "millilitre": 0.001,
        "litre": 1.0,
        "cubic_metre": 1000.0,
        "us_gallon": 3.785411784,
        "imperial_gallon": 4.54609,
        "us_cup": 0.2365882365,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a volume value between two units, e.g. convert(1, "litre", "litre")."""
    return VOLUME.convert(value, from_unit, to_unit)
