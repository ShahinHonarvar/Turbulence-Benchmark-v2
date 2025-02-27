import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    result = []
    for i in range(2, x):
        num = i
        is_right_truncatable = True
        while num > 0:
            if not is_prime(num):
                is_right_truncatable = False
                break
            num //= 10
        if is_right_truncatable:
            result.append(i)
    return sorted(result, reverse=True)