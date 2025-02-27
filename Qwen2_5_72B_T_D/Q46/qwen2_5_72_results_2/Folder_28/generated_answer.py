from math import gcd

def gcf_three_nums(nums):
    a = nums[99]
    b = nums[63]
    c = nums[74]
    return gcd(gcd(a, b), c)