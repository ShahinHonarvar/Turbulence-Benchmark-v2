def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[100:201]) if x < 0]