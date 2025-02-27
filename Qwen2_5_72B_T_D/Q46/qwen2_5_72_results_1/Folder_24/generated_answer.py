from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[18], nums[37], nums[43])
    return gcd(gcd(a, b), c)