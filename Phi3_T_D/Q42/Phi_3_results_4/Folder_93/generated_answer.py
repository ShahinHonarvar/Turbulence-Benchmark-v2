from functools import reduce
from sympy import primefactors

def prime_factors(integers):
    if len(integers) < 46:
        return 'The list must contain at least 46 integers.'
    return set(primefactors(integers[45]))