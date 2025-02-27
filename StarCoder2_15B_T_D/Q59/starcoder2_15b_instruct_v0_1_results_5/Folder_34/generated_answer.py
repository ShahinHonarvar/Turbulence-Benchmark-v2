from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[18]
    result = []
    for i in range(1, x):
        num = i
        while num < x:
            if not is_prime(num):
                break
            num //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)