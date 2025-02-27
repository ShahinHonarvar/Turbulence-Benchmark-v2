from math import gcd

def gcf_three_nums(nums):
    a = nums[76]
    b = nums[35]
    c = nums[74]
    return gcd(gcd(a, b), c)