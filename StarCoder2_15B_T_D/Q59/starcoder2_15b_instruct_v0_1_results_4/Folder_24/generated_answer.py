def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    x = x[65]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n, [])], reverse=True)

def is_left_truncatable_prime(n, primes):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return is_left_truncatable_prime(n // 10, primes + [n])