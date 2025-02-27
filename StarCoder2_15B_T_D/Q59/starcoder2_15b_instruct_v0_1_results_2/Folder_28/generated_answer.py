import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[19]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return sorted(result)