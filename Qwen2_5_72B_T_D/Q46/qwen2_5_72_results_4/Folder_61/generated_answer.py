from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[1], nums[2], nums[7])
    return gcd(gcd(a, b), c)