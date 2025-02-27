from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[56], nums[54], nums[13]])