import math

def gcf_three_nums(nums):
    if len(nums) >= 15:
        gcf = math.gcd(nums[64], nums[80])
        gcf = math.gcd(gcf, nums[15])
        return gcf
    else:
        raise ValueError('The list must have at least 15 elements.')