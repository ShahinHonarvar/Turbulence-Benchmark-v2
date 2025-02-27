from math import gcd

def gcf_three_nums(nums):
    gcf_91_45 = gcd(nums[91], nums[45])
    return gcd(gcf_91_45, nums[48])