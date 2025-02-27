import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    result = []
    for i in range(2, x):
        n = i
        while n > 0:
            if is_prime(n):
                result.append(n)
                break
            n //= 10
    result.sort()
    return result