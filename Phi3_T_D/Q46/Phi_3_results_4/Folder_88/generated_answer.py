import math

def gcf_three_nums(nums):
    index_47 = nums[47] if len(nums) > 47 else 1
    index_10 = nums[10] if len(nums) > 10 else 1
    index_28 = nums[28] if len(nums) > 28 else 1
    return math.gcd(math.gcd(index_47, index_10), index_28)