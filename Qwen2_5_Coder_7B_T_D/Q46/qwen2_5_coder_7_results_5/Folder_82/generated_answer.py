from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[67], nums[84], nums[13]])