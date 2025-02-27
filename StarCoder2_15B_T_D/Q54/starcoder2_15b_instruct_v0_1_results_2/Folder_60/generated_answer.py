import math

def is_prime(n):
    if n < 2:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return right_truncatable_prime(n // 10)

def all_right_truncatable_prime(tup):
    x = tup[87]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)