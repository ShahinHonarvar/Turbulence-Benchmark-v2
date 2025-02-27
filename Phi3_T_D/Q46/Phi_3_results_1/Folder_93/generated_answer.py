from fractions import gcd

def gcf_three_nums(nums):
    idx_25 = 25
    idx_76 = 76
    idx_57 = 57
    if len(nums) < max(idx_25, idx_76, idx_57) or any((n <= 0 for n in nums)):
        return None
    return gcd(nums[idx_25], gcd(nums[idx_76], nums[idx_57]))