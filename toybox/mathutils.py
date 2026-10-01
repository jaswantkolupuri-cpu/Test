"""Small arithmetic helpers."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Product of a and b."""
    return a * b


def divide(a, b):
    """Quotient of a and b; raises ZeroDivisionError when b is 0."""
    if b == 0:
        raise ZeroDivisionError("divide() by zero")
    return a / b
