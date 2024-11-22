"""
math_functions.py
Release Tag: v1.0
"""

import math


def power(base, exponent):
    result = base ** exponent
    return result

def divide(numerator, denominator):
    if(denominator == 0):
        raise ValueError("Denominator cannot be zero.")
  
    elif(numerator == 0):
        return 0

    result = numerator/denominator
    return result
   
