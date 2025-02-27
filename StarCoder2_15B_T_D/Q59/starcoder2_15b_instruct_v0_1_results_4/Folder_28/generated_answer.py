import re
import math

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    prime_numbers = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_prime_numbers = [n for n in prime_numbers if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_prime_numbers)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    if is_prime(n) and is_left_truncatable_prime(n // 10):
        return True
    return False