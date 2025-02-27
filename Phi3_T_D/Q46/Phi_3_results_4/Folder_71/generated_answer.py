from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 3 or 24 not in range(len(nums)) or 45 not in range(len(nums)) or (38 not in range(len(nums))):
        raise ValueError('List must have at least 3 elements and contain indices 24, 45, and 38.')
    first, middle, last = (nums[24], nums[45], nums[38])
    result = gcd(first, middle)
    result = gcd(result, last)
    return result