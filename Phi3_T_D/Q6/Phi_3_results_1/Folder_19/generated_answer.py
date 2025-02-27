def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[2:5], start=2) if x < 0]