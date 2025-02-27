import math

def gcf_three_nums(nums):
    gcf = nums[477]
    gcf = math.gcd(gcf, nums[696])
    gcf = math.gcd(gcf, nums[663])
    return gcf