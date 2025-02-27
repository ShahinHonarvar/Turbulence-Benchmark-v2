import sympy

def is_truncatable_prime(n):
    if not sympy.isprime(n) or '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        s = s[1:-1]
        if not sympy.isprime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(tuples):
    x = tuples[61]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)])