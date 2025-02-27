def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 1 < x < 8]