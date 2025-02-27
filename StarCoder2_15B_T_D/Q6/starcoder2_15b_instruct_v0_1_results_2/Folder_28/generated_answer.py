def all_neg_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx >= 20 and idx < 51 and (num < 0)]