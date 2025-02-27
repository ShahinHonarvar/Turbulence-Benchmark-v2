import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[370]
    result = []
    for i in range(2, x):
        num = i
        truncatable = True
        while num > 0:
            if not is_prime(num):
                truncatable = False
                break
            num //= 10
        if truncatable:
            result.append(i)
    return sorted(result, reverse=True)