from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(arr):
    if len(arr) <= 100:
        return set()
    factors = set()
    number = arr[100]
    while number % 2 == 0:
        factors.add(2)
        number //= 2
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 2:
        factors.add(number)
    return factors if is_prime(arr[100]) else set()