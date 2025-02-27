import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[0]
    result = []
    for i in range(10, x + 1):
        num = i
        while num >= 10:
            if not is_prime(num):
                break
            num //= 10
        if num == 0:
            continue
        num = i
        while num >= 10:
            if not is_prime(num):
                break
            num %= 10 ** (len(str(num)) - 1)
        if num == 0:
            continue
        result.append(i)
    result.sort()
    return result