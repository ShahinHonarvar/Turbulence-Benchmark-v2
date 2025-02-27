import math

def gcf_three_nums(nums):
    gcf = math.gcd(nums[1], nums[2])
    gcf = math.gcd(gcf, nums[7])
    return gcf