import sympy

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    while len(str_num) > 1:
        if not sympy.isprime(int(str_num)):
            return False
        str_num = str_num[1:-1]
    return sympy.isprime(int(str_num))

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    primes = [n for n in range(2, x + 1) if sympy.isprime(n)]
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)