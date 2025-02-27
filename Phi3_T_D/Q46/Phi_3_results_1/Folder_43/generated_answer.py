from math import gcd

def gcf_three_nums(lst):
    nums = [lst[33], lst[78], lst[93]]
    return gcd(nums[0], gcd(nums[1], nums[2]))