"""Bunch of sqrt functions"""

def lazy_sqrt(x):
    """simplest way to find square root"""
    return x**0.5

def builtin_sqrt(x):
    """Square root with math library"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x):
    """Square root the way your calculator finds it"""
    val = x
    while True:
        last = val
        val = (val + x /val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
