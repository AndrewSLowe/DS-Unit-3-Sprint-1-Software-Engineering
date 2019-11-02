"""Writing functions to work with arrays and strings"""

import string
import numpy as np

def increment(x):
    """adds one to x"""
    return x + 1

def strip_punctuation(text):
    """strips out punctuation"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exlude)
