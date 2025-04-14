import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    try:
        c = math.sqrt(a)
        return c
    except ValueError as e:
        print(e)

def hypotenuse(a,b):
    return math.hypot(a,b)


# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        print(e)


def logarithm(a, b):
    try:
        c = math.log(b, a)
        return c
    except ValueError as e:
        print(e)


def exp(a, b):
    return a ** b
