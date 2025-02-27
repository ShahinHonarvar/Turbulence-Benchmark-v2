from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) > 63:
        return set(primefactors(numbers[63]))
    else:
        return 'List does not contain 64 elements'