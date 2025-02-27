def all_pos_ints_inclusive(lst):
    if len(lst) < 65:
        return []
    return [x for x in lst[14:65] if x > 0]