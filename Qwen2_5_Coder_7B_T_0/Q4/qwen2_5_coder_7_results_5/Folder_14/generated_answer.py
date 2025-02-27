def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 1 < i < 8 and x > 0]