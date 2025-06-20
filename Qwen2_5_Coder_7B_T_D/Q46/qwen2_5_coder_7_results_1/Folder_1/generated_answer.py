from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[74], nums[51], nums[27]])