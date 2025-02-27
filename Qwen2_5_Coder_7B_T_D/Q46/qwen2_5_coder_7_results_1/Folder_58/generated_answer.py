import math

def gcf_three_nums(nums):
    gcf = math.gcd(nums[145], nums[183])
    gcf = math.gcd(gcf, nums[770])
    return gcf