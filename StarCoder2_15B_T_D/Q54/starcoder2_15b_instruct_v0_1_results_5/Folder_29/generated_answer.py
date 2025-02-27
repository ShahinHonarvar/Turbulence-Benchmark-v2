import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[55]
    result = []
    for i in range(1, len(str(x)) + 1):
        num = int(str(x)[:-i])
        if is_prime(num):
            result.append(num)
        else:
            break
    return sorted(result, reverse=True)