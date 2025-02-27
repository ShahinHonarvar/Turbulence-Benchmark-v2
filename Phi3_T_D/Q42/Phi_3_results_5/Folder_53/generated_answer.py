from sympy import primefactors

def prime_factors(num):
    if 73 < len(num):
        raise IndexError('Index 73 is out of range.')
    return set(primefactors(num[73]))