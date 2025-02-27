from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[90], nums[84], nums[47]])