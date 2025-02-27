def all_pos_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if 1 < i < 2 and n > 0]