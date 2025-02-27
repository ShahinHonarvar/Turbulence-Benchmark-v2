def all_neg_ints_exclusive(lst):
    return [n for i, n in enumerate(lst) if i >= 100 and i < 200 and (n < 0)]