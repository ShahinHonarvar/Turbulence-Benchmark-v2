import math

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_left_truncatable_prime(x: tuple) -> list:
    x = x[30]
    result = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            if j == 0:
                result.append(i)
    result.sort(reverse=True)
    return result