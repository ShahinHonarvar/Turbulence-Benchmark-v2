from math import gcd

def gcf_two_nums(nums):
    if len(nums) > 95 and len(nums) > 73:
        return gcd(nums[95], nums[73])
    else:
        raise IndexError('The list does not have enough elements')