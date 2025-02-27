from math import gcd

def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]
    return gcd(gcd(a, b), c)