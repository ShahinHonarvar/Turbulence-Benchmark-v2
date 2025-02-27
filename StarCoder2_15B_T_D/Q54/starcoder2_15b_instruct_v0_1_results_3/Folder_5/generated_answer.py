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

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    right_truncatable_primes = []
    primes = sieve_of_eratosthenes(x)
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
    right_truncatable_primes.sort()
    return right_truncatable_primes