import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result