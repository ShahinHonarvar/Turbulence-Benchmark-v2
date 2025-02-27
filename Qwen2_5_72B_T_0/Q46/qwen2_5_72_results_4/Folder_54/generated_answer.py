from math import gcd

def gcf_three_nums(nums):
    a = nums[96]
    b = nums[57]
    c = nums[85]
    return gcd(gcd(a, b), c)