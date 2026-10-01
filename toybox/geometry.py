"""2-D geometry helpers: points, distances, polygon area and perimeter, bounding boxes."""

import math
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def norm(self) -> float:
        return math.hypot(self.x, self.y)


def distance(a: Point, b: Point) -> float:
    """Euclidean distance between two points."""
    return (a - b).norm()


def polygon_area(vertices: Sequence[Point]) -> float:
    """Area of a simple polygon by the shoelace formula; vertex order may be either direction."""
    if len(vertices) < 3:
        raise ValueError("a polygon needs at least 3 vertices")
    twice = sum(p.x * q.y - q.x * p.y for p, q in zip(vertices, [*vertices[1:], vertices[0]]))
    return abs(twice) / 2


def perimeter(vertices: Sequence[Point]) -> float:
    """Total edge length of a closed polygon."""
    return sum(distance(p, q) for p, q in zip(vertices, [*vertices[1:], vertices[0]]))


def bounding_box(points: Iterable[Point]) -> tuple[Point, Point]:
    """(lower-left, upper-right) corners of the smallest axis-aligned box holding every point."""
    pts = list(points)
    if not pts:
        raise ValueError("bounding_box() of no points")
    return (Point(min(p.x for p in pts), min(p.y for p in pts)),
            Point(max(p.x for p in pts), max(p.y for p in pts)))


def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * radius ** 2
