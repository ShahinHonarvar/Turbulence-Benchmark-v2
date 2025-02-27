from math import gcd

def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]
    return gcd(gcd(a, b), c)