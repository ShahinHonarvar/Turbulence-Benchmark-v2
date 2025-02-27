from functools import reduce
import math

def gcf_three_nums(nums):
    return reduce(math.gcd, [nums[38], nums[52], nums[69]])