import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num >= 10:
        num //= 10
        if not is_prime(num):
            return False
    return True