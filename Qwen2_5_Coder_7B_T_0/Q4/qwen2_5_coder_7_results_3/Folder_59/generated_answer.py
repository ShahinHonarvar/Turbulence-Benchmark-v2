def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < x < 10 and i > 0 and (i < 10)]