from math import gcd

def gcf_three_nums(nums):
    a = nums[31]
    b = nums[25]
    c = nums[80]
    return gcd(gcd(a, b), c)