from math import gcd

def gcf_three_nums(nums):
    a = nums[59]
    b = nums[93]
    c = nums[84]
    return gcd(gcd(a, b), c)