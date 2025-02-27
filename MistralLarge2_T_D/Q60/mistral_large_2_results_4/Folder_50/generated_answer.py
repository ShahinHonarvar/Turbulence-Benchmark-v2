from sympy import isprime

def is_left_right_truncatable(n):
    s = str(n)
    while len(s) > 1:
        if not isprime(int(s)) or '0' in s:
            return False
        s = s[1:-1]
    return isprime(int(s))

def all_left_right_truncatable_prime(tup):
    x = tup[57]
    primes = [n for n in range(2, x + 1) if isprime(n)]
    truncatable_primes = [n for n in primes if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)