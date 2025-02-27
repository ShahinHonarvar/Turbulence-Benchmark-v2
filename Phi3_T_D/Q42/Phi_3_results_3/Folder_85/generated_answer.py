from sympy import primefactors

def prime_factors(numbers):
    num = numbers[23]
    return set(primefactors(num))