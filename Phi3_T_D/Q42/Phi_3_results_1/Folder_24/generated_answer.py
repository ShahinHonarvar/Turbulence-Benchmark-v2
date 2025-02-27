import math

def prime_factors(numbers):
    if len(numbers) < 75:
        raise IndexError('Index out of range')
    number_to_factorize = numbers[74]
    factors = set()
    while number_to_factorize % 2 == 0:
        factors.add(2)
        number_to_factorize //= 2
    for i in range(3, int(math.sqrt(number_to_factorize)) + 1, 2):
        while number_to_factorize % i == 0:
            factors.add(i)
            number_to_factorize //= i
    if number_to_factorize > 2:
        factors.add(number_to_factorize)
    return factors