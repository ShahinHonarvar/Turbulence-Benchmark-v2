def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[111:473]) if x < 0 and i + 111 != 473]