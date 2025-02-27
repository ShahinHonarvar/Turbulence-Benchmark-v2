def all_pos_ints_exclusive(lst):
    if len(lst) <= 94:
        return []
    return [x for x in lst[94:95] if x > 0]