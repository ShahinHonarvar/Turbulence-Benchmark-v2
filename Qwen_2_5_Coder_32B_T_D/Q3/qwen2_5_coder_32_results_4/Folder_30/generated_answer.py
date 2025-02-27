def all_pos_ints_inclusive(lst):
    if len(lst) < 99:
        return []
    return [x for x in lst[55:99] if x > 0]