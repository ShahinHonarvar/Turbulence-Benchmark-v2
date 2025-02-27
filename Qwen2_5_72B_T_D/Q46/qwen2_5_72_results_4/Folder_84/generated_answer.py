from math import gcd

def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]
    return gcd(gcd(a, b), c)