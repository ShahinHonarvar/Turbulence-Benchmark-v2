import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(arg):
    x = arg[79]
    result = []
    for i in range(2, x):
        number = i
        while number > 0:
            if is_prime(number):
                result.append(number)
                break
            number //= 10
    result.sort(reverse=True)
    return result