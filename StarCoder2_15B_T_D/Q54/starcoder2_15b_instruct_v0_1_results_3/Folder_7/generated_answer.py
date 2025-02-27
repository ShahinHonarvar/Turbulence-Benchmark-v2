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

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    result = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                result.append(i)
    result.sort()
    return result