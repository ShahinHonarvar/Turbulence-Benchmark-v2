from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) < 36:
        raise ValueError('The list must contain at least 36 positive integers.')
    return set(primefactors(numbers[35]))