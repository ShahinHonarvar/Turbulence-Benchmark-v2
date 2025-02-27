def all_pos_ints_exclusive(nums):
    pos_ints = [num for num in nums if num > 0]
    return pos_ints[86:90] if len(pos_ints) >= 86 else []