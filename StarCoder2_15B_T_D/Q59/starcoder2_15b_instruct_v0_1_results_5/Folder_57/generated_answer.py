import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        is_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result