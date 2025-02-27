from functools import reduce
import math

def gcf_three_nums(nums):
    return reduce(math.gcd, [nums[37], nums[30], nums[48]])