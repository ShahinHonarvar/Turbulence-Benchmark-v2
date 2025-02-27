import itertools
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:-i])
        if not is_prime(left) or not is_prime(right):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)