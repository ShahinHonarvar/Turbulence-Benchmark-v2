from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) <= 985:
        return primefactors(numbers[985])
    else:
        return 'Index out of range'