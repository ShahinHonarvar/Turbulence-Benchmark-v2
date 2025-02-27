def all_pos_ints_exclusive(integers):
    return [x for i, x in enumerate(integers) if 36 < i < 52 and x > 0]