def is_left_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def all_left_truncatable_prime(t):
    x = t[758]
    left_truncatable_primes = []
    n = 2
    while n < x:
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
        n += 1
    left_truncatable_primes.sort()
    return left_truncatable_primes