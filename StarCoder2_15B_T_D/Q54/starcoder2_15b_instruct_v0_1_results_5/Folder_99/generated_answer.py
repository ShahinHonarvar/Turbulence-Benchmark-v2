import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    result = []
    x = numbers[758]
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(len(str(i)) - 1, 0, -1):
            if not is_prime(int(str(i)[:j])):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(i):
            result.append(i)
    return sorted(result)