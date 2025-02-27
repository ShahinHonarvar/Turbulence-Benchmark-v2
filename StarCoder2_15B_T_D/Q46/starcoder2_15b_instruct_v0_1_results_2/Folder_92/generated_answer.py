import math

def gcf_three_nums(nums):
    gcf = math.gcd(nums[7], nums[9])
    gcf = math.gcd(gcf, nums[0])
    return gcf