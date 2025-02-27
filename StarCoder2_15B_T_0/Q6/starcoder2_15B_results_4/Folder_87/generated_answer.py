def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 32 and i < 99 and (x < 0)]