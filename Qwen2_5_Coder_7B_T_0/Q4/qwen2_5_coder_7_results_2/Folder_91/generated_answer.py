def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < x < 6 and i > 0 and (i < 6)]