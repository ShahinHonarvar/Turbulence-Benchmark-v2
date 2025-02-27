from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[558], nums[110], nums[628]])