from math import gcd

def gcf_three_nums(nums):
    a = nums[13]
    b = nums[46]
    c = nums[49]
    return gcd(gcd(a, b), c)