def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def isRTruncatable(n, base):
    while n > 0:
        if not isprime(n):
            return False
        n //= base
    return True

def all_right_truncatable_prime(n_tuple):
    x = n_tuple[32]
    base = 10
    truncable_primes = []
    for p in range(2, x):
        if isprime(p) and isRTruncatable(p, base):
            truncable_primes.append(p)
    return sorted(truncable_primes)