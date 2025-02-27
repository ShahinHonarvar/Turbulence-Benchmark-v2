from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[0], nums[8], nums[3])
    return gcd(gcd(a, b), c)