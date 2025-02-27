from math import gcd
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[654], nums[312], nums[441]])