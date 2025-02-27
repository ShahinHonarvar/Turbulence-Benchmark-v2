from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[991], nums[244], nums[974]])