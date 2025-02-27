from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[145], nums[183], nums[770]])