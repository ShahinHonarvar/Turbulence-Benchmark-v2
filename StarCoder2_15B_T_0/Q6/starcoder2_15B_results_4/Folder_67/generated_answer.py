def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 49 and i < 74 and (x < 0)]