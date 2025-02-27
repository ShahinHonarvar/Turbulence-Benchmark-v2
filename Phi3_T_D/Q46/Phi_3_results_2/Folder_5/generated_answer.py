from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[64] if len(nums) > 64 else 1, nums[80] if len(nums) > 80 else 1, nums[15] if len(nums) > 15 else 1)