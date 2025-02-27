def all_neg_ints_inclusive(lst):
    if len(lst) < 201:
        return []
    return [x for i, x in enumerate(lst) if i >= 80 and i <= 200 and (x < 0)]