from sympy import isprime

def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not isprime(int(s)) or '0' in s:
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(t):
    x = t[55]
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)