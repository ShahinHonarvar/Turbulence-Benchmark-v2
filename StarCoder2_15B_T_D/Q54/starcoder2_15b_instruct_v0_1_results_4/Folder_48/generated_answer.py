import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[835]
    result = []
    for n in range(2, x):
        num = n
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            result.append(n)
    return sorted(result)