from math import gcd

def gcf_two_nums(nums):
    return gcd(nums[793], nums[449]) if 793 in range(len(nums)) and 449 in range(len(nums)) else None