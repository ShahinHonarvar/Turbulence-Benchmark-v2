from math import gcd

def gcf_three_nums(nums):
    index_637 = nums[637] if len(nums) > 637 else 1
    index_411 = nums[411] if len(nums) > 411 else 1
    index_757 = nums[757] if len(nums) > 757 else 1
    gcf_637_411 = gcd(index_637, index_411)
    return gcd(gcf_637_411, index_757)