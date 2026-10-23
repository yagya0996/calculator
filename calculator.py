import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Can not divide by zero")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulo(a, b):
    return a % b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("2 ** 3 =", power(2, 3))