def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[31:200]) if x < 0]