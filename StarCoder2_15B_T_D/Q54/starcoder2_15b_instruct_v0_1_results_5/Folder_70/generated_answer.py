import math

def is_right_truncatable_prime(num):
    if num < 10 and is_prime(num):
        return True
    if num % 10 == 0 or not is_prime(num):
        return False
    return is_right_truncatable_prime(num // 10)

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result