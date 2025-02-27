from sympy import primefactors

def prime_factors(numbers_list):
    try:
        index = 45
        prime_factors_set = set(primefactors(numbers_list[index]))
        return prime_factors_set
    except IndexError:
        return {}