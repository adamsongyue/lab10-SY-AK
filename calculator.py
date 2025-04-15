# https://github.com/adamsongyue/lab10-SY-AK
# Partner 1: Artur Kashafutdinov
# Partner 2: Yue, Song
import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):

    if a < 0:
        raise ValueError
    c = math.sqrt(a)
    return c


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
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b,a)


def exp(a, b):
    return a ** b

