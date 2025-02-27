from math import gcd

def gcf_three_nums(nums):
    a = nums[0]
    b = nums[3]
    c = nums[8]
    return gcd(gcd(a, b), c)