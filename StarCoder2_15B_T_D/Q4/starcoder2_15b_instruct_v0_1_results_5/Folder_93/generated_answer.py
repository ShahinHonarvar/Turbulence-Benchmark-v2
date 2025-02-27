def all_pos_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if num > 0 and i in range(19, 94)]