import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        print(e)

def logarithm(a,b):
    try:
        c = math.log(b,a)
        return c
    except ValueError as e:
        print(e)

def exponent(a,b):
    return a ** b




