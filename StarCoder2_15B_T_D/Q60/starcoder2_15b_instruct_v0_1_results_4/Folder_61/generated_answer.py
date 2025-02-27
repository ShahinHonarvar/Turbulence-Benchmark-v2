import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(11, x + 1):
        is_truncatable = True
        num_str = str(i)
        for j in range(len(num_str) - 1):
            if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:len(num_str) - j])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result