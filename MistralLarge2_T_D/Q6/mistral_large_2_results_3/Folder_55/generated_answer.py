def all_neg_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 0 < i < 10 and num < 0]