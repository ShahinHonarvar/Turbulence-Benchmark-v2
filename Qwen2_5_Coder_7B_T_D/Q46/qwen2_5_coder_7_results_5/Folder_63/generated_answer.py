from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[38], nums[52], nums[69]])