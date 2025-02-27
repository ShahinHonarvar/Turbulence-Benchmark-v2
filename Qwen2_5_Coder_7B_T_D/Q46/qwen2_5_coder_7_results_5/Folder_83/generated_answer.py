from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, nums[56:57] + nums[54:55] + nums[13:14])