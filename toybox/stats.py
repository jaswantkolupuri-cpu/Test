"""Small descriptive statistics without numpy: mean, median, mode, variance, percentiles, z-scores."""

import math
from collections import Counter
from typing import Sequence


def _require(data: Sequence[float], at_least: int = 1) -> None:
    if len(data) < at_least:
        raise ValueError(f"need at least {at_least} value(s), got {len(data)}")


def mean(data: Sequence[float]) -> float:
    _require(data)
    return sum(data) / len(data)


def median(data: Sequence[float]) -> float:
    _require(data)
    s = sorted(data)
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2


def mode(data: Sequence[float]) -> list[float]:
    """Every most-common value, smallest first (data can be multimodal)."""
    _require(data)
    counts = Counter(data)
    top = max(counts.values())
    return sorted(v for v, c in counts.items() if c == top)


def variance(data: Sequence[float], sample: bool = True) -> float:
    """Sample variance (n-1) by default; population variance with sample=False."""
    _require(data, 2 if sample else 1)
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - (1 if sample else 0))


def stdev(data: Sequence[float], sample: bool = True) -> float:
    return math.sqrt(variance(data, sample))


def percentile(data: Sequence[float], p: float) -> float:
    """Linear-interpolated percentile, p in [0, 100]."""
    _require(data)
    if not 0 <= p <= 100:
        raise ValueError("p must be between 0 and 100")
    s = sorted(data)
    k = (len(s) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def zscores(data: Sequence[float]) -> list[float]:
    m, sd = mean(data), stdev(data)
    if sd == 0:
        raise ValueError("z-scores are undefined when every value is equal")
    return [(x - m) / sd for x in data]
