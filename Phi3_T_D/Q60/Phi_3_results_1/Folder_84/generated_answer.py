def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
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

def is_truncatable_prime(n):
    """Verify if a number is both left-truncatable and right-truncatable prime."""
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_primes(params):
    x = params[630]
    primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)