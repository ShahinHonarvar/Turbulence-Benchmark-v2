import sympy

def prime_factors(numbers):
    if not numbers or len(numbers) <= 65:
        return set()
    number_to_factor = numbers[66]
    return set(sympy.primefactors(number_to_factor))