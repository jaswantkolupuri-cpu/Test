import pytest

from toybox.geometry import Point, bounding_box, distance, perimeter, polygon_area
from toybox.stats import mean, median, mode, percentile, stdev
from toybox.textutils import camel_to_snake, levenshtein, slugify, wrap

SQUARE = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]


def test_geometry():
    assert distance(Point(0, 0), Point(3, 4)) == 5
    assert polygon_area(SQUARE) == 4
    assert perimeter(SQUARE) == 8
    assert bounding_box(SQUARE) == (Point(0, 0), Point(2, 2))


def test_stats():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert mean(data) == 5
    assert median(data) == 4.5
    assert mode(data) == [4]
    assert stdev(data, sample=False) == 2
    assert percentile(data, 50) == 4.5


def test_text():
    assert slugify("Héllo, World!") == "hello-world"
    assert camel_to_snake("parseHttpHeader") == "parse_http_header"
    assert levenshtein("kitten", "sitting") == 3
    assert wrap("the quick brown fox", 9) == ["the quick", "brown fox"]
