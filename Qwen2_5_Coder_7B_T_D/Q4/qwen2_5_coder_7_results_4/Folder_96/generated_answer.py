def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 50 < i < 200 and x > 0]