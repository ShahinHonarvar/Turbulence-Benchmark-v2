import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) < 88:
        raise IndexError('Index out of range')
    number = numbers[87]
    prime_factors = set()
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_factors.add(i)
    return prime_factors