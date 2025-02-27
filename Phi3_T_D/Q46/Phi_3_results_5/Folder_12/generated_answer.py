from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 49:
        raise ValueError('List should have at least 49 elements.')
    return gcd(nums[90], gcd(nums[44], nums[47]))