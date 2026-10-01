"""Temperature conversions. Not linear tables: offsets differ, so each scale maps via kelvin."""

_TO_KELVIN = {
    "kelvin": lambda v: v,
    "celsius": lambda v: v + 273.15,
    "fahrenheit": lambda v: (v - 32) * 5 / 9 + 273.15,
    "rankine": lambda v: v * 5 / 9,
}
_FROM_KELVIN = {
    "kelvin": lambda k: k,
    "celsius": lambda k: k - 273.15,
    "fahrenheit": lambda k: (k - 273.15) * 9 / 5 + 32,
    "rankine": lambda k: k * 9 / 5,
}


def convert(value: float, from_scale: str, to_scale: str) -> float:
    """Convert between kelvin, celsius, fahrenheit and rankine. Rejects results below absolute zero."""
    if from_scale not in _TO_KELVIN or to_scale not in _FROM_KELVIN:
        raise KeyError(f"unknown temperature scale: {from_scale!r} or {to_scale!r}")
    kelvin = _TO_KELVIN[from_scale](value)
    if kelvin < 0:
        raise ValueError(f"{value} {from_scale} is below absolute zero")
    return _FROM_KELVIN[to_scale](kelvin)
