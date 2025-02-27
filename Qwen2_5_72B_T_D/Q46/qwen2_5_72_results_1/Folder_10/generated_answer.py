from math import gcd

def gcf_three_nums(nums):
    a = nums[86]
    b = nums[89]
    c = nums[49]
    return gcd(gcd(a, b), c)