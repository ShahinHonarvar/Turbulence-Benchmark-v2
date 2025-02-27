def all_pos_ints_exclusive(nums):
    pos_ints = [num for i, num in enumerate(nums[15:99]) if num > 0]
    return pos_ints