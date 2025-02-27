def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[:8]) if 0 < x < 9]