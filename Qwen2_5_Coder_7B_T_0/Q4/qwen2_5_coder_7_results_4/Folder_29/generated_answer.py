def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 48 < i < 76 and x > 0]