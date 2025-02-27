from math import gcd

def gcf_three_nums(nums):
    a = nums[99]
    b = nums[28]
    c = nums[53]
    return gcd(gcd(a, b), c)