from math import gcd

def gcf_three_nums(nums):
    a = nums[3]
    b = nums[8]
    c = nums[9]
    return gcd(gcd(a, b), c)