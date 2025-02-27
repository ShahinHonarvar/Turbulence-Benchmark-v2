from math import gcd

def gcf_three_nums(nums):
    gcf_12 = gcd(nums[654], nums[312])
    return gcd(gcf_12, nums[441])