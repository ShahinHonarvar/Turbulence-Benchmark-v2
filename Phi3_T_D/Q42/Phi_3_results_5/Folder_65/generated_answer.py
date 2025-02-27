from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) > 35:
        return primefactors(numbers[35])
    else:
        raise ValueError('The list must contain more than 35 elements')