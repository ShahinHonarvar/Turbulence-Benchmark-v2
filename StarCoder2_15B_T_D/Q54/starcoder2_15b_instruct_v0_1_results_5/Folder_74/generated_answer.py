import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if num < 37:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                truncated_num = int(str(num)[:-i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    result.sort()
    return result