def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < x < 11 and i in range(1, 11)]