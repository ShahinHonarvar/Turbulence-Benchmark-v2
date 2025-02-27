def all_neg_ints_inclusive(lst):
    start, end = (262, 746)
    return [x for x in lst[start:end + 1] if x < 0]