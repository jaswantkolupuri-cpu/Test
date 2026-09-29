from toybox.mathutils import add, factorial, is_prime, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_factorial():
    assert factorial(5) == 120


def test_is_prime_true():
    assert is_prime(7)


def test_is_prime_false():
    assert not is_prime(8)
