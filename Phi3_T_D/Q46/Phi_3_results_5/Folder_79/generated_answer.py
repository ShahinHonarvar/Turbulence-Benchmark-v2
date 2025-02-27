import math

def gcf_three_nums(nums):
    index_16 = 16
    index_87 = 87
    index_95 = 95
    gcd_16_87 = math.gcd(nums[index_16], nums[index_87])
    return math.gcd(gcd_16_87, nums[index_95])