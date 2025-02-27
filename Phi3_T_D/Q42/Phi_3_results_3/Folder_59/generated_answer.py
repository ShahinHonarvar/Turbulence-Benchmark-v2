from sympy import primefactors

def prime_factors(numbers):
    factor_set = set(primefactors(numbers[2]))
    return factor_set