from itertools import dropwhile
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not (isprime(int(n_str[i:])) and isprime(int(n_str[:-i]))):
                return False
        return True
    return list(dropwhile(lambda v: v > x, filter(is_truncatable_prime, (2, 3, 5, 7, *range(11, x + 1)))))