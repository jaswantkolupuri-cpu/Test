"""Unit conversion: `convert(quantity, value, from_unit, to_unit)` dispatches to one module per quantity."""

from toybox.units import area, data, duration, length, mass, temperature, volume
from toybox.units._core import UnitTable, UnknownUnitError

_MODULES = {m.__name__.rsplit(".", 1)[1]: m for m in (area, data, duration, length, mass, temperature, volume)}


def convert(quantity: str, value: float, from_unit: str, to_unit: str) -> float:
    """Convert `value` of `quantity` (e.g. "length") from one unit to another."""
    try:
        module = _MODULES[quantity]
    except KeyError:
        raise KeyError(f"unknown quantity {quantity!r}; known: {', '.join(sorted(_MODULES))}") from None
    return module.convert(value, from_unit, to_unit)


def quantities() -> list[str]:
    return sorted(_MODULES)


__all__ = ["UnitTable", "UnknownUnitError", "convert", "quantities"]
