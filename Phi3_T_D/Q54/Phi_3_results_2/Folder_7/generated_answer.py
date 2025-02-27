def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_right_truncatable_prime(n, primes_cache):
    if n == 0:
        return True
    if n not in primes_cache:
        return is_prime(n) and all((is_right_truncatable_prime(int(str(n)[:-i]), primes_cache) for i in range(len(str(n)), 0, -1)))
    return primes_cache[n]

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[802]
    primes_cache = {2: True}
    for i in range(3, x, 2):
        if is_prime(i):
            primes_cache[i] = is_right_truncatable_prime(i, primes_cache)
    return sorted([prime for prime in primes_cache if primes_cache[prime]])