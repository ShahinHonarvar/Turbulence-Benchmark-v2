def all_pos_ints_inclusive(lst):
    if len(lst) < 925:
        return []
    return [x for x in lst[661:925] if x > 0]