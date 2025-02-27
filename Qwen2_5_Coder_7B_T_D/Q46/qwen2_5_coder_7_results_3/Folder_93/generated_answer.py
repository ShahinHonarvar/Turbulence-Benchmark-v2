from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, nums[25:26] + nums[76:77] + nums[57:58])