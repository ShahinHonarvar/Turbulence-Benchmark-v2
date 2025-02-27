import sympy

def prime_factors(numbers):
    return set(sympy.primefactors(numbers[28])) if len(numbers) > 28 else set()