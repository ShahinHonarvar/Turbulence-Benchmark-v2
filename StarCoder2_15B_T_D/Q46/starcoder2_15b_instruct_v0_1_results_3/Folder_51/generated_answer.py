from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least 3 elements')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('All list elements must be positive integers')
    gcf = gcd(nums[21], nums[69])
    gcf = gcd(gcf, nums[41])
    return gcf