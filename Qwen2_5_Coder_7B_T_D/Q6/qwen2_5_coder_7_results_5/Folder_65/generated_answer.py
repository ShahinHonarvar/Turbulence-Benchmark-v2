def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 42 and i < 87 and (x < 0)]