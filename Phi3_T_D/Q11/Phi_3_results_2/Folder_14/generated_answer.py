def find_largest_num(nums):
    if len(nums) < 8:
        return None
    return max(nums[5:8])