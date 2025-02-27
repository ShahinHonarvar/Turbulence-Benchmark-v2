from itertools import takewhile
from math import sqrt

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_truncatable_prime(n)], reverse=True)