import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            result.append(num)
    return sorted(result)