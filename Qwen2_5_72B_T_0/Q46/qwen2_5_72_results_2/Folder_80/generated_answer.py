from math import gcd

def gcf_three_nums(nums):
    a = nums[13]
    b = nums[76]
    c = nums[44]
    return gcd(gcd(a, b), c)