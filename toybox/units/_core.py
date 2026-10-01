"""Shared machinery for linear unit tables (a unit is a fixed multiple of the base unit)."""

from dataclasses import dataclass, field


class UnknownUnitError(KeyError):
    """Raised when a unit name is not in the table being used."""


@dataclass(frozen=True)
class UnitTable:
    quantity: str
    base: str
    factors: dict[str, float] = field(default_factory=dict)

    def __post_init__(self):
        if self.factors.get(self.base) != 1.0:
            raise ValueError(f"{self.quantity}: base unit {self.base!r} must have factor 1.0")

    def factor(self, unit: str) -> float:
        try:
            return self.factors[unit]
        except KeyError:
            known = ", ".join(sorted(self.factors))
            raise UnknownUnitError(f"unknown {self.quantity} unit {unit!r}; known: {known}") from None

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        return value * self.factor(from_unit) / self.factor(to_unit)

    def units(self) -> list[str]:
        return sorted(self.factors, key=self.factors.__getitem__)
