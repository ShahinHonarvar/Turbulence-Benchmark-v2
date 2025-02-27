import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[803]
    result = []
    for n in range(2, x):
        is_left_truncatable = True
        temp = n
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            result.append(n)
    return sorted(result)