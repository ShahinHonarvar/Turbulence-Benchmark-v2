from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[252], nums[149], nums[564]])