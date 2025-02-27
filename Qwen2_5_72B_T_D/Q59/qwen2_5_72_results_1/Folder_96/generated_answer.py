from itertools import takewhile
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[29]

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    candidates = filter(lambda n: '0' not in str(n), range(2, x))
    return sorted(filter(is_left_truncatable_prime, candidates))