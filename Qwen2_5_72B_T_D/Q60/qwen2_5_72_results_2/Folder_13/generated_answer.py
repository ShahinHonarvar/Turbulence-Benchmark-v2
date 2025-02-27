from itertools import takewhile
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]

    def is_truncatable_prime(n):
        if '0' in str(n) or n < 2:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return True
    primes = list(takewhile(lambda p: p <= x, (i for i in range(2, x + 1) if isprime(i))))
    truncatable_primes = list(filter(is_truncatable_prime, primes))
    return truncatable_primes