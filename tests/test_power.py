from toybox.mathutils import power


def test_power_integer():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1
