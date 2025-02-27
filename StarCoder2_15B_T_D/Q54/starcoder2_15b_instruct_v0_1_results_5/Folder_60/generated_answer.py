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
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[:len(num_str) - i])
            if not is_prime(truncated_num):
                break
        else:
            result.append(num)
    result.sort()
    return result