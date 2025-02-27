def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst, 1) if i >= 10 and i <= 100 and (x > 0)]