def all_pos_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if 10 < i < 100 and n > 0]