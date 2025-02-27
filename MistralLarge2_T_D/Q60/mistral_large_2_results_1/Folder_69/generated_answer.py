def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        if not is_prime(int(s[1:])) or not is_prime(int(s[:-1])):
            return False
        s = s[1:-1]
    return is_prime(int(s))

def all_left_right_truncatable_prime(t):
    x = t[760]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)