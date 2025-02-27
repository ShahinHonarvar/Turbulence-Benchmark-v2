from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def all_left_truncatable_prime(nums):
    x = nums[94]
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        truncated_prime = prime
        while truncated_prime > 0:
            if truncated_prime not in primes:
                is_left_truncatable = False
                break
            truncated_prime //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)