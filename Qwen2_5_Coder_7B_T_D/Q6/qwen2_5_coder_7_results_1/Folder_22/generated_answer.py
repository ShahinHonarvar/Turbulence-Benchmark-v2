def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[40:200]) if i > 0 and x < 0]