from math import gcd

def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]
    return gcd(gcd(a, b), c)