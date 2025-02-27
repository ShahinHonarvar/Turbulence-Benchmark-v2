from math import gcd

def gcf_three_nums(nums):
    if len(nums) < max(70, 41, 20):
        raise IndexError('List is too short!')
    return gcd(gcd(nums[70], nums[41]), nums[20])