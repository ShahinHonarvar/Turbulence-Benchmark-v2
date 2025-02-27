from math import gcd

def gcf_three_nums(nums):
    factor36 = gcd(nums[36], gcd(nums[85], nums[83]))
    return factor36