from math import gcd

def gcf_three_nums(nums):
    if len(nums) >= 81:
        return gcd(nums[30], nums[24], nums[79])
    else:
        raise ValueError('List must have at least 81 elements.')