def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 36 and i < 52 and (x > 0)]