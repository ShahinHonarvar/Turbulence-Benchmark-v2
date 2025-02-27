import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    return all((is_prime(int(n[:i])) for i in range(1, len(n))))

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    return sorted(filter(left_truncatable_prime, (str(i) for i in range(2, x) if '0' not in str(i))))