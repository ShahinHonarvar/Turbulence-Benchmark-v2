def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 19 and i < 94 and (x < 0)]