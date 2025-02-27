def all_neg_ints_inclusive(lst):
    try:
        return [i for i in lst[74:96] if i < 0]
    except IndexError:
        return []