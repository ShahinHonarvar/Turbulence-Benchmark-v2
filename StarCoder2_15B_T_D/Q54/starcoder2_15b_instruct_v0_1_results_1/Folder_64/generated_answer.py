import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[4]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result