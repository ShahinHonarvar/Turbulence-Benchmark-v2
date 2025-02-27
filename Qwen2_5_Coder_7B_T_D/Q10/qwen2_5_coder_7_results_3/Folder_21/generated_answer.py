def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 743 and i < 867 and (x % 2 != 0)]