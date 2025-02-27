from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 88 and len(nums) > 35:
        return gcd(nums[88], nums[35])
    else:
        return None