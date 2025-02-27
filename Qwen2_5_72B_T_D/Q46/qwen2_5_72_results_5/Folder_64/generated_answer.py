from math import gcd

def gcf_three_nums(nums):
    a = nums[0]
    b = nums[8]
    c = nums[3]
    return gcd(gcd(a, b), c)