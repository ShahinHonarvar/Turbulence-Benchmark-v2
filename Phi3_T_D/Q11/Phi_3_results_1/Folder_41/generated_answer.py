def find_largest_num(nums):
    if len(nums) > 6:
        return max(nums[6:8])
    return max(nums)