import sympy

def is_left_right_truncatable_prime(n):
    if not sympy.isprime(n):
        return False
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(len(n_str)):
        if not sympy.isprime(int(n_str[i:])):
            return False
    for i in range(len(n_str), 0, -1):
        if not sympy.isprime(int(n_str[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])