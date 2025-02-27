import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1)))

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    return sorted((i for i in range(2, x) if is_right_truncatable_prime(i)))