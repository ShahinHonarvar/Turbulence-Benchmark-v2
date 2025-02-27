import math

def gcf_two_nums(nums):
    if len(nums) >= 10:
        gcf = math.gcd(nums[6], nums[9])
        return gcf
    else:
        return None