def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 10 < i < 100 and x > 0]