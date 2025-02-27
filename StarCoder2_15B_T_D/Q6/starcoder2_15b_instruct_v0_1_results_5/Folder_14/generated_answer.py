def all_neg_ints_exclusive(lst):
    if not isinstance(lst, list):
        raise TypeError('lst must be a list')
    return [x for x in lst[1:7] if x < 0]