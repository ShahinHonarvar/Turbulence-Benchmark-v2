def all_pos_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx > 48 and idx < 76 and (num > 0)]