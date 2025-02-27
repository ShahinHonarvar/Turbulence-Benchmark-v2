def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 10 < i < 76 and x > 0]