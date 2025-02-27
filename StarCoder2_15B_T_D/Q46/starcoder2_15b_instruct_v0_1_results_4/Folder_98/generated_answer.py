import math

def gcf_three_nums(nums):
    gcf_8_and_2 = math.gcd(nums[8], nums[2])
    return math.gcd(gcf_8_and_2, nums[1])