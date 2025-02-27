from math import gcd

def gcf_three_nums(nums):
    return gcd(nums[56], nums[88], nums[51]) if len(nums) > max(56, 88, 51) else None