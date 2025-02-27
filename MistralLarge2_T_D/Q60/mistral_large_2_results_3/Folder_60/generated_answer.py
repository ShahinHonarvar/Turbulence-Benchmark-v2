import sympy

def is_truncatable_prime(n):
    if any((digit == '0' for digit in str(n))):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[87]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes)