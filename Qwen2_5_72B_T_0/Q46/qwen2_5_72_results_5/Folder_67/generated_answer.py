from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[70], nums[41], nums[20])
    return gcd(gcd(a, b), c)