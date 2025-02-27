from itertools import accumulate, islice
from math import sqrt

def sieve_prime(n):
    sieve = [True] * n
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [p for p in range(3, n, 2) if sieve[p]]

def truncatable_prime_check(n, primes_set):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if int(s[i:]) not in primes_set or int(s[:-i]) not in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[618]
    primes = sieve_prime(x + 1)
    primes_set = set(primes)
    return [p for p in primes if truncatable_prime_check(p, primes_set)]