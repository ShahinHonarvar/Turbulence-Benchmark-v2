from math import gcd

def gcf_three_nums(nums):
    a = nums[67]
    b = nums[84]
    c = nums[13]
    return gcd(gcd(a, b), c)