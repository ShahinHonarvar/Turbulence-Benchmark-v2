def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 1 < i < 2 and x > 0]