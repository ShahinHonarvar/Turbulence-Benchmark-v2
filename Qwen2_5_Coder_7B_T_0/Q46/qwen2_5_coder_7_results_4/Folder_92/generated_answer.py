from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[7], nums[9], nums[0]])