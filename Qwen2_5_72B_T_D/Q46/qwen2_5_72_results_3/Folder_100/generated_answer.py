from math import gcd

def gcf_three_nums(nums):
    a = nums[21]
    b = nums[51]
    c = nums[33]
    return gcd(gcd(a, b), c)