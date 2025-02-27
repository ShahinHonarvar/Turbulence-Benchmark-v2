from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[66], nums[56], nums[92]])