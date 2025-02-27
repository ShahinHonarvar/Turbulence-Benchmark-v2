from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[10], nums[55], nums[36]])