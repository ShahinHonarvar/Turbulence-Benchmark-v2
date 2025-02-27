import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[65]
    results = []
    for num in range(2, x):
        is_right_truncatable = True
        for i in range(len(str(num)) - 1):
            truncated_num = int(str(num)[:-i - 1])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(num):
            results.append(num)
    return sorted(results, reverse=True)