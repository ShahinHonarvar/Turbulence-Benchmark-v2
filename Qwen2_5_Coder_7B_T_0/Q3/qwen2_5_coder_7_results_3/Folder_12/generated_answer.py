def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 14 <= i <= 64 and x > 0]