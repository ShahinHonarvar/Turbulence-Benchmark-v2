def all_pos_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 10 < i < 100 and num > 0]