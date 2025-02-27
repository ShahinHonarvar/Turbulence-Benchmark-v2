def all_pos_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 48 < i < 76 and num > 0]