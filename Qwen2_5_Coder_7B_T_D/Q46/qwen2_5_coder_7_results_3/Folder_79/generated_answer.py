from math import gcd
    import functools

def gcf_three_nums(nums):
    return functools.reduce(gcd, [nums[16], nums[87], nums[95]])