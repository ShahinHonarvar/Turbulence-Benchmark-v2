def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(1, 3) and x < 0]