def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 0 and i < 10 and (x > 0)]