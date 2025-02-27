from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[96], nums[53], nums[35])
    return gcd(gcd(a, b), c)