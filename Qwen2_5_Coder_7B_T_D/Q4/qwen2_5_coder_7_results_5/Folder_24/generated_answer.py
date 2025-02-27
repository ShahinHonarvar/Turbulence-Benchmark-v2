def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 13 < i < 67 and x > 0]