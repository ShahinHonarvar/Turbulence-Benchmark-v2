from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 100:
        raise ValueError('The provided list must have at least 100 elements.')
    return gcd(gcd(nums[99], nums[63]), nums[74])