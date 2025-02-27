import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[86]
    result = []
    for num in range(2, x):
        if is_prime(num):
            left_truncatable = True
            for i in range(len(str(num)) - 1):
                truncated_num = int(str(num)[i + 1:])
                if not is_prime(truncated_num):
                    left_truncatable = False
                    break
            if left_truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result