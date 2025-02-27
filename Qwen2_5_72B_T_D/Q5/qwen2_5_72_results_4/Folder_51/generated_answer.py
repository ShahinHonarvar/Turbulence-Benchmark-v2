def all_neg_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[1:9], start=1) if num < 0]