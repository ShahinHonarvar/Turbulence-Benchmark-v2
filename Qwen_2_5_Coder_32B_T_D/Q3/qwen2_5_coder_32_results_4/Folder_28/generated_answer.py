def all_pos_ints_inclusive(lst):
    if 63 < len(lst) < 62:
        return []
    return [x for x in lst[62:64] if x > 0]