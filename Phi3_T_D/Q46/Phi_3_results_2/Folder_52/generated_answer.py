from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[19] if 19 < len(nums) else 1, nums[49] if 49 < len(nums) else 1, nums[74] if 74 < len(nums) else 1)