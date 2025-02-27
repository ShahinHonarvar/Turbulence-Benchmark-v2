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

def all_left_right_truncatable_prime(tup):
    if len(tup) < 32:
        return []
    x = tup[31]
    result = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        num_str = str(i)
        length = len(num_str)
        is_truncatable = True
        for j in range(length):
            if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:length - j])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(i)
    return sorted(result, reverse=True)