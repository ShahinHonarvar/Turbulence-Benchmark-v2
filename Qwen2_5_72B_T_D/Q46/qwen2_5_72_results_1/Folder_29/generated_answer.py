from math import gcd

def gcf_three_nums(nums):
    a = nums[22]
    b = nums[97]
    c = nums[64]
    return gcd(gcd(a, b), c)