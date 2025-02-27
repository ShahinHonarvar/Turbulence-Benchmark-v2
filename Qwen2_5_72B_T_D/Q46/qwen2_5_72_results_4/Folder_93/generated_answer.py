from math import gcd

def gcf_three_nums(nums):
    a = nums[25]
    b = nums[76]
    c = nums[57]
    return gcd(gcd(a, b), c)