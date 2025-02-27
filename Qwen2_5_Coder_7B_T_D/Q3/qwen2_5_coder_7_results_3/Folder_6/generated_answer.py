def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 10 and i <= 66 and (x > 0)]