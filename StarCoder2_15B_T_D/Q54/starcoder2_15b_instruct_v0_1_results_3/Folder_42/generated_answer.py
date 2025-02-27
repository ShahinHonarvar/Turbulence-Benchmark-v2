import math

def is_right_truncatable_prime(num):
    num_str = str(num)
    while len(num_str) > 0:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[:-1]
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[64]
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)