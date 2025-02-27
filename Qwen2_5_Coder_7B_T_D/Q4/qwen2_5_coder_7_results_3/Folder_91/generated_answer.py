def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(1, 6) and x > 0]