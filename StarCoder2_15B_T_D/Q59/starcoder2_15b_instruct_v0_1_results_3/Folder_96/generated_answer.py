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
        if is_prime(num) and num > 9:
            remaining = num // 10
            if is_prime(remaining):
                result.append(num)
    return sorted(result)