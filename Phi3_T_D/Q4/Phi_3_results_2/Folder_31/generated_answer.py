def all_pos_ints_exclusive(nums):
    start_idx, end_idx = (87, 95)
    return [num for num in nums[start_idx:end_idx] if num > 0]