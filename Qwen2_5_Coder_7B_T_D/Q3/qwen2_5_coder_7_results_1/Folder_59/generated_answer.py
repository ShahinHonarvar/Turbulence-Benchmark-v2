def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:10]) if i >= 0 and i <= 9 and (x > 0)]