from math import gcd

def gcf_three_nums(nums):
    a = nums[44]
    b = nums[91]
    c = nums[42]
    return gcd(gcd(a, b), c)