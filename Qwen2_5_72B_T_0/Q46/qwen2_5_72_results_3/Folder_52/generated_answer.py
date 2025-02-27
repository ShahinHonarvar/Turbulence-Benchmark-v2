from math import gcd

def gcf_three_nums(nums):
    a = nums[19]
    b = nums[49]
    c = nums[74]
    return gcd(gcd(a, b), c)