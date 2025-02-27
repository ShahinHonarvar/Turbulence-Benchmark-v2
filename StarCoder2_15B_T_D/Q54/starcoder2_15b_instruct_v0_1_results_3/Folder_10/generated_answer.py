import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[38]
    result = []
    for i in range(2, x):
        temp = i
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            result.append(i)
    result.sort(reverse=True)
    return result