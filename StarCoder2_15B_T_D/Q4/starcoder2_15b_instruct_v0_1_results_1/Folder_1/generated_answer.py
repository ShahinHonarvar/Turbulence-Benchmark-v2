def all_pos_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 65 and i < 90 and (num > 0)]