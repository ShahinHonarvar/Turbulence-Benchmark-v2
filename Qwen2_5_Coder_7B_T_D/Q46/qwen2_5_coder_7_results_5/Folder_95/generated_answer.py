from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[87], nums[20], nums[36]])