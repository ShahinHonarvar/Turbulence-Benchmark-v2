import math

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def all_left_truncatable_prime(t):
    x = t[0]
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for prime in primes:
        if prime < 10:
            continue
        is_left_truncatable = True
        while prime > 0:
            if prime not in primes:
                is_left_truncatable = False
                break
            prime //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)