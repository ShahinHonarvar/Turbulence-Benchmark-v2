def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 20 and i < 51 and (x < 0)]