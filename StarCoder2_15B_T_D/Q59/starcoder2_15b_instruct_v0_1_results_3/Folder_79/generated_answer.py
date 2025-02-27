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

def all_left_truncatable_prime(tup):
    x = tup[90]
    result = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            j = i
            while j > 0:
                if not is_prime(j):
                    truncatable = False
                    break
                j //= 10
            if truncatable:
                result.append(i)
    result.sort()
    return result