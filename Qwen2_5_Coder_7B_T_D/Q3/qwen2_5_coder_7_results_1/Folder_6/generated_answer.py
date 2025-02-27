def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 10 <= i <= 66 and x > 0]