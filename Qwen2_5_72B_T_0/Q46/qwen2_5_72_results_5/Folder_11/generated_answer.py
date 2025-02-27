from math import gcd

def gcf_three_nums(nums):
    a = nums[37]
    b = nums[30]
    c = nums[48]
    return gcd(gcd(a, b), c)