from math import gcd

def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    return gcd(gcd(a, b), c)