from math import gcd

def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    return gcd(gcd(a, b), c)