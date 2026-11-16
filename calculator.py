"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate square root of a negative number")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise ValueError("Invalid values for hypotenuse")

def add(a, b):
    return a+b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    result = math.log(b, a)
    if result == 0 or result < 0:
        raise ValueError
    else:
        return result

def exponent(a, b):
    return a**b



