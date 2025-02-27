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

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    result = []
    for i in range(1, x + 1):
        if is_prime(i):
            num_str = str(i)
            is_truncatable = True
            for j in range(len(num_str) - 1):
                if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:len(num_str) - j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result