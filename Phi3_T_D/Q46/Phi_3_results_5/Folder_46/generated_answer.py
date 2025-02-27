import math

def gcf_three_nums(nums):
    if len(nums) < 13:
        return None
    return math.gcd(nums[78], nums[19], nums[13])