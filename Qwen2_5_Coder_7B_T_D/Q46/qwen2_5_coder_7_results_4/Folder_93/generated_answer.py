from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[25], nums[76], nums[57]])