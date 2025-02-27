import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(10):
            number = int(str(j) + str(numbers[i]))
            if is_prime(number):
                result.append(number)
            else:
                break
    return sorted(result)