import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[65]
    primes = sieve_of_eratosthenes(x)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        truncated_prime = prime // 10
        while truncated_prime > 0:
            if truncated_prime not in primes:
                is_right_truncatable = False
                break
            truncated_prime //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes