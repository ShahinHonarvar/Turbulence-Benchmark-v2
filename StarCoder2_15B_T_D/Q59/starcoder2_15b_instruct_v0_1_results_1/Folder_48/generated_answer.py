import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[835]
    result = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                result.append(i)
    return sorted(result)