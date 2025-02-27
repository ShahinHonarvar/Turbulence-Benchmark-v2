import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[49]
    result = []
    for i in range(2, x):
        temp = i
        while temp >= 10:
            if not is_prime(temp):
                break
            temp //= 10
        if temp == 0 and is_prime(i):
            result.append(i)
    return sorted(result)