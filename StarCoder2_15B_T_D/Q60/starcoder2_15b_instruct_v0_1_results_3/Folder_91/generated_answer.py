import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    if len(x) == 0 or x[0] < 2:
        return []
    result = []
    for i in range(2, x[0] + 1):
        if is_prime(i):
            num_str = str(i)
            if '0' not in num_str:
                for j in range(1, len(num_str)):
                    if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:len(num_str) - j])):
                        break
                else:
                    result.append(i)
    return sorted(result, reverse=True)