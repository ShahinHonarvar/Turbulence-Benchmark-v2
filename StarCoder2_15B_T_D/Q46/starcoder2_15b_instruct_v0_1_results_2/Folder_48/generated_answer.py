from functools import reduce
import math

def gcf_three_nums(nums):
    return reduce(math.gcd, [nums[654], nums[312], nums[441]])