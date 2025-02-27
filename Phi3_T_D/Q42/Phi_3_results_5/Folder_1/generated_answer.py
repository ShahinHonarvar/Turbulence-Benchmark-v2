from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) > 85:
        return primefactors(numbers[85])
    return set()