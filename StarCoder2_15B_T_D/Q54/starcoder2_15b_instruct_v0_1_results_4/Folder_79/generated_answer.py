import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[91]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            for j in range(len(str(i)) - 1):
                truncated_number = int(str(i)[:-j - 1])
                if not is_prime(truncated_number):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(i)
    result.sort()
    return result