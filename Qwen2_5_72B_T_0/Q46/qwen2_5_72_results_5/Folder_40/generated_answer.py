from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[1], nums[6], nums[8])
    return gcd(gcd(a, b), c)