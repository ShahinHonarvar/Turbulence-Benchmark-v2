from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 105:
        raise ValueError('The list must have at least 105 elements.')
    return gcd(nums[90], gcd(nums[41], nums[95]))