import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[23]
    result = []
    for i in range(2, x):
        num = i
        is_truncatable = True
        while num > 0:
            if not is_prime(num):
                is_truncatable = False
                break
            num //= 10
        if is_truncatable:
            result.append(i)
    return sorted(result)