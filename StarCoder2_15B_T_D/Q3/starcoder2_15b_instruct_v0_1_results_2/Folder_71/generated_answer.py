def all_pos_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if 26 <= i <= 52 and num > 0]