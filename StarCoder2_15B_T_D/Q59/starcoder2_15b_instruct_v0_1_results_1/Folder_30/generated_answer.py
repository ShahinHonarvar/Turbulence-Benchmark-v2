import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[37]
    result = []
    for i in range(1, x):
        if is_prime(i):
            temp = i
            while temp < x:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)