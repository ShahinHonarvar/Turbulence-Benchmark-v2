def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 100 and i <= 200 and (x > 0)]