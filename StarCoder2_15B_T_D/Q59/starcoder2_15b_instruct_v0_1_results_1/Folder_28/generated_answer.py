import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[19]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                is_left_truncatable = False
                break
            num //= 10
        if is_left_truncatable:
            result.append(i)
    result.sort()
    return result