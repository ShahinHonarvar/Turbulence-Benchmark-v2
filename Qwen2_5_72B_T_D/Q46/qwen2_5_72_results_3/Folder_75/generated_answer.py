from math import gcd

def gcf_three_nums(nums):
    a = nums[70]
    b = nums[98]
    c = nums[22]
    return gcd(gcd(a, b), c)