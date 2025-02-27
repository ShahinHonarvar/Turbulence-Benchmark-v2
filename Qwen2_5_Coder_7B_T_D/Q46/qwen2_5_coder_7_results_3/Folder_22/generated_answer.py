from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[27], nums[85], nums[51]])