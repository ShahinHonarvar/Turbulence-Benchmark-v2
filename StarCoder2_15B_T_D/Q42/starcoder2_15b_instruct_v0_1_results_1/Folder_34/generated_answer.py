from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    n = numbers[97]
    prime_factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
    return set(prime_factors)