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

def cube(a):
    return a ** 3

def square(a):
    """Return a squared."""
    return a * a

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


if __name__ == "__main__":
    operations = {"+": add, "-": subtract, "*": multiply,
                  "/": divide, "**": power, "%": modulo}
    try:
        a = float(input("First number: "))
        op = input("Operation (+ - * / ** %): ")
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
    else:
        if op not in operations:
            print(f"Unknown operation: {op}")
        else:
            try:
                print("Result:", operations[op](a, b))
            except (ValueError, ZeroDivisionError) as error:
                print("Error:", error)