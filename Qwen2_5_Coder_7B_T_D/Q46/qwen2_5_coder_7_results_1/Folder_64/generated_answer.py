from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[0], nums[8], nums[3]])