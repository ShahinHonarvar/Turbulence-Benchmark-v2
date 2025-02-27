from sympy import isprime

def is_left_right_truncatable_prime(n):
    if not isprime(n) or '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        if not isprime(int(s[1:-1])):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[618]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])