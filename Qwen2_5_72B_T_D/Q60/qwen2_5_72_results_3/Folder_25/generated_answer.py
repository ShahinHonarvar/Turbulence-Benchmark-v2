from itertools import dropwhile
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = [p for p in range(2, x + 1) if isprime(p) and '0' not in str(p)]

    def is_truncatable(prime):
        s = str(prime)
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:-i]))):
                return False
        return True
    truncatable_primes = list(filter(is_truncatable, primes))
    return truncatable_primes