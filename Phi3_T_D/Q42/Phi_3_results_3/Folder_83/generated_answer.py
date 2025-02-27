from sympy import primefactors

def prime_factors(integers):
    if 95 < len(integers):
        raise IndexError('The list does not contain 96 integers.')
    return set(primefactors(integers[95]))