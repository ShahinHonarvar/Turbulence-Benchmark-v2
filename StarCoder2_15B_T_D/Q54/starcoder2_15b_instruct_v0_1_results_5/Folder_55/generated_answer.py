import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[73]
    result = []
    for i in range(2, x):
        current = i
        while current > 0:
            if not is_prime(current):
                break
            current //= 10
        if current == 0:
            result.append(i)
    return sorted(result, reverse=True)