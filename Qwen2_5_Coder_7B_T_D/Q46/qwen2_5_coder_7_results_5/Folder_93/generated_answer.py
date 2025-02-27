from math import gcd
    import functools

def gcf_three_nums(nums):
    return functools.reduce(gcd, (nums[25], nums[76], nums[57]))