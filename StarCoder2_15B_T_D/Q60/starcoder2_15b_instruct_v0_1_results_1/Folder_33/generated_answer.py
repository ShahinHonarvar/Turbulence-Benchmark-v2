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

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]

    def is_truncatable(n):
        if not is_prime(n):
            return False
        s = str(n)
        if len(s) <= 2:
            return is_prime(n)
        if not is_truncatable(int(s[1:])):
            return False
        if not is_truncatable(int(s[:-1])):
            return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    return result