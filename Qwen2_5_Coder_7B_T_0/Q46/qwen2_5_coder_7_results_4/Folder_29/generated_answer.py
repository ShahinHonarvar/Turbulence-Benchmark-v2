from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[22], nums[97], nums[64]])