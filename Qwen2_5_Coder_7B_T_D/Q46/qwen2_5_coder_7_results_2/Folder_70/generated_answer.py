from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[990], nums[671], nums[711]])