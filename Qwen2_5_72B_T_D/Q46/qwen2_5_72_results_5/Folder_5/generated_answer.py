from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[64], nums[80], nums[15])
    return gcd(gcd(a, b), c)