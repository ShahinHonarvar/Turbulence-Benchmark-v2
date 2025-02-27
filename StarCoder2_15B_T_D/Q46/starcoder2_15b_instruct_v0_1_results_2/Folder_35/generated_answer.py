from fractions import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[742], nums[888], nums[629]])