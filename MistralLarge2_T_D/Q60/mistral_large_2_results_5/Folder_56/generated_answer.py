from sympy import isprime

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    while s:
        if not isprime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[30]
    primes = [n for n in range(2, x + 1) if isprime(n)]
    truncatable_primes = [n for n in primes if is_truncatable_prime(n)]
    return sorted(truncatable_primes)