import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            result.append(num)
    result = sorted(result)
    if len(result) > 0:
        return result
    else:
        return []