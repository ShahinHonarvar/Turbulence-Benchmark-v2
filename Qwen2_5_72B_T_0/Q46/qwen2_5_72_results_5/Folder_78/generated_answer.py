from math import gcd

def gcf_three_nums(nums):
    a = nums[13]
    b = nums[70]
    c = nums[32]
    return gcd(gcd(a, b), c)