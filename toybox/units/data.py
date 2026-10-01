"""Data conversions. Every unit is stored as its size in bytes."""

from toybox.units._core import UnitTable

DATA = UnitTable(
    "data",
    "byte",
    {
        "bit": 0.125,
        "byte": 1.0,
        "kilobyte": 1000.0,
        "megabyte": 1000000.0,
        "gigabyte": 1000000000.0,
        "kibibyte": 1024.0,
        "mebibyte": 1048576.0,
        "gibibyte": 1073741824.0,
    },
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a data value between two units, e.g. convert(1, "byte", "byte")."""
    return DATA.convert(value, from_unit, to_unit)
