def all_neg_ints_exclusive(lst):
    if len(lst) < 6:
        return []
    return [x for x in lst[4:6] if x < 0]