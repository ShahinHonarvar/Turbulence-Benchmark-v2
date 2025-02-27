import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[37]
    result = []
    for i in range(2, x):
        number = i
        while number > 0:
            if not is_prime(number):
                break
            number //= 10
        else:
            result.append(i)
    result.sort(reverse=True)
    return result