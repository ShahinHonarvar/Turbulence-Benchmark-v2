from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[29], nums[74], nums[49])
    return gcd(gcd(a, b), c)