def all_pos_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if 0 < i <= 8 and num > 0]