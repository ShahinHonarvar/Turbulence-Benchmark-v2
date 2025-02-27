from math import gcd

def gcf_three_nums(nums):
    a = nums[36]
    b = nums[85]
    c = nums[83]
    return gcd(gcd(a, b), c)