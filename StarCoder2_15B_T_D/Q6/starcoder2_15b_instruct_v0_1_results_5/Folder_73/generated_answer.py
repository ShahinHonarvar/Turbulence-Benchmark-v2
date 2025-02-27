def all_neg_ints_exclusive(lst):
    return [num for idx, num in enumerate(lst) if idx > 36 and idx < 85 and (num < 0)]