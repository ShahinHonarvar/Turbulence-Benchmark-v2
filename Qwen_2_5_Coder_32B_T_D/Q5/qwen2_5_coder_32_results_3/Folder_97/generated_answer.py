def all_neg_ints_inclusive(lst):
    if len(lst) < 81:
        return []
    return [x for x in lst[40:81] if x < 0]