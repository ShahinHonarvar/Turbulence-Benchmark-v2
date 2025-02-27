def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[111:473], start=111) if x < 0]