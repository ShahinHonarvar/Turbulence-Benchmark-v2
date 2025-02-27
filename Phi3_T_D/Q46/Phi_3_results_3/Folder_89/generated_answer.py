from math import gcd

def gcf_three_nums(nums):
    if len(nums) > 11:
        return gcd(gcd(nums[63], nums[73]), nums[11])
    else:
        raise ValueError('List must contain at least 12 elements')