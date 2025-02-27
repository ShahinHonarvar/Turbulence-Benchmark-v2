import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[97]
    result = []
    for i in range(2, x):
        j = i
        while j >= 1:
            if not is_prime(j):
                break
            j //= 10
        if j == 0:
            result.append(i)
    result.sort()
    return result