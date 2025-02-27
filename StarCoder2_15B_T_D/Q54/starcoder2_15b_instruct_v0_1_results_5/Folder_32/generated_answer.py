from math import log10, floor

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    result = []
    x = nums[42]
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            for j in range(int(log10(i)) - 1, -1, -1):
                if not is_prime(floor(i / 10 ** j)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(i)
    result.sort()
    return result