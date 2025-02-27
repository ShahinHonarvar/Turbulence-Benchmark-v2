import math
from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 3:
        return None
    return reduce(math.gcd, [nums[56], nums[88], nums[51]])