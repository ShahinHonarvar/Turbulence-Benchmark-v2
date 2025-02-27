def all_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 32 < i < 99]