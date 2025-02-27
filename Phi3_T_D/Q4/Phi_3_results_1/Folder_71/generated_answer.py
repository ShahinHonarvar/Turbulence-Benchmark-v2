def all_pos_ints_exclusive(nums):
    if len(nums) < 54:
        return []
    return [num for num in nums[36:54] if num > 0]