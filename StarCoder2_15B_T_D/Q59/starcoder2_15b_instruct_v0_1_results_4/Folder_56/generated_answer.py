import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[30]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            result.append(i)
    return sorted(result)