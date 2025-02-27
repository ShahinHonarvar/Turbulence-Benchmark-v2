def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 26 <= i <= 52 and x > 0]