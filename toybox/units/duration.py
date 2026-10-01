"""Duration conversions. Every unit is stored as its size in seconds."""

from toybox.units._core import UnitTable

DURATION = UnitTable(
    "duration",
    "second",
    {
        "millisecond": 0.001,
        "second": 1.0,
        "minute": 60.0,
        "hour": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a duration value between two units, e.g. convert(1, "second", "second")."""
    return DURATION.convert(value, from_unit, to_unit)
