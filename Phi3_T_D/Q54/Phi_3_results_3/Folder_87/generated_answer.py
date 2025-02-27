def is_right_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    primes = set(range(2, x))
    for num in range(2, x):
        if num in primes:
            primes -= set(range(num * 2, x, num))
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, set(primes))]
    return sorted(right_truncatable_primes, reverse=True)