import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[49]
    result = []
    for i in range(1, x):
        s = str(i)
        is_left_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return result