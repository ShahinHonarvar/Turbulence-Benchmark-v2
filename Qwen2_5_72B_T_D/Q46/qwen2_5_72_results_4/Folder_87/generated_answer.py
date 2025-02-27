from math import gcd

def gcf_three_nums(nums):
    a = nums[74]
    b = nums[60]
    c = nums[28]
    return gcd(gcd(a, b), c)