"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/DevikaPramod2907/lab11--DP---PA-.git
# Partner 1: Devika Pramod
# Partner 2: Pavitra Anand
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate square root of a negative number")


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid logarithm arguments")


def exp(a, b):
    return a ** b


def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
       return b / a

def log(a, b):
    if math.log(b, a) == 0 or math.log(b,a) < 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b
