from sympy import primefactors

def prime_factors(integers):
    return primefactors(integers[410]) if len(integers) > 410 else []