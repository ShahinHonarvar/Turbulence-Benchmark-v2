def all_pos_ints_inclusive(lst):
    return [x for x in lst[:11] if isinstance(x, int) and x > 0]