def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[:7]) if i > 0 and x < 0]