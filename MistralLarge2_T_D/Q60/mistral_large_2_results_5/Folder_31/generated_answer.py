import sympy

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    while s:
        if not sympy.isprime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[50]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)