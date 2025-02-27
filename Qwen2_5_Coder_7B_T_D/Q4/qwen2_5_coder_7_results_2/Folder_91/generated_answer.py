def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < x <= 5 and i in range(1, 6)]