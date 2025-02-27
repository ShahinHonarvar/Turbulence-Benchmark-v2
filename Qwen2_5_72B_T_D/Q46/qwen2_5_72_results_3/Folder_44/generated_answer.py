from math import gcd

def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    return gcd(gcd(a, b), c)