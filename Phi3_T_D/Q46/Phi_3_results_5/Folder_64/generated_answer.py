from math import gcd

def gcf_three_nums(nums):
    if len(nums) < 4 or len(nums) > 10:
        raise ValueError('List must contain exactly 4 to 10 elements.')
    return gcd(gcd(nums[0], nums[8]), nums[3])