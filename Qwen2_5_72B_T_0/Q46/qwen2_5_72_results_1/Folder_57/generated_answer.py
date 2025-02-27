from math import gcd

def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    return gcd(gcd(a, b), c)