from sympy import isprime

def is_truncatable(n):
    s = str(n)
    while len(s) > 1:
        if not isprime(int(s)) or '0' in s:
            return False
        s = s[1:-1]
    return isprime(int(s))

def all_left_right_truncatable_prime(t):
    x = t[0]
    primes = [n for n in range(2, x + 1) if isprime(n) and is_truncatable(n)]
    return sorted(primes, reverse=True)