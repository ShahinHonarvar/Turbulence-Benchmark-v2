def all_pos_ints_exclusive(nums):
    pos_ints = [num for num in nums if num > 0]
    if len(pos_ints) > 34:
        return pos_ints[27:34]
    else:
        return []