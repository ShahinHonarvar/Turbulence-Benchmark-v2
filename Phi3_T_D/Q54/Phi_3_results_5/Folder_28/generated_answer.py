def is_right_truncatable_prime(n, prime_set):
    while n > 0:
        if not is_prime(n, prime_set):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 20:
        raise ValueError('Tuple must contain at least 20 positive integers.')
    x = numbers[19]
    return sorted([p for p in range(2, x) if is_right_truncatable_prime(p, primes_sieve(x))])

def primes_sieve(x):
    sieve = [True] * (x + 1)
    for p in range(2, x + 1):
        if sieve[p]:
            for i in range(p * p, x + 1, p):
                sieve[i] = False
    return set((p for p in range(2, x) if sieve[p]))

def is_prime(n, prime_set):
    return n in prime_set