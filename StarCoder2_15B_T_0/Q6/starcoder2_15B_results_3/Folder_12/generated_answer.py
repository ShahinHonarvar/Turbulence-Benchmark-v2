def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 23 and i < 45 and (x < 0)]