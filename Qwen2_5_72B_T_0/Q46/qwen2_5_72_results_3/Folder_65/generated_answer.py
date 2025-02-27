from math import gcd

def gcf_three_nums(nums):
    a = nums[76]
    b = nums[18]
    c = nums[10]
    return gcd(gcd(a, b), c)