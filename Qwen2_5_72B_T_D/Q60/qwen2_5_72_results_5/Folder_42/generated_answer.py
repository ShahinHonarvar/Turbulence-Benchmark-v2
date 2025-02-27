from itertools import dropwhile
from sympy import isprime

def all_left_right_truncatable_prime(data):
    x = data[64]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not (isprime(int(str(n)[i:])) and isprime(int(str(n)[:-i]))):
                return False
        return True
    return list(dropwhile(lambda n: not is_truncatable_prime(n), reversed(range(2, x + 1))))