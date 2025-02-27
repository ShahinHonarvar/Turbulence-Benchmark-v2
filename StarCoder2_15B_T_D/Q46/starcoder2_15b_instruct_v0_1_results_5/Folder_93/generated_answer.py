from functools import reduce
from math import gcd

def gcf_three_nums(nums):
    return reduce(gcd, nums[25], nums[76], nums[57])