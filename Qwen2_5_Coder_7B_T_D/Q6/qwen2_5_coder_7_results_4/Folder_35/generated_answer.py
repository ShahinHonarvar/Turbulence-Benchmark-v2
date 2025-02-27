def all_neg_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 10 < i < 80 and num < 0]