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

def all_left_truncatable_prime(tup):
    x = tup[24]
    result = []
    for i in range(2, x):
        if is_prime(i):
            left_truncatable = True
            for j in range(len(str(i)) - 1):
                if not is_prime(int(str(i)[j + 1:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                result.append(i)
    return sorted(result)