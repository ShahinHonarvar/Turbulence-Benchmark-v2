def all_pos_ints_inclusive(lst):
    if len(lst) < 96:
        return []
    return [x for x in lst[74:96] if x > 0]