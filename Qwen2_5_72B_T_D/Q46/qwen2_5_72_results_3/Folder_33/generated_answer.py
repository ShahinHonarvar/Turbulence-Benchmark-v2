from math import gcd

def gcf_three_nums(nums):
    a = nums[252]
    b = nums[149]
    c = nums[564]
    return gcd(gcd(a, b), c)