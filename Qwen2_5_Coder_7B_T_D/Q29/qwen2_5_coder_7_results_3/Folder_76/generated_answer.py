from math import gcd
from functools import reduce

def gcf_two_nums(nums):
    return reduce(gcd, [nums[184], nums[307]])