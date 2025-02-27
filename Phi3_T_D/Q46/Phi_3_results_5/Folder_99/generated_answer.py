from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[912 % len(nums)], gcd(nums[170 % len(nums)], nums[500 % len(nums)]))