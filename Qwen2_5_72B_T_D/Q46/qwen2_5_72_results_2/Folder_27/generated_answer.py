from math import gcd

def gcf_three_nums(nums):
    a = nums[76]
    b = nums[64]
    c = nums[28]
    return gcd(gcd(a, b), c)