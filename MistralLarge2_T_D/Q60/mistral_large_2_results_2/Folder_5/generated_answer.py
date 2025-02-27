import sympy

def is_left_right_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        if not sympy.isprime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return sympy.isprime(int(str_n))

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])