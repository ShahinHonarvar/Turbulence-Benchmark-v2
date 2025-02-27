from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    if len(lst) < 991:
        raise IndexError('List does not have an index 990')
    num = lst[990]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors