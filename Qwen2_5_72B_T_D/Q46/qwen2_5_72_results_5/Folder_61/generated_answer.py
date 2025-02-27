from math import gcd

def gcf_three_nums(nums):
    x, y, z = (nums[1], nums[2], nums[7])
    return gcd(gcd(x, y), z)