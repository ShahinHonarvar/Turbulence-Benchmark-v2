from sympy import primefactors

def prime_factors(int_list):
    return set(primefactors(int_list[94])) if len(int_list) > 94 else 'List index out of range.'