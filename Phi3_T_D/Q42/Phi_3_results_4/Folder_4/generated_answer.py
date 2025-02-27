from sympy import factorint

def prime_factors(numbers):
    if 15 < len(numbers):
        number = numbers[15]
    elif len(numbers) < 16:
        return set()
    else:
        number = 0
    if number <= 1:
        return set()
    factors = factorint(number)
    return set(factors.keys())