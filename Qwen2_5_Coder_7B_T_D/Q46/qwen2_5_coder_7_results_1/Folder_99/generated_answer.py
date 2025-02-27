import math
    from functools import reduce

def gcf_three_nums(nums):
    return reduce(math.gcd, [nums[912], nums[170], nums[500]])