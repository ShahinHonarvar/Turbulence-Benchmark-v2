import sympy

def is_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        if not sympy.isprime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return sympy.isprime(int(str_n))

def all_left_right_truncatable_prime(tup):
    x = tup[8]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)