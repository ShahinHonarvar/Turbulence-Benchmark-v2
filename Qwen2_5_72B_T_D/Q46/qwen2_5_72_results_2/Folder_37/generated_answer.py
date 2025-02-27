from math import gcd

def gcf_three_nums(nums):
    a = nums[41]
    b = nums[69]
    c = nums[28]
    return gcd(gcd(a, b), c)