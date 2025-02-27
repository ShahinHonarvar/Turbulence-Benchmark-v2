from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[74], nums[51], nums[27])
    return gcd(gcd(a, b), c)