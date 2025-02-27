import math

def is_prime(n: int) -> bool:
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

def all_left_truncatable_prime(t: tuple) -> list:
    x = t[28]
    result = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j < x:
                if not is_prime(j):
                    break
                j //= 10
            else:
                result.append(i)
    return sorted(result)