import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[25]
    result = []
    for i in range(2, x):
        temp = i
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)