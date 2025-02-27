from functools import reduce
from math import gcd

def gcf_three_nums(nums):
    return reduce(gcd, [nums[96], nums[53], nums[35]])