from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[637], nums[411], nums[757]])