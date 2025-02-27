from math import gcd

def gcf_three_nums(nums):
    x = gcd(nums[0], nums[4])
    y = gcd(x, nums[8])
    return y