from itertools import permutations
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes