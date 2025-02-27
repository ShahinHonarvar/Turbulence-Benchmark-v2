import math

def gcf_three_nums(nums):
    if len(nums) < 97:
        return None
    return math.gcd(nums[90], math.gcd(nums[54], nums[96]))