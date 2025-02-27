def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 12 <= i <= 92 and x > 0]