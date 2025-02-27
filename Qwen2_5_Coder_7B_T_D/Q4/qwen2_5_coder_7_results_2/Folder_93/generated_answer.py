def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 19 < i < 94 and x > 0]