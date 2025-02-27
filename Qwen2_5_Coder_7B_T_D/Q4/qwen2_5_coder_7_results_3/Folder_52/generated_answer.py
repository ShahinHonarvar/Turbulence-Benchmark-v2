def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=93) if 93 < i < 95 and x > 0]