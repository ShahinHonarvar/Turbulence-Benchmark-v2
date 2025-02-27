def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 48 and i < 76 and (x < 0)]