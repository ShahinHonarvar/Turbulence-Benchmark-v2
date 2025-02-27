import math

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def all_left_truncatable_prime(t):
    if len(t) == 0:
        return []
    x = t[32]
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        number = prime
        while number > 0:
            number //= 10
            if number == 0:
                break
            if number not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)