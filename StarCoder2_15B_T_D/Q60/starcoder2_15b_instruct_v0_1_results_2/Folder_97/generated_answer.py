import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))