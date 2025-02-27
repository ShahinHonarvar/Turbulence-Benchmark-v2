import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    result = []
    for i in range(2, x):
        left_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                left_truncatable = False
                break
        if left_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result