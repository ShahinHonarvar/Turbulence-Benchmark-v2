from functools import reduce
import math

def gcf_two_nums(nums):
    return reduce(math.gcd, nums[63:85])