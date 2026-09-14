"""Small arithmetic helpers."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
