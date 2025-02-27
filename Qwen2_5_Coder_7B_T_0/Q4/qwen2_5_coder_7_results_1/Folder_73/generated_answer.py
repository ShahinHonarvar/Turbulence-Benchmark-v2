def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 36 < i < 85 and x > 0]