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

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[14]
    result = []
    for i in range(2, x):
        is_right_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                is_right_truncatable = False
                break
            num //= 10
        if is_right_truncatable:
            result.append(i)
    result.sort()
    return result