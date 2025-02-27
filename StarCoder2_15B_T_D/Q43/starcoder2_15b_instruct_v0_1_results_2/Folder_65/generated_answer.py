import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [n for i, n in enumerate(lst) if 76 <= i <= 92 and is_prime(n)]
    return sorted(primes)