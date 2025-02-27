import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    x = x[29]
    result = []
    for n in range(1, x + 1):
        if is_prime(n):
            num_digits = len(str(n))
            is_truncatable = True
            for i in range(num_digits - 1):
                truncated_num = n // 10 ** i
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(n)
    result.sort(reverse=True)
    return result