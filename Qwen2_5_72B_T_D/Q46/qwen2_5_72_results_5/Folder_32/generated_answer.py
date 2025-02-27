from math import gcd

def gcf_three_nums(nums):
    a = nums[20]
    b = nums[43]
    c = nums[95]
    return gcd(gcd(a, b), c)