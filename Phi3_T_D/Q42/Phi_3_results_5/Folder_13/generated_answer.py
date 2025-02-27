from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) < 127 or not all((isinstance(n, int) and n > 0 for n in numbers)):
        raise ValueError('The input list must contain at least 127 positive integers.')
    return frozenset(primefactors(numbers[126]))