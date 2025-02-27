import sympy

def is_left_right_truncatable_prime(n):
    if not sympy.isprime(n):
        return False
    digits = [int(d) for d in str(n)]
    for i in range(1, len(digits)):
        if not sympy.isprime(int(''.join(map(str, digits[i:])))):
            return False
    for i in range(len(digits) - 1, 0, -1):
        if not sympy.isprime(int(''.join(map(str, digits[:i])))):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[792]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])