def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 15 < i < 99 and x > 0]