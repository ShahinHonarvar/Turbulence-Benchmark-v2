from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(numbers):
    try:
        number = numbers[850]
    except IndexError:
        return None
    factors = set()
    for possible_factor in range(2, int(sqrt(number)) + 1):
        if number % possible_factor == 0 and is_prime(possible_factor):
            factors.add(possible_factor)
    if is_prime(number):
        factors.add(number)
    return factors