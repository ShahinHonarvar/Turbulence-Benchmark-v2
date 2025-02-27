def all_neg_ints_inclusive(lst):
    if len(lst) < 775:
        return []
    return [x for x in lst[667:775] if x < 0]