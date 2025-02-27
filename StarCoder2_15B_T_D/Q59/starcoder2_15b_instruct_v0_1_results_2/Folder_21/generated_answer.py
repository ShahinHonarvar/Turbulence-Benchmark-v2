import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    result = []
    for i in range(2, x):
        truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                truncatable = False
                break
            num //= 10
        if truncatable:
            result.append(i)
    return sorted(result)