from math import sqrt
from random import randrange

def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k, q = (0, n - 1)
    while q % 2 == 0:
        k += 1
        q //= 2

    def trial_composite(a):
        if pow(a, q, n) == 1:
            return False
        for i in range(k):
            if pow(a, 2 ** i * q, n) == n - 1:
                return False
        return True
    for i in range(10):
        a = randrange(2, n)
        if trial_composite(a):
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[618]
    truncatable_primes = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        truncatable = True
        for j in range(len(str(i)) - 1):
            if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:len(str(i)) - j])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)