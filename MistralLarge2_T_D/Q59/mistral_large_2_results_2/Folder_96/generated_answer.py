from sympy import isprime

def is_left_truncatable_prime(n):
    n = str(n)
    if '0' in n:
        return False
    while n:
        if not isprime(int(n)):
            return False
        n = n[1:]
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    return sorted((n for n in range(2, x) if is_left_truncatable_prime(n)))