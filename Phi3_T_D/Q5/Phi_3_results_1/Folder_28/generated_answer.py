def all_neg_ints_inclusive(lst):
    index_start, index_end = (62, 63)
    return [x for x in lst[index_start:index_end + 1] if x < 0]