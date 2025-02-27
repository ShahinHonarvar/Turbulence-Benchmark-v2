from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[3], nums[8], nums[9])
    return gcd(gcd(a, b), c)