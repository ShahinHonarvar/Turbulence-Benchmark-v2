from math import gcd

def gcf_three_nums(nums):
    a = nums[27]
    b = nums[85]
    c = nums[51]
    return gcd(gcd(a, b), c)