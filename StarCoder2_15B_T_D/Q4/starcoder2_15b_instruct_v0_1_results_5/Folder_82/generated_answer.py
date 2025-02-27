def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 20 < i < len(lst) - 20 and x > 0]