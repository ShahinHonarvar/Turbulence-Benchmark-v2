from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 10:
        return gcd(nums[8], nums[3])
    else:
        return None