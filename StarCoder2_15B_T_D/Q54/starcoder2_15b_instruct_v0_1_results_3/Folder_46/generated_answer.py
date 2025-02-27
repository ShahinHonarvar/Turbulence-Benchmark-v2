import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[33]
    result = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            result.append(i)
    return sorted(result)