from sympy import primefactors

def prime_factors(lst):
    try:
        return set(primefactors(lst[19]))
    except IndexError:
        return 'The list does not have an element at index 19.'