from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[62], nums[96], nums[26]])