def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i < 80 and (x < 0)]