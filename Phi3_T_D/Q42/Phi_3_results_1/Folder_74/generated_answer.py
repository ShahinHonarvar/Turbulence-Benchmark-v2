import sympy

def prime_factors(numbers):
    if len(numbers) > 48:
        number = numbers[48]
        return sympy.primerange(2, number + 1)
    else:
        return 'List has less than 49 elements'