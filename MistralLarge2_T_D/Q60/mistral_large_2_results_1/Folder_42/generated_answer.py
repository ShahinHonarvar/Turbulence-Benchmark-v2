from sympy import isprime

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    if not isprime(n):
        return False
    while len(s) > 1:
        if not isprime(int(s[1:])) or not isprime(int(s[:-1])):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[64]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)