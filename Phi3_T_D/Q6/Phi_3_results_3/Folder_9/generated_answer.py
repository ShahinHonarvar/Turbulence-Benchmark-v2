def all_neg_ints_exclusive(lst):
    start, end = (70, 200)
    return [x for i, x in enumerate(lst) if start <= i < end and x < 0]