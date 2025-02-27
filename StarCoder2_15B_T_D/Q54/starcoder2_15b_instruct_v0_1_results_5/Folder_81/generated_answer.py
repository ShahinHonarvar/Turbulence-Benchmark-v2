import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    x = nums[98]
    for i in range(2, x):
        n = i
        while n < x:
            if not is_prime(n):
                break
            n //= 10
        else:
            result.append(i)
    return sorted(result)