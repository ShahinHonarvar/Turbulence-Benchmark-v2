from itertools import takewhile
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    target = numbers[35]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not (isprime(int(str(n)[i:])) and isprime(int(str(n)[:-i]))):
                return False
        return True
    primes = filter(is_truncatable_prime, takewhile(lambda x: x <= target, range(2, target + 1)))
    return sorted(primes, reverse=True)