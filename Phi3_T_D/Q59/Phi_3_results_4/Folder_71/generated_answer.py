def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def left_truncatable_primes_generator(n, primes):
    for p in reversed(primes):
        if p <= n and is_left_truncatable_prime(p, primes):
            yield p

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[22]
    primes = set(filter(is_prime, range(2, x)))
    return sorted(left_truncatable_primes_generator(x, primes), reverse=True)