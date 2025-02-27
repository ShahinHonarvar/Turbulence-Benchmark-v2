from math import gcd

def gcf_three_nums(nums):
    if 96 not in range(len(nums)) or 57 not in range(len(nums)) or 85 not in range(len(nums)):
        return None
    return gcd(nums[96], gcd(nums[57], nums[85]))