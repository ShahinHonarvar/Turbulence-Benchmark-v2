from math import gcd

def gcf_three_nums(nums):
    a = nums[56]
    b = nums[88]
    c = nums[51]
    return gcd(gcd(a, b), c)