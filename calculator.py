"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def add(a, b):
    return a + b

import math
def add(a, b): 
    return a+b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    result = math.log(b, a)
    if result == 0 or result < 0:
        raise ValueError
    else:
        return result

def exponent(a, b):
    return a**b


def sub(a, b):
    return a - b

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
