import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if num >= 10 ** 2 and num <= 10 ** 2 + 96:
            s = str(num)
            if not '0' in s and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
                result.append(num)
    result.sort(reverse=True)
    return result