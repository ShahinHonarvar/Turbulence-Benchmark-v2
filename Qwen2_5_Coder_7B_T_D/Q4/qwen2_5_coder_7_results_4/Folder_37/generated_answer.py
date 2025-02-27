def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if i > 1 and i < 3 and (x > 0)]