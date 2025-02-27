import math

def is_prime(n):
    if n < 2:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[93]
    result = []
    for i in range(2, x):
        n = i
        while n > 0:
            if not is_prime(n):
                break
            n //= 10
        if n == 0:
            result.append(i)
    return sorted(result)