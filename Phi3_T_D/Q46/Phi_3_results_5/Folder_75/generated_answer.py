import math

def gcf_three_nums(nums):
    index_70 = nums[70] if len(nums) > 70 else 1
    index_98 = nums[98] if len(nums) > 98 else 1
    index_22 = nums[22] if len(nums) > 22 else 1
    return math.gcd(math.gcd(index_70, index_98), index_22)