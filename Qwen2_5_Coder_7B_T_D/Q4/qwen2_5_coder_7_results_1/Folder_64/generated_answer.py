def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < i < 5 and x > 0]